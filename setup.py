#!/usr/bin/env python
from setuptools import setup
from setuptools.command.test import test as TestCommand
import harvest
import sys


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren"t loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

with open("README.rst") as readme:
    long_description = readme.read()

setup(
    name="harvest",
    version=harvest.__version__,
    description=("Harvest: the gathering"),
    long_description=long_description,
    url="https://github.com/blueoct/harvest",
    author="Blue October",
    author_email="derek.sudduth@gmail.com",
    license="GNU General Public License (GPL), Version 3.0",
    packages=["harvest"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: General Public License"
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Langueage :: Python :: 3.4",
        "Programming Langueage :: Python :: 3.5",
    ],
    install_requires=["logstash_formatter"],
    packages=find_packages(),
    tests_require=[
        "mock>=1.0.0",
        "pytest",
        "pytest-cov",
    ],
    cmdclass={"test": PyTest}
)
