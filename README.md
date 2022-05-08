pynmeagps
=========

[Current Status](#currentstatus) |
[Installation](#installation) |
[How to Use](#howtouse) |
[Author & License](#author)

`pysocketstream` is an simple utility class which wraps a socket object and allows it to be handled using standard stream-like `read(bytes)` and `readline()` methods.

The intention is to make it as easy as possible to read, parse and utilise NMEA GNSS/GPS messages in Python applications. 

The `pysocketstream` homepage is located at [https://github.com/semuconsulting/pysocketstream](https://github.com/semuconsulting/pysocketstream).

---
## <a name="currentstatus">Current Status</a>

Sphinx API Documentation in HTML format is available at [https://www.semuconsulting.com/pysocketstream](https://www.semuconsulting.com/pysocketstream).

Contributions welcome - please refer to [CONTRIBUTING.MD](https://github.com/semuconsulting/pynmeagps/blob/master/CONTRIBUTING.md).

[Bug reports](https://github.com/semuconsulting/pynmeagps/blob/master/.github/ISSUE_TEMPLATE/bug_report.md) and [Feature requests](https://github.com/semuconsulting/pynmeagps/blob/master/.github/ISSUE_TEMPLATE/feature_request.md) - please use the templates provided.

---
## <a name="installation">Installation</a>

`pysocketstream` is compatible with Python >=3.7 and has no third-party library dependencies.

In the following, `python` & `pip` refer to the Python 3 executables. You may need to type 
`python3` or `pip3`, depending on your particular environment.

![Python version](https://img.shields.io/pypi/pyversions/pynmeagps.svg?style=flat)
[![PyPI version](https://img.shields.io/pypi/v/pynmeagps.svg?style=flat)](https://pypi.org/project/pynmeagps/)
![PyPI downloads](https://img.shields.io/pypi/dm/pynmeagps.svg?style=flat)

The recommended way to install the latest version of `pysocketstream` is with
[pip](http://pypi.python.org/pypi/pip/):

```shell
python -m pip install --upgrade pysocketstream
```

---
## <a name="howtouse">How to Use</a>

```
class SocketStream(socket, **kwargs)
```

You can create an `SocketStream` object by calling the constructor with an active socket object. 

**NB:** It is the responsibility of the calliing application to monitor the returned data for error or end of stream conditions e.g. by checking length of returned data matches requested number of bytes.

Example (*in this illustration the socket is streaming NMEA data from a GNSS receiver*):

```python
>>> import socket
>>> from pysocketstream import SocketStream
>>> sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM):
>>> sock.connect(("192.168.0.72", 50007))
>>> stream = SocketStream(sock, bufsize=4096)
>>> data = stream.readline()
>>> data
b'$GNDTM,W84,,0.0,N,0.0,E,0.0,W84*71\r\n'
```

---
## <a name="author">Author & License Information</a>

semuadmin@semuconsulting.com

`pysocketstream` is maintained entirely by volunteers. If you find it useful, a small donation would be greatly appreciated!

[![Donations](https://www.paypalobjects.com/en_GB/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=4TG5HGBNAM7YJ)