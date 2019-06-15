from tinyengine.core import *
import os


class App(Core):
    @start
    def start(self):
        self.transform.position = Vector(250, 250)
        self.add_component(Sprite(os.path.abspath('../art/mario.png'), 0.1))
        # self.add_component(Square(100, 100))

    @update
    def update(self):
        if Input.get_key('A'):
            self.transform.move(Vector().right)
