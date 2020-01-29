from random import randint
from unittest import TestCase

from tests_examples.example_1.division_detect import division_detect


class TestDivisionDetect(TestCase):
    def setUp(self) -> None:
        self.random_numerator = randint(0, 100000)

    def test_it_returns_true_if_division_by_number_is_successful(self):
        result = division_detect(
            numerator=self.random_numerator, denominator=randint(1, 100000)
        )
        self.assertTrue(result)

    def test_it_returns_false_if_division_by_number_is_not_possible(self):
        result = division_detect(numerator=self.random_numerator, denominator=0)
        self.assertFalse(result)


