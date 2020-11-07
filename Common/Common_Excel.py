#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:Common_Excel.py
@time:2020年8月28日
'''
import xlrd
from xlutils.copy import copy
from Common.Common_Conf import expath


# #打开文件
# xls = xlrd.open_workbook(r'H:\time.xls')
# #获取表数
# sheets = xls.nsheets
# #获取第一张表对象
# a = xls.sheets()[0]
# #获取列数
# b = a.ncols
# #获取行数
# c = a.nrows
# print(b,c)

def get_xls(i):
    xls = xlrd.open_workbook(r'%s' % expath, formatting_info=True)
    xlsc = copy(xls)
    shtc = xlsc.get_sheet(i)
    return xlsc,shtc

def get_nrows(i):
    xls = xlrd.open_workbook(r'%s' % expath)
    a = xls.sheets()[i]
    number = a.nrows
    return number

if __name__ == '__main__':
    pass
