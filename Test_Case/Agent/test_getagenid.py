#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_getagentid.py
@time:2020年9月9日
'''
import unittest

import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Agent.getagentid_data import data, path
from Common.Common_Unittest import Meiyin_Port
res = RunMain()

class Meiyin_port_Getagentid(Meiyin_Port):

    # 获取代理ID
    def test_1_getagentid(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data[0], method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'), 200, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '获取成功', '返回信息错误')
            self.assertNotEquals(r.json().get('data').get('userId'),None,'ID为空')
            self.logger.info('获取代理ID成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('获取代理ID失败')