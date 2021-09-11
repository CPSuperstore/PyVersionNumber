import unittest
import sys

sys.path.append('..')
from PyVersionNumber import VersionNumber


class TestCaseComparisons(unittest.TestCase):
    def test_less_than(self):
        # equals
        self.assertEqual(VersionNumber(1, 2, 3) < VersionNumber(1, 2, 3), False)

        # greater than
        self.assertEqual(VersionNumber(1, 2, 3) < VersionNumber(0, 2, 3), False)
        self.assertEqual(VersionNumber(1, 2, 3) < VersionNumber(1, 1, 3), False)
        self.assertEqual(VersionNumber(1, 2, 3) < VersionNumber(1, 2, 2), False)
        self.assertEqual(VersionNumber(3, 2, 1) < VersionNumber(1, 2, 2), False)

        # less than
        self.assertEqual(VersionNumber(0, 2, 3) < VersionNumber(1, 2, 3), True)
        self.assertEqual(VersionNumber(1, 1, 3) < VersionNumber(1, 2, 3), True)
        self.assertEqual(VersionNumber(1, 2, 2) < VersionNumber(1, 2, 3), True)
        self.assertEqual(VersionNumber(1, 2, 2) < VersionNumber(3, 2, 1), True)

    def test_greater_than(self):
        # equals
        self.assertEqual(VersionNumber(1, 2, 3) > VersionNumber(1, 2, 3), False)

        # greater than
        self.assertEqual(VersionNumber(1, 2, 3) > VersionNumber(0, 2, 3), True)
        self.assertEqual(VersionNumber(1, 2, 3) > VersionNumber(1, 1, 3), True)
        self.assertEqual(VersionNumber(1, 2, 3) > VersionNumber(1, 2, 2), True)
        self.assertEqual(VersionNumber(3, 2, 1) > VersionNumber(1, 2, 2), True)

        # less than
        self.assertEqual(VersionNumber(0, 2, 3) > VersionNumber(1, 2, 3), False)
        self.assertEqual(VersionNumber(1, 1, 3) > VersionNumber(1, 2, 3), False)
        self.assertEqual(VersionNumber(1, 2, 2) > VersionNumber(1, 2, 3), False)
        self.assertEqual(VersionNumber(1, 2, 2) > VersionNumber(3, 2, 1), False)

    def test_equal_to(self):
        # equals
        self.assertEqual(VersionNumber(1, 2, 3) == VersionNumber(1, 2, 3), True)

        # greater than
        self.assertEqual(VersionNumber(1, 2, 3) == VersionNumber(0, 2, 3), False)
        self.assertEqual(VersionNumber(1, 2, 3) == VersionNumber(1, 1, 3), False)
        self.assertEqual(VersionNumber(1, 2, 3) == VersionNumber(1, 2, 2), False)
        self.assertEqual(VersionNumber(3, 2, 1) == VersionNumber(1, 2, 2), False)

        # less than
        self.assertEqual(VersionNumber(0, 2, 3) == VersionNumber(1, 2, 3), False)
        self.assertEqual(VersionNumber(1, 1, 3) == VersionNumber(1, 2, 3), False)
        self.assertEqual(VersionNumber(1, 2, 2) == VersionNumber(1, 2, 3), False)
        self.assertEqual(VersionNumber(1, 2, 2) == VersionNumber(3, 2, 1), False)

    def test_not_equal_to(self):
        # equals
        self.assertEqual(VersionNumber(1, 2, 3) != VersionNumber(1, 2, 3), False)

        # greater than
        self.assertEqual(VersionNumber(1, 2, 3) != VersionNumber(0, 2, 3), True)
        self.assertEqual(VersionNumber(1, 2, 3) != VersionNumber(1, 1, 3), True)
        self.assertEqual(VersionNumber(1, 2, 3) != VersionNumber(1, 2, 2), True)
        self.assertEqual(VersionNumber(3, 2, 1) != VersionNumber(1, 2, 2), True)

        # less than
        self.assertEqual(VersionNumber(0, 2, 3) != VersionNumber(1, 2, 3), True)
        self.assertEqual(VersionNumber(1, 1, 3) != VersionNumber(1, 2, 3), True)
        self.assertEqual(VersionNumber(1, 2, 2) != VersionNumber(1, 2, 3), True)
        self.assertEqual(VersionNumber(1, 2, 2) != VersionNumber(3, 2, 1), True)

    def test_less_than_equals(self):
        # equals
        self.assertEqual(VersionNumber(1, 2, 3) <= VersionNumber(1, 2, 3), True)

        # greater than
        self.assertEqual(VersionNumber(1, 2, 3) <= VersionNumber(0, 2, 3), False)
        self.assertEqual(VersionNumber(1, 2, 3) <= VersionNumber(1, 1, 3), False)
        self.assertEqual(VersionNumber(1, 2, 3) <= VersionNumber(1, 2, 2), False)
        self.assertEqual(VersionNumber(3, 2, 1) <= VersionNumber(1, 2, 2), False)

        # less than
        self.assertEqual(VersionNumber(0, 2, 3) <= VersionNumber(1, 2, 3), True)
        self.assertEqual(VersionNumber(1, 1, 3) <= VersionNumber(1, 2, 3), True)
        self.assertEqual(VersionNumber(1, 2, 2) <= VersionNumber(1, 2, 3), True)
        self.assertEqual(VersionNumber(1, 2, 2) <= VersionNumber(3, 2, 1), True)

    def test_greater_than_equals(self):
        # equals
        self.assertEqual(VersionNumber(1, 2, 3) >= VersionNumber(1, 2, 3), True)

        # greater than
        self.assertEqual(VersionNumber(1, 2, 3) >= VersionNumber(0, 2, 3), True)
        self.assertEqual(VersionNumber(1, 2, 3) >= VersionNumber(1, 1, 3), True)
        self.assertEqual(VersionNumber(1, 2, 3) >= VersionNumber(1, 2, 2), True)
        self.assertEqual(VersionNumber(3, 2, 1) >= VersionNumber(1, 2, 2), True)

        # less than
        self.assertEqual(VersionNumber(0, 2, 3) >= VersionNumber(1, 2, 3), False)
        self.assertEqual(VersionNumber(1, 1, 3) >= VersionNumber(1, 2, 3), False)
        self.assertEqual(VersionNumber(1, 2, 2) >= VersionNumber(1, 2, 3), False)
        self.assertEqual(VersionNumber(1, 2, 2) >= VersionNumber(3, 2, 1), False)


if __name__ == '__main__':
    unittest.main()
