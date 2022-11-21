import pytest


@pytest.mark.dependency(name='test1')
@pytest.mark.parametrize("input1,input2", [(12, 6)])
def test_nos(input1, input2):
    assert input1 >= input2


@pytest.mark.dependency()
@pytest.mark.parametrize("input1,input2", [(12, 6)])
def test_add(input1, input2):
    assert input1 + input2 == 18


@pytest.mark.dependency(depends=['test1'])
@pytest.mark.parametrize("input1,input2", [(12, 6)])
def test_division(input1, input2):
    assert input1 / input2 == 2


@pytest.mark.dependency()
@pytest.mark.parametrize("input1,input2", [(12, 6)])
def test_multiplication(input1, input2):
    assert input1 * input2 == 72
