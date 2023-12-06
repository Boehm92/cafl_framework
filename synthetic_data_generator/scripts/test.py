import pandas as pd
import os
import madcad as mdc
from MachiningFeature import MachiningFeature
import numpy as np
from stl import mesh


for i in range(1, 20):
    machining_feature_id = 23
    cad_directory = 'TRAINING_DATASET_SOURCE'
    cube = mdc.brick(width=mdc.vec3(10)).transform(mdc.vec3(5, 5, 5))

    machining_feature = MachiningFeature(machining_feature_id, 1).create()
    machining_feature_for_labeling = np.array([point.to_tuple() for point in machining_feature.points])

    product = mdc.difference(cube, machining_feature)
    product.mergeclose()
    product = mdc.segmentation(product)

    # mdc.show([cube, machining_feature])
    mdc.show([product])

    mdc.write(product, os.getenv(cad_directory) + "/" + str(i) + ".stl")
    m = mesh.Mesh.from_file(os.getenv(cad_directory) + "/" + str(i) + ".stl")
    x = np.array(np.unique(m.vectors.reshape([int(m.vectors.size / 3), 3]), axis=0))

    def truncate_coordinates(coord):
        return [float(f"{c:.3f}") for c in coord]

    machining_feature_for_labeling = [truncate_coordinates(coord) for coord in machining_feature_for_labeling]
    x = [truncate_coordinates(coord) for coord in x]
    label_list = [machining_feature_id if coord in machining_feature_for_labeling else 2 for coord in x]

    labels = pd.DataFrame(label_list)
    labels.to_csv(os.getenv(cad_directory) + "/" + str(i) + ".csv", header=False, index=False)

    all_elements_in_x = any(coord in x for coord in machining_feature_for_labeling)

    print(label_list)

    if all_elements_in_x:
        print("enthalten")
    else:
        print("nicht enthalten")

    del cube
    del machining_feature
    del machining_feature_for_labeling
    del product
