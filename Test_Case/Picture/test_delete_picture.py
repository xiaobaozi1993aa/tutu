#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:test_delete_picture.py
@time:2020年9月7日
'''
import unittest
import Common.Common_gol as gg
from Common.Common_Conf import host
from Common.Common_Monthd import RunMain
from Test_Data.Picture.delete_picture_data import top_path,path,del_path
from Common.Common_Unittest import Meiyin_Port

res = RunMain()

class Meiyin_port_Delpicture(Meiyin_Port):

    @unittest.skip('暂时跳过')
    # 相册置顶
    def test_1_top_picture(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        data = gg.get_value('pictureid')
        r = res.run_main(url=''.join([host, top_path]), data=data, method='post', headers=self.headers)
        try:
            self.assertEqual(r.json().get('code'),200,'接口请求失败')
            self.assertEqual(r.json().get('msg'),'成功','返回信息不一致')
            self.logger.info('相册置顶成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('相册置顶失败')

    @unittest.skip('暂时跳过')
    def test_2_del_picture(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        a = gg.get_value('pictureid')
        data = {'albumId':[a.get('albumId')]}
        try:
            r = res.run_main(url=''.join([host, del_path]), data=data, method='post', headers=self.headers)
            self.assertEqual(r.json().get('code'), 200, '接口请求失败')
            self.assertEqual(r.json().get('msg'), '成功！', '返回信息不一致')
            self.logger.info('相册删除成功')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('相册删除失败')

    # 删除相册
    def test_3_del_picture(self):
        self.headers['X-TOKEN'] = gg.get_value("token")
        data = gg.get_value('pictureid')
        try:
            r = res.run_main(url=''.join([host, path]), data=data, method='post', headers=self.headers)
            self.assertEqual(r.json().get('code'),200,'接口请求失败')
            self.assertEqual(r.json().get('msg'),'删除成功!','返回信息不一致')
            self.logger.info('相册删除完成')
        except Exception as e:
            self.logger.error(e)
            self.logger.error('相册删除失败')

