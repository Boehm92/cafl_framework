import math
import numpy as np
import madcad as mdc


class SixSidePocket:
    def __init__(self, limit):
        self.dir = np.random.choice(["direction_1", "direction_2", "direction_3", "direction_4", "direction_5",
                                     "direction_6"])
        self.limit = limit
        self.radius = np.random.uniform(1, (4.5 * self.limit))
        self.Cx = np.random.uniform(0.5 + self.radius, 9.5 - self.radius)
        self.Cy = np.random.uniform(0.5 + self.radius, 9.5 - self.radius)
        self.depth = np.random.uniform(1, 9)
        self.negative_start_point = -0.0002
        self.positive_start_point = 10.0002

        self.six_side_vectors = {
            # top side
            "direction_1": {
                "vector_A": mdc.vec3(self.Cx - self.radius, self.Cy, self.positive_start_point),
                "vector_B": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-120)),
                                     self.Cy + self.radius * math.sin(math.radians(-120)), self.positive_start_point),
                "vector_C": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-60)),
                                     self.Cy + self.radius * math.sin(math.radians(-60)), self.positive_start_point),
                "vector_D": mdc.vec3(self.Cx + self.radius, self.Cy, self.positive_start_point),
                "vector_E": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-300)),
                                     self.Cy + self.radius * math.sin(math.radians(-300)), self.positive_start_point),
                "vector_F": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-240)),
                                     self.Cy + self.radius * math.sin(math.radians(-240)), self.positive_start_point),
            },
            # bottom side
            "direction_2": {
                "vector_A": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-240)),
                                     self.Cy + self.radius * math.sin(math.radians(-240)), self.negative_start_point),
                "vector_B": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-300)),
                                     self.Cy + self.radius * math.sin(math.radians(-300)), self.negative_start_point),
                "vector_C": mdc.vec3(self.Cx + self.radius, self.Cy, self.negative_start_point),
                "vector_D": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-60)),
                                     self.Cy + self.radius * math.sin(math.radians(-60)), self.negative_start_point),
                "vector_E": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-120)),
                                     self.Cy + self.radius * math.sin(math.radians(-120)), self.negative_start_point),
                "vector_F": mdc.vec3(self.Cx - self.radius, self.Cy, self.negative_start_point),
            },
            # front side
            "direction_3": {
                "vector_A": mdc.vec3(self.Cx - self.radius, self.negative_start_point, self.Cy),
                "vector_B": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-120)),
                                     self.negative_start_point, self.Cy + self.radius * math.sin(math.radians(-120))),
                "vector_C": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-60)),
                                     self.negative_start_point,
                                     self.Cy + self.radius * math.sin(math.radians(-60))),
                "vector_D": mdc.vec3(self.Cx + self.radius, self.negative_start_point, self.Cy),
                "vector_E": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-300)), self.negative_start_point,
                                     self.Cy + self.radius * math.sin(math.radians(-300))),
                "vector_F": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-240)), self.negative_start_point,
                                     self.Cy + self.radius * math.sin(math.radians(-240))),
            },
            # back side
            "direction_4": {
                "vector_A": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-240)), self.positive_start_point,
                                     self.Cy + self.radius * math.sin(math.radians(-240))),
                "vector_B": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-300)), self.positive_start_point,
                                     self.Cy + self.radius * math.sin(math.radians(-300))),
                "vector_C": mdc.vec3(self.Cx + self.radius, self.positive_start_point, self.Cy, ),
                "vector_D": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-60)),
                                     self.positive_start_point, self.Cy + self.radius * math.sin(math.radians(-60))),
                "vector_E": mdc.vec3(self.Cx + self.radius * math.cos(math.radians(-120)),
                                     self.positive_start_point, self.Cy + self.radius * math.sin(math.radians(-120))),
                "vector_F": mdc.vec3(self.Cx - self.radius, self.positive_start_point, self.Cy)},
            # right side
            "direction_5": {
                "vector_A": mdc.vec3(self.negative_start_point, self.Cx + self.radius * math.cos(math.radians(-240)),
                                     self.Cy + self.radius * math.sin(math.radians(-240))),
                "vector_B": mdc.vec3(self.negative_start_point, self.Cx + self.radius * math.cos(math.radians(-300)),
                                     self.Cy + self.radius * math.sin(math.radians(-300))),
                "vector_C": mdc.vec3(self.negative_start_point, self.Cx + self.radius, self.Cy),
                "vector_D": mdc.vec3(self.negative_start_point, self.Cx + self.radius * math.cos(math.radians(-60)),
                                     self.Cy + self.radius * math.sin(math.radians(-60))),
                "vector_E": mdc.vec3(self.negative_start_point, self.Cx + self.radius * math.cos(math.radians(-120)),
                                     self.Cy + self.radius * math.sin(math.radians(-120))),
                "vector_F": mdc.vec3(self.negative_start_point, self.Cx - self.radius, self.Cy)},
            # right side
            "direction_6": {
                "vector_A": mdc.vec3(self.positive_start_point, self.Cx - self.radius, self.Cy),
                "vector_B": mdc.vec3(self.positive_start_point, self.Cx + self.radius * math.cos(math.radians(-120)),
                                     self.Cy + self.radius * math.sin(math.radians(-120))),
                "vector_C": mdc.vec3(self.positive_start_point, self.Cx + self.radius * math.cos(math.radians(-60)),
                                     self.Cy + self.radius * math.sin(math.radians(-60))),
                "vector_D": mdc.vec3(self.positive_start_point, self.Cx + self.radius, self.Cy),
                "vector_E": mdc.vec3(self.positive_start_point, self.Cx + self.radius * math.cos(math.radians(-300)),
                                     self.Cy + self.radius * math.sin(math.radians(-300))),
                "vector_F": mdc.vec3(self.positive_start_point, self.Cx + self.radius * math.cos(math.radians(-240)),
                                     self.Cy + self.radius * math.sin(math.radians(-240)))},
        }

        self.depth = {
            "direction_1": -self.depth * mdc.Z,
            "direction_2": self.depth * mdc.Z,
            "direction_3": self.depth * mdc.Y,
            "direction_4": -self.depth * mdc.Y,
            "direction_5": self.depth * mdc.X,
            "direction_6": -self.depth * mdc.X,
        }

    def transformation(self):
        _six_side_passage_primitive = [mdc.Segment(self.six_side_vectors[self.dir]["vector_A"],
                                                   self.six_side_vectors[self.dir]["vector_B"]),
                                       mdc.Segment(self.six_side_vectors[self.dir]["vector_B"],
                                                   self.six_side_vectors[self.dir]["vector_C"]),
                                       mdc.Segment(self.six_side_vectors[self.dir]["vector_C"],
                                                   self.six_side_vectors[self.dir]["vector_D"]),
                                       mdc.Segment(self.six_side_vectors[self.dir]["vector_D"],
                                                   self.six_side_vectors[self.dir]["vector_E"]),
                                       mdc.Segment(self.six_side_vectors[self.dir]["vector_E"],
                                                   self.six_side_vectors[self.dir]["vector_F"]),
                                       mdc.Segment(self.six_side_vectors[self.dir]["vector_F"],
                                                   self.six_side_vectors[self.dir]["vector_A"])],

        _six_side_passage = mdc.extrusion(self.depth[self.dir], mdc.flatsurface(_six_side_passage_primitive))

        return _six_side_passage
