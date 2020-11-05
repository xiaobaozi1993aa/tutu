#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:Common_gol.py
@time:2020年9月2日
'''


import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Oreder.creatorder_data import data, path
from Common.Common_Unittest import Meiyin_Port

res = RunMain()
class Meiyin_port_Creatorder(Meiyin_Port):

    # 创建产品订单id
    def test_creat_orderid(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),200,'接口请求失败')
            self.assertEqual(r.json().get('msg'),'成功','返回信息错误')
            self.assertNotEquals(r.json().get('data').get('orderId'),None,'订单ID提取成功')
            orderid = r.json().get("data").get("orderId")
            gg.set_value('orderid', orderid)
            self.logger.info('创建产品订单ID成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('创建产品订单ID失败')