#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time


def now():
    timeArray = time.localtime()
    now = time.strftime(r"%Y-%m-%d,%H:%M:%S", timeArray)
    return now
