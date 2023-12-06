import numpy as np
import madcad as mdc


class CircularBlindStep:
    def __init__(self, limit):
        self.dir = np.random.choice(["direction_1", "direction_2", "direction_3", "direction_4", "direction_5",
                                     "direction_6", "direction_7", "direction_8", "direction_9", "direction_10",
                                     "direction_11", "direction_12", "direction_13", "direction_14", "direction_15",
                                     "direction_16", "direction_17", "direction_18", "direction_19", "direction_20",
                                     "direction_21", "direction_22", "direction_23", "direction_24"])
        self.limit = limit
        self.radius = np.random.uniform(1, (9 * self.limit))
        self.depth = np.random.uniform(1, 9)

        self.negative_start_point = -0.0002
        self.positive_start_point = 10.0002

        self.circular_vectors = {
            # front bottom left
            "direction_1": [mdc.vec3(self.negative_start_point, self.negative_start_point, self.negative_start_point),
                            mdc.vec3(self.negative_start_point, self.negative_start_point, self.depth)],
            "direction_2": [mdc.vec3(self.negative_start_point, self.negative_start_point, self.negative_start_point),
                            mdc.vec3(self.negative_start_point, self.depth, self.negative_start_point)],
            "direction_3": [mdc.vec3(self.negative_start_point, self.negative_start_point, self.negative_start_point),
                            mdc.vec3(self.depth, self.negative_start_point, self.negative_start_point)],

            # front bottom right
            "direction_4": [mdc.vec3(self.positive_start_point, self.negative_start_point, self.negative_start_point),
                            mdc.vec3(self.positive_start_point, self.negative_start_point, self.depth)],
            "direction_5": [mdc.vec3(self.positive_start_point, self.negative_start_point, self.negative_start_point),
                            mdc.vec3(self.positive_start_point, self.depth, self.negative_start_point)],
            "direction_6": [mdc.vec3(self.positive_start_point, self.negative_start_point, self.negative_start_point),
                            mdc.vec3(self.depth, self.negative_start_point, self.negative_start_point)],

            # front upper left
            "direction_7": [mdc.vec3(self.negative_start_point, self.negative_start_point, self.positive_start_point),
                            mdc.vec3(self.negative_start_point, self.negative_start_point, self.depth)],
            "direction_8": [mdc.vec3(self.negative_start_point, self.negative_start_point, self.positive_start_point),
                            mdc.vec3(self.negative_start_point, self.depth, self.positive_start_point)],
            "direction_9": [mdc.vec3(self.negative_start_point, self.negative_start_point, self.positive_start_point),
                            mdc.vec3(self.depth, self.negative_start_point, self.positive_start_point)],

            # front upper left
            "direction_10": [mdc.vec3(self.positive_start_point, self.negative_start_point, self.positive_start_point),
                             mdc.vec3(self.positive_start_point, self.negative_start_point, self.depth)],
            "direction_11": [mdc.vec3(self.positive_start_point, self.negative_start_point, self.positive_start_point),
                             mdc.vec3(self.positive_start_point, self.depth, self.positive_start_point)],
            "direction_12": [mdc.vec3(self.positive_start_point, self.negative_start_point, self.positive_start_point),
                             mdc.vec3(self.depth, self.negative_start_point, self.positive_start_point)],

            # back bottom left
            "direction_13": [mdc.vec3(self.negative_start_point, self.positive_start_point, self.negative_start_point),
                             mdc.vec3(self.negative_start_point, self.positive_start_point, self.depth)],
            "direction_14": [mdc.vec3(self.negative_start_point, self.positive_start_point, self.negative_start_point),
                             mdc.vec3(self.negative_start_point, self.depth, self.negative_start_point)],
            "direction_15": [mdc.vec3(self.negative_start_point, self.positive_start_point, self.negative_start_point),
                             mdc.vec3(self.depth, self.positive_start_point, self.negative_start_point)],

            # back bottom right
            "direction_16": [mdc.vec3(self.positive_start_point, self.positive_start_point, self.negative_start_point),
                             mdc.vec3(self.positive_start_point, self.positive_start_point, self.depth)],
            "direction_17": [mdc.vec3(self.positive_start_point, self.positive_start_point, self.negative_start_point),
                             mdc.vec3(self.positive_start_point, self.depth, self.negative_start_point)],
            "direction_18": [mdc.vec3(self.positive_start_point, self.positive_start_point, self.negative_start_point),
                             mdc.vec3(self.depth, self.positive_start_point, self.negative_start_point)],

            # back upper left
            "direction_19": [mdc.vec3(self.negative_start_point, self.positive_start_point, self.positive_start_point),
                             mdc.vec3(self.negative_start_point, self.positive_start_point, self.depth)],
            "direction_20": [mdc.vec3(self.negative_start_point, self.positive_start_point, self.positive_start_point),
                             mdc.vec3(self.negative_start_point, self.depth, self.positive_start_point)],
            "direction_21": [mdc.vec3(self.negative_start_point, self.positive_start_point, self.positive_start_point),
                             mdc.vec3(self.depth, self.positive_start_point, self.positive_start_point)],

            # back upper left
            "direction_22": [mdc.vec3(self.positive_start_point, self.positive_start_point, self.positive_start_point),
                             mdc.vec3(self.positive_start_point, self.positive_start_point, self.depth)],
            "direction_23": [mdc.vec3(self.positive_start_point, self.positive_start_point, self.positive_start_point),
                             mdc.vec3(self.positive_start_point, self.depth, self.positive_start_point)],
            "direction_24": [mdc.vec3(self.positive_start_point, self.positive_start_point, self.positive_start_point),
                             mdc.vec3(self.depth, self.positive_start_point, self.positive_start_point)],
        }

    def transformation(self):
        _circular_blind_step = mdc.cylinder(self.circular_vectors[self.dir][0], self.circular_vectors[self.dir][1],
                                            self.radius)

        return _circular_blind_step
