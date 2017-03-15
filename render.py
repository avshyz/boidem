import pygame

PREY_COLOR = (255, 255, 255)


class PyGameRender(object):
    def __init__(self, height, width):
        pygame.init()
        self.screen = pygame.display.set_mode((height, width))
        self.clock = pygame.time.Clock()

    def _draw_prey(self, prey):
        pygame.draw.rect(self.screen, PREY_COLOR, pygame.Rect(prey.pos[0], prey.pos[1], 2, 2))

    def _clean(self):
        self.screen.fill((0, 0, 0))

    def should_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def draw(self, biosphere):
        pygame.event.get()
        self._clean()

        for prey in biosphere.herd:
            self._draw_prey(prey)
            pygame.display.flip()
            self.clock.tick(120)
