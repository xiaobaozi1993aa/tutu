#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:Common_Conf.py
@time:2020年8月28日
'''
from functools import wraps
import shutil
import datetime, os, time


#excel初始路径
start_expath = "H:\\美印\\tt_time\\time.xls"

#日志路径
logpath = "H:\\美印\\tt_log\\"

#报告路径
reportpath = "H:\\美印\\tt_report\\"



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
    if int(week_day) == 1:
        if not isExists:
            os.makedirs(path)
            end_path = path + 'time.xls'
            shutil.copyfile(start_expath, end_path)
            return path
        else:
            return path
    else:
        lists = os.listdir(logpath)
        lists.sort(key=lambda fn: os.path.getmtime(logpath + "\\" + fn))
        file_new = os.path.join(logpath, lists[-1])
        return  file_new+'\\'

path = get_log_time()
end_path = str(path) + 'time.xls'

# 测试
ceshi_host = 'https://m-dev.meiyintutu.com'
# 生产
shengchan_host = 'https://m.meiyintutu.com'

host = shengchan_host

