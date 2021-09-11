import unittest
import sys

sys.path.append('..')
from PyVersionNumber import VersionNumber


class TestCaseMisc(unittest.TestCase):
    def test_in_development(self):
        self.assertEqual(VersionNumber(0, 1, 2).in_development, True)
        self.assertEqual(VersionNumber(0, 2, 3).in_development, True)
        self.assertEqual(VersionNumber(1, 1, 1).in_development, False)
        self.assertEqual(VersionNumber(1, 5, 0).in_development, False)


if __name__ == '__main__':
    unittest.main()
