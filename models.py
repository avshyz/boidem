import numpy as np
import random
from collections import namedtuple

FIELD_HEIGHT = 400
FIELD_WIDTH = 400

PREY_SPEED = 1

Biosphere = namedtuple('Biosphere', ['herd'])

random.seed(1)

class Prey(object):
    def __init__(self, starting_pos=None):
        if starting_pos is None:
            starting_pos = np.array([
                random.randrange(FIELD_WIDTH),
                random.randrange(FIELD_HEIGHT)
            ], dtype=float)

        self.pos = starting_pos

    def _get_k_nearest(self, entities, k):
        return sorted(entities, key=lambda e: np.linalg.norm(self.pos - e.pos))[:k]


    def step(self, biosphere):
        friends = self._get_k_nearest(biosphere.herd, 10000)
        pull = np.average([friend.pos for friend in friends], axis=0) - self.pos
        # push = np.average(self._get_k_nearest(biosphere.predators, 5))

        pull = PREY_SPEED * (pull / np.linalg.norm(pull))
        # pull *= 0.3
        #push *= 0.7

        self.pos += pull #+ push
        self._clip_position()

    def _clip_position(self):
        self.pos = np.min([self.pos, [FIELD_HEIGHT - 1, FIELD_WIDTH - 1]], axis=0)
        self.pos = np.max([self.pos, [1, 1]], axis=0)
