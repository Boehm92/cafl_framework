class HyperParameter:
    def __init__(self, trial, network_model):
        self.params = {
            "batch_size": trial.suggest_categorical("batch_size", [32, 64, 128, 256]),
            "dropout_probability": trial.suggest_categorical("dropout_probability", [0.1, 0.2, 0.3, 0.4, 0.5]),
            "learning_rate": trial.suggest_categorical("learning_rate", [0.01, 0.001, 0.0001]),
        }
        if network_model == "GcNetwork":
            self.params.update({
                "number_conv_layers": trial.suggest_categorical("conv_layer", [2, 3, 4, 5, 6, 7, 8]),
                "conv_hidden_channels": trial.suggest_categorical("conv_hidden_channels", [16, 32, 64, 128, 256, 512]),
            })
        elif network_model == "DgcnNetwork":
            self.params.update({
                "number_conv_layers": trial.suggest_categorical("number_conv_layers", [2, 3, 4, 5]),
                "conv_hidden_channels": trial.suggest_categorical("conv_hidden_channels", [32, 64, 128, 512]),
                "mlp_hidden_channels": trial.suggest_categorical("mlp_hidden_channels", [32, 64, 128, 256]),
                "aggr": "max",
            })
        elif network_model == "SageGnNetwork":
            self.params.update({
                "number_conv_layers": trial.suggest_categorical("number_conv_layers", [1, 2, 3, 4, 5]),
                "hidden_channels": trial.suggest_categorical("hidden_channels", [32, 64, 128, 256, 512]),
                "aggr": trial.suggest_categorical("conv_hidden_channels", ["mean"]),
            })
        elif network_model == "FeaStNetwork":
            self.params.update({
                "number_conv_layers": trial.suggest_categorical("conv_layer", [2, 3, 4]),
                "conv_hidden_channels": trial.suggest_categorical("conv_hidden_channels", [4, 8, 16, 32, 64]),
                "lin_hidden_channels": trial.suggest_categorical("lin_hidden_channels", [64, 128, 256, 512]),
                "attention_heads": trial.suggest_categorical("attention_heads", [6, 8, 10, 11, 12]),
            })
        elif network_model == "GATNetwork":
            self.params.update({
                "number_conv_layers": trial.suggest_categorical("conv_layer", [2, 3]),
                "conv_hidden_channels": trial.suggest_categorical("conv_hidden_channels", [4, 8, 16]),
                "attention_heads": trial.suggest_categorical("attention_heads", [1, 2, 3, 4, 5, 6, 7, 8]),
            })
        elif network_model == "GATV2Network":
            self.params.update({
                "number_conv_layers": trial.suggest_categorical("conv_layer", [2, 3]),
                "conv_hidden_channels": trial.suggest_categorical("conv_hidden_channels", [4, 8, 16]),
                "attention_heads": trial.suggest_categorical("attention_heads", [1, 2, 3, 4]),
            })
        elif network_model == "ChebNetwork":
            self.params.update({
                "number_conv_layers": trial.suggest_categorical("conv_layer", [2, 3]),
                "conv_hidden_channels": trial.suggest_categorical("conv_hidden_channels", [4, 8, 16, 32]),
                "graph_filters": trial.suggest_categorical("attention_heads", [1, 2, 3, 4, 5]),
            })
        elif network_model == "ArmaNetwork":
            self.params.update({
                "number_conv_layers": trial.suggest_categorical("conv_layer", [2, 3, 4]),
                "conv_hidden_channels": trial.suggest_categorical("conv_hidden_channels", [4, 8, 16, 32, 64]),
                "graph_filters": trial.suggest_categorical("attention_heads", [1, 2, 3, 4, 5]),
                "layer_dropout_probability": trial.suggest_categorical("layer_dropout_probability", [0.25, 0.5, 0.75]),
                "num_stacks": trial.suggest_categorical("num_stacks", [1, 2, 3, 4, 5]),
                "num_layer": trial.suggest_categorical("num_layer", [1, 2, 3, 4, 5]),
            })
        elif network_model == "AgnNetwork":
            self.params.update({
                "number_conv_layers": trial.suggest_categorical("conv_layer", [2, 3, 4]),
                "hidden_channels": trial.suggest_categorical("hidden_channels", [16, 32, 64, 128, 256, 512]),
            })
        else:
            raise ValueError(f"Invalid Network: {network_model}")

        self.__dict__.update(self.params)
