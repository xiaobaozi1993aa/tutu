#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_code.py
@time:2020年9月7日
'''
import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Person.code_data import data, path
import unittest
res = RunMain()
from Common.Common_Unittest import Meiyin_Port
class Meiyin_port_Code(Meiyin_Port):

    # 验证码
    # @unittest.skip
    def test_1_code(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),402,'接口请求成功')
            self.assertEqual(r.json().get('msg'),'验证码失效','返回信息错误')
            self.logger.info('接口验证成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('接口验证失败')
