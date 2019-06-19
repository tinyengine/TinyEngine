import unittest

from tinyengine.core import Vector


class TestVector(unittest.TestCase):

    def setUp(self):
        self.vector = Vector()

    def test_vector_visualization(self):
        self.assertEqual(type(self.vector.position), type(tuple()))

    def test_vector_init(self):
        self.assertEqual(self.vector.position, (0, 0))

    def test_vector_init_1_1(self):
        v_one_one = Vector(1, 1)
        self.assertEqual(v_one_one.position, (1, 1))

    def test_vector_move_up(self):
        self.assertEqual(self.vector.up.position, (0, -1))

    def test_vector_move_down(self):
        self.assertEqual(self.vector.down.position, (0, 1))

    def test_vector_move_left(self):
        self.assertEqual(self.vector.left.position, (-1, 0))

    def test_vector_move_right(self):
        self.assertEqual(self.vector.right.position, (1, 0))

    def test_vector_zero(self):
        v_5_5 = Vector(5, 5)
        self.assertEqual(v_5_5.position, (5, 5))
        self.assertEqual(v_5_5.zero.position, (0, 0))

