import os
import numpy as np
import pandas as pd
from stl import mesh


class MachiningFeatureLabels:
    def __init__(self, machining_feature_list, model_id, target_directory, machining_feature_id_list):
        self.machining_feature_list = machining_feature_list
        self.target_directory = target_directory
        self.model_id = model_id
        self.machining_feature_for_labeling = None
        self.machining_feature_id_list = machining_feature_id_list

    @staticmethod
    def truncate_coordinates(vertices):
        return [float(f"{c:.3f}") for c in vertices]

    def write_csv_file(self, label_list):
        _label_list = pd.DataFrame(label_list)
        _label_list.to_csv(
            os.getenv(self.target_directory) + "/" + str(self.model_id) + ".csv", header=False, index=False)

    def write_localization_training_file(self):
        # get vertices for new cad model and machining features
        _new_cad_model = mesh.Mesh.from_file(os.getenv(self.target_directory) + "/" + str(self.model_id) + ".stl")
        _new_cad_model_vertices = np.array(np.unique(
            _new_cad_model.vectors.reshape([int(_new_cad_model.vectors.size / 3), 3]), axis=0))
        _new_cad_model_vertices = [self.truncate_coordinates(vertices)
                                   for vertices in _new_cad_model_vertices]

        _label_list = [24] * len(_new_cad_model_vertices)

        for machining_feature_id, machining_feature in enumerate(self.machining_feature_list):
            _machining_feature_for_labeling = np.array([point.to_tuple() for point in machining_feature.points])

            # round vertices of new cad model and machining feature, so a correct comparison is possible
            _machining_feature_for_labeling = [self.truncate_coordinates(vertices)
                                               for vertices in _machining_feature_for_labeling]
            # _label_list = [self.machining_feature_id[count]
            #              if coord in self.machining_feature_for_labeling else 24 for coord in _new_cad_model_vertices]

            for vertices_index, cad_model_vertices in enumerate(_new_cad_model_vertices):
                for machining_feature_vertices in _machining_feature_for_labeling:
                    if cad_model_vertices == machining_feature_vertices:
                        _label_list[vertices_index] = self.machining_feature_id_list[machining_feature_id]

        self.write_csv_file(_label_list)

    def write_ssd_net_training_file(self):
        _label_list = []
        _new_cad_model = mesh.Mesh.from_file(os.getenv(self.target_directory) + "/" + str(self.model_id) + ".stl")
        _new_cad_model_vertices = np.array(np.unique(
            _new_cad_model.vectors.reshape([int(_new_cad_model.vectors.size / 3), 3]), axis=0))
        _new_cad_model_vertices = [self.truncate_coordinates(vertices)
                                   for vertices in _new_cad_model_vertices]

        for machining_feature_id, machining_feature in enumerate(self.machining_feature_list):

            _machining_feature_for_labeling = np.array([point.to_tuple() for point in machining_feature.points])
            _machining_feature_for_labeling = np.clip(_machining_feature_for_labeling, 0, 10)

            if (coord in _new_cad_model_vertices for coord in _machining_feature_for_labeling):
                x_values = [vector[0] for vector in _machining_feature_for_labeling]
                y_values = [vector[1] for vector in _machining_feature_for_labeling]
                z_values = [vector[2] for vector in _machining_feature_for_labeling]

                _label_list.append(
                    [min(x_values), min(y_values), min(z_values),
                     max(x_values), max(y_values), max(z_values),
                     self.machining_feature_id_list[machining_feature_id]])

        self.write_csv_file(_label_list)
