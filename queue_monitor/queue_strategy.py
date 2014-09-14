#!/usr/bin/env python
# -*- coding: utf-8 -*-

from triggers.trigger import TriggerFactory


class QueueStrategy(object):
    
    def __init__(self, queue, strategies):
        self.queue = queue
        self.strategies = strategies

    def run_strategies(self, queue_size):
        for strategy in self.strategies:
            TriggerFactory.get_trigger(strategy).run(queue_size)
