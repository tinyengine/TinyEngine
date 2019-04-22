import pygame
from pygame.locals import *
import sys
sys.path.append('../')
import scripts
from scripts import *
import pkgutil
import importlib


class Display():
    # Default window size
    WIDTH = 500
    HEIGHT = 500
    FRAMERATE = 30


class GameObject():
    def __init__(self, root, name):
        self.root = root
        self.name = name

    def __str__(self):
        return self.name


class Engine():
    def __init__(self):
        self.display = Display()

        # Dict to care all game objects created
        self.game_objects = dict()

    def setup(self):
        # Take all scripts on scripts folder, wrap on game object variables on dictionary
        package = scripts
        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
            # Get module from package and create gameObject with the same name as script and attach an instance
            module = importlib.import_module('scripts.{}'.format(modname))
            my_class = getattr(module, '{}'.format(modname.capitalize()))
            self.game_objects[modname] = GameObject(my_class(), str(modname))
            print(type(self.game_objects[str(modname)].root))

    #################################################################################################################
    # This run function below is just to open the window. I will be improved to fit on the project in a near future #
    #################################################################################################################

    def run(self):
        pygame.display.init()  # Initialize display module
        print('Initializing display module') if pygame.display.get_init() else print('Display module initialization failed')
        self.screen = pygame.display.set_mode([self.display.WIDTH, self.display.HEIGHT], 0, 32)  # Setup window size to display
        self.screen.fill((0, 0, 0))  # Fill the screen with a default color - temporary
        self.clock = pygame.time.Clock()  # Instantiating clock from framework

        # Updating function
        while True:
            for gameObject_name in self.game_objects:
                self.game_objects[gameObject_name].root.update()
                #   self.game_objects[gameObject_name].name

            pygame.display.flip()  # Updating frame
            self.clock.tick(self.display.FRAMERATE)  # Framerate clock


if __name__ == "__main__":
    engine = Engine()
    engine.setup()
    engine.run()
