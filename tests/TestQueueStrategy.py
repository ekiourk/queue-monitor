#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import sys
reload(sys)
sys.setdefaultencoding("utf8")

from queue_monitor.strategy_parser import StrategyParser
from queue_monitor.queue_strategy import QueueStrategy


class TestQueueStrategy(unittest.TestCase):

    def test_instantiate_queue_strategy(self):
        """Test if the QueueStrategy can be instantiated"""

        queue, strategies = StrategyParser("monitoring_example.yaml").strategies.popitem()

        queue_strategy = QueueStrategy(queue, strategies)

        self.assertEquals(queue, queue_strategy.queue)
        self.assertEquals(strategies, queue_strategy.strategies)