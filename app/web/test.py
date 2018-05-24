#!/usr/bin/env python
__author__ = 'Albino'

from . import web

@web.route('/test')
def test():
    return 'hello', 200