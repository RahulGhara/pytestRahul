import pytest


@pytest.mark.parametrize("test_input,expected", [(6, 15), (5, 8)])
def test_opr(test_input, expected):
    assert 3+test_input == expected
