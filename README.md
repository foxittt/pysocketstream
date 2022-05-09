pysocketstream
=========

[Current Status](#currentstatus) |
[Installation](#installation) |
[How to Use](#howtouse) |
[Author & License](#author)

`pysocketstream` is a simple utility class which wraps a socket object and allows it to be handled using standard stream-like `read(num)`, `readuntil(separator)` and `readline()` methods. The class incorporates a configurable iterator.

The `pysocketstream` homepage is located at [https://github.com/semuconsulting/pysocketstream](https://github.com/semuconsulting/pysocketstream).

---
## <a name="currentstatus">Current Status</a>

Currently in Alpha.

![Build](https://img.shields.io/github/workflow/status/semuconsulting/pysocketstream/pysocketstream)
![Release Date](https://img.shields.io/github/release-date-pre/semuconsulting/pysocketstream)
![Last Commit](https://img.shields.io/github/last-commit/semuconsulting/pysocketstream)
![Contributors](https://img.shields.io/github/contributors/semuconsulting/pysocketstream.svg)
![Open Issues](https://img.shields.io/github/issues-raw/semuconsulting/pysocketstream)

Sphinx API Documentation in HTML format is available at [https://www.semuconsulting.com/pysocketstream](https://www.semuconsulting.com/pysocketstream).

Contributions welcome - please refer to [CONTRIBUTING.MD](https://github.com/semuconsulting/pysocketstream/blob/master/CONTRIBUTING.md).

[Bug reports](https://github.com/semuconsulting/pysocketstream/blob/master/.github/ISSUE_TEMPLATE/bug_report.md) and [Feature requests](https://github.com/semuconsulting/pysocketstream/blob/master/.github/ISSUE_TEMPLATE/feature_request.md) - please use the templates provided.

---
## <a name="installation">Installation</a>

`pysocketstream` is compatible with Python >=3.7 and has no third-party library dependencies.

The recommended way to install the latest version of `pysocketstream` is with
[pip](http://pypi.python.org/pypi/pip/):

```shell
python3 -m pip install -i https://testpypi.python.org/pypi pysocketstream
```

---
## <a name="howtouse">How to Use</a>

```
class SocketStream(socket, **kwargs)
```

You can create a `SocketStream` object by calling the constructor with an active socket object. 

**kwargs:**
- `bufsize` - default buffer size (defaults to 4096)
- `itersize` - number of bytes to read in iterator; if == 0, will use readuntil(iterseparator)
- `iterseparator` - separator to use in iterator (defaults to CRLF)
 
**NB:** It is the responsibility of the calliing application to monitor the returned data for error or end of stream conditions e.g. by checking length of returned data matches requested number of bytes.

Example (*in this illustration the socket is streaming NMEA data from a GNSS receiver*):

```python
>>> import socket
>>> from pysocketstream import SocketStream, CRLF
>>> sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM):
>>> sock.connect(("192.168.0.72", 50007))
>>> stream = SocketStream(sock, bufsize=4096, iterseparator=CRLF)
>>> data = stream.readline()
>>> data
b'$GNDTM,W84,,0.0,N,0.0,E,0.0,W84*71\r\n'
```

---
## <a name="author">Author & License Information</a>

semuadmin@semuconsulting.com

![License](https://img.shields.io/github/license/semuconsulting/pysocketstream.svg)

`pysocketstream` is maintained entirely by volunteers. If you find it useful, a small donation would be greatly appreciated!

[![Donations](https://www.paypalobjects.com/en_GB/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=4TG5HGBNAM7YJ)
