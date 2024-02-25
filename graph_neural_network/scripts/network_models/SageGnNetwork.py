import torch
from thop import profile
from statistics import mean
import torch.nn.functional as f
from torch_geometric.nn import SAGEConv
from sklearn.metrics import f1_score


class SageGnNetwork(torch.nn.Module):
    def __init__(self, dataset, device, hyper_parameter):
        super().__init__()
        self.dataset = dataset
        self.device = device
        self.batch_size = hyper_parameter.batch_size
        self.dropout_probability = hyper_parameter.dropout_probability
        self.number_conv_layers = hyper_parameter.number_conv_layers
        self.hidden_channels = hyper_parameter.hidden_channels
        self.aggr = hyper_parameter.aggr

        self.conv1 = SAGEConv(dataset.num_features, self.hidden_channels, self.aggr)
        if self.number_conv_layers > 1:
            self.conv2 = SAGEConv(self.hidden_channels, self.hidden_channels, self.aggr)
        if self.number_conv_layers > 2:
            self.conv3 = SAGEConv(self.hidden_channels, self.hidden_channels, self.aggr)
        if self.number_conv_layers > 3:
            self.conv4 = SAGEConv(self.hidden_channels, self.hidden_channels, self.aggr)
        if self.number_conv_layers > 4:
            self.conv5 = SAGEConv(self.hidden_channels, dataset.num_classes, self.aggr)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = x.relu()
        x = f.dropout(x, p=self.dropout_probability, training=self.training)
        if self.number_conv_layers > 1:
            x = self.conv2(x, edge_index)
            x = x.relu()
            x = f.dropout(x, p=self.dropout_probability, training=self.training)
        if self.number_conv_layers > 2:
            x = self.conv3(x, edge_index)
            x = x.relu()
            x = f.dropout(x, p=self.dropout_probability, training=self.training)
        if self.number_conv_layers > 3:
            x = self.conv4(x, edge_index)
            x = x.relu()
            x = f.dropout(x, p=self.dropout_probability, training=self.training)
        if self.number_conv_layers > 4:
            x = self.conv5(x, edge_index)
            x = x.relu()
            x = f.dropout(x, p=self.dropout_probability, training=self.training)

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
        flops_list = []
        params_list = []

        for index, data in enumerate(loader):
            print(index)
            out = self(data.x.to(self.device), data.edge_index.to(self.device))
            predicted_labels = out.argmax(dim=1).cpu().numpy()
            true_labels = data.y.cpu().numpy()
            all_predicted_labels.extend(predicted_labels)
            all_true_labels.extend(true_labels)

            flops, params = profile(self, inputs=(data.x.to(self.device), data.edge_index.to(self.device),),
                                    verbose=False)
            print(flops)
            print(params)
            flops_list.append(flops)
            params_list.append(params)

        f1 = f1_score(all_true_labels, all_predicted_labels, average='micro')

        return f1, mean(flops_list), mean(params_list)