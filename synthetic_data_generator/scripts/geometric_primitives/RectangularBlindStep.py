import numpy as np
import madcad as mdc


class RectangularBlindStep:
    def __init__(self, limit):
        self.dir = np.random.choice(["direction_1", "direction_2", "direction_3", "direction_4", "direction_5",
                                     "direction_6", "direction_7", "direction_8"])

        self.limit = limit
        self.positive_length = np.random.uniform(1, (9 * self.limit))
        self.positive_width = np.random.uniform(1, (9 * self.limit))
        self.negative_length = 9 - np.random.uniform(1, (9 * self.limit))
        self.negative_width = 9 - np.random.uniform(1, (9 * self.limit))
        self.depth = np.random.uniform(1, 9)

        self.negative_start_point = -0.0002
        self.positive_start_point = 10.0002

        self.rectangular_vectors = {
            # front bottom left
            "direction_1": [mdc.vec3(self.negative_start_point, self.negative_start_point, self.negative_start_point),
                            mdc.vec3(self.positive_width, self.positive_length, self.depth)],

            # front bottom right
            "direction_2": [mdc.vec3(self.negative_width, self.negative_length, self.depth),
                            mdc.vec3(self.positive_start_point, self.negative_start_point, self.negative_start_point)],

            # front upper left
            "direction_3": [mdc.vec3(self.positive_width, self.positive_length, self.depth),
                            mdc.vec3(self.negative_start_point, self.negative_start_point, self.positive_start_point)],

            # front upper left
            "direction_4": [mdc.vec3(self.positive_start_point, self.negative_start_point, self.positive_start_point),
                            mdc.vec3(self.negative_width, self.positive_length, self.depth)],

            # back bottom left
            "direction_5": [mdc.vec3(self.positive_width, self.negative_length, self.depth),
                            mdc.vec3(self.negative_start_point, self.positive_start_point, self.negative_start_point)],

            # back bottom right
            "direction_6": [mdc.vec3(self.positive_start_point, self.positive_start_point, self.negative_start_point),
                            mdc.vec3(self.negative_length, self.negative_width, self.depth)],

            # back upper left
            "direction_7": [mdc.vec3(self.negative_start_point, self.positive_start_point, self.positive_start_point),
                            mdc.vec3(self.positive_width, self.negative_length, self.depth)],

            # back upper left
            "direction_8": [mdc.vec3(self.negative_width, self.negative_width, self.depth),
                            mdc.vec3(self.positive_start_point, self.positive_start_point, self.positive_start_point)]
        }

    def transformation(self):
        _rectangular_blind_step = mdc.brick(self.rectangular_vectors[self.dir][0],
                                            self.rectangular_vectors[self.dir][1])

        return _rectangular_blind_step
