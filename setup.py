#!/usr/bin/env python
from setuptools import setup, find_packages
from harvest import __version__ as version

setup(
    name="harvest",
    version=version,
    url="http://github.com/blueoct/harvest",
    author="Blue October",
    author_email="derek.sudduth@gmail.com",
    description=("Harvest: the gathering"),
    long_description=open("README.md").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Langueage :: Python :: 3.4",
        "Programming Langueage :: Python :: 3.5",
    ],
    install_requires=["behave","pyyaml"],
)
