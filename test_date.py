#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime
import time

"""
datetime 日期+时间组合
datetime.date 日期
datetime.time 时间

timedelta 两个时间之间的差异?
tzinfo 时区抽象类
timezone UTC 具体 tz
"""

#print(type(datetime.now()))
#t = time(datetime.now())
#print(datetime.time(datetime.now()))
#print(datetime.date(datetime.now()))
#print(date.today())
#print(date.weekday(date.today()))
#print(datetime.weekday(datetime.today()))
#print(datetime.now().replace(microsecond=0))

#当前时间
print(datetime.now())
#当前时间不带毫秒
print(datetime.now().replace(microsecond=0))
#今天是星期几
print(datetime.weekday(datetime.now()))
#日期
print(datetime.date(datetime.now()))
#时间
print(datetime.time(datetime.now()))

#当前时间戳
print(time.time())

#datetime 从时间戳
print(datetime.fromtimestamp(time.time()))
