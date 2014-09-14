#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import httplib

import sys
reload(sys)
sys.setdefaultencoding("utf8")

from backends.rabbitmq import RabbitMqBackend
from queue_monitor.strategy_parser import StrategyParser


class TestRabbitMqBackend(unittest.TestCase):

    def test_instantiate_parser(self):
        """Test if the RabbitMqBackend can be instantiated"""

        with RabbitMqBackend(StrategyParser("monitoring_example.yaml").backend) as backend:

            self.assertIsInstance(backend, RabbitMqBackend)

    def test_connect_to_rabbitmq(self):

        with RabbitMqBackend(StrategyParser("monitoring_example.yaml").backend) as backend:
            self.assertIsInstance(backend.conn, httplib.HTTPConnection)

        self.assertEquals('Idle', backend.conn._HTTPConnection__state)

    def test_query_rabbitmq(self):

        with RabbitMqBackend(StrategyParser("monitoring_example.yaml").backend) as backend:

            result = backend.query('queues/')

        self.assertTrue(isinstance(result, list))
        self.assertTrue(len(result) > 1)

    def test_wrong_query_rabbitmq(self):

        with RabbitMqBackend(StrategyParser("monitoring_example.yaml").backend) as backend:

            result = backend.query('wrongcommand/')

        self.assertTrue(isinstance(result, list))
        self.assertEquals([], result)

