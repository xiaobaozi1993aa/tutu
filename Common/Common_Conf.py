#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:Common_Conf.py
@time:2020年8月28日
'''
from functools import wraps
import datetime
import datetime, os, time


def print_func(func):
    @ wraps(func)
    def start_pr(*args,**kwargs):
        print(str(datetime.datetime.now()))
        print("*************************用例{}开始执行***************************".format(func.__name__))
        test_func = func(*args,**kwargs)
        print("*************************用例{}执行结束***************************".format(func.__name__))
        return test_func
    return start_pr

def get_log_time():
    t_date=datetime.date.today()
    week_day = t_date.strftime("%w")
    name =  time.strftime("%Y_%m_%d")
    path = "H:\\美印\\tt_log\\%s\\" % name
    isExists = os.path.exists(path)
    if int(week_day) == 6:
        if not isExists:
            os.makedirs(path)
            #print(path + ' 创建成功')
        else:
            pass
            #rint(path + ' 目录已存在')
    return path

path = get_log_time()
# 测试
ceshi_host = 'https://m-dev.meiyintutu.com'
# 生产
shengchan_host = 'https://m.meiyintutu.com'

host = shengchan_host


#excel路径
expath = "H:\\美印\\tt_log\\time.xls"

#日志路径
logpath = "H:\\美印\\tt_log\\"

#报告路径
reportpath = "H:\\美印\\tt_report\\"


