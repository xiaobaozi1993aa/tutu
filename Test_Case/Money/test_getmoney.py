#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_getmoney.py
@time:2020年9月7日
'''
from Common.Common_Unittest import Meiyin_Port
import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Money.gettubi_data import data, path
import unittest
res = RunMain()
class Meiyin_port_Getmoney(Meiyin_Port):

    # 余额/兔币查询
    # @unittest.skip
    def test_1_getmoney(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),200,'接口请求失败')
            self.assertEqual(r.json().get('msg'),'获取成功','返回信息错误')
            self.logger.info('余额兔币查询成功')
            self.logger.info('余额:{}'.format(r.json().get('data').get('balance')))
            self.logger.info('兔币:{}个'.format(r.json().get('data').get('tuTuBiBalance')))
            self.logger.info('红包:{}个'.format(r.json().get('data').get('redPacketCount')))
            self.logger.info('卡券:{}个'.format(r.json().get('data').get('couponCount')))
        except Exception as e:
            self.logger.error(e)
            self.logger.error('余额兔币查询失败')
