import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500


class Visualization():
    def __init__(self, r1=10, r2=10):
        self.r1 = r1
        self.r2 = r2
        pygame.init()
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Planety")
        self.clock = pygame.time.Clock()

    def draw(self, planet_position, arrow_end = None, rad=None):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit()
        self.screen.fill((255, 255, 255))

        r1 = rad[0] if rad is not None else self.r1
        r2 = rad[1] if rad is not None else self.r2

        cords = self.__convert_coords(planet_position)
        pygame.draw.circle(self.screen, (200, 0, 0), (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)), r1)
        pygame.draw.circle(self.screen, (0, 0, 20), cords, r2)
        if arrow_end is not None:
            endarr = self.__convert_coords(arrow_end)
            pygame.draw.aaline(self.screen, (255, 0, 0), cords, endarr, True)

        self.clock.tick(60)
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    @staticmethod
    def __convert_coords(abs_coords):
        x = int(SCREEN_WIDTH / 2 + abs_coords[0])
        y = int(SCREEN_HEIGHT / 2 - abs_coords[1])
        return x, y



if __name__ == '__main__':
    pass