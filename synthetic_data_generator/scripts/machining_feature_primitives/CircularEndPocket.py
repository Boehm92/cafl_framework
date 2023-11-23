import numpy as np
import madcad as mdc


class CircularEndPocket:
    def __init__(self, limit):
        self.dir = np.random.choice(["direction_1", "direction_2", "direction_3", "direction_4", "direction_5",
                                     "direction_6", "direction_7", "direction_8", "direction_9", "direction_10",
                                     "direction_11", "direction_12"])
        self.limit = limit
        self.width = np.random.uniform(1, (8 * self.limit))
        self.length = np.random.uniform(1, (9 * self.limit) - self.width)
        self.depth = np.random.uniform(1, 9)
        self.X = np.random.uniform(0.5, 9 - self.width)
        self.Y = np.random.uniform(0.5, 9.5 - (self.width + self.length))

        self.negative_start_point = -0.0002
        self.positive_start_point = 10.0002

        self.circular_vectors = {
            # bottom side
            "direction_1": {
                "vector_A": mdc.vec3(self.X, self.Y + (self.length + (self.width / 2)), self.negative_start_point),
                "vector_B": mdc.vec3(self.X + (self.width / 2), self.Y + (self.length + self.width),
                                     self.negative_start_point),
                "vector_C": mdc.vec3(self.X + self.width, self.Y + (self.length + (self.width / 2)),
                                     self.negative_start_point),
                "vector_D": mdc.vec3(self.X + self.width, self.Y + (self.width / 2), self.negative_start_point),
                "vector_E": mdc.vec3(self.X + (self.width / 2), self.Y, self.negative_start_point),
                "vector_F": mdc.vec3(self.X, self.Y + (self.width / 2), self.negative_start_point),
            },

            "direction_2": {
                "vector_A": mdc.vec3(self.Y + (self.width / 2), self.X, self.negative_start_point),
                "vector_B": mdc.vec3(self.Y, self.X + (self.width / 2), self.negative_start_point),
                "vector_C": mdc.vec3(self.Y + (self.width / 2), self.X + self.width, self.negative_start_point),
                "vector_D": mdc.vec3(self.Y + (self.length + (self.width / 2)), self.X + self.width,
                                     self.negative_start_point),
                "vector_E": mdc.vec3(self.Y + (self.length + self.width), self.X + (self.width / 2),
                                     self.negative_start_point),
                "vector_F": mdc.vec3(self.Y + (self.length + (self.width / 2)), self.X, self.negative_start_point),
            },

            # upper side
            "direction_3": {
                "vector_A": mdc.vec3(self.X, self.Y + (self.width / 2), self.positive_start_point),
                "vector_B": mdc.vec3(self.X + (self.width / 2), self.Y, self.positive_start_point),
                "vector_C": mdc.vec3(self.X + self.width, self.Y + (self.width / 2), self.positive_start_point),
                "vector_D": mdc.vec3(self.X + self.width, self.Y + (self.length + (self.width / 2)),
                                     self.positive_start_point),
                "vector_E": mdc.vec3(self.X + (self.width / 2), self.Y + (self.length + self.width),
                                     self.positive_start_point),
                "vector_F": mdc.vec3(self.X, self.Y + (self.length + (self.width / 2)), self.positive_start_point),
            },

            "direction_4": {
                "vector_A": mdc.vec3(self.Y + (self.length + (self.width / 2)), self.X, self.positive_start_point),
                "vector_B": mdc.vec3(self.Y + (self.length + self.width), self.X + (self.width / 2),
                                     self.positive_start_point),
                "vector_C": mdc.vec3(self.Y + (self.length + (self.width / 2)), self.X + self.width,
                                     self.positive_start_point),
                "vector_D": mdc.vec3(self.Y + (self.width / 2), self.X + self.width, self.positive_start_point),
                "vector_E": mdc.vec3(self.Y, self.X + (self.width / 2), self.positive_start_point),
                "vector_F": mdc.vec3(self.Y + (self.width / 2), self.X, self.positive_start_point),
            },

            "direction_5": {
                "vector_A": mdc.vec3(self.X, self.negative_start_point, self.Y + (self.width / 2)),
                "vector_B": mdc.vec3(self.X + (self.width / 2), self.negative_start_point, self.Y),
                "vector_C": mdc.vec3(self.X + self.width, self.negative_start_point, self.Y + (self.width / 2)),
                "vector_D": mdc.vec3(self.X + self.width, self.negative_start_point,
                                     self.Y + (self.length + (self.width / 2))),
                "vector_E": mdc.vec3(self.X + (self.width / 2), self.negative_start_point,
                                     self.Y + (self.length + self.width)),
                "vector_F": mdc.vec3(self.X, self.negative_start_point, self.Y + (self.length + (self.width / 2))),
            },

            # front side
            "direction_6": {
                "vector_A": mdc.vec3(self.Y + (self.length + (self.width / 2)), self.negative_start_point, self.X),
                "vector_B": mdc.vec3(self.Y + (self.length + self.width), self.negative_start_point,
                                     self.X + (self.width / 2)),
                "vector_C": mdc.vec3(self.Y + (self.length + (self.width / 2)), self.negative_start_point,
                                     self.X + self.width),
                "vector_D": mdc.vec3(self.Y + (self.width / 2), self.negative_start_point, self.X + self.width),
                "vector_E": mdc.vec3(self.Y, self.negative_start_point, self.X + (self.width / 2)),
                "vector_F": mdc.vec3(self.Y + (self.width / 2), self.negative_start_point, self.X),
            },

            "direction_7": {
                "vector_A": mdc.vec3(self.X, self.positive_start_point, self.Y + (self.length + (self.width / 2))),
                "vector_B": mdc.vec3(self.X + (self.width / 2), self.positive_start_point,
                                     self.Y + (self.length + self.width)),
                "vector_C": mdc.vec3(self.X + self.width, self.positive_start_point,
                                     self.Y + (self.length + (self.width / 2))),
                "vector_D": mdc.vec3(self.X + self.width, self.positive_start_point, self.Y + (self.width / 2)),
                "vector_E": mdc.vec3(self.X + (self.width / 2), self.positive_start_point, self.Y),
                "vector_F": mdc.vec3(self.X, self.positive_start_point, self.Y + (self.width / 2)),
            },

            # back side
            "direction_8": {
                "vector_A": mdc.vec3(self.Y + (self.width / 2), self.positive_start_point, self.X),
                "vector_B": mdc.vec3(self.Y, self.positive_start_point, self.X + (self.width / 2)),
                "vector_C": mdc.vec3(self.Y + (self.width / 2), self.positive_start_point, self.X + self.width),
                "vector_D": mdc.vec3(self.Y + (self.length + (self.width / 2)), self.positive_start_point,
                                     self.X + self.width),
                "vector_E": mdc.vec3(self.Y + (self.length + self.width), self.positive_start_point,
                                     self.X + (self.width / 2)),
                "vector_F": mdc.vec3(self.Y + (self.length + (self.width / 2)), self.positive_start_point, self.X)
            },

            # left side
            "direction_9": {
                "vector_A": mdc.vec3(self.negative_start_point, self.X, self.Y + (self.length + (self.width / 2))),
                "vector_B": mdc.vec3(self.negative_start_point, self.X + (self.width / 2),
                                     self.Y + (self.length + self.width)),
                "vector_C": mdc.vec3(self.negative_start_point, self.X + self.width,
                                     self.Y + (self.length + (self.width / 2))),
                "vector_D": mdc.vec3(self.negative_start_point, self.X + self.width, self.Y + (self.width / 2)),
                "vector_E": mdc.vec3(self.negative_start_point, self.X + (self.width / 2), self.Y),
                "vector_F": mdc.vec3(self.negative_start_point, self.X, self.Y + (self.width / 2)),
            },

            "direction_10": {
                "vector_A": mdc.vec3(self.negative_start_point, self.Y + (self.width / 2), self.X),
                "vector_B": mdc.vec3(self.negative_start_point, self.Y, self.X + (self.width / 2)),
                "vector_C": mdc.vec3(self.negative_start_point, self.Y + (self.width / 2), self.X + self.width),
                "vector_D": mdc.vec3(self.negative_start_point, self.Y + (self.length + (self.width / 2)),
                                     self.X + self.width),
                "vector_E": mdc.vec3(self.negative_start_point, self.Y + (self.length + self.width),
                                     self.X + (self.width / 2)),
                "vector_F": mdc.vec3(self.negative_start_point, self.Y + (self.length + (self.width / 2)), self.X),
            },

            # right side
            "direction_11": {
                "vector_A": mdc.vec3(self.positive_start_point, self.X, self.Y + (self.width / 2)),
                "vector_B": mdc.vec3(self.positive_start_point, self.X + (self.width / 2), self.Y),
                "vector_C": mdc.vec3(self.positive_start_point, self.X + self.width, self.Y + (self.width / 2)),
                "vector_D": mdc.vec3(self.positive_start_point, self.X + self.width,
                                     self.Y + (self.length + (self.width / 2))),
                "vector_E": mdc.vec3(self.positive_start_point, self.X + (self.width / 2),
                                     self.Y + (self.length + self.width)),
                "vector_F": mdc.vec3(self.positive_start_point, self.X, self.Y + (self.length + (self.width / 2))),
            },

            "direction_12": {
                "vector_A": mdc.vec3(self.positive_start_point, self.Y + (self.length + (self.width / 2)), self.X),
                "vector_B": mdc.vec3(self.positive_start_point, self.Y + (self.length + self.width),
                                     self.X + (self.width / 2)),
                "vector_C": mdc.vec3(self.positive_start_point, self.Y + (self.length + (self.width / 2)),
                                     self.X + self.width),
                "vector_D": mdc.vec3(self.positive_start_point, self.Y + (self.width / 2), self.X + self.width),
                "vector_E": mdc.vec3(self.positive_start_point, self.Y, self.X + (self.width / 2), ),
                "vector_F": mdc.vec3(self.positive_start_point, self.Y + (self.width / 2), self.X),
            },
        }

        self.dept = {
            "direction_1": self.depth * mdc.Z,
            "direction_2": self.depth * mdc.Z,
            "direction_3": -self.depth * mdc.Z,
            "direction_4": -self.depth * mdc.Z,
            "direction_5": self.depth * mdc.Y,
            "direction_6": self.depth * mdc.Y,
            "direction_7": -self.depth * mdc.Y,
            "direction_8": -self.depth * mdc.Y,
            "direction_9": self.depth * mdc.X,
            "direction_10": self.depth * mdc.X,
            "direction_11": -self.depth * mdc.X,
            "direction_12": -self.depth * mdc.X,
        }

    def transformation(self):
        _circular_end_pocket_primitive = [mdc.ArcThrough(self.circular_vectors[self.dir]["vector_A"],
                                                         self.circular_vectors[self.dir]["vector_B"],
                                                         self.circular_vectors[self.dir]["vector_C"]),
                                          mdc.Segment(self.circular_vectors[self.dir]["vector_C"],
                                                      self.circular_vectors[self.dir]["vector_D"]),
                                          mdc.ArcThrough(self.circular_vectors[self.dir]["vector_D"],
                                                         self.circular_vectors[self.dir]["vector_E"],
                                                         self.circular_vectors[self.dir]["vector_F"]),
                                          mdc.Segment(self.circular_vectors[self.dir]["vector_F"],
                                                      self.circular_vectors[self.dir]["vector_A"])],

        _circular_end_pocket = mdc.extrusion(self.dept[self.dir], mdc.flatsurface(_circular_end_pocket_primitive))

        return _circular_end_pocket
