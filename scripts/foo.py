from tinyengine.core import *


class Foo(Core):
    @start
    def start(self):
        print('foo start')

    @update
    def update(self):
        pass
