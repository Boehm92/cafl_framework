import torch
import torch.nn.functional as f
from torch_geometric.nn import GATv2Conv
from sklearn.metrics import f1_score


class GATV2Network(torch.nn.Module):
    def __init__(self, dataset, device, hyper_parameter):
        super().__init__()
        self.dataset = dataset
        self.device = device
        self.batch_size = hyper_parameter.batch_size
        self.dropout_probability = hyper_parameter.dropout_probability
        self.attention_heads = hyper_parameter.attention_heads
        self.number_conv_layers = hyper_parameter.number_conv_layers
        self.conv_hidden_channels = hyper_parameter.conv_hidden_channels

        self.conv1 = GATv2Conv(dataset.num_features, self.conv_hidden_channels, heads=self.attention_heads)
        if self.number_conv_layers == 2:
            self.conv2 = GATv2Conv(self.conv_hidden_channels * self.attention_heads,
                                   dataset.num_classes, concat=False, heads=1, dropout=0.6)
        elif self.number_conv_layers > 1:
            self.conv2 = GATv2Conv(self.conv_hidden_channels * self.attention_heads,
                                   self.conv_hidden_channels * (self.attention_heads ** 2), concat=False,
                                   heads=self.attention_heads, dropout=0.6)
        if self.number_conv_layers > 2:
            self.conv3 = GATv2Conv(self.conv_hidden_channels * (self.attention_heads ** 2),
                                   dataset.num_classes, concat=False, heads=1, dropout=0.6)

    def forward(self, x, edge_index):
        x = f.elu(self.conv1(x, edge_index))
        if self.number_conv_layers > 1:
            x = f.elu(self.conv2(x, edge_index))
        if self.number_conv_layers > 2:
            x = f.elu(self.conv3(x, edge_index))

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
