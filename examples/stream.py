"""
stream.py.

A simple test of the pysocketstream iterator.

This streams any line-delimited (LF = 0x0a) protocol from a socket (e.g. NMEA)

Press CTRL-C to terminate.

Created on 5 May 2022

:author: semuadmin
:copyright: SEMU Consulting © 2022
:license: BSD 3-Clause
"""

import socket
from pysocketstream import SocketStream, LF

# amend as required...
HOST = "192.168.0.72"
PORT = 50007
BUFSIZE = 2048

with socket.socket() as sock:
    try:

        sock.connect((HOST, PORT))
        stream = SocketStream(sock, bufsize=BUFSIZE, iterseparator=LF)
        for data in stream:
            print(data)

    except KeyboardInterrupt:
        print("Terminated by user")
