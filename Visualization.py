import numpy as np
import pygame

from Simulation import Simulation

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500


class Visualization:
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2
        pygame.init()
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Planety")
        self.clock = pygame.time.Clock()

    def draw(self, planet_position):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit()
        self.screen.fill((255, 255, 255))

        cords = self.__convert_coords(planet_position)
        pygame.draw.circle(self.screen, (200, 200, 200), (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT/2)), self.r1)
        pygame.draw.circle(self.screen, (0, 0, 0), cords, self.r2)
        self.clock.tick(60)
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    @staticmethod
    def __convert_coords(abs_coords):
        x = int(SCREEN_WIDTH/2 + abs_coords[0])
        y = int(SCREEN_HEIGHT/2 - abs_coords[1])
        return x, y


if __name__ == '__main__':
    v = Visualization(10, 10)
    s = Simulation((1, 100), (-3, -4), 1/20, -52100000000000, -10000000, 10, 10)

    for i in s:
        v.draw(i)

