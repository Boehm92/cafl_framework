import numpy as np
import madcad as mdc


class VerticalCircularEndBlindSlot:
    def __init__(self, limit):
        self.dir = np.random.choice(["direction_1", "direction_2", "direction_3", "direction_4", "direction_5",
                                     "direction_6", "direction_7", "direction_8", "direction_9", "direction_10",
                                     "direction_11", "direction_12", "direction_13", "direction_14", "direction_15",
                                     "direction_16", "direction_17", "direction_18", "direction_19", "direction_20",
                                     "direction_21", "direction_22", "direction_23", "direction_24"])
        self.limit = limit
        self.edge_position = np.random.uniform(0.5, (8 * self.limit))
        self.width = np.random.uniform(1, (9 * self.limit) - self.edge_position)
        self.length = np.random.uniform(1, (9.5 * self.limit) - self.width)
        self.depth = np.random.uniform(1, 9)

        self.negative_start_point = -0.0002
        self.positive_start_point = 10.0002

        self.circular_vectors = {
            # front side bottom edge
            "direction_1": {
                "vector_A": mdc.vec3(self.edge_position, self.negative_start_point, self.negative_start_point),
                "vector_B": mdc.vec3(self.edge_position + self.width, self.negative_start_point,
                                     self.negative_start_point),
                "vector_C": mdc.vec3((self.edge_position + self.width), self.negative_start_point, self.length),
                "vector_D": mdc.vec3((self.edge_position + (self.width / 2)), self.negative_start_point,
                                     (self.length + (self.width / 2))),
                "vector_E": mdc.vec3(self.edge_position, self.negative_start_point, self.length)
            },
            # front side top edge
            "direction_2": {
                "vector_A": mdc.vec3(self.edge_position + self.width, self.negative_start_point,
                                     self.positive_start_point),
                "vector_B": mdc.vec3(self.edge_position, self.negative_start_point, self.positive_start_point),
                "vector_C": mdc.vec3(self.edge_position, self.negative_start_point,
                                     self.positive_start_point - self.length),
                "vector_D": mdc.vec3((self.edge_position + (self.width / 2)), self.negative_start_point,
                                     self.positive_start_point - (self.length + (self.width / 2))),
                "vector_E": mdc.vec3((self.edge_position + self.width), self.negative_start_point,
                                     self.positive_start_point - self.length)
            },
            # front side left edge
            "direction_3": {
                "vector_A": mdc.vec3(self.negative_start_point, self.negative_start_point,
                                     self.edge_position + self.width),
                "vector_B": mdc.vec3(self.negative_start_point, self.negative_start_point,
                                     self.edge_position),
                "vector_C": mdc.vec3(self.length, self.negative_start_point, self.edge_position),
                "vector_D": mdc.vec3((self.length + (self.width / 2)), self.negative_start_point,
                                     (self.edge_position + (self.width / 2))),
                "vector_E": mdc.vec3(self.length, self.negative_start_point,
                                     self.edge_position + self.width)
            },
            # front side right edge
            "direction_4": {
                "vector_B": mdc.vec3(self.positive_start_point, self.negative_start_point,
                                     self.edge_position + self.width),
                "vector_A": mdc.vec3(self.positive_start_point, self.negative_start_point,
                                     self.edge_position),
                "vector_E": mdc.vec3(self.positive_start_point - self.length, self.negative_start_point,
                                     self.edge_position),
                "vector_D": mdc.vec3(self.positive_start_point - (self.length + (self.width / 2)),
                                     self.negative_start_point,
                                     (self.edge_position + (self.width / 2))),
                "vector_C": mdc.vec3(self.positive_start_point - self.length, self.negative_start_point,
                                     self.edge_position + self.width)
            },
            # back side bottom edge
            "direction_5": {
                "vector_A": mdc.vec3(self.edge_position + self.width, self.positive_start_point,
                                     self.negative_start_point),
                "vector_B": mdc.vec3(self.edge_position, self.positive_start_point, self.negative_start_point),
                "vector_C": mdc.vec3(self.edge_position, self.positive_start_point, self.length),
                "vector_D": mdc.vec3((self.edge_position + (self.width / 2)), self.positive_start_point,
                                     (self.length + (self.width / 2))),
                "vector_E": mdc.vec3((self.edge_position + self.width), self.positive_start_point, self.length)
            },
            # back side top edge
            "direction_6": {
                "vector_A": mdc.vec3(self.edge_position, self.positive_start_point, self.positive_start_point),
                "vector_B": mdc.vec3(self.edge_position + self.width, self.positive_start_point,
                                     self.positive_start_point),
                "vector_C": mdc.vec3((self.edge_position + self.width), self.positive_start_point,
                                     self.positive_start_point - self.length),
                "vector_D": mdc.vec3((self.edge_position + (self.width / 2)), self.positive_start_point,
                                     self.positive_start_point - (self.length + (self.width / 2))),
                "vector_E": mdc.vec3(self.edge_position, self.positive_start_point,
                                     self.positive_start_point - self.length)
            },
            # back side left edge
            "direction_7": {
                "vector_A": mdc.vec3(self.negative_start_point, self.positive_start_point,
                                     self.edge_position),
                "vector_B": mdc.vec3(self.negative_start_point, self.positive_start_point,
                                     self.edge_position + self.width),
                "vector_C": mdc.vec3(self.length, self.positive_start_point,
                                     self.edge_position + self.width),
                "vector_D": mdc.vec3((self.length + (self.width / 2)), self.positive_start_point,
                                     (self.edge_position + (self.width / 2))),
                "vector_E": mdc.vec3(self.length, self.positive_start_point, self.edge_position)
            },
            # back side right edge
            "direction_8": {
                "vector_A": mdc.vec3(self.positive_start_point, self.positive_start_point,
                                     self.edge_position + self.width),
                "vector_B": mdc.vec3(self.positive_start_point, self.positive_start_point,
                                     self.edge_position),
                "vector_C": mdc.vec3(self.positive_start_point - self.length, self.positive_start_point,
                                     self.edge_position),
                "vector_D": mdc.vec3(self.positive_start_point - (self.length + (self.width / 2)),
                                     self.positive_start_point,
                                     (self.edge_position + (self.width / 2))),
                "vector_E": mdc.vec3(self.positive_start_point - self.length, self.positive_start_point,
                                     self.edge_position + self.width)
            },
            # top side front edge
            "direction_9": {
                "vector_A": mdc.vec3(self.edge_position, self.negative_start_point, self.positive_start_point),
                "vector_B": mdc.vec3(self.edge_position + self.width, self.negative_start_point,
                                     self.positive_start_point),
                "vector_C": mdc.vec3((self.edge_position + self.width), self.length, self.positive_start_point),
                "vector_E": mdc.vec3(self.edge_position, self.length, self.positive_start_point),
                "vector_D": mdc.vec3((self.edge_position + (self.width / 2)), (self.length + (self.width / 2)),
                                     self.positive_start_point)
            },
            # tob side back edge
            "direction_10": {
                "vector_A": mdc.vec3(self.edge_position + self.width, self.positive_start_point,
                                     self.positive_start_point),
                "vector_B": mdc.vec3(self.edge_position, self.positive_start_point, self.positive_start_point),
                "vector_C": mdc.vec3(self.edge_position, self.positive_start_point - self.length,
                                     self.positive_start_point),
                "vector_D": mdc.vec3((self.edge_position + (self.width / 2)),
                                     self.positive_start_point - (self.length + (self.width / 2)),
                                     self.positive_start_point),
                "vector_E": mdc.vec3((self.edge_position + self.width), self.positive_start_point - self.length,
                                     self.positive_start_point)
            },
            # top side left edge
            "direction_11": {
                "vector_A": mdc.vec3(self.negative_start_point, self.edge_position + self.width,
                                     self.positive_start_point),
                "vector_B": mdc.vec3(self.negative_start_point, self.edge_position, self.positive_start_point),
                "vector_C": mdc.vec3(self.length, self.edge_position, self.positive_start_point),  #
                "vector_D": mdc.vec3((self.length + (self.width / 2)), (self.edge_position + (self.width / 2)),
                                     self.positive_start_point),
                "vector_E": mdc.vec3(self.length, (self.edge_position + self.width), self.positive_start_point)
            },
            # top side right edge
            "direction_12": {
                "vector_A": mdc.vec3(self.positive_start_point, self.edge_position, self.positive_start_point),
                "vector_B": mdc.vec3(self.positive_start_point, self.edge_position + self.width,
                                     self.positive_start_point),
                "vector_C": mdc.vec3(self.positive_start_point - self.length, (self.edge_position + self.width),
                                     self.positive_start_point),
                "vector_D": mdc.vec3(self.positive_start_point - (self.length + (self.width / 2)),
                                     (self.edge_position + (self.width / 2)),
                                     self.positive_start_point),
                "vector_E": mdc.vec3(self.positive_start_point - self.length, self.edge_position,
                                     self.positive_start_point)
            },
            # bottom side front edge
            "direction_13": {
                "vector_A": mdc.vec3(self.edge_position + self.width, self.negative_start_point,
                                     self.negative_start_point),
                "vector_B": mdc.vec3(self.edge_position, self.negative_start_point, self.negative_start_point),
                "vector_C": mdc.vec3(self.edge_position, self.length, self.negative_start_point),
                "vector_D": mdc.vec3((self.edge_position + (self.width / 2)), (self.length + (self.width / 2)),
                                     self.negative_start_point),
                "vector_E": mdc.vec3((self.edge_position + self.width), self.length, self.negative_start_point)
            },
            # bottom side back edge
            "direction_14": {
                "vector_A": mdc.vec3(self.edge_position, self.positive_start_point, self.negative_start_point),
                "vector_B": mdc.vec3(self.edge_position + self.width, self.positive_start_point,
                                     self.negative_start_point),
                "vector_C": mdc.vec3((self.edge_position + self.width), self.positive_start_point - self.length,
                                     self.negative_start_point),
                "vector_D": mdc.vec3((self.edge_position + (self.width / 2)),
                                     self.positive_start_point - (self.length + (self.width / 2)),
                                     self.negative_start_point),
                "vector_E": mdc.vec3(self.edge_position, self.positive_start_point - self.length,
                                     self.negative_start_point)
            },
            # bottom side left edge
            "direction_15": {
                "vector_B": mdc.vec3(self.negative_start_point, self.edge_position + self.width,
                                     self.negative_start_point),
                "vector_A": mdc.vec3(self.negative_start_point, self.edge_position, self.negative_start_point),
                "vector_E": mdc.vec3(self.length, self.edge_position, self.negative_start_point),
                "vector_D": mdc.vec3((self.length + (self.width / 2)), (self.edge_position + (self.width / 2)),
                                     self.negative_start_point),
                "vector_C": mdc.vec3(self.length, (self.edge_position + self.width), self.negative_start_point)
            },
            # bottom side right edge
            "direction_16": {
                "vector_A": mdc.vec3(self.positive_start_point, self.edge_position + self.width,
                                     self.negative_start_point),
                "vector_B": mdc.vec3(self.positive_start_point, self.edge_position, self.negative_start_point),
                "vector_C": mdc.vec3(self.positive_start_point - self.length, self.edge_position,
                                     self.negative_start_point),
                "vector_D": mdc.vec3(self.positive_start_point - (self.length + (self.width / 2)),
                                     (self.edge_position + (self.width / 2)), self.negative_start_point),
                "vector_E": mdc.vec3(self.positive_start_point - self.length, (self.edge_position + self.width),
                                     self.negative_start_point)
            },
            # left side top edge
            "direction_17": {
                "vector_A": mdc.vec3(self.negative_start_point, self.edge_position, self.positive_start_point),
                "vector_B": mdc.vec3(self.negative_start_point, self.edge_position + self.width,
                                     self.positive_start_point),
                "vector_C": mdc.vec3(self.negative_start_point, (self.edge_position + self.width),
                                     self.positive_start_point - self.length),
                "vector_D": mdc.vec3(self.negative_start_point, (self.edge_position + (self.width / 2)),
                                     self.positive_start_point - (self.length + (self.width / 2)), ),
                "vector_E": mdc.vec3(self.negative_start_point, self.edge_position,
                                     self.positive_start_point - self.length)
            },
            # left side bottom edge
            "direction_18": {
                "vector_A": mdc.vec3(self.negative_start_point, self.edge_position + self.width,
                                     self.negative_start_point),
                "vector_B": mdc.vec3(self.negative_start_point, self.edge_position, self.negative_start_point),
                "vector_C": mdc.vec3(self.negative_start_point, self.edge_position,
                                     self.negative_start_point + self.length),
                "vector_D": mdc.vec3(self.negative_start_point, (self.edge_position + (self.width / 2)),
                                     self.negative_start_point + (self.length + (self.width / 2))),
                "vector_E": mdc.vec3(self.negative_start_point, (self.edge_position + self.width),
                                     self.negative_start_point + self.length)
            },
            # left side front edge
            "direction_19": {
                "vector_A": mdc.vec3(self.negative_start_point, self.negative_start_point, self.edge_position),
                "vector_B": mdc.vec3(self.negative_start_point, self.negative_start_point,
                                     self.edge_position + self.width),
                "vector_C": mdc.vec3(self.negative_start_point, self.negative_start_point + self.length,
                                     (self.edge_position + self.width)),
                "vector_D": mdc.vec3(self.negative_start_point,
                                     self.negative_start_point + (self.length + (self.width / 2)),
                                     (self.edge_position + (self.width / 2))),
                "vector_E": mdc.vec3(self.negative_start_point, self.negative_start_point + self.length,
                                     self.edge_position)
            },
            # left side back edge
            "direction_20": {
                "vector_A": mdc.vec3(self.negative_start_point, self.positive_start_point,
                                     self.edge_position + self.width),
                "vector_B": mdc.vec3(self.negative_start_point, self.positive_start_point, self.edge_position),
                "vector_C": mdc.vec3(self.negative_start_point, self.positive_start_point - self.length,
                                     self.edge_position),
                "vector_D": mdc.vec3(self.negative_start_point,
                                     self.positive_start_point - (self.length + (self.width / 2)),
                                     (self.edge_position + (self.width / 2))),
                "vector_E": mdc.vec3(self.negative_start_point, self.positive_start_point - self.length,
                                     (self.edge_position + self.width))
            },
            # right side top edge
            "direction_21": {
                "vector_A": mdc.vec3(self.positive_start_point, self.edge_position + self.width,
                                     self.positive_start_point),
                "vector_B": mdc.vec3(self.positive_start_point, self.edge_position, self.positive_start_point),
                "vector_C": mdc.vec3(self.positive_start_point, self.edge_position,
                                     self.positive_start_point - self.length),
                "vector_D": mdc.vec3(self.positive_start_point, (self.edge_position + (self.width / 2)),
                                     self.positive_start_point - (self.length + (self.width / 2)), ),
                "vector_E": mdc.vec3(self.positive_start_point, (self.edge_position + self.width),
                                     self.positive_start_point - self.length)
            },
            # right side bottom edge
            "direction_22": {
                "vector_A": mdc.vec3(self.positive_start_point, self.edge_position, self.negative_start_point),
                "vector_B": mdc.vec3(self.positive_start_point, self.edge_position + self.width,
                                     self.negative_start_point),
                "vector_C": mdc.vec3(self.positive_start_point, (self.edge_position + self.width),
                                     self.negative_start_point + self.length),
                "vector_D": mdc.vec3(self.positive_start_point, (self.edge_position + (self.width / 2)),
                                     self.negative_start_point + (self.length + (self.width / 2))),
                "vector_E": mdc.vec3(self.positive_start_point, self.edge_position,
                                     self.negative_start_point + self.length)
            },
            # right side front edge
            "direction_23": {
                "vector_A": mdc.vec3(self.positive_start_point, self.negative_start_point,
                                     self.edge_position + self.width),
                "vector_B": mdc.vec3(self.positive_start_point, self.negative_start_point, self.edge_position),
                "vector_C": mdc.vec3(self.positive_start_point, self.negative_start_point + self.length,
                                     self.edge_position),
                "vector_D": mdc.vec3(self.positive_start_point,
                                     self.negative_start_point + (self.length + (self.width / 2)),
                                     (self.edge_position + (self.width / 2))),
                "vector_E": mdc.vec3(self.positive_start_point, self.negative_start_point + self.length,
                                     (self.edge_position + self.width))
            },
            # right side back edge
            "direction_24": {
                "vector_A": mdc.vec3(self.positive_start_point, self.positive_start_point, self.edge_position),
                "vector_B": mdc.vec3(self.positive_start_point, self.positive_start_point,
                                     self.edge_position + self.width),
                "vector_C": mdc.vec3(self.positive_start_point, self.positive_start_point - self.length,
                                     (self.edge_position + self.width)),
                "vector_D": mdc.vec3(self.positive_start_point,
                                     self.positive_start_point - (self.length + (self.width / 2)),
                                     (self.edge_position + (self.width / 2))),
                "vector_E": mdc.vec3(self.positive_start_point, self.positive_start_point - self.length,
                                     self.edge_position),
            }
        }

        self.dept = {
            "direction_1": self.depth * mdc.Y,
            "direction_2": self.depth * mdc.Y,
            "direction_3": self.depth * mdc.Y,
            "direction_4": self.depth * mdc.Y,
            "direction_5": -self.depth * mdc.Y,
            "direction_6": -self.depth * mdc.Y,
            "direction_7": -self.depth * mdc.Y,
            "direction_8": -self.depth * mdc.Y,
            "direction_9": -self.depth * mdc.Z,
            "direction_10": -self.depth * mdc.Z,
            "direction_11": -self.depth * mdc.Z,
            "direction_12": -self.depth * mdc.Z,
            "direction_13": self.depth * mdc.Z,
            "direction_14": self.depth * mdc.Z,
            "direction_15": self.depth * mdc.Z,
            "direction_16": self.depth * mdc.Z,
            "direction_17": self.depth * mdc.X,
            "direction_18": self.depth * mdc.X,
            "direction_19": self.depth * mdc.X,
            "direction_20": self.depth * mdc.X,
            "direction_21": -self.depth * mdc.X,
            "direction_22": -self.depth * mdc.X,
            "direction_23": -self.depth * mdc.X,
            "direction_24": -self.depth * mdc.X,
        }

    def transformation(self):
        _vertical_circular_end_blind_slot_primitive = [mdc.Segment(self.circular_vectors[self.dir]["vector_A"],
                                                                   self.circular_vectors[self.dir]["vector_B"]),
                                                       mdc.Segment(self.circular_vectors[self.dir]["vector_B"],
                                                                   self.circular_vectors[self.dir]["vector_C"]),
                                                       mdc.ArcThrough(self.circular_vectors[self.dir]["vector_C"],
                                                                      self.circular_vectors[self.dir]["vector_D"],
                                                                      self.circular_vectors[self.dir]["vector_E"]),
                                                       mdc.Segment(self.circular_vectors[self.dir]["vector_E"],
                                                                   self.circular_vectors[self.dir]["vector_A"]),
                                                       ],
        _vertical_circular_end_blind_slot = mdc.extrusion(self.dept[self.dir],
                                                          mdc.flatsurface(_vertical_circular_end_blind_slot_primitive))

        return _vertical_circular_end_blind_slot
