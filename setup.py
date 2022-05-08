"""
Created on 5 May 2022

@author: semuadmin
"""
import setuptools

from pysocketstream import version as VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysocketstream",
    version=VERSION,
    author="semuadmin",
    author_email="semuadmin@semuconsulting.com",
    description="Socket Stream Wrapper",
    long_description="Allows sockets to be handled using stream-like `read(bytes)` and `readline()` methods",
    long_description_content_type="text/markdown",
    url="https://github.com/semuconsulting/pynmeagps",
    packages=setuptools.find_packages(exclude=["tests", "examples", "docs"]),
    license="BSD 3-Clause 'Modified' License",
    keywords="pysocketstream socket",
    platforms="Windows, MacOS, Linux",
    project_urls={
        "Bug Tracker": "https://github.com/semuconsulting/pysocketstream",
        "Documentation": "https://github.com/semuconsulting/pysocketstream",
        "Sphinx API Documentation": "https://www.semuconsulting.com/pysocketstream",
        "Source Code": "https://github.com/semuconsulting/pysocketstream",
    },
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 2 - Beta",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: BSD License",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
)
