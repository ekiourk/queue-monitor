# -*- coding: utf-8 -*-

import unittest

import sys
reload(sys)
sys.setdefaultencoding("utf8")

from queue_monitor.strategy_parser import StrategyParser


class TestStrategyParser(unittest.TestCase):

    def test_instantiate_parser(self):
        """Test if the parser can be instantiated"""

        parser = StrategyParser("monitoring_example.yaml")

        self.assertIsInstance(parser, StrategyParser)

    def test_parser_parsing_example_file(self):
        """Test if the parser parses correctly the example file"""

        parser = StrategyParser("monitoring_example.yaml")

        self.assertTrue( 'celery' in parser.strategies )
        self.assertTrue( 'rabbitmq' in parser.backend['name'] )