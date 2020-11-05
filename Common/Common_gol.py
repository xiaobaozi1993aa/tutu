#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:Common_gol.py
@time:2020年8月28日
'''
def _init():
    global _global_dict
    _global_dict = {}

def set_value(name, value):
    _global_dict[name] = value

def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue


'''
公共参数说明：
token       请求头使用，test_login提供
addid       下单时使用，test_get_addid提供
orderid     下单时使用，test_creatorder提供
payid       支付时使用，test_buy_order提供
pictureid   删除相册使用，test_creat_picture提供


'''