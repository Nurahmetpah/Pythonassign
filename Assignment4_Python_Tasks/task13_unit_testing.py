import unittest

from mypackage.calculator import add
from task08_math_tools import cube, square


class TestMathFunctions(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(4), 16)

    def test_cube(self):
        self.assertEqual(cube(5), 125)

    def test_add(self):
        self.assertEqual(add(10, 5), 15)


if __name__ == "__main__":
    unittest.main()
