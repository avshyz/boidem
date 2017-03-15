import random
from collections import namedtuple

FIELD_HEIGHT = 400
FIELD_WIDTH = 400

Vector = namedtuple('Point', ['x', 'y'])
Biosphere = namedtuple('Biosphere', ['herd'])

class Prey(object):
    def __init__(self, starting_pos=None):
        if starting_pos is None:
            starting_pos = Vector(random.randrange(FIELD_WIDTH),
                                  random.randrange(FIELD_HEIGHT))


        self.pos = starting_pos

    def step(self, biosphere):
        pass