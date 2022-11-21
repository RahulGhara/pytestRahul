import logging
import pytest
import subprocess

logging.basicConfig(filename='ping_log.log', level=logging.INFO)
logging.info("Starting the code")
@pytest.fixture
def ping(c= "yahoo.com"):
    c = ["ping", "-n", "4", c]
    x = subprocess.run(c)
    if not x:
        logging.error("Not getting the reply")
    else:
        logging.info(x)
    yield x


# @pytest.fixture
def p_c():
    ping()
    yield ping



# def logAssert(test, msg):
#     if not test:
#         logging.error(msg)
#         assert test, msg


def test_ping(ping):
    logging.info("testing ping")
    assert ping == "CompletedProcess(args=['ping', '-n', '4', 'yahoo.com'], returncode=0)"
    # logAssert(ping == " CompletedProcess(args=['ping', '-n', '4', 'yahoo.com'], returncode=0)", "response not coming")


# log_file(ping)
# c = "yahoo.com"
# ping(c)
# logging.info(ping)
# logging.info("finish")
# p_c()