#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_creat_picture.py
@time:2020年9月7日
'''

import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Picture.creat_picture_data import data, path
from Common.Common_Unittest import Meiyin_Port

res = RunMain()

class Meiyin_port_Creatpicture(Meiyin_Port):
    # 创建相册
    def test_1_creat_picture(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        try:
            r = res.run_main(url=''.join([host, path]), data=data, method='post', headers=self.headers)
            self.assertEqual(r.json().get('code'), 200, '接口请求失败')
            self.assertNotEqual(r.json().get('data').get('albumId'), None, '相册ID为空')
            pictureid = r.json().get('data')
            gg.set_value('pictureid',pictureid)
            self.logger.info('相册ID提取成功')
            self.logger.info('相册创建成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('相册创建失败')
            exit()


