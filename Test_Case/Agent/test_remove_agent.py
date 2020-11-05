#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_remove_agent.py
@time:2020年9月9日
'''
import unittest

import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Agent.remove_agent_data import data, path
from Common.Common_Unittest import Meiyin_Port
res = RunMain()

class Meiyin_port_Removeagent(Meiyin_Port):

    # 解除绑定关系
    def test_1_removeagent(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'), 200, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '成功', '返回信息错误')
            self.logger.info('粉丝解除成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('粉丝解除失败')