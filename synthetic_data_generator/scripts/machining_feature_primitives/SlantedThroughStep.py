import numpy as np
import madcad as mdc


class SlantedThroughStep:
    def __init__(self, limit):
        self.dir = np.random.choice(["direction_1", "direction_2", "direction_3", "direction_4", "direction_5",
                                     "direction_6", "direction_7", "direction_8"])
        self.limit = limit
        self.width_A = np.random.uniform(1, (9 * self.limit))
        self.width_B = np.random.uniform(1, (9 * self.limit))
        self.depth = np.random.uniform(1, 9)
        self.negative_start_point = -0.0002
        self.positive_start_point = 10.0002

        self.slanted_vectors = {
            # back top
            "direction_1": {
                "vector_A": mdc.vec3(self.positive_start_point, self.positive_start_point, self.positive_start_point),
                "vector_B": mdc.vec3(self.negative_start_point, self.positive_start_point, self.positive_start_point),
                "vector_C": mdc.vec3(self.negative_start_point, self.positive_start_point - self.width_A,
                                     self.positive_start_point),
                "vector_D": mdc.vec3(self.positive_start_point, self.positive_start_point - self.width_B,
                                     self.positive_start_point)
            },
            # back bottom
            "direction_2": {
                "vector_A": mdc.vec3(self.positive_start_point, self.positive_start_point - self.width_A,
                                     self.negative_start_point),
                "vector_B": mdc.vec3(self.negative_start_point, self.positive_start_point - self.width_B,
                                     self.negative_start_point),
                "vector_C": mdc.vec3(self.negative_start_point, self.positive_start_point, self.negative_start_point),
                "vector_D": mdc.vec3(self.positive_start_point, self.positive_start_point, self.negative_start_point),
            },
            # front top
            "direction_3": {
                "vector_A": mdc.vec3(self.positive_start_point, self.negative_start_point + self.width_A,
                                     self.positive_start_point),
                "vector_B": mdc.vec3(self.negative_start_point, self.negative_start_point + self.width_B,
                                     self.positive_start_point),
                "vector_C": mdc.vec3(self.negative_start_point, self.negative_start_point, self.positive_start_point),
                "vector_D": mdc.vec3(self.positive_start_point, self.negative_start_point, self.positive_start_point)
            },
            # front bottom
            "direction_4": {
                "vector_A": mdc.vec3(self.positive_start_point, self.negative_start_point, self.negative_start_point),
                "vector_B": mdc.vec3(self.negative_start_point, self.negative_start_point, self.negative_start_point),
                "vector_C": mdc.vec3(self.negative_start_point, self.negative_start_point + self.width_A,
                                     self.negative_start_point),
                "vector_D": mdc.vec3(self.positive_start_point, self.negative_start_point + self.width_B,
                                     self.negative_start_point),
            },
            # left top
            "direction_5": {
                "vector_A": mdc.vec3(self.negative_start_point, self.negative_start_point, self.positive_start_point),
                "vector_B": mdc.vec3(self.negative_start_point + self.width_A, self.negative_start_point,
                                     self.positive_start_point),
                "vector_C": mdc.vec3(self.negative_start_point + self.width_B, self.positive_start_point,
                                     self.positive_start_point),
                "vector_D": mdc.vec3(self.negative_start_point, self.positive_start_point, self.positive_start_point)
            },
            # left bottom
            "direction_6": {
                "vector_A": mdc.vec3(self.negative_start_point, self.positive_start_point, self.negative_start_point),
                "vector_B": mdc.vec3(self.negative_start_point + self.width_A, self.positive_start_point,
                                     self.negative_start_point),
                "vector_C": mdc.vec3(self.negative_start_point + self.width_B, self.negative_start_point,
                                     self.negative_start_point),
                "vector_D": mdc.vec3(self.negative_start_point, self.negative_start_point, self.negative_start_point)
            },
            # right top
            "direction_7": {
                "vector_A": mdc.vec3(self.positive_start_point, self.positive_start_point, self.positive_start_point),
                "vector_B": mdc.vec3(self.positive_start_point - self.width_A, self.positive_start_point,
                                     self.positive_start_point),
                "vector_C": mdc.vec3(self.positive_start_point - self.width_B, self.negative_start_point,
                                     self.positive_start_point),
                "vector_D": mdc.vec3(self.positive_start_point, self.negative_start_point, self.positive_start_point),
            },
            # right bottom
            "direction_8": {
                "vector_A": mdc.vec3(self.positive_start_point, self.negative_start_point, self.negative_start_point),
                "vector_B": mdc.vec3(self.positive_start_point - self.width_A, self.negative_start_point,
                                     self.negative_start_point),
                "vector_C": mdc.vec3(self.positive_start_point - self.width_B, self.positive_start_point,
                                     self.negative_start_point),
                "vector_D": mdc.vec3(self.positive_start_point, self.positive_start_point, self.negative_start_point)
            },
        }

        self.depth = {"direction_1": -self.depth * mdc.Z,
                      "direction_2": self.depth * mdc.Z,
                      "direction_3": -self.depth * mdc.Z,
                      "direction_4": self.depth * mdc.Z,
                      "direction_5": -self.depth * mdc.Z,
                      "direction_6": self.depth * mdc.Z,
                      "direction_7": -self.depth * mdc.Z,
                      "direction_8": self.depth * mdc.Z}

    def transformation(self):
        _slanted_through_step = [
            mdc.Segment(self.slanted_vectors[self.dir]["vector_A"], self.slanted_vectors[self.dir]["vector_B"]),
            mdc.Segment(self.slanted_vectors[self.dir]["vector_B"], self.slanted_vectors[self.dir]["vector_C"]),
            mdc.Segment(self.slanted_vectors[self.dir]["vector_C"], self.slanted_vectors[self.dir]["vector_D"]),
            mdc.Segment(self.slanted_vectors[self.dir]["vector_D"], self.slanted_vectors[self.dir]["vector_A"])]

        _slanted_through_step = mdc.extrusion(self.depth[self.dir], mdc.flatsurface(_slanted_through_step))

        return _slanted_through_step
