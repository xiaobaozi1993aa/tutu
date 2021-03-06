#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_address.py
@time:2020年8月31日
'''

import unittest
import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Address.address_data import path,data
res = RunMain()
from Common.Common_Unittest import Meiyin_Port

class Meiyin_port_Address(Meiyin_Port):

    # 添加地址
    def test_7_add_address(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data[0], method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'), 200, '接口请求失败')
            self.assertEqual(r.json().get('data').get('status'), 'succ', '返回信息错误')
            self.logger.info('地址添加成功')
        except Exception as e:
            self.logger(e)
            self.logger.info('地址添加失败')


    @unittest.skip
    def test_2_add_address(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data[1], method='post', headers=self.headers)
        try:
            if r.json().get('code') != 200:
                self.logger.info(r.json().get('msg'))
        except:
            exit()

    @unittest.skip
    def test_3_add_address(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data[2], method='post', headers=self.headers)
        try:
            if r.json().get('code') != 200:
                self.logger.info(r.json().get('msg'))
        except:
            exit()


