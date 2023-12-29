import torch
import torch.nn.functional as f
from torch_geometric.nn import AGNNConv
from torch.nn import Linear


class AgnNetwork(torch.nn.Module):
    def __init__(self, dataset, device, batch_size, dropout_probability, number_conv_layers, hidden_channels):
        super().__init__()
        self.device = device
        self.batch_size = batch_size
        self.dropout_probability = dropout_probability
        self.number_conv_layers = number_conv_layers
        self.conv_layers = []

        self.lin1 = torch.nn.Linear(dataset.num_features, 16)
        self.prop1 = AGNNConv(requires_grad=False)
        self.prop2 = AGNNConv(requires_grad=True)
        self.lin2 = torch.nn.Linear(16, dataset.num_classes)


    def forward(self, x, edge_index, batch):
        x = f.dropout(x, training=self.training)
        x = f.relu(self.lin1(x))
        x = self.prop1(x, edge_index)
        x = self.prop2(x, edge_index)
        x = f.dropout(x, training=self.training)
        x = self.lin2(x)
        return f.log_softmax(x, dim=1)

    def train_loss(self, loader, criterion, optimizer):
        self.train()

        total_loss = 0
        for i, data in enumerate(loader):  # Iterate in batches over the training dataset.
            data = data.to(self.device)
            optimizer.zero_grad()  # Clear gradients.
            out = self(data.x, data.edge_index, data.batch)  # Perform a single forward pass.
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
            out = self(data.x, data.edge_index, data.batch)  # Perform a single forward pass.
            loss = criterion(out, data.y)
            total_loss += loss.item() * data.num_graphs

        return total_loss / len(loader.dataset)

    @torch.no_grad()
    def accuracy(self, loader):
        self.eval()
        correct_predictions, total_predictions = 0, 0

        for data in loader:
            out = self(data.x.to(self.device), data.edge_index.to(self.device), data.batch.to(self.device))
            predicted_labels = out.argmax(dim=1).cpu()
            true_labels = data.y.cpu()
            correct_predictions += (predicted_labels == true_labels).sum().item()
            total_predictions += len(true_labels)

        accuracy = correct_predictions / total_predictions if total_predictions > 0 else 0.0

        return 100 * accuracy
