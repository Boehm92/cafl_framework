import os
import torch
import wandb
import optuna
from torch_geometric.loader import DataLoader
from graph_neural_network.scripts.utils.HyperParameter import HyperParameter


class MachiningFeatureLocalizer:
    def __init__(self, config, trial):
        self.max_epoch = config.max_epoch
        self.training_dataset = config.training_dataset
        self.network_model = config.network_model
        self.network_model_id = config.network_model_id
        self.amount_training_data = config.amount_training_data
        self.amount_validation_data = config.amount_validation_data
        self.trial = trial
        self.hyper_parameters = HyperParameter(trial, config.network_model_id)
        self.device = config.device
        self.project_name = config.project_name
        self.study_name = config.study_name

    def training(self):
        _best_accuracy = 0

        self.training_dataset.shuffle()
        _train_loader = DataLoader(self.training_dataset[:self.amount_training_data],
                                   batch_size=self.hyper_parameters.batch_size, shuffle=True, drop_last=True)
        _val_loader = DataLoader(self.training_dataset[self.amount_training_data:
                                                       self.amount_training_data + self.amount_validation_data],
                                 batch_size=self.hyper_parameters.batch_size, shuffle=True, drop_last=True)

        _network_model = self.network_model(self.training_dataset, self.device, self.hyper_parameters).to(self.device)
        print(_network_model)
        print(self.device)

        # Configuring learning functions
        criterion = torch.nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(_network_model.parameters(), lr=self.hyper_parameters.learning_rate)

        # Setting up hyperparameter function and wandb
        _config = dict(self.trial.params)
        _config["trial.number"] = self.trial.number
        wandb.init(project=self.project_name, entity="boehm92", config=_config, group=self.study_name, reinit=True)

        # Training
        for epoch in range(1, self.max_epoch):
            training_loss = _network_model.train_loss(_train_loader, criterion, optimizer)
            val_loss = _network_model.val_loss(_val_loader, criterion)
            train_f1 = _network_model.accuracy(_train_loader)
            val_f1 = _network_model.accuracy(_val_loader)
            self.trial.report(val_f1, epoch)

            wandb.log({'training_loss': training_loss, 'val_los': val_loss, 'train_F1': train_f1, 'val_F1': val_f1})

            if (_best_accuracy < val_f1) & ((val_loss - training_loss) < 0.04):
                torch.save(_network_model.state_dict(), os.getenv('WEIGHTS') + '/weights.pt')
                _best_accuracy = val_f1
                print("Saved model due to better found accuracy")

            if self.trial.should_prune():
                wandb.run.summary["state"] = "pruned"
                wandb.finish(quiet=True)
                raise optuna.exceptions.TrialPruned()

            if (train_f1 + 0.2) < val_f1:
                wandb.run.summary["state"] = "pruned"
                wandb.finish(quiet=True)
                raise optuna.exceptions.TrialPruned()

            print(f'Epoch: {epoch:03d}, training_loss: {training_loss:.4f}, val_los: {val_loss:.4f}, '
                  f'train_F1: {train_f1:.4f}, val_F1: {val_f1:.4f}')

        wandb.run.summary["Final F-Score"] = val_f1
        wandb.run.summary["state"] = "completed"
        wandb.finish(quiet=True)

        return val_f1
