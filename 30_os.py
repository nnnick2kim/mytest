#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-

import platform

os = platform.system()
bit = platform.architecture()
ver = platform.version()
result = os + ' ' + bit[0]
print result

