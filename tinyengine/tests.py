import unittest

from tinyengine.core import Vector, RGB


class TestVector(unittest.TestCase):

    def setUp(self):
        self.vector = Vector()

    def test_vector_visualization(self):
        self.assertEqual(type(self.vector.position), type(tuple()))

    def test_vector_init(self):
        self.assertEqual(self.vector.position, (0, 0))

    def test_vector_init_1_1(self):
        self.assertEqual(Vector(1, 1).position, (1, 1))

    def test_vector_move_up(self):
        self.assertEqual(self.vector.up, (0, -1))

    def test_vector_move_down(self):
        self.assertEqual(self.vector.down, (0, 1))

    def test_vector_move_left(self):
        self.assertEqual(self.vector.left, (-1, 0))

    def test_vector_move_right(self):
        self.assertEqual(self.vector.right, (1, 0))

    def test_vector_zero(self):
        v_5_5 = Vector(5, 5)
        self.assertEqual(v_5_5.position, (5, 5))
        self.assertEqual(v_5_5.zero, (0, 0))

    def test_vector_str_representation(self):
        self.assertEqual(Vector().__str__(), "Vector(0, 0)")


class TestRGB(unittest.TestCase):
    def setUp(self):
        self.rgb = RGB()

    def test_rgb_visualization(self):
        """ Checks if value returned by RGB is a tuple """
        self.assertEqual(type(self.rgb.value), type(tuple()))

    def test_rgb_init(self):
        self.assertEqual(self.rgb.value, (0, 0, 0))

    def test_rgb_str_representation(self):
        self.assertEqual(RGB().__str__(), "RGB(0, 0, 0)")

    def test_rgb_init_1(self):
        self.assertEqual(RGB(100, 20, 0).value, (100, 20, 0))

    def test_rgb_wrong_init(self):
        self.assertEqual(RGB(-100, -1, 0).value, (0, 0, 0))

    def test_rgb_black(self):
        self.rgb = RGB().black
        self.assertEqual(self.rgb, (0, 0, 0))

    def test_rgb_white(self):
        self.rgb = RGB().white
        self.assertEqual(self.rgb, (255, 255, 255))

    def test_rgb_red(self):
        self.rgb = RGB().red
        self.assertEqual(self.rgb, (255, 0, 0))

    def test_rgb_green(self):
        self.rgb = RGB().green
        self.assertEqual(self.rgb, (0, 255, 0))

    def test_rgb_blue(self):
        self.rgb = RGB().blue
        self.assertEqual(self.rgb, (0, 0, 255))
