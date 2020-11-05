#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_login.py
@time:2020年8月29日
'''
import unittest
import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Headers import header
from Common.Common_Monthd import RunMain
from Test_Data.login_data import data, path
from Common.Common_Unittest import Meiyin_Port
gg._init()
res = RunMain()

class Meiyin_port_login(Meiyin_Port):

    @unittest.skip
    def test_1_login(self):
        r = res.run_main(url=''.join([host, path]), data=data[1], method='post', headers=header)
        try:
            self.assertEqual(r.json().get('code'), 402, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '账号未注册,请在底部使用微信登录', '返回信息不一致')
        except Exception as e:
            self.logger.error(e)
            exit()

    @unittest.skip
    def test_2_login(self):
        r = res.run_main(url=''.join([host, path]), data=data[2], method='post', headers=header)
        try:
            self.assertEqual(r.json().get('code'), 402, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '手机号或密码不正确', '返回信息不一致')
        except Exception as e:
            self.logger.error(e)
            exit()

    @unittest.skip
    def test_3_login(self):
        r = res.run_main(url=''.join([host, path]), data=data[3], method='post', headers=header)
        try:
            self.assertEqual(r.json().get('code'), 402, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '手机号或密码不正确', '返回信息不一致')
        except Exception as e:
            self.logger.error(e)
            exit()

    @unittest.skip
    def test_4_login(self):
        r = res.run_main(url=''.join([host, path]), data=data[4], method='post', headers=header)
        try:
            self.assertEqual(r.json().get('code'), 402, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '手机号或密码不正确', '返回信息不一致')
        except Exception as e:
            self.logger.error(e)
            exit()

    @unittest.skip
    def test_5_login(self):
        r = res.run_main(url=''.join([host, path]), data=data[5], method='post', headers=header)
        try:
            self.assertEqual(r.json().get('code'), 402, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '手机号错误', '返回信息不一致')
        except Exception as e:
            self.logger.error(e)
            exit()

    def test_6_login(self):
        r = res.run_main(url=''.join([host, path]), data=data[0], method='post', headers=header)
        try:
            self.assertEqual(r.json().get('code'), 200, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '获取成功', '返回信息不一致')
            self.assertNotEquals(r.json().get('data').get('token'), None, 'TOKEN提取失败')
            token = r.json().get('data').get('token')
            gg.set_value('token',token)
            self.logger.info('token为:%s' % token)
        except Exception as e:
            self.logger.error(e)
            exit()

