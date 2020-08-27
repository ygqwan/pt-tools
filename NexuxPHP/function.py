import time


def now():
    timeArray = time.localtime()
    now = time.strftime(r"%Y-%m-%d,%H:%M:%S", timeArray)
    return now
