import torch
import torch.nn.functional as f
from torch_geometric.nn import EdgeConv
from torch.nn import Sequential as Seq, Dropout, Linear as Lin, ReLU, BatchNorm1d as BN

def MLP(channels, batch_norm=True):
    return Seq(*[
        Seq(Lin(channels[i - 1], channels[i]), ReLU(), BN(channels[i]))
        for i in range(1, len(channels))
    ])

class DgcnNetwork(torch.nn.Module):
    def __init__(self, dataset, device, hyper_parameter):
        super().__init__()
        self.device = device
        self.aggr = 'add'

        self.conv1 = EdgeConv(MLP([2 * dataset.num_features, 64, 64]), self.aggr)
        self.conv2 = EdgeConv(MLP([2 * 64, 64, 64]), self.aggr)
        self.conv3 = EdgeConv(MLP([2 * 64, 64, 64]), self.aggr)
        self.conv4 = EdgeConv(MLP([2 * 64, 64, 64]), self.aggr)
        self.lin1 = MLP([4 * 64, 1024])

        self.mlp = Seq(
            MLP([1024, 256]), Dropout(0.5), MLP([256, 128]), Dropout(0.5), Lin(128, dataset.num_classes))

    def forward(self, x, edge_index, batch):

        x1 = self.conv1(x, edge_index)
        x2 = self.conv2(x1, edge_index)
        x3 = self.conv3(x2, edge_index)
        x4 = self.conv3(x2, edge_index)
        out = self.lin1(torch.cat([x1, x2, x3, x4], dim=1))
        out = self.mlp(out)
        return f.log_softmax(out, dim=1)

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
