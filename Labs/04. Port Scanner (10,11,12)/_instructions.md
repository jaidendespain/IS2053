# Instructions

For this lab, you will create a port scanner similar to "nmap." You only need to determine if the port is OPEN. If it is CLOSED or UNKNOWN, then your scanner will not report that information to the user (unless you want to go the extra mile).

You can test your program by scanning the first 500 ports


#### Imports needed:
import socket
import time (to see how long it takes to scan 500 ports)


#### Methods Used:
You will need to look up some of the methods contained in the socket import using this online resource: https://docs.python.org/3/library/socket.html