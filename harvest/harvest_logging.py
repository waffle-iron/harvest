"""Logging for Harvest.
Uses python-logstash-formatter to create JSON logs that can be easily fed into
logstash.
http://github.com/exoscale/python-logstash-formatter
"""
import logging
from logstash_formatter import LogstashFormatterV1


def filelogger(path="./harvest.log", name=None, level=logging.info):
    file_logger = logging.getLogger(name)
    handler = logging.FileHandler(path)
    formatter = LogstashFormatterV1()
    handler.setFormatter(formatter)
    file_logger.setLevel(level)
    file_logger.addHandler(handler)
    return file_logger


def streamlogger(name=None, level=logging.warning):
    stream_logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = LogstashFormatterV1()
    handler.setFormatter(formatter)
    stream_logger.setLevel(level)
    stream_logger.addHandler(handler)
    return stream_logger
