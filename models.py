import numpy as np
import random
from collections import namedtuple

FIELD_HEIGHT = 400
FIELD_WIDTH = 400

Biosphere = namedtuple('Biosphere', ['herd'])

random.seed(1)

class Prey(object):
    def __init__(self, starting_pos=None):
        if starting_pos is None:
            starting_pos = np.array([
                random.randrange(FIELD_WIDTH),
                random.randrange(FIELD_HEIGHT)
            ])

        self.pos = starting_pos

    def step(self, biosphere):
        self.pos += np.array([1, 1])
