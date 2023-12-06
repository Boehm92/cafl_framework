import numpy as np
import madcad as mdc


class BlindHole:
    def __init__(self, limit):
        self.dir = np.random.choice(["direction_1", "direction_2", "direction_3", "direction_4", "direction_5",
                                     "direction_6"])
        self.limit = limit
        self.radius = np.random.uniform(0.5, (4.5 * self.limit))
        self.pos_x = np.random.uniform(self.radius + 0.5, 9.5 - self.radius)
        self.pos_y = np.random.uniform(self.radius + 0.5, 9.5 - self.radius)
        self.start_point = -0.0002
        self.end_point = np.random.uniform(1, 9)

        self.transform = {
            "direction_1": [mdc.vec3(self.pos_x, self.pos_y, self.end_point),
                            mdc.vec3(self.pos_x, self.pos_y, self.start_point)],
            "direction_2": [mdc.vec3(self.pos_x, self.pos_y, self.start_point),
                            mdc.vec3(self.pos_x, self.pos_y, self.end_point)],
            "direction_3": [mdc.vec3(self.pos_x, self.start_point, self.pos_y),
                            mdc.vec3(self.pos_x, self.end_point, self.pos_y)],
            "direction_4": [mdc.vec3(self.pos_x, self.end_point, self.pos_y),
                            mdc.vec3(self.pos_x, self.start_point, self.pos_y)],
            "direction_5": [mdc.vec3(self.start_point, self.pos_x, self.pos_y),
                            mdc.vec3(self.end_point, self.pos_x, self.pos_y)],
            "direction_6": [mdc.vec3(self.end_point, self.pos_x, self.pos_y),
                            mdc.vec3(self.start_point, self.pos_x, self.pos_y)],
        }

    def transformation(self):
        _through_hole = mdc.cylinder(self.transform[self.dir][0], self.transform[self.dir][1], self.radius)

        return _through_hole
