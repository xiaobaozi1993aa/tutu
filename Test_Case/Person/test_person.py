#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_person.py
@time:2020年9月7日
'''
from Common.Common_Unittest import Meiyin_Port
import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Person.person_name_data import data, path
import unittest
res = RunMain()
class Meiyin_port_Name(Meiyin_Port):

    # 修改名字
    # @unittest.skip
    def test_1_getmoney(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),200,'接口请求失败')
            self.assertEqual(r.json().get('msg'),'修改成功','返回信息错误')
            self.logger.info('改名成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('改名失败')
