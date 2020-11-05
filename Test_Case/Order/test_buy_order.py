#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_buy_order.py
@time:2020年9月2日
'''
import json
import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Oreder.buy_order_data import data, path
res = RunMain()
from Common.Common_Unittest import Meiyin_Port

class Meiyin_port_Buyorder(Meiyin_Port):
    # 创建订单
    def test_1_buy_order(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        data[0]['addressId'] = gg.get_value('addid')
        data[0]['orders'] = [{'orderId':'{}'.format(gg.get_value('orderid')),'couponId':'','couponCount':0}]
        data[0]['orders'] = json.dumps(data[0]['orders'])
        r = res.run_main(url=''.join([host, path]), data=data[0], method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),200,'接口请求失败')
            self.assertEqual(r.json().get('msg'),'成功','返回信息错误')
            self.assertNotEqual(r.json().get('data').get('mergePayId'), None, '支付ID为空')
            payid = r.json().get("data").get("mergePayId")
            gg.set_value('payid',payid)
            self.logger.info("支付ID创建成功，订单支付ID为:{}".format( r.json().get("data").get("mergePayId")))
        except Exception as e:
            self.logger.info(e)
            self.logger.error('支付ID创建失败')

    # 重复提交订单
    def test_2_buy_order(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        data[0]['addressId'] = gg.get_value('addid')
        data[0]['orders'] = [{'orderId':'{}'.format(gg.get_value('orderid')),'couponId':'','couponCount':0}]
        data[0]['orders'] = json.dumps(data[0]['orders'])
        r = res.run_main(url=''.join([host, path]), data=data[0], method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),409,'接口请求失败')
            self.assertEqual(r.json().get('msg'),'不能重复提交订单','返回信息错误')
            self.logger.info('不能重复提交订单，支付ID创建失败')
        except Exception as e:
            self.logger.error(e)

    # 缺少订单信息
    def test_3_buy_order(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data[1], method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'), 409, '接口请求失败')
            self.assertEqual(r.json().get('msg'),'订单信息错误','返回信息错误')
            self.logger.info('订单信息错误，支付ID创建失败')
        except Exception as e:
            self.logger.error(e)

    # 缺少地址信息
    def test_4_buy_order(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        data[2]['orders'] = [{'orderId':'{}'.format(gg.get_value('orderid')),'couponId':'','couponCount':0}]
        data[2]['orders'] = json.dumps(data[0]['orders'])
        r = res.run_main(url=''.join([host, path]), data=data[2], method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),503,'接口请求失败')
            self.assertEqual(r.json().get('msg'),'请稍后再试','返回信息错误')
            self.logger.info('收货地址为空，支付ID创建失败')
        except Exception as e:
            self.logger.error(e)