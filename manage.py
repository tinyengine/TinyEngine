import os
import sys


# sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def run():
    os.system('cd tinyengine && python engine.py')


def error():
    print('Unexpected argument or lack of it')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'run':
            run()
        else:
            error()
    else:
        error()
