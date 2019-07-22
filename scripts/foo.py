from tinyengine.core import (
    Core, start, update
)


class Foo(Core):
    @start
    def start(self):
        print('foo start')

    @update
    def update(self):
        pass
