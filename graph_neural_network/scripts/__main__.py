import os
import optuna
import argparse
import torch
from graph_neural_network.scripts.utils.DataImporter import DataImporter
from graph_neural_network.scripts.MachiningFeatureLocalizer import MachiningFeatureLocalizer

from graph_neural_network.scripts.network_models.GcNetwork import GcNetwork
from graph_neural_network.scripts.network_models.DgcnNetwork import DgcnNetwork

_parser = argparse.ArgumentParser(description='Base configuration of the synthetic data generator')
_parser.add_argument('--training_dataset',
                     dest='training_dataset', default=DataImporter(os.getenv('TRAINING_DATASET_SOURCE'),
                                                                   os.getenv('TRAINING_DATASET_DESTINATION')).shuffle(),
                     help='The training_dataset config holds the training data. The data is converted via the'
                          'DataImporter class into a fitting graph representation and then loaded for training. The'
                          'conversion process takes some time, especially for larger data, but it has to be done only'
                          'once, as long as the data doesnt change. '
                          '(Not used for testing)')
_parser.add_argument('--train_val_partition',
                     dest='train_val_partition', default=22000, type=int,
                     help='This variable allows you to separate the training data, taken from the "data -> cad ->'
                          'training" folder, into training and validation datasets. For example, if you have 24000 '
                          'cad models, if you type in value 22000 models, then 22000 models will be utilized for '
                          'training and 2000 models for validation. NOTE: The cad models will be first converted into a'
                          'fitting graph representation and saved into the data -> graph -> training folder.'
                          '(Not used for testing)')
_parser.add_argument('--device',
                     dest='device', default=("cuda" if torch.cuda.is_available() else "cpu"), type=str,
                     help='The device variable defines if the code is run on the gpu or the cpu. If you installed the'
                          'cuda toolkit and the related pytorch and pytorch-geometric packages, then the code should '
                          'run on the gpu. If not, the code automatically will run on the cpu, which will be far '
                          'slower. Please note, that in the requirements1 and 2 files, there are example of '
                          'installations setting, however the necessary python packages vary strongly in regard to'
                          'used operation system, python interpreter, used graphic card and installed cuda toolkit.'
                          'So, it may take some time to find the right setting for you. We suggest, for the first '
                          'implementation, to install the packages manually.')
_parser.add_argument('--network_model', dest='network_model', default=DgcnNetwork, help='GcNetwork, DgcnNetwork')
_parser.add_argument('--network_model_id', dest='network_model_id', default='GcNetwork', type=str)
_parser.add_argument('--max_epoch',
                     dest='max_epoch', default=100, type=int,
                     help='The max epoch defines how often the complete training data is run trough. One epoch means'
                          'therefore, that the graph neural network is fitted ones an all available training data. '
                          'More epochs generally decreases the network loss, but can also lead to overfitting,'
                          'memorizing the training data and not be applicable to new data. We utilized 100 epochs for'
                          'most of our experiments')
_parser.add_argument('--project_name',
                     dest='project_name', default='testi', type=str,
                     help='This name belongs to the wandb project which is created when the code is started. The wandb '
                          'code publishes training parameters like train_accuracy to your personal wandb dashboard. You'
                          'just have to register at www.wandb.ai and follow the instructions at: '
                          'https://docs.wandb.ai/quickstart.'
                          '(Not used for testing)')
_parser.add_argument('--study_name',
                     dest='study_name', default='test_1', type=str,
                     help='The study name defines a subgroup for the wandb project, which is defined above. This helps'
                          'to repeat an experiment or training process without creating every time a new wandb project.'
                          '(Not used for testing)')

if __name__ == '__main__':
    _config = _parser.parse_args()

    _study = optuna.create_study(direction="maximize", study_name="testi")
    _study.optimize(lambda trial: MachiningFeatureLocalizer(_config, trial).training(), n_trials=1)
