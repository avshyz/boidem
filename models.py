import numpy as np
import random
from collections import namedtuple

FIELD_HEIGHT = 400
FIELD_WIDTH = 400

PREY_SPEED = 10

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

    def _get_closest_neighbors(self, entities, threshold=None):
        if threshold is None:
            return sorted(entities, key=lambda e: np.linalg.norm(self.pos - e.pos))
        else:
            res = map(lambda e: (e, np.linalg.norm(self.pos - e.pos)), entities)
            res = filter(lambda (e, distance): distance < threshold, res)
            res.sort(key=lambda (e, distance): distance)
            return [e for (e, d) in res]


    def step(self, biosphere):
        friends = self._get_closest_neighbors(biosphere.herd)
        overall_force = np.array([0., 0.])
        for friend in friends:
            if np.array_equal(friend.pos, self.pos):
                continue
            herding_force = friend.pos - self.pos
            density_force = self.pos - friend.pos

            herding_direction = herding_force / np.linalg.norm(herding_force)
            density_direction = density_force / np.linalg.norm(density_force)

            distance = np.linalg.norm(self.pos - friend.pos)
            l = 0.4 + (1 / distance)

            overall_force += (herding_direction * (1 - l) + density_direction * l)
        self.pos += overall_force * PREY_SPEED / len(friends)
        self._clip_position()


    def _clip_position(self):
        self.pos = np.min([self.pos, [FIELD_HEIGHT - 2, FIELD_WIDTH - 2]], axis=0)
        self.pos = np.max([self.pos, [1, 1]], axis=0)
