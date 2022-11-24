import pytest
from pytestRahul import conftest

# import sys
# sys.path.insert(0, 'C:\Users\cbnits\PycharmProjects\pythonProjectRahul\pytestRahul1')


#   @pytest.fixture(scope="session")
# def b_setup():
#     total = 100
#     print("Launch browser")
#     print("Login")
#     x = "Ready to add items"
#     print("Browse product")
#     y = "Ready to check out"
#     yield x, y, total
#   print("Log off")


# class cal:
#
#     def add(n1, n2):
#         return n1 + n2
#
#     def sub(n1, n2):
#         return n1 - n2
#
#     def multiply(n1, n2):
#         return n1 * n2
#
#     def div(n1, n2):
#         return n1 / n2
#
#
# @pytest.fixture()
# def calculator():
#     yield cal

# @pytest.fixture(params=[8, 9])
# def check_no(request):
#     yield request.param


@pytest.fixture()
def add(input_nos):
    s = input_nos[0] + input_nos[1]
    yield s
