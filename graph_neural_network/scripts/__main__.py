import os
import optuna
import argparse
import torch
from graph_neural_network.scripts.utils.DataImporter import DataImporter
from graph_neural_network.scripts.MachiningFeatureLocalizer import MachiningFeatureLocalizer

from graph_neural_network.scripts.network_models.GcNetwork import GcNetwork
from graph_neural_network.scripts.network_models.DgcnNetwork import DgcnNetwork
from graph_neural_network.scripts.network_models.SageGnNetwork import SageGnNetwork
from graph_neural_network.scripts.network_models.FeaStNetwork import FeaStNetwork
from graph_neural_network.scripts.network_models.GATNetwork import GATNetwork
from graph_neural_network.scripts.network_models.GATV2Network import GATV2Network
from graph_neural_network.scripts.network_models.ChebNetwork import ChebNetwork
from graph_neural_network.scripts.network_models.ArmaNetwork import ArmaNetwork
from graph_neural_network.scripts.network_models.AgnNetwork import AgnNetwork

_parser = argparse.ArgumentParser(description='Base configuration of the synthetic data generator')
_parser.add_argument('--project_name',
                     dest='project_name', default='CAFL', type=str,
                     help='This name belongs to the wandb project which is created when the code is started. The wandb '
                          'code publishes training parameters like train_accuracy to your personal wandb dashboard. You'
                          'just have to register at www.wandb.ai and follow the instructions at: '
                          'https://docs.wandb.ai/quickstart.'
                          '(Not used for testing)')
_parser.add_argument('--study_name',
                     dest='study_name', default='DGCNN-max', type=str,
                     help='The study name defines a subgroup for the wandb project, which is defined above. This helps'
                          'to repeat an experiment or training process without creating every time a new wandb project.'
                          '(Not used for testing)')
_parser.add_argument('--hyperparameter_trials',
                     dest='hyperparameter_trials', default=100, type=int,
                     help='The hyperparameter_trials value defines how often the training procedure is repeated.'
                          'Reason for repeated training is, that this framework applies a hyperparameter optimization '
                          'for the training procedure. Here, an optimization algorithm tries to find the best hyper '
                          'parameters like hidden channels or amount of graph conv layers. To find the best hyper '
                          'parameter, the training procedure has to be conducted multiple times, so the optimization '
                          'algorithms can analyze how different values of each parameter influences the training '
                          'procedure of the network. More information about hyperparameter optimization at:'
                          'https://optuna.org/'
                     )
_parser.add_argument('--training_dataset',
                     dest='training_dataset', default=DataImporter(os.getenv('TRAINING_DATASET_SOURCE'),
                                                                   os.getenv('TRAINING_DATASET_DESTINATION')).shuffle(),
                     help='The training_dataset config holds the training data. The data is converted via the'
                          'DataImporter class into a fitting graph representation and then loaded for training. The'
                          'conversion process takes some time, especially for larger data, but it has to be done only'
                          'once, as long as the data doesnt change. '
                          '(Not used for testing)')
_parser.add_argument('--amount_training_data',
                     dest='amount_training_data', default=50707, type=int,
                     help='This variable allows you to separate the training data, taken from the "data -> cad ->'
                          'training" folder, into training and validation datasets. For example, if you have 24000 '
                          'cad models, if you type in value 22000 models, then 22000 models will be utilized for '
                          'training and 2000 models for validation. NOTE: The cad models will be first converted into a'
                          'fitting graph representation and saved into the data -> graph -> training folder.')
_parser.add_argument('--amount_validation_data',
                     dest='amount_validation_data', default=8948, type=int,
                     help='')
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
_parser.add_argument('--max_epoch', dest='max_epoch', default=100, type=int,
                     help='The max epoch defines how often the complete training data is run trough. One epoch means'
                          'therefore, that the graph neural network is fitted ones an all available training data. '
                          'More epochs generally decreases the network loss, but can also lead to overfitting,'
                          'memorizing the training data and not be applicable to new data. We utilized 100 epochs for'
                          'most of our experiments')
_parser.add_argument('--network_model', dest='network_model', default=DgcnNetwork,
                     help='GcNetwork, DgcnNetwork, SageGnNetwork, FeaStNetwork, GATNetwork, GATV2Network, ChebNetwork,'
                          'ArmaNetwork, AgnNetwork')
_parser.add_argument('--network_model_id', dest='network_model_id', default="DgcnNetwork", type=str,
                     help='GcNetwork, DgcnNetwork, SageGnNetwork, FeaStNetwork, GATNetwork, GATV2Network, ChebNetwork,'
                          'ArmaNetwork, AgnNetwork')

if __name__ == '__main__':
    _config = _parser.parse_args()

    _study = optuna.create_study(direction="maximize", study_name=_config.study_name)
    _study.optimize(lambda trial: MachiningFeatureLocalizer(_config, trial).training(),
                    n_trials=_config.hyperparameter_trials)
