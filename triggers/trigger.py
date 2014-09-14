#!/usr/bin/env python
# -*- coding: utf-8 -*-

from actions.actions import ActionFactory


class Trigger(object):

    def __init__(self, data):
        self.data = data

    def run_actions(self):
        for action, params in self.data['actions'].iteritems():
            ActionFactory.get_action(action, params).run()


class LimitTrigger(Trigger):
    def run(self, queue_size):
        if self.data['type'] == "more_than":
            if self.data['value'] < queue_size:
                self.run_actions()
        if self.data['type'] == "less_than":
            if self.data['value'] > queue_size:
                self.run_actions()


class TriggerFactory(object):
    @staticmethod
    def get_trigger(data):
        return globals()[data['trigger_type'].capitalize()+"Trigger"](data)
