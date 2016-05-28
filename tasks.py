#!/usr/bin/env python3
"""Tasks made easy with invoke library.

Using the awesome invoke library as a task runner to assist with
local builds.

"""

from invoke import run, task


@task
def clean():
    """cleans the build environment"""
    pass


@task
def build():
    """builds locally for test purposes"""
    pass
