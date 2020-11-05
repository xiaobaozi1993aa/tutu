#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_get_address.py
@time:2020年8月31日
'''

import unittest

import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Address.get_addid_data import data, path
res = RunMain()
from Common.Common_Unittest import Meiyin_Port

class Meiyin_port_Getaddid(Meiyin_Port):

    # 获取地址id
    def test_1_get_addid(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'), 200, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '获取成功', '返回信息错误')
            addid = r.json().get('data')[0].get('addressId')
            gg.set_value('addid', addid)
            self.logger.info('获取地址id成功:{}'.format(r.json().get('data')[0].get('addressId')))
        except Exception as e:
            self.logger.error(e)
            self.logger.error('获取地址id失败')

