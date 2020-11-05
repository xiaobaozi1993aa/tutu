#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:Common_Db.py
@time:2020年8月15日
'''
import pymysql
import redis


def common_db():
    db = pymysql.Connect('drdsbggaj9sk0176public.drds.aliyuncs.com',
                         'mytutu',
                         'dev_java_mytutu_130532',
                         'mytutu')
    cursor = db.cursor()
    return db,cursor

def common_rd():
    pool = redis.ConnectionPool(host='172.16.38.134', port=6379, password='130532Zzre', db=0)
    r = redis.Redis(connection_pool=pool)
    return r

# get 键值对获取
# set 键值对修改
# hget hash获取
# hset hash修改