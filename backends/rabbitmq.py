#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib
import base64
import json


class RabbitMqBackend(object):
    def __init__(self, config):
        """
        Access to the RabbitMQ Management HTTP API
        """
        self.config = config
        self.auth = base64.encodestring("%s:%s" % (self.config['user'], self.config['pass']))
        self.headers = {"Authorization" : "Basic %s" % self.auth}
        self.conn = httplib.HTTPConnection(self.config['host'], self.config['port'])

    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.conn.close()  

    def query(self, command):
        self.conn.request('GET', "/api/"+command, headers=self.headers)
        resp = self.conn.getresponse()
        content = resp.read()

        if resp is not None and resp.status == 200:
            return json.loads(content)
        return []

