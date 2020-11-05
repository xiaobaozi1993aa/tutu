#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:qiege.py
@time:2020年8月25日
'''


a = input('输入url：')

number = a.count('=')			#获取data个数
b = a.split('?')[1]				#URL分割成路径和数据
url = a.split('?')[0]
print(url)
c = b.split('&')
e = []
data = {}
for i in range(number):
    d = c[i].split('=')
    e.append(d)
for i in e:
    data[i[0]] = i[1]
print(data)

