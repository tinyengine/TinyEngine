from tinyengine.core import *
import os


class App(Core):
    @start
    def start(self):
        self.transform.position = Vector(250, 250)
        self.add_component(Sprite('mario.png', 0.1))
        # self.add_component(Square(100, 100))

    @update
    def update(self):
        if Input.get_key('A'):
            self.transform.move(self.transform.position.left)

        if Input.get_key('S'):
            self.transform.move(self.transform.position.down)

        if Input.get_key('D'):
            self.transform.move(self.transform.position.right)

        if Input.get_key('W'):
            self.transform.move(self.transform.position.up)