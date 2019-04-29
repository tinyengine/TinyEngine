import pygame
from pygame.locals import *
import sys
sys.path.append('../')
import settings
import scripts
from scripts import *
import pkgutil
import importlib
from core import *


screen = pygame.display.set_mode([settings.WIDTH, settings.HEIGHT], 0, 32)  # Setup window size to display
screen.fill((0, 0, 0))  # Fill the screen with a default color - temporary


def main():
    # Dict to care all game objects created
    game_objects = dict()

    clock = pygame.time.Clock()

    # Take all scripts on scripts folder, wrap on game object variables on dictionary
    package = scripts
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        # Get module from package and create gameObject with the same name as script and attach an instance
        module = importlib.import_module('scripts.{}'.format(modname))
        my_class = getattr(module, '{}'.format(modname.capitalize()))
        # self.game_objects[modname] = GameObject(my_class(), str(modname))
        game_objects[modname] = my_class()

    # Setting up display and clock
    pygame.display.init()  # Initialize display module
    print('Initializing display module') if pygame.display.get_init() else print('Display module initialization failed')

    # Running start function in all gameObjects
    for gameObject_name in game_objects:
        try:
            game_objects[gameObject_name].start()
        except:
            print('error start')

    # Updating function
    while True:
        for gameObject_name in game_objects:
            game_objects[gameObject_name].update()

        pygame.display.flip()  # Updating frame
        clock.tick(settings.FRAMERATE)  # Framerate clock


if __name__ == "__main__":
    main()
