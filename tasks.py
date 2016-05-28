#!/usr/bin/env python3
"""Tasks made easy with invoke library.

Using the awesome invoke library as a task runner to assist with
local builds.

"""

from invoke import task
from invoke import run
import os
import shutil
import sys


@task
def clean():
    """Cleans build artifacts.

    Cleans build artifacts by removing temp directories and files.

    """
    build_dirs = ['./harvest/__pycache__',
                  './harvest.egg-info',
                  './dist',
                  './build',
                  './__pycache__']
    for dir in build_dirs:
        if os.path.exists(dir):
            sys.stdout.write('removing {}\n'.format(dir))
            shutil.rmtree(dir)
    sys.stdout.write('environment is clean!\n')


@task
def build():
    """Builds a pip package (wheel) for mason.

    Executes ``python setup.py bdist_wheel`` command which generates a python
    wheel file.  If running on an OS other than Windows, ``python3`` will be
    called instead.

    """
    run('python3 setup.py sdist bdist_wheel')
