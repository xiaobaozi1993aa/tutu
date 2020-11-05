#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_get_buyorder.py
@time:2020年9月15日
'''
import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Pageone.get_order_data import data, path
import unittest
res = RunMain()
from Common.Common_Unittest import Meiyin_Port

class Meiyin_port_Get_buyorder(Meiyin_Port):

    # 随机弹出购买信息弹出
    # @unittest.skip
    def test_1_get_buyorder(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),200   ,'接口请求成功')
            self.assertEqual(r.json().get('msg'),'成功','返回信息错误')
            self.assertNotEqual(r.json().get('data'),None,'随机购买弹窗没有放数据')
            self.logger.info('随机弹出购买信息接口获取成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('接口验证失败')
