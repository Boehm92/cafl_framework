import os
import time
import torch
import wandb
import optuna
from DataImporter import DataImporter
from torch_geometric.loader import DataLoader
from NetworkModel import NetworkModel
import torch.optim.lr_scheduler

STUDY_NAME = "CAFL_Experiment"
torch.manual_seed(1)
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)
data_partition = 12000

# test_dataset = DataImporter(os.getenv('TEST_DATASET_SOURCE'), os.getenv('TEST_DATASET_DESTINATION'))
training_dataset = DataImporter(
    os.getenv('TRAINING_DATASET_SOURCE'), os.getenv('TRAINING_DATASET_DESTINATION')).shuffle()

def objective(trial):
    # Hyperparameter
    best_accuracy = 0
    max_epoch = 100
    number_conv_layers = 2  # trial.suggest_int("number_conv_layers", 2, 7)
    h_channel = 8  # trial.suggest_categorical("h_channel", [32, 64, 128, 256, 512])
    b_size = 16  # trial.suggest_categorical("b_size", [32, 64, 128, 256])
    lr = 0.001  # trial.suggest_categorical("lr", [0.01, 0.001, 0.0001])
    dropout_probability = 0.2  # trial.suggest_float("dropout_probability", 0.1, 0.5, step=0.1)

    print("b_size: ", b_size)
    print("lr: ", lr)
    print("dropout_probability: ", dropout_probability)

    training_dataset.shuffle()
    # test_dataset.shuffle()

    train_loader = DataLoader(training_dataset[:data_partition], batch_size=b_size, shuffle=True, drop_last=True)
    val_loader = DataLoader(training_dataset[data_partition:], batch_size=b_size, shuffle=True, drop_last=True)
    # test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False, drop_last=True)

    model = NetworkModel(dataset=training_dataset, device=device, batch_size=b_size,
                      dropout_probability=dropout_probability, number_conv_layers=number_conv_layers,
                      hidden_channels=h_channel).to(device)

    # model.load_state_dict(torch.load(os.getenv('WEIGHTS') + '/weights.pt'))
    print(model)

    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    # scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', factor=0.1, patience=15, verbose=True)
    # scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1, verbose=True)

    config = dict(trial.params)
    config["trial.number"] = trial.number
    wandb.init(project="CAFL_Experiment_1",
               entity="boehm92", config=config, group=STUDY_NAME, reinit=True)

    for epoch in range(1, max_epoch):
        training_loss = model.train_loss(train_loader, criterion, optimizer)
        val_loss = model.val_loss(val_loader, criterion)
        train_f1 = model.accuracy(train_loader)
        val_f1 = model.accuracy(val_loader)
        test_f1 = 0 # model.accuracy(test_loader)
        trial.report(val_f1, epoch) # test
        # scheduler.step() # test

        wandb.log({'training_loss': training_loss, 'val_los': val_loss, 'train_F1': train_f1, 'val_F1': val_f1,
                  'test_F1': test_f1})  #

        if best_accuracy < val_f1:
            torch.save(model.state_dict(), os.getenv('WEIGHTS') + '/weights.pt')
            best_accuracy = val_f1
            print("Saved model due to better found accuracy")

        if trial.should_prune():
            wandb.run.summary["state"] = "pruned"
            wandb.finish(quiet=True)
            raise optuna.exceptions.TrialPruned()

        print(f'Epoch: {epoch:03d}, training_loss: {training_loss:.4f}, val_los: {val_loss:.4f},'
              f'train_F1: {train_f1:.4f}, val_F1: {val_f1:.4f}') # test_F1: {test_f1:.4f}

    wandb.run.summary["Final F-Score"] = val_f1
    wandb.run.summary["state"] = "completed"
    wandb.finish(quiet=True)

    return val_f1

if __name__ == '__main__':
    study = optuna.create_study(direction="maximize", study_name=STUDY_NAME)

    start_time = time.time()
    study.optimize(objective, n_trials=1)
    end_time = time.time()

    print("Time: ", end_time - start_time)


