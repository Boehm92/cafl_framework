import math
import numpy as np
import madcad as mdc


class Round:
    def __init__(self, limit):
        self.dir = np.random.choice(["direction_1", "direction_2", "direction_3", "direction_4", "direction_5",
                                     "direction_6", "direction_7", "direction_8", "direction_9", "direction_10",
                                     "direction_11", "direction_12"])
        self.limit = limit
        self.radius = np.random.uniform(1, (9 * self.limit))
        self.length = self.radius - (self.radius * math.sin(math.radians(45)))
        self.width = self.radius - (self.radius * math.sin(math.radians(45)))
        self.depth = 10.0004

        self.negative_start_point = -0.0002
        self.positive_start_point = 10.0002

        self.round_vectors = {
            # front side top edge
            "direction_1": {
                "vector_A": mdc.vec3(self.negative_start_point, self.negative_start_point,
                                     self.positive_start_point - self.radius),
                "vector_B": mdc.vec3(self.negative_start_point, self.negative_start_point, self.positive_start_point),
                "vector_C": mdc.vec3(self.negative_start_point, self.negative_start_point + self.radius,
                                     self.positive_start_point),
                "vector_D": mdc.vec3(self.negative_start_point, self.negative_start_point + self.length,
                                     self.positive_start_point - self.width)
            },
            # front side bottom edge
            "direction_2": {
                "vector_A": mdc.vec3(self.negative_start_point, self.negative_start_point + self.radius,
                                     self.negative_start_point),
                "vector_B": mdc.vec3(self.negative_start_point, self.negative_start_point, self.negative_start_point),
                "vector_C": mdc.vec3(self.negative_start_point, self.negative_start_point,
                                     self.negative_start_point + self.radius),
                "vector_D": mdc.vec3(self.negative_start_point, self.negative_start_point + self.length,
                                     self.negative_start_point + self.width)
            },
            # back side top edge
            "direction_3": {
                "vector_A": mdc.vec3(self.negative_start_point, self.positive_start_point - self.radius,
                                     self.positive_start_point),
                "vector_B": mdc.vec3(self.negative_start_point, self.positive_start_point, self.positive_start_point),
                "vector_C": mdc.vec3(self.negative_start_point, self.positive_start_point,
                                     self.positive_start_point - self.radius),
                "vector_D": mdc.vec3(self.negative_start_point, self.positive_start_point - self.length,
                                     self.positive_start_point - self.width)
            },
            # back side bottom edge
            "direction_4": {
                "vector_A": mdc.vec3(self.negative_start_point, self.positive_start_point,
                                     self.negative_start_point + self.radius),
                "vector_B": mdc.vec3(self.negative_start_point, self.positive_start_point, self.negative_start_point),
                "vector_C": mdc.vec3(self.negative_start_point, self.positive_start_point - self.radius,
                                     self.negative_start_point),
                "vector_D": mdc.vec3(self.negative_start_point, self.positive_start_point - self.length,
                                     self.negative_start_point + self.width)
            },
            # left side top edge
            "direction_5": {
                "vector_A": mdc.vec3(self.negative_start_point + self.radius, self.negative_start_point,
                                     self.positive_start_point),
                "vector_B": mdc.vec3(self.negative_start_point, self.negative_start_point, self.positive_start_point),
                "vector_C": mdc.vec3(self.negative_start_point, self.negative_start_point,
                                     self.positive_start_point - self.radius),
                "vector_D": mdc.vec3(self.negative_start_point + self.length, self.negative_start_point,
                                     self.positive_start_point - self.width)
            },
            # left side bottom edge
            "direction_6": {
                "vector_A": mdc.vec3(self.negative_start_point, self.negative_start_point,
                                     self.negative_start_point + self.radius),
                "vector_B": mdc.vec3(self.negative_start_point, self.negative_start_point, self.negative_start_point),
                "vector_C": mdc.vec3(self.negative_start_point + self.radius, self.negative_start_point,
                                     self.negative_start_point),
                "vector_D": mdc.vec3(self.negative_start_point + self.length, self.negative_start_point,
                                     self.negative_start_point + self.width)
            },
            # left side front edge
            "direction_7": {
                "vector_A": mdc.vec3(self.negative_start_point + self.radius, self.negative_start_point,
                                     self.negative_start_point),
                "vector_B": mdc.vec3(self.negative_start_point, self.negative_start_point, self.negative_start_point),
                "vector_C": mdc.vec3(self.negative_start_point, self.negative_start_point + self.radius,
                                     self.negative_start_point),
                "vector_D": mdc.vec3(self.negative_start_point + self.length, self.negative_start_point + self.width,
                                     self.negative_start_point)
            },
            # left side back edge
            "direction_8": {
                "vector_A": mdc.vec3(self.negative_start_point, self.positive_start_point - self.radius,
                                     self.negative_start_point),
                "vector_B": mdc.vec3(self.negative_start_point, self.positive_start_point, self.negative_start_point),
                "vector_C": mdc.vec3(self.negative_start_point + self.radius, self.positive_start_point,
                                     self.negative_start_point),
                "vector_D": mdc.vec3(self.negative_start_point + self.length, self.positive_start_point - self.width,
                                     self.negative_start_point)
            },
            # right side top edge
            "direction_9": {
                "vector_A": mdc.vec3(self.positive_start_point, self.negative_start_point,
                                     self.positive_start_point - self.radius),
                "vector_B": mdc.vec3(self.positive_start_point, self.negative_start_point, self.positive_start_point),

                "vector_C": mdc.vec3(self.positive_start_point - self.radius, self.negative_start_point,
                                     self.positive_start_point),
                "vector_D": mdc.vec3(self.positive_start_point - self.length, self.negative_start_point,
                                     self.positive_start_point - self.width)
            },
            # right side bottom edge
            "direction_10": {
                "vector_A": mdc.vec3(self.positive_start_point - self.radius, self.negative_start_point,
                                     self.negative_start_point),
                "vector_B": mdc.vec3(self.positive_start_point, self.negative_start_point, self.negative_start_point),
                "vector_C": mdc.vec3(self.positive_start_point, self.negative_start_point,
                                     self.negative_start_point + self.radius),
                "vector_D": mdc.vec3(self.positive_start_point - self.length, self.negative_start_point,
                                     self.negative_start_point + self.width)
            },
            # right side front edge
            "direction_11": {
                "vector_A": mdc.vec3(self.positive_start_point, self.negative_start_point + self.radius,
                                     self.negative_start_point),
                "vector_B": mdc.vec3(self.positive_start_point, self.negative_start_point, self.negative_start_point),
                "vector_C": mdc.vec3(self.positive_start_point - self.radius, self.negative_start_point,
                                     self.negative_start_point),
                "vector_D": mdc.vec3(self.positive_start_point - self.length, self.negative_start_point + self.width,
                                     self.negative_start_point)
            },
            # right side back edge
            "direction_12": {
                "vector_C": mdc.vec3(self.positive_start_point, self.positive_start_point - self.radius,
                                     self.negative_start_point),
                "vector_B": mdc.vec3(self.positive_start_point, self.positive_start_point, self.negative_start_point),
                "vector_A": mdc.vec3(self.positive_start_point - self.radius, self.positive_start_point,
                                     self.negative_start_point),
                "vector_D": mdc.vec3(self.positive_start_point - self.length, self.positive_start_point - self.width,
                                     self.negative_start_point)
            },
        }

        self.depth = {
            "direction_1": self.depth * mdc.X,
            "direction_2": self.depth * mdc.X,
            "direction_3": self.depth * mdc.X,
            "direction_4": self.depth * mdc.X,
            "direction_5": self.depth * mdc.Y,
            "direction_6": self.depth * mdc.Y,
            "direction_7": self.depth * mdc.Z,
            "direction_8": self.depth * mdc.Z,
            "direction_9": self.depth * mdc.Y,
            "direction_10": self.depth * mdc.Y,
            "direction_11": self.depth * mdc.Z,
            "direction_12": self.depth * mdc.Z,
        }

    def transformation(self):
        _round = [mdc.Segment(self.round_vectors[self.dir]["vector_A"], self.round_vectors[self.dir]["vector_B"]),
                  mdc.Segment(self.round_vectors[self.dir]["vector_B"], self.round_vectors[self.dir]["vector_C"]),
                  mdc.ArcThrough(self.round_vectors[self.dir]["vector_C"], self.round_vectors[self.dir]["vector_D"],
                                 self.round_vectors[self.dir]["vector_A"])]

        _round = mdc.extrusion(self.depth[self.dir], mdc.flatsurface(_round))

        return _round
