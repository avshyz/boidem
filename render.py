import pygame

PREY_COLOR = (0, 128, 255)


class PyGameRender(object):
    def __init__(self, height, width):
        pygame.init()
        self.screen = pygame.display.set_mode((height, width))
        self.clock = pygame.time.Clock()

    def _draw_prey(self, prey):
        pygame.draw.rect(self.screen, PREY_COLOR, pygame.Rect(prey.pos.x, prey.pos.y, 2, 2))

    def _clean(self):
        self.screen.fill((0, 0, 0))

    def draw(self, biosphere):
        pygame.event.get()
        for prey in biosphere.herd:
            self._draw_prey(prey)
            pygame.display.flip()
            self.clock.tick(60)
