import subprocess


def ping(c="yahoo.com"):
    c = ["ping", "-n", "4", c]
    x = subprocess.run(c)
    # if not x:
    #     logging.error("Not getting the reply")
    # else:
    #     logging.info(x)
    print(x)
ping()