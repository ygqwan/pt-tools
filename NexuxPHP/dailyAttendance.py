#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from config import COOKIE, HEADER, URL
import requests
import re
import time

session = requests.session()
session.headers.update(HEADER)
session.cookies.update(COOKIE)


attendanceUrl = URL + '/attendance.php'


with session.get(URL) as res:
    r = re.compile(r'签到已得\d+')
    tip = r.search(res.text).group() if r.search(res.text) else '也许、、、'
    timeArray = time.localtime()
    otherStyleTime = time.strftime(r"%Y-%m-%d,%H:%M:%S", timeArray)
    print(otherStyleTime, tip)


COO = os.environ["COOKIE"]
print(COO)
