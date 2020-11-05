#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_get_shop.py
@time:2020年9月15日
'''
import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Pageone.get_shop_data import data, path
import unittest
res = RunMain()
from Common.Common_Unittest import Meiyin_Port

class Meiyin_port_Get_shop(Meiyin_Port):

    # 获取店铺信息
    # @unittest.skip
    def test_1_get_shop(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),200   ,'接口请求成功')
            self.assertEqual(r.json().get('msg'),'成功','返回信息错误')
            self.assertEqual(r.json().get('data').get('levelName'),'钻石店铺','返回信息错误')
            self.logger.info('获取店铺信息成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('接口验证失败')
