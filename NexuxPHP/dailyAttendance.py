#!/usr/bin/python
# -*- coding: UTF-8 -*-

from function import now
from config import SESSION, URL
import re
import time

# 完整签到url
attendanceUrl = URL + '/attendance.php'

with SESSION.get(attendanceUrl) as res:
    r = re.compile(r'签到已得\d+')
    tip = r.search(res.text).group() if r.search(res.text) else res.text

    print(now(), tip)
