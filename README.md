# configurable-automated-feature-localization-framework
This framework includes two microservices: a synthetic data generator as well as a novel gnn architecture to classify each vertice in a surface CAD model. 

Synthetic data generator (python3.10):
For using the synthetic data generator microservice please install following packages in the same order:
1. pymadcad==0.16.0
2. numpy-stl==3.0.1
3. pandas==2.1.1

Graph neural network (python3.10):
using the synthetic graph neural network microservice please install following packages in the same order:
1. torch-geometric==2.4.0 
2. torch==1.12.1 --extra-index-url https://download.pytorch.org/whl/cu102
3. torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-1.12.1%2Bcu102.html
4. numpy-stl==3.0.1
5. wandb==0.15.12 (for wandb an account at wandb is necessary)
6. optuna==3.4.0
