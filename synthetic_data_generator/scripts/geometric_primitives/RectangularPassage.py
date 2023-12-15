import numpy as np
import madcad as mdc


class RectangularPassage:
    def __init__(self, limit):
        self.dir = np.random.choice(["direction_1", "direction_2", "direction_3", "direction_4", "direction_5",
                                     "direction_6"])
        self.limit = limit
        self.pos_x = np.random.uniform(0.5, 8.5)
        self.pos_y = np.random.uniform(0.5, 8.5)
        self.width = np.random.uniform(self.pos_x, 9.5)
        self.length = np.random.uniform(self.pos_y, 9.5)
        self.start_point = -0.0002
        self.end_point = 10.0002

        self.transform = {
            "direction_1": [mdc.vec3(self.pos_x, self.pos_y, self.start_point),
                            mdc.vec3(self.width, self.length, self.end_point)],

            "direction_2": [mdc.vec3(self.pos_x, self.pos_y, self.start_point),
                            mdc.vec3(self.width, self.length, self.end_point)],

            "direction_3": [mdc.vec3(self.pos_x, self.start_point, self.pos_y),
                            mdc.vec3(self.width, self.end_point, self.length)],
            "direction_4": [mdc.vec3(self.pos_x, self.start_point, self.pos_y),
                            mdc.vec3(self.width, self.end_point, self.length)],

            "direction_5": [mdc.vec3(self.start_point, self.pos_x, self.pos_y),
                            mdc.vec3(self.end_point, self.width, self.length)],
            "direction_6": [mdc.vec3(self.start_point, self.pos_x, self.pos_y),
                            mdc.vec3(self.end_point, self.width, self.length)]
        }

    def transformation(self):
        _rectangular_passage = mdc.brick(self.transform[self.dir][0], self.transform[self.dir][1])

        return _rectangular_passage
