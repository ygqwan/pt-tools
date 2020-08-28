#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

def now():
    timeArray = time.localtime()
    now = time.strftime(r"%Y-%m-%d,%H:%M:%S", timeArray)
    return now

# cookie字符串解析成字典
def cookieParse(cookiesStr):
    cookie_dict = {}
    cookies = cookiesStr.split(';')

    for cookie in cookies:
        cookie = cookie.split('=')
        cookie_dict[cookie[0]] = cookie[1]

    return cookie_dict

