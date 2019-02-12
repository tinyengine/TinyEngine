from tinyengine.engine import Engine


# Setup Tinyengine
def main():
    engine = Engine()

    # Setting window size
    engine.display.WIDTH = 800
    engine.display.HEIGHT = 600

    # running the game
    engine.run()


if __name__ == "__main__":
    main()
