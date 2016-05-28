"""Harvest functional tests."""

from harvest import harvest
import mock
import os
import unittest
import sys


class TestHarvest:
    def test_answer(self):
        test_data = "test"
        return harvest.test(test_data)
