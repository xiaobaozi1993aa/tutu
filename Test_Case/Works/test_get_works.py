#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_get_works.py
@time:2020年9月14日
'''

import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Works.works_data import data, path
from Common.Common_Unittest import Meiyin_Port

res = RunMain()

class Meiyin_port_Get_works(Meiyin_Port):
    # 获取作品列表
    def test_1_creat_picture(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        try:
            r = res.run_main(url=''.join([host, path]), data=data, method='post', headers=self.headers)
            self.assertEqual(r.json().get('code'), 200, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '成功', '作品获取失败')
            self.logger.info('作品列表获取成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('作品列表获取失败')
            exit()
