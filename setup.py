#!/usr/bin/env python
from setuptools import setup, find_packages
from harvest import __version__ as version

setup(
    name="harvest",
    version=version,

    author="Blue October",
    author_email="derek.sudduth@gmail.com",

    description=("Harvest: the gathering"),
    long_description=open("README").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Langueage :: Python :: 3.4",
        "Programming Langueage :: Python :: 3.5",
    ],
)
