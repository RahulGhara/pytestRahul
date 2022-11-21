# import subprocess
# import logging
#
# logging.basicConfig(filename="ping_test.txt", level=logging.DEBUG, filemode='w')
#
# logging.info("Found the ip address 192.168.1.97")
# host = "192.168.1.97"
#
#
# def ping_check(host):
#     command = ['ping', '-n', '4', host]
#     logging.debug("calling the command")
#
#     return subprocess.run(command, stdout=f)
#
#
# # logger.debug("checking the ip")
# ping_check(host)
# with open('ping_test.txt') as f:
#     (ping_check)
