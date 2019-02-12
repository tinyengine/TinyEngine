import pygame
from pygame.locals import *


class Display():
    # Default window size
    WIDTH = 500
    HEIGHT = 500
    FRAMERATE = 30


class Engine():
    display = Display()

    def run(self):
        pygame.display.init()  # Initialize display module
        print('Initializing display module') if pygame.display.get_init() else print('Display module initialization failed')
        self.screen = pygame.display.set_mode([self.display.WIDTH, self.display.HEIGHT], 0, 32)  # Setup window size to display
        self.screen.fill((0, 0, 0))  # Fill the screen with a default color - temporary
        self.clock = pygame.time.Clock()  # Instantiating clock from framework

        # Updating function
        while True:
            pygame.display.flip()  # Updating frame
            self.clock.tick(self.display.FRAMERATE)  # Framerate clock
