#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import requests
import configparser

HOST = 'www.hddolby.com'
URL = 'https://' + HOST


HEADER = {
    'Host': HOST,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept-Language': 'zh-CN',
    'Referer': URL + '/details.php?id=17793&hit=1',
}

# 获取cookie , 环境变量取不到就到配置文件取
try:
    # COOKIE JSON 格式放入 github 仓库 Secrets中
    COOKIE_STR = os.environ["COOKIE"]
except:
    # COOKIE DICT 格式在此填写 ，此处会明文暴露 ，不建议在此填写
    config = configparser.RawConfigParser()
    config.read('./NexusPHP/config.ini')
    COOKIE_STR = config['c1']['cookie']

COOKIE = eval(COOKIE_STR)


# 设置请求头 、 cookie
SESSION = requests.session()
SESSION.headers.update(HEADER)
SESSION.cookies.update(COOKIE)
