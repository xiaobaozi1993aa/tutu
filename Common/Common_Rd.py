#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:Common_Rd.py
@time:2020年8月20日
'''
import random

def get_rdconf():
    id = random.randint(100000000000000000, 9000000000000000000)
    mobile = random.randint(13900000000,13999999999)
    vipid = 'C'+str(random.randint(1000000000,9000000000))
    return id,mobile,vipid

