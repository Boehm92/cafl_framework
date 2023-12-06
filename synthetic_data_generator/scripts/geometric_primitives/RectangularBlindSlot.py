import numpy as np
import madcad as mdc


class RectangularBlindSlot:
    def __init__(self, limit):
        self.dir = np.random.choice(["direction_1", "direction_2", "direction_3", "direction_4", "direction_5",
                                     "direction_6", "direction_7", "direction_8", "direction_9", "direction_10"
                                     "direction_11", "direction_12"])
        self.limit = limit
        self.pos_x = np.random.uniform(0.5, 8.5)
        self.width = np.random.uniform(self.pos_x, 9.5)

        self.pos_y = np.random.uniform(0.5, 8.5)
        self.length = np.random.uniform(self.pos_y, 9.5)

        self.pos_z = np.random.uniform(0.5, 8.5)
        self.depth = np.random.uniform(self.pos_z, 9.5)

        self.start_point = -0.0002
        self.end_point = 10.0002

        self.transform = {
            # Front Side
            "direction_1": [mdc.vec3(self.pos_x, self.start_point, self.start_point),
                            mdc.vec3(self.width, self.length, self.depth)],

            "direction_2": [mdc.vec3(self.pos_x, self.start_point, self.depth),
                            mdc.vec3(self.width, self.length, self.end_point)],

            "direction_3": [mdc.vec3(self.start_point, self.start_point, self.pos_z),
                            mdc.vec3(self.width, self.length, self.depth)],

            "direction_4": [mdc.vec3(self.width, self.start_point, self.pos_z),
                            mdc.vec3(self.end_point, self.length, self.depth)],
            # Back Side
            "direction_5": [mdc.vec3(self.pos_x, self.length, self.start_point),
                            mdc.vec3(self.width, self.end_point, self.depth)],

            "direction_6": [mdc.vec3(self.pos_x, self.length, self.depth),
                            mdc.vec3(self.width, self.end_point, self.end_point)],

            "direction_7": [mdc.vec3(self.start_point, self.width, self.pos_z),
                            mdc.vec3(self.width, self.end_point, self.depth)],

            "direction_8": [mdc.vec3(self.width, self.width, self.pos_z),
                            mdc.vec3(self.end_point, self.end_point, self.depth)],

            # Left Side (The right, left, upper and bottom side are covert by front and back side)
            "direction_9": [mdc.vec3(self.start_point, self.pos_y, self.start_point),
                            mdc.vec3(self.width, self.length, self.depth)],

            "direction_10": [mdc.vec3(self.start_point, self.pos_y, self.depth),
                             mdc.vec3(self.width, self.length, self.end_point)],

            # Right Side
            "direction_11": [mdc.vec3(self.width, self.pos_y, self.start_point),
                             mdc.vec3(self.end_point, self.length, self.depth)],

            "direction_12": [mdc.vec3(self.width, self.pos_y, self.depth),
                             mdc.vec3(self.end_point, self.length, self.end_point)],
        }

    def transformation(self):
        _rectangular_passage = mdc.brick(self.transform[self.dir][0], self.transform[self.dir][1])

        return _rectangular_passage
