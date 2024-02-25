import torch
from thop import profile
import torch.nn.functional as f
from torch_geometric.nn import FeaStConv as GraphConvLayer
import torch.nn as nn
from sklearn.metrics import f1_score


class FeaStNetwork(torch.nn.Module):
    def __init__(self, dataset, device, hyper_parameter):
        super().__init__()
        self.dataset = dataset
        self.device = device
        self.batch_size = hyper_parameter.batch_size
        self.dropout_probability = hyper_parameter.dropout_probability
        self.number_conv_layers = hyper_parameter.number_conv_layers
        self.conv_hidden_channels = hyper_parameter.conv_hidden_channels
        self.lin_hidden_channels = hyper_parameter.lin_hidden_channels
        self.attention_heads = hyper_parameter.attention_heads

        self.fc0 = nn.Linear(dataset.num_features, int(self.conv_hidden_channels))
        self.conv1 = GraphConvLayer(int(self.conv_hidden_channels), int(self.conv_hidden_channels * 2),
                                    heads=self.attention_heads)
        if self.number_conv_layers > 1:
            self.conv2 = GraphConvLayer(int(self.conv_hidden_channels * 2), int(self.conv_hidden_channels * 4),
                                        heads=self.attention_heads)
            _conv_hidden_channels = int(self.conv_hidden_channels * 4)

        if self.number_conv_layers > 2:
            self.conv3 = GraphConvLayer(int(self.conv_hidden_channels * 4), int(self.conv_hidden_channels * 8),
                                        heads=self.attention_heads)
            _conv_hidden_channels = int(self.conv_hidden_channels * 8)

        if self.number_conv_layers > 3:
            self.conv4 = GraphConvLayer(int(self.conv_hidden_channels * 8), int(self.conv_hidden_channels * 16),
                                        heads=self.attention_heads)
            _conv_hidden_channels = int(self.conv_hidden_channels * 16)

        self.fc1 = nn.Linear(_conv_hidden_channels, self.lin_hidden_channels)
        self.fc2 = nn.Linear(self.lin_hidden_channels, dataset.num_classes)

    def forward(self, x, edge_index):
        x = f.elu(self.fc0(x))
        x = f.elu(self.conv1(x, edge_index))
        if self.number_conv_layers > 1:
            x = f.elu(self.conv2(x, edge_index))
        if self.number_conv_layers > 2:
            x = f.elu(self.conv3(x, edge_index))
        if self.number_conv_layers > 3:
            x = f.elu(self.conv4(x, edge_index))
        x = f.elu(self.fc1(x))
        x = f.dropout(x, training=self.training)
        x = self.fc2(x)

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

        for index, data in enumerate(loader):
            print(index)
            out = self(data.x.to(self.device), data.edge_index.to(self.device))
            predicted_labels = out.argmax(dim=1).cpu().numpy()
            true_labels = data.y.cpu().numpy()

            all_predicted_labels.extend(predicted_labels)
            all_true_labels.extend(true_labels)

            flops, params = profile(self, inputs=(data.x.to(self.device), data.edge_index.to(self.device),),
                                    verbose=False)

        f1 = f1_score(all_true_labels, all_predicted_labels, average='micro')

        return f1, flops, params
