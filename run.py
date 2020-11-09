#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:run.py
@time:2020年9月1日
'''

import unittest
# from Meiyin_Report import HTMLTestRunner
# from HTMLTestRunner import HTMLTestRunner
import time
from gevent import pywsgi
from Common.Common_Log import MeiyinLog

logger = MeiyinLog().get_log()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.test_login'))                        #登录
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Person.test_sign'))                  #签到
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Person.test_person'))                #更改姓名
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Person.test_getmessage'))            #获取信息列表
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Person.test_search'))                #搜索/查看商品
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Person.test_code'))                  #验证码验证
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Money.test_getmoney'))               #查询余额/兔币等
    suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Picture.test_creat_picture'))        #创建相册
    suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Picture.test_delete_picture'))       #删除相册
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Address.test_addres'))               #添加地址
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Address.test_get_addid'))            #获取地址ID
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Order.test_creatorder'))             #创建订单ID
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Order.test_buy_order'))              #创建支付ID
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Order.test_cancel_order'))           #取消未支付订单
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Address.test_delete_address'))       #删除地址
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Agent.test_bindagent'))              #绑定上级
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Agent.test_getagenid'))              #获取上级代理ID
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Agent.test_remove_agent'))           #解除绑定关系
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Works.test_get_works'))              #获取作品列表
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Pageone.test_get_buyorder'))         #获取随机购买弹窗信息
    # suite.addTest(unittest.TestLoader().loadTestsFromName('Test_Case.Pageone.test_get_shop'))             #获取店铺信息
    #





    # reportname = time.strftime("%Y-%m-%d")+'-'+time.strftime("%H %M %S ")+'report.html'
    # test_report_path = reportpath+reportname
    # with open(test_report_path, "wb") as report_file:
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=report_file, title="兔兔接口测试报告", description="")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    logger.info('接口运行完毕')
    from Tool.get_rtime import add_rtime
    add_rtime()
    from rtime_demo import app
    logger.info('flask服务启动中。。。')
    server = pywsgi.WSGIServer(('0.0.0.0', 5001), app)
    server.serve_forever()
