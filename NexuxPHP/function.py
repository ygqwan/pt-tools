import time


def now():
    timeArray = time.localtime()
    now = time.strftime(r"%Y-%m-%d,%H:%M:%S", timeArray)
    return now

# cookie字符串解析成字典
def cookieParse(str):
    return eval(COOKIE_STR)

