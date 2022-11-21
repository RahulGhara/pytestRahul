import pytest


@pytest.fixture()
def input_nos():
    n1 = 50
    n2 = 7
    yield n1, n2
