import os
import numpy as np
import pandas as pd
import madcad as mdc
from synthetic_data_generator.scripts.geometric_primitives.base_primitive import Cube
from synthetic_data_generator.scripts.utils.MachiningFeature import MachiningFeature
from synthetic_data_generator.scripts.utils.CsgOperation import CsgOperation
from synthetic_data_generator.scripts.utils.MachiningFeatureLabels import MachiningFeatureLabels


class DataGenerator:
    def __init__(self, config):
        self.cad_data_generation_start_cycle = config.cad_data_generation_start_cycle
        self.cad_data_generation_end_cycles = config.cad_data_generation_end_cycles
        self.max_machining_feature_count = config.max_machining_feature_count
        self.max_machining_feature_dimension = config.max_machining_feature_dimension
        self.target_directory = config.target_directory
        self.rotate_base_primitive = config.rotate_base_primitive
        self.select_machining_feature_id_random = config.select_machining_feature_id_random
        self.machining_feature_id = config.machining_feature_id

    def generate(self):
        for _model_id in range(self.cad_data_generation_start_cycle, self.cad_data_generation_end_cycles):
            _machining_feature_id_list = []
            _machining_feature_list = []

            _new_cad_model = Cube(10, mdc.vec3(5, 5, 5)).transform()

            _machining_feature_count = np.random.randint(1, self.max_machining_feature_count)

            try:
                for _ in range(_machining_feature_count):
                    if self.select_machining_feature_id_random:
                        _machining_feature_id = np.random.randint(0, 24)
                    else:
                        _machining_feature_id = self.machining_feature_id

                    _machining_feature = MachiningFeature(_machining_feature_id,
                                                          self.max_machining_feature_dimension).create()
                    _new_cad_model = CsgOperation(_new_cad_model, _machining_feature).difference()

                    if self.rotate_base_primitive:
                        _new_cad_model = Cube.rotate_model_randomly(_new_cad_model)

                    _machining_feature_id_list.append(_machining_feature_id)
                    _machining_feature_list.append(_machining_feature)

                print(f"Created CAD model {_model_id} with {_machining_feature_count} machining feature was "
                      f"created")

            except:
                # We use here a broad exception clause to avoid applying machining feature if not enough surface is
                # available
                print(f"One or more machining feature for the CAD model {_model_id} were not feasible."
                      f" For CAD model {_model_id}, {_} from {_machining_feature_count} have been applied."
                      f" This can happen when not enough surface is available for the CSG difference operation")

            # For Experiment 1 of the configurable machining feature framework, it is necessary to append
            # "str(machining_feature_id) + "_" + str(model_id) + ".stl"
            # to both the .stl write function and the CSV write function. This requirement arises from the necessity
            # imposed by the SSL framework available at https://github.com/whjdark/ssl_for_MFR, which relies on the
            # specific naming convention for .stl files.

            mdc.write(_new_cad_model, os.getenv(self.target_directory) + "/" + str(_model_id) + ".stl")
            MachiningFeatureLabels(_machining_feature_list, _model_id, self.target_directory,
                                   _machining_feature_id_list).write_localization_training_file()

            del _new_cad_model
            del _machining_feature_id_list
