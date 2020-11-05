#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:run.py
@time:2020年9月7日
'''
from Common.Common_Unittest import Meiyin_Port
import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Oreder.cancel_oreder_data import data, path,del_path

res = RunMain()
class Meiyin_port_Delorder(Meiyin_Port):

    # 未支付订单取消
    def test_1_cancel_order(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        data['orderId'] = gg.get_value('orderid')
        r = res.run_main(url=''.join([host, path]), data=data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),200,'接口请求失败')
            self.assertEqual(r.json().get('msg'),'成功','返回信息错误')
            self.logger.info('订单取消成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('订单取消失败')

    # 未支付订单删除
    def test_2_del_order(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        data['orderId'] = gg.get_value('orderid')
        r = res.run_main(url=''.join([host, del_path]), data=data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),200,'接口请求失败')
            self.assertEqual(r.json().get('msg'),'成功','返回信息错误')
            self.logger.info('订单删除成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('订单删除失败')