#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import sys
reload(sys)
sys.setdefaultencoding("utf8")

from utils.utils import *

class TestUtils(unittest.TestCase):

    def test_underscore_to_camelcase(self):
        self.assertEquals('HelloWorld', underscore_to_camelcase('hello_world'))
        self.assertEquals('_HelloWorld', underscore_to_camelcase('_hello_world'))
        self.assertEquals('Hello_World', underscore_to_camelcase('hello__world'))
        self.assertEquals('Hello_World_', underscore_to_camelcase('hello__world_'))
        self.assertEquals('_Hello_World_', underscore_to_camelcase('_hello__world_'))
        self.assertEquals('helloWorld', underscore_to_camelcase('hello_world', capitalize_first=False))