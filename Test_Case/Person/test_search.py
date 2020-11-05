#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_person.py
@time:2020年9月8日
'''
from Common.Common_Unittest import Meiyin_Port
import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Person.search_data import *
import unittest
res = RunMain()

class Meiyin_port_Search(Meiyin_Port):

    # 搜索产品
    # @unittest.skip
    def test_1_search(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, search_path]), data=search_data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),200,'接口请求失败')
            self.assertEqual(r.json().get('msg'),'成功','返回信息错误')
            self.logger.info('搜索成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('搜索失败')

    # 查看商品详情
    def test_2_goodsdetail(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, info_path]), data=info_data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'), 200, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '获取成功', '返回信息错误')
            self.logger.info('查看商品详情成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('查看商品详情失败')