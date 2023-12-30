import torch
import torch.nn.functional as f
from torch_geometric.nn import AGNNConv
from sklearn.metrics import f1_score


class AgnNetwork(torch.nn.Module):
    def __init__(self, dataset, device, hyper_parameter):
        super().__init__()
        self.dataset = dataset
        self.device = device
        self.batch_size = hyper_parameter.batch_size
        self.dropout_probability = hyper_parameter.dropout_probability
        self.number_conv_layers = hyper_parameter.number_conv_layers
        self.hidden_channels = hyper_parameter.hidden_channels

        self.lin1 = torch.nn.Linear(dataset.num_features, self.hidden_channels)
        self.prop1 = AGNNConv(requires_grad=False)
        if self.number_conv_layers > 1:
            self.prop2 = AGNNConv(requires_grad=False)
        if self.number_conv_layers > 2:
            self.prop3 = AGNNConv(requires_grad=False)
        if self.number_conv_layers > 3:
            self.prop4 = AGNNConv(requires_grad=False)
        self.lin2 = torch.nn.Linear(self.hidden_channels, dataset.num_classes)

    def forward(self, x, edge_index):
        x = f.relu(self.lin1(x))
        x = f.dropout(x, p=self.dropout_probability, training=self.training)

        x = self.prop1(x, edge_index)
        if self.number_conv_layers > 1:
            x = self.prop2(x, edge_index)
        if self.number_conv_layers > 2:
            x = self.prop3(x, edge_index)
        if self.number_conv_layers > 3:
            x = self.prop4(x, edge_index)
        x = f.dropout(x, p=self.dropout_probability, training=self.training)

        x = self.lin2(x)
        return f.log_softmax(x, dim=1)

    def train_loss(self, loader, criterion, optimizer):
        self.train()

        total_loss = 0
        for i, data in enumerate(loader):  # Iterate in batches over the training dataset.
            data = data.to(self.device)
            optimizer.zero_grad()  # Clear gradients.
            out = self(data.x, data.edge_index)  # Perform a single forward pass.
            loss = criterion(out, data.y)
            total_loss += loss.item() * data.num_graphs
            loss.backward()  # Derive gradients.
            optimizer.step()  # Update parameters based on gradients.

        return total_loss / len(loader.dataset)

    def val_loss(self, loader, criterion):
        self.eval()

        total_loss = 0
        for data in loader:  # Iterate in batches over the training dataset.
            data = data.to(self.device)
            out = self(data.x, data.edge_index)  # Perform a single forward pass.
            loss = criterion(out, data.y)
            total_loss += loss.item() * data.num_graphs

        return total_loss / len(loader.dataset)

    @torch.no_grad()
    def accuracy(self, loader):
        self.eval()
        all_predicted_labels = []
        all_true_labels = []

        for data in loader:
            out = self(data.x.to(self.device), data.edge_index.to(self.device))
            predicted_labels = out.argmax(dim=1).cpu().numpy()
            true_labels = data.y.cpu().numpy()

            all_predicted_labels.extend(predicted_labels)
            all_true_labels.extend(true_labels)

        f1 = f1_score(all_true_labels, all_predicted_labels, average='micro')

        return f1
