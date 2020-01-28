import unittest

from tests_examples.square.square import square


class TestSquare(unittest.TestCase):
    def test_it_returns_square_of_number(self):
        result = square(2)
        expected = 4

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

