from tinyengine.core import *
import os


class App(Core):
    @start
    def start(self):
        self.transform.position = Vector(250, 0)
        self.add_component(Sprite(os.path.abspath('../art/mario.png'), 0.1))

    @update
    def update(self):
        if(Input.get_key_down('A')):
            print('apertou A')
