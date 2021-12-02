import pytest

from day4 import day4 as day


class TestDay4:

    def test_is_six_digit(self):
        assert day.is_six_digit(123456) is True
        assert day.is_six_digit(21) is False

    def test_is_in_range(self):
        assert day.is_in_range(168630) is True
        assert day.is_in_range(718098) is True
        assert day.is_in_range(1) is False
        assert day.is_in_range(200123) is True
        assert day.is_in_range(2001230) is False

    def test_has_adjacent(self):
        assert day.has_adjacent(123446) is True
        assert day.has_adjacent(123456) is False
        assert day.has_adjacent(111111) is True

    def test_never_decreses(self):
        assert day.never_decreases(135679) is True
        assert day.never_decreases(111123) is True
        assert day.never_decreases(111132) is False
        assert day.never_decreases(7651) is False

    def test_has_unique_adjacent(self):
        assert day.has_unique_adjacent(112233) is True
        assert day.has_unique_adjacent(111122) is True
        assert day.has_unique_adjacent(123444) is False
