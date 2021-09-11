import unittest
import sys

sys.path.append('..')
from PyVersionNumber import VersionNumber


class TestCaseMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(VersionNumber(1, 2, 3) + VersionNumber(3, 2, 1), VersionNumber(4, 4, 4))
        self.assertEqual(VersionNumber(1, 2, 3) + VersionNumber(1, 2, 3), VersionNumber(2, 4, 6))
        self.assertEqual(VersionNumber(1, 1, 1) + VersionNumber(2, 2, 2), VersionNumber(3, 3, 3))

    def test_subtraction(self):
        self.assertEqual(VersionNumber(1, 2, 3) - VersionNumber(3, 2, 1), VersionNumber(-2, 0, 2))
        self.assertEqual(VersionNumber(1, 2, 3) - VersionNumber(1, 2, 3), VersionNumber(0, 0, 0))
        self.assertEqual(VersionNumber(1, 1, 1) - VersionNumber(2, 2, 2), VersionNumber(-1, -1, -1))

    def test_multiplication(self):
        self.assertEqual(VersionNumber(1, 2, 3) * VersionNumber(3, 2, 1), VersionNumber(3, 4, 3))
        self.assertEqual(VersionNumber(1, 2, 3) * VersionNumber(1, 2, 3), VersionNumber(1, 4, 9))
        self.assertEqual(VersionNumber(1, 1, 1) * VersionNumber(2, 2, 2), VersionNumber(2, 2, 2))

    def test_division(self):
        self.assertEqual(VersionNumber(1, 2, 3) / VersionNumber(3, 2, 1), VersionNumber(0, 1, 3))
        self.assertEqual(VersionNumber(1, 2, 3) / VersionNumber(1, 2, 3), VersionNumber(1, 1, 1))
        self.assertEqual(VersionNumber(1, 1, 1) / VersionNumber(2, 2, 2), VersionNumber(0, 0, 0))

    def test_floor_division(self):
        self.assertEqual(VersionNumber(1, 2, 3) // VersionNumber(3, 2, 1), VersionNumber(0, 1, 3))
        self.assertEqual(VersionNumber(1, 2, 3) // VersionNumber(1, 2, 3), VersionNumber(1, 1, 1))
        self.assertEqual(VersionNumber(1, 1, 1) // VersionNumber(2, 2, 2), VersionNumber(0, 0, 0))

    def test_exponent(self):
        self.assertEqual(VersionNumber(1, 2, 3) ** VersionNumber(3, 2, 1), VersionNumber(1, 4, 3))
        self.assertEqual(VersionNumber(1, 2, 3) ** VersionNumber(1, 2, 3), VersionNumber(1, 4, 27))
        self.assertEqual(VersionNumber(1, 1, 1) ** VersionNumber(2, 2, 2), VersionNumber(1, 1, 1))

    def test_modulus(self):
        self.assertEqual(VersionNumber(1, 2, 3) % VersionNumber(3, 2, 1), VersionNumber(1, 0, 0))
        self.assertEqual(VersionNumber(1, 2, 3) % VersionNumber(1, 2, 3), VersionNumber(0, 0, 0))
        self.assertEqual(VersionNumber(1, 1, 1) % VersionNumber(2, 2, 2), VersionNumber(1, 1, 1))


if __name__ == '__main__':
    unittest.main()
