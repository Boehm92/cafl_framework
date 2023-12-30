import torch
import torch.nn.functional as f
from torch_geometric.nn import EdgeConv
from torch.nn import Sequential as Seq, Dropout, Linear as Lin, ReLU, BatchNorm1d as BN
from sklearn.metrics import f1_score


def MLP(channels):
    return Seq(*[
        Seq(Lin(channels[i - 1], channels[i]), ReLU(), BN(channels[i]))
        for i in range(1, len(channels))
    ])

class DgcnNetwork(torch.nn.Module):
    def __init__(self, dataset, device, hyper_parameter):
        super().__init__()
        self.device = device
        self.aggr = 'add'
        self.number_conv_layers = hyper_parameter.number_conv_layers
        self.conv_hidden_channels = hyper_parameter.conv_hidden_channels
        self.mlp_hidden_channels = hyper_parameter.mlp_hidden_channels

        self.conv1 = EdgeConv(MLP([2 * dataset.num_features, self.conv_hidden_channels, self.conv_hidden_channels]),
                              self.aggr)
        if self.number_conv_layers > 1:
            self.conv2 = EdgeConv(MLP([int(2 * self.conv_hidden_channels), self.conv_hidden_channels,
                                       self.conv_hidden_channels]), self.aggr)
        if self.number_conv_layers > 2:
            self.conv3 = EdgeConv(MLP([int(2 * self.conv_hidden_channels), self.conv_hidden_channels,
                                       self.conv_hidden_channels]), self.aggr)
        if self.number_conv_layers > 3:
            self.conv4 = EdgeConv(MLP([int(2 * self.conv_hidden_channels), self.conv_hidden_channels,
                                       self.conv_hidden_channels]), self.aggr)
        if self.number_conv_layers > 4:
            self.conv5 = EdgeConv(MLP([int(2 * self.conv_hidden_channels), self.conv_hidden_channels,
                                       self.conv_hidden_channels]), self.aggr)

        print(self.number_conv_layers * self.conv_hidden_channels)
        print(self.mlp_hidden_channels)

        self.lin1 = MLP([self.number_conv_layers * self.conv_hidden_channels, self.mlp_hidden_channels])
        self.mlp = Seq(MLP([self.mlp_hidden_channels, int(self.mlp_hidden_channels / 4)]), Dropout(0.5),
                       MLP([int(self.mlp_hidden_channels / 4), int(self.mlp_hidden_channels / 8)]), Dropout(0.5),
                       Lin(int(self.mlp_hidden_channels / 8), dataset.num_classes))

    def forward(self, x, edge_index):

        x1 = self.conv1(x, edge_index)
        out = self.lin1(torch.cat([x1], dim=1))

        if self.number_conv_layers > 1:
            x2 = self.conv2(x1, edge_index)
            out = self.lin1(torch.cat([x1, x2], dim=1))

        if self.number_conv_layers > 2:
            x3 = self.conv3(x2, edge_index)
            out = self.lin1(torch.cat([x1, x2, x3], dim=1))

        if self.number_conv_layers > 3:
            x4 = self.conv4(x2, edge_index)
            out = self.lin1(torch.cat([x1, x2, x3, x4], dim=1))

        if self.number_conv_layers > 4:
            x5 = self.conv5(x2, edge_index)
            out = self.lin1(torch.cat([x1, x2, x3, x4, x5], dim=1))

        out = self.mlp(out)
        return f.log_softmax(out, dim=1)

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
