import pytest
n1=8
n2=2
def test_add():
    print("rahul")
    assert n1+n2==10, "passed"
def test_sub():
    assert n1-n2==6, "passed"
def test_multiply():
    assert n1*n2==10, "failed"
def test_div():
    assert n1/n2==4, "passed"