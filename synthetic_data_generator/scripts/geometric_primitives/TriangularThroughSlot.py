import math
import numpy as np
import madcad as mdc


class TriangularThroughSlot:
    def __init__(self, limit):
        self.dir = np.random.choice(["direction_1", "direction_2", "direction_3", "direction_4", "direction_5",
                                     "direction_6", "direction_7", "direction_8", "direction_9", "direction_10",
                                     "direction_11", "direction_12"])

        self.limit = limit
        self.length = np.random.uniform(1, 9 * self.limit)
        self.pos_x = np.random.uniform(0.5, 9.5 - self.length)
        self.pos_y = np.random.uniform(0.5, 9.5 - self.length)
        self.negative_start_point = -0.0002
        self.positive_start_point = 10.0002
        self.depth = 10.0004
        self.angle = math.sin(math.radians(60))

        self.triangle_vectors = {
            "direction_1": [mdc.vec3(self.pos_x + self.length, self.negative_start_point, self.negative_start_point),
                            mdc.vec3(self.pos_x, self.negative_start_point, self.negative_start_point),
                            mdc.vec3(self.pos_x + (self.length / 2),
                                     self.pos_y + (self.length * self.angle), self.negative_start_point)],

            "direction_2": [mdc.vec3(self.negative_start_point, self.negative_start_point, self.pos_x),
                            mdc.vec3(self.negative_start_point, self.negative_start_point, self.pos_x + self.length),
                            mdc.vec3(self.negative_start_point, self.pos_y + (self.length * self.angle),
                                     self.pos_x + (self.length / 2))],

            "direction_3": [mdc.vec3(self.pos_x, self.positive_start_point, self.negative_start_point),
                            mdc.vec3(self.pos_x + self.length, self.positive_start_point, self.negative_start_point),
                            mdc.vec3(self.pos_x + (self.length / 2),
                                     self.positive_start_point - (self.length * self.angle),
                                     self.negative_start_point)],

            "direction_4": [mdc.vec3(self.positive_start_point, self.positive_start_point, self.pos_x),
                            mdc.vec3(self.positive_start_point, self.positive_start_point, self.pos_x + self.length),
                            mdc.vec3(self.positive_start_point, self.positive_start_point - (self.length * self.angle),
                                     self.pos_x + (self.length / 2))],

            "direction_5": [mdc.vec3(self.pos_x, self.negative_start_point, self.negative_start_point),
                            mdc.vec3(self.pos_x + self.length, self.negative_start_point, self.negative_start_point),
                            mdc.vec3(self.pos_x + (self.length / 2),
                                     self.negative_start_point, self.pos_y + (self.length * self.angle))],

            "direction_6": [mdc.vec3(self.positive_start_point, self.pos_x, self.negative_start_point),
                            mdc.vec3(self.positive_start_point, self.pos_x + self.length, self.negative_start_point),
                            mdc.vec3(self.positive_start_point, self.pos_x + (self.length / 2),
                                     self.pos_y + (self.length * self.angle))],

            "direction_7": [mdc.vec3(self.pos_x + self.length, self.negative_start_point, self.positive_start_point),
                            mdc.vec3(self.pos_x, self.negative_start_point, self.positive_start_point),
                            mdc.vec3(self.pos_x + (self.length / 2), self.negative_start_point,
                                     self.positive_start_point - (self.length * self.angle))],

            "direction_8": [mdc.vec3(self.positive_start_point, self.pos_x + self.length, self.positive_start_point),
                            mdc.vec3(self.positive_start_point, self.pos_x, self.positive_start_point),
                            mdc.vec3(self.positive_start_point, self.pos_x + (self.length / 2),
                                     self.positive_start_point - (self.length * self.angle))],

            "direction_9": [mdc.vec3(self.negative_start_point, self.negative_start_point, self.pos_y + self.length),
                            mdc.vec3(self.negative_start_point, self.negative_start_point, self.pos_y),
                            mdc.vec3(self.negative_start_point + (self.length * self.angle), self.negative_start_point,
                                     self.pos_y + (self.length / 2))],

            "direction_10": [mdc.vec3(self.negative_start_point, self.pos_y, self.negative_start_point),
                             mdc.vec3(self.negative_start_point, self.pos_y + self.length, self.negative_start_point),
                             mdc.vec3(self.negative_start_point + (self.length * self.angle),
                                      self.pos_y + (self.length / 2), self.negative_start_point)],

            "direction_11": [mdc.vec3(self.positive_start_point, self.negative_start_point, self.pos_y),
                             mdc.vec3(self.positive_start_point, self.negative_start_point, self.pos_y + self.length),
                             mdc.vec3(self.positive_start_point - (self.length * self.angle), self.negative_start_point,
                                      self.pos_y + (self.length / 2))],

            "direction_12": [mdc.vec3(self.positive_start_point, self.pos_y + self.length, self.negative_start_point),
                             mdc.vec3(self.positive_start_point, self.pos_y, self.negative_start_point),
                             mdc.vec3(self.positive_start_point - (self.length * self.angle),
                                      self.pos_y + (self.length / 2), self.negative_start_point)],
        }

        self.dept = {
            "direction_1": self.depth * mdc.Z,
            "direction_2": self.depth * mdc.X,
            "direction_3": self.depth * mdc.Z,
            "direction_4": -self.depth * mdc.X,
            "direction_5": self.depth * mdc.Y,
            "direction_6": -self.depth * mdc.X,
            "direction_7": self.depth * mdc.Y,
            "direction_8": -self.depth * mdc.X,
            "direction_9": self.depth * mdc.Y,
            "direction_10": self.depth * mdc.Z,
            "direction_11": self.depth * mdc.Y,
            "direction_12": self.depth * mdc.Z,
        }

    def transformation(self):
        _triangular_primitive = [mdc.Segment(self.triangle_vectors[self.dir][0], self.triangle_vectors[self.dir][1]),
                                 mdc.Segment(self.triangle_vectors[self.dir][1], self.triangle_vectors[self.dir][2]),
                                 mdc.Segment(self.triangle_vectors[self.dir][2], self.triangle_vectors[self.dir][0])],

        _triangular_passage = mdc.extrusion(self.dept[self.dir], mdc.flatsurface(_triangular_primitive))

        return _triangular_passage
