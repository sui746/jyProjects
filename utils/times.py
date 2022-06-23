# -*- coding:utf-8 -*-

import time
import datetime
from functools import wraps
# wraps函数：避免多个函数被两个装饰器装饰时就报错,因为两个函数名一样,第二个函数再去装饰的话就报错，最好是加上这个，代码更加健壮

def timestamp():
    """时间戳"""
    return time.time()


def dt_strftime(fmt="%Y%m"):
    """
    datetime格式化时间
    :param fmt "%Y%m%d %H%M%S
    """
    return datetime.datetime.now().strftime(fmt)


def sleep(seconds=1.0):
    """
    睡眠时间
    """
    time.sleep(seconds)


def running_time(func):
    """函数运行时间"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timestamp()
        res = func(*args, **kwargs)
        print("校验元素done！用时%.3f秒！" % (timestamp() - start))
        return res

    return wrapper


if __name__ == '__main__':
    print(dt_strftime("%Y%m%d%H%M%S"))