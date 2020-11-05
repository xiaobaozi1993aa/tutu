#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_bindagent.py
@time:2020年9月9日
'''
import unittest

import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Agent.bind_agent_data import data, path
from Common.Common_Unittest import Meiyin_Port
from Common.Common_Headers import common_hd
res = RunMain()

class Meiyin_port_Bindagent(Meiyin_Port):

    # 绑定上级代理
    def test_1_bindagent(self):
        headers = common_hd(13613286027)
        r = res.run_main(url=''.join([host, path]), data=data[0], method='post', headers=headers)
        try:
            self.assertEqual(r.json().get('code'), 200, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '获取成功', '返回信息错误')
            self.logger.info('绑定上级成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('绑定上级失败')

    def test_2_bindagent(self):
        headers = common_hd(13613286027)
        r = res.run_main(url=''.join([host, path]), data=data[0], method='post', headers=headers)
        try:
            self.assertEqual(r.json().get('code'), 200, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '获取成功', '返回信息错误')
            self.assertEqual(r.json().get('data').get('msg'), '已有会员', '返回信息错误')
            self.logger.info('绑定上级重复请求失败')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('绑定上级失败')
#
    def test_3_bindagent(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data[1], method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'), 0, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '未找到上级会员信息', '返回信息错误')
            self.logger.info('缺少上级ID请求断言正确')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('绑定上级失败')