import pytest
from src.main import EvenOrOdd


def test_even_number():
    assert EvenOrOdd(2) == "even"
    assert EvenOrOdd(0) == "even"
    assert EvenOrOdd(-4) == "even"


def test_odd_number():
    assert EvenOrOdd(3) == "odd"
    assert EvenOrOdd(1) == "odd"
    assert EvenOrOdd(-5) == "odd"
