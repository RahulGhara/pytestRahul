 import pytest


class Operation:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        sum1 = self.n1 + self.n2
        return sum1


@pytest.fixture()
def b():
    obj1 = Operation(8, 2)
    yield obj1.add()


def test_operation(b):
    assert b == 12, "Passed"

def test_fd(cal):
    assert cal.sum(1, 2)
