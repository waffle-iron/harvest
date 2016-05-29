=======
Harvest
=======

Automation Done Right.  Harvest gathers all the tooling you need to create, test, and deploy your code.

Overview
========

If you're tired of using in-house tools for testing and development that never seem to work together, this is for you.

Harvest is all about productive coding - achieved by being highly automatable by design.  This framework provides a CLI which can wrap the tools that you use every day.

Testing
=======
.. image:: https://travis-ci.org/blueoct/harvest.svg?branch=master
  :target: https://travis-ci.org/blueoct/harvest

.. image:: https://codecov.io/gh/blueoct/harvest/branch/master/graph/badge.svg?branch=master
  :target: https://codecov.io/gh/blueoct/harvest?branch=master

Builds and test execution are handled by Travis CI.

The following can be executed to build and test locally::

  pip install -e .
  pip install -r dev_requirements.txt
  py.test
