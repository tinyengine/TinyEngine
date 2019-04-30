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

key_map = {
    'A': pygame.K_a,
    'B': pygame.K_b,
    'C': pygame.K_c,
    'D': pygame.K_d,
    'E': pygame.K_e,
    'F': pygame.K_f,
    'G': pygame.K_g,
    'H': pygame.K_h,
    'I': pygame.K_i,
    'J': pygame.K_j,
    'K': pygame.K_k,
    'L': pygame.K_l,
    'M': pygame.K_m,
    'N': pygame.K_n,
    'O': pygame.K_o,
    'P': pygame.K_p,
    'Q': pygame.K_q,
    'R': pygame.K_r,
    'S': pygame.K_s,
    'T': pygame.K_t,
    'U': pygame.K_u,
    'V': pygame.K_v,
    'W': pygame.K_w,
    'X': pygame.K_x,
    'Y': pygame.K_y,
    'Z': pygame.K_z
}


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
        except e:
            print('error start')

    # Updating function
    while True:
        for gameObject_name in game_objects:
            game_objects[gameObject_name].update()

        pygame.display.flip()  # Updating frame
        clock.tick(settings.FRAMERATE)  # Framerate clock


if __name__ == "__main__":
    main()
