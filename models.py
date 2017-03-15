import numpy as np
import random
from collections import namedtuple

FIELD_HEIGHT = 400
FIELD_WIDTH = 400

PREY_SPEED = 2

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
        """
        friends = self._get_closest_neighbors(biosphere.herd)
        pull = np.average([friend.pos for friend in friends], axis=0) - self.pos
        close_neighbors = self._get_closest_neighbors(biosphere.herd, threshold=5)

        if close_neighbors:
            push = self.pos - np.average([x.pos for x in close_neighbors])
        else:
            push = self.pos

        l = np.linalg.norm(push - pull)
        direction = (pull * (1 - l)) + (push * l)

        direction = PREY_SPEED * (direction / np.linalg.norm(direction))
        self.pos += direction
        self._clip_position()"""
        friends = self._get_closest_neighbors(biosphere.herd)
        centroid = np.average([friend.pos for friend in friends], axis=0)

        herding_force = centroid - self.pos
        density_force = self.pos - centroid

        herding_direction = herding_force / np.linalg.norm(herding_force)
        density_direction = density_force / np.linalg.norm(density_force)

        distance = np.linalg.norm(self.pos - centroid)
        l = 0.1 + (1 / distance)

        overall_force = (herding_direction * (1 - l) + density_direction * l)
        self.pos += overall_force * PREY_SPEED
        self._clip_position()


    def _clip_position(self):
        self.pos = np.min([self.pos, [FIELD_HEIGHT - 2, FIELD_WIDTH - 2]], axis=0)
        self.pos = np.max([self.pos, [1, 1]], axis=0)
