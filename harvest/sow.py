""" Gathers gherkin style tests using behave module then prepares them to run
in the environment of choice.
"""
import yaml
import logging


class Sow:
    """Gathers and preps features for test environment"""

    def __init__(self, ):
        self.silo = []
        self.config = {}
        self.parse_config()

    def parse_configs(self, path=None):
        """Parses sow's yaml config file."""

        with open("./config/defaults/sow.yaml", "r") as defaults:
            self.config = yaml.safe_load(defaults.read())
        if path is not None:
            with open(path, "r") as custom:
                custom_config = yaml.safe_load(custom.read())

    def 
