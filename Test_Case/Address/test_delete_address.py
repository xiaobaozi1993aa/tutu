#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_delete_address.py
@time:2020年8月31日
'''

import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Address.datele_address_data import data, path
res = RunMain()
from Common.Common_Unittest import Meiyin_Port

class Meiyin_port_Deladderss(Meiyin_Port):
    #删除地址
    def test_1_delete_address(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        data['addressId'] = gg.get_value('addid')
        r = res.run_main(url=''.join([host, path]), data=data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'), 200, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '删除成功', '返回信息错误')
            self.logger.info('地址删除成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('地址删除失败')
