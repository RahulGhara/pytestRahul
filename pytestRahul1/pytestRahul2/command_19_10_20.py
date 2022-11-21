import logging
import subprocess

# import pytest


def ping_log(x):
    logging.basicConfig(filename="ping.log", level=logging.INFO)
    logging.info(x)


# @pytest.fixture
def ping_check(command):
    command = ['ping', '-n', '4', command]
    x = subprocess.run(command)
    if x:
        ping_log(x)
    return x

# @pytest.fixture
# def p_c(ping_check):
#     ping_check.make_ful()
#     yield ping_check

# def test_ping(ping_check):
#     assert ping_check == True, "getting reply"
#     if ping_check:
#         logging.DEBUG("Getting reply")
#         logging.info(ping_check)
#     else:
#         logging.debug("not getting response")


p = input("Enter the url: ")
ping_check(p)
