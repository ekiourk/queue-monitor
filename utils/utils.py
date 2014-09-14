#!/usr/bin/env python
# -*- coding: utf-8 -*-


def underscore_to_camelcase(value, capitalize_first=True):
    def camelcase(capitalize_first):
        if not capitalize_first:
            yield str.lower
        while True:
            yield str.capitalize
    c = camelcase(capitalize_first)
    return "".join(c.next()(x) if x else '_' for x in value.split("_"))