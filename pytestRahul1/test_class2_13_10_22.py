import pytest


def test_sum(calculator):
    assert calculator.add() == 10


def test_sub(calculator):
    assert calculator.sub(5, 5) == 10


def test_multiplication(calculator):
    assert calculator.multiply(5, 6) == 30


def test_division(calculator):
    assert calculator.div(60, 3) == 20
