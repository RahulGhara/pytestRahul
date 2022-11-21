import pytest
import logging
import subprocess


def ping_log(x):
    logging.basicConfig(filename="test_command.log", level=logging.INFO)
    logging.info(x)


# @pytest.fixture
def ping_check(command):
    command = ['ping', '-n', '4', command]
    x = subprocess.run(command)
    ping_log(x)
    return x


@pytest.fixture
def p_c():
    yield ping_check


def test_ping(p_c):
    assert p_c, "getting reply"
    if p_c!=0:
        logging.debug("Getting reply")
        logging.info(p_c)
        ping_log(ping_check)
    else:
        logging.debug("not getting response")


# p = input("Enter the url: ")
ping_check("google.com")
