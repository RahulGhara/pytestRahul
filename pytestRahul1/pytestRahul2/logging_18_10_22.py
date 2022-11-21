import logging

LOG_FORMAT = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="log3.txt", level=logging.DEBUG)

logging.info("inputs are 5 and 6.......")
logging.error("oops..")
logging.debug("code is running")
