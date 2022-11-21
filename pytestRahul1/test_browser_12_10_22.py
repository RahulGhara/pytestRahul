import pytest


@pytest.mark.shopping
def test_add_item(b_setup):
    print("item added to cart")
    assert b_setup[0] == "Ready to add items"


def test_purchase(b_setup):
    print("cart empty and checked out")
    assert b_setup[1] == "Ready to checkout"


@pytest.mark.stock
def test_stock(b_setup):
    assert b_setup[2] == 100
