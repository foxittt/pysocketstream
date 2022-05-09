"""
test_iter.py.

A simple test of the pysocketstream iterator.

Created on 5 May 2022

:author: semuadmin
:copyright: SEMU Consulting © 2022
:license: BSD 3-Clause
"""

import socket
from pysocketstream import SocketStream, CRLF

with socket.socket() as sock:
    try:

        sock.connect(("localhost", 50007))
        stream = SocketStream(sock, bufsize=2048, iterseparator=CRLF)
        for data in stream:
            print(data)

    except KeyboardInterrupt: 
        print("Terminated by user")
