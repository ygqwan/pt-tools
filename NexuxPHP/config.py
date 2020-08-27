#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import requests


Host = 'www.hddolby.com'

URL = 'https://' + Host

HEADER = {
    'Host': Host,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept-Language': 'zh-CN',
    'Referer': URL + '/details.php?id=17793&hit=1', }

COOKIE = {}

# 获取cookie , 环境变量取不到就到配置文件取
try:
    # COOKIE JSON 格式放入 github 仓库 Secrets中
    COOKIE_STR = os.environ["COOKIE"]
    COOKIE = eval(COOKIE_STR)
except:
    # COOKIE DICT 格式在此填写 ，此处会明文暴露 ，不建议在此填写
    COOKIE = {
        '__cfduid': 'd7910ed696e066626a66764184d04fe7b1598230158',
        'c_secure_uid': 'MjEwMTA%3D',
        'c_secure_pass': 'a7b591404cda1eb1ce113e26230988db',
        'c_secure_ssl': 'eWVhaA%3D%3D',
        'c_secure_tracker_ssl': 'bm9wZQ%3D%3D',
        'c_secure_login': 'bm9wZQ % 3D % 3D'
    }


# 设置请求头 、 cookie
SESSION = requests.session()

SESSION.headers.update(HEADER)
SESSION.cookies.update(COOKIE)
