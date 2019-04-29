from tinyengine.core import *


class App(Core):
    @start
    def start(self):
        self.transform.position = Vector(250, 250)
        self.add_component(Square(100, 100))

    @update
    def update(self):
        pass
