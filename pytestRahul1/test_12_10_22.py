import pytest

a = 8
b = 2

#add
@pytest.fixture()
def add():
    add = a + b
    yield add


@pytest.fixture()
def sub():
    sub = a - b
    yield sub


@pytest.fixture()
def multiply():
    mul = a * b
    yield mul


@pytest.fixture()
def division():
    div = a / b
    yield div


def test_add(add):
    assert add == 10, "test passed"


def test_sub(sub):
    assert sub == 6, "test passed"


def test_multiplication(multiply):
    assert multiply == 20, "test failed"


def test_division(division):
    assert division == 4, "test passed"
