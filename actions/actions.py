#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.utils import underscore_to_camelcase
from subprocess import call

import smtplib
from email.mime.text import MIMEText


class Action(object):

    def __init__(self, params):
        self.params = params

    def run(self):
        #print "Action not implemented yet"
        pass


class RunCommand(Action):
    def run(self):
        call(self.params['cmd'].split())


class Email(Action):
    def run(self):
        msg = MIMEText(self.params['subject'])
        msg['Subject'] = self.params['subject']
        msg['From'] = self.params['from']
        msg['To'] = self.params['to']

        s = smtplib.SMTP('localhost')
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
        s.quit()


class ActionFactory(object):
    @staticmethod
    def get_action(action, params):
        try:
            return globals()[underscore_to_camelcase(action)](params)
        except Exception, e:
            return Action(params)