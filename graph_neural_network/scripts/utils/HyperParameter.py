class HyperParameter:
    def __init__(self, trial, network_model):
        self.params = {
            "batch_size": trial.suggest_categorical("batch_size", [16, 32, 64, 128, 256]),
            "dropout_probability": trial.suggest_categorical("dropout_probability", [0.1, 0.2, 0.3, 0.4, 0.5]),
            "learning_rate": trial.suggest_categorical("learning_rate", [0.01, 0.001, 0.0001]),
        }
        if network_model == "GcNetwork":
            self.params.update({
                "number_conv_layer": trial.suggest_categorical("conv_layer", [1, 2, 3, 4, 5, 6, 7, 8]),
                "hidden_channels": trial.suggest_categorical("hidden_channels", [16, 32, 64, 128, 256, 512]),
            })
        elif network_model == "DgcnNetwork":
            self.params.update({
                "number_conv_layer": trial.suggest_categorical("conv_layer", [1, 2, 3, 4, 5, 6]),
                "hidden_channels": trial.suggest_categorical("hidden_channels", [16, 32, 64, 128, 256]),
            })
        elif network_model == "FeaStNetwork":
            self.params.update({
                "attention_heads": trial.suggest_categorical("attention_heads", [2, 4, 6, 8, 10, 12]),
            })
        else:
            raise ValueError(f"Invalid Network: {network_model}")

        self.__dict__.update(self.params)
