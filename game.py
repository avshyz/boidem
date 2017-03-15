import pygame

from models import Biosphere, Prey, FIELD_HEIGHT, FIELD_WIDTH
from render import PyGameRender

HERD_SIZE = 10
EPOCH = 10

def main():
    herd = [Prey() for _ in xrange(HERD_SIZE)]
    world = Biosphere(herd)
    renderer = PyGameRender(FIELD_HEIGHT, FIELD_WIDTH)
    while EPOCH and not renderer.should_quit():

        map(lambda prey: prey.step(world), world.herd)
        renderer.draw(world)


if __name__ == '__main__':
    main()