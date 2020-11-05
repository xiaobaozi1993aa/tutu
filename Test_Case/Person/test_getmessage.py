#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_get_message.py
@time:2020年9月8日
'''
import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Person.get_message_data import *
from Common.Common_Unittest import Meiyin_Port
import unittest
res = RunMain()
class Meiyin_port_Getmessage(Meiyin_Port):

    # 获取总消息列表
    # @unittest.skip
    def test_1_getmessage(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),200,'接口请求成功')
            self.assertEqual(r.json().get('msg'),'获取成功','返回信息错误')
            self.logger.info('获取消息列表验证成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('获取消息列表验证失败')

    # 获取卡券助手信息
    def test_2_getmessage(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, card_path]), data=card_data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),200,'接口请求成功')
            self.assertEqual(r.json().get('msg'),'获取成功','返回信息错误')
            self.logger.info('获取卡券消息列表验证成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('获取卡券消息列表验证失败')

    # 获取系统通知信息
    def test_3_getmessage(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, sys_path]), data=sys_data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'), 200, '接口请求成功')
            self.assertEqual(r.json().get('msg'), '获取成功', '返回信息错误')
            self.logger.info('获取系统通知列表验证成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('获取系统通知列表验证失败')

    # 获取签到提醒信息
    def test_4_getmessage(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, sign_path]), data=sign_data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'), 200, '接口请求成功')
            self.assertEqual(r.json().get('msg'), '获取成功', '返回信息错误')
            self.logger.info('获取签到提醒列表验证成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('获取签到提醒列表验证失败')

    # 获取账户通知信息
    def test_5_getmessage(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, money_path]), data=money_data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'), 200, '接口请求成功')
            self.assertEqual(r.json().get('msg'), '获取成功', '返回信息错误')
            self.logger.info('获取账户通知列表验证成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('获取账户通知列表验证失败')