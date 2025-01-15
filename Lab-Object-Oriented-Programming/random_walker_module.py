import numpy as np


class RandomWalker:
    """Class for representing a random walker"""

    def __init__(self):  # initialize two attributes as starting point (0, 0)
        self.x_pos = 0
        self.y_pos = 0

    def step(self):
        """Evolve random walker one step ahead"""
        self.x_pos += np.random.normal(0, 1)
        self.y_pos += np.random.normal(0, 1)

    def get_x_pos(self):  # getter that returns current x
        return self.x_pos

    def get_y_pos(self):  # getter that returns current y
        return self.y_pos


class ModifiedRandomWalker(RandomWalker):
    """Modified Class for representing a random walker"""

    def step(self, walker):
        """Find the closest walker using Euclidean distance"""
        closest = min(walker, key=lambda w: np.sqrt((self.x_pos -
                                                    w.get_x_pos())**2 +
                                                    (self.y_pos -
                                                    w.get_y_pos())**2))

        self.x_pos = closest.get_x_pos()  # getter that returns current x
        self.y_pos = closest.get_y_pos()  # getter that returns current y

        # Evolve random walker one step ahead
        self.x_pos += np.random.normal(0, 1)
        self.y_pos += np.random.normal(0, 1)
