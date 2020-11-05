#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_sign.py
@time:2020年9月7日
'''

import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Person.sign_data import data, path
from Common.Common_Unittest import Meiyin_Port

res = RunMain()

class Meiyin_port_S(Meiyin_Port):

    # 签到
    def test_1_creat_picture(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        r = res.run_main(url=''.join([host, path]), data=data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),200,'接口请求失败')
            if r.json().get('data').get("money") != None:
                self.logger.info(r.json().get('msg'))
            if r.json().get('data').get("money") == None:
                self.logger.info('今日已签到')
        except Exception as e:
            self.logger(e)
            self.logger.error(r.json().get('msg'))

