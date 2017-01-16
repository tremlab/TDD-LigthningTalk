import unittest
from sample_math_stuff import *


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_1_1(self):
        self.assertEqual(add_and_square(1, 1), 4)


if __name__ == '__main__':
    unittest.main()
