#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:get_rtime.py
@time:2020年9月17日
'''

import time,re
from Common.Common_Excel import get_nrows,get_xls
from Common.Common_Conf import expath
from Common.Common_Log import MeiyinLog
from collections import Counter

logger = MeiyinLog().get_log()

xlsc,shtc = get_xls()
number = get_nrows()
path = "H:\\美印\\tt_log\\"
name =  time.strftime("%Y_%m_%d_")+'test'+'.log'
file = path+name
# 筛选列表
portlist = ['usercenter/sign', 'editUserInfo','getMessageGroup','productSearch',
            'getProductInfo','checkCodeIsOk','getMineWallet','addAlbum','delAlbumBatch','editAddressNew',
            ]

def add_rtime():
    try:
        with open(expath, 'r', encoding='utf-8') as f:
            for lines in f.readlines():
                lines = lines.replace("\n", "").split(",")
                if 'loginByPhone' in str(lines):
                    a = str(lines)[3:22] + ',' + str(lines)[26:29]
                    shtc.write(number, 0, a)
                    shtc.write(number, 1, lines[2])
                    xlsc.save(r'%s' % expath)

                for i in portlist:
                    if i in str(lines):
                        b = portlist.index(i) + 2
                        shtc.write(number, b, lines[2])
                        xlsc.save(r'%s' % expath)
            logger.info('响应时间EXCEL保存完毕')
    except Exception as e:
        logger.error(e)

def add_errnum():
    linelist = []
    errlist = []
    alllist = []
    try:
        with open(file, 'r',encoding='utf-8') as f:
            for lines in f.readlines():
                lines = lines.replace("\n", "").split(",")
                if 'ERROR' in str(lines):
                    if 'test_' in str(lines):
                        errlist.append(re.findall(r"] (.+?).py", str(lines))[0])
                if 'line:33' in str(lines):
                    linelist.append(lines)
                if '接口运行完毕' in str(lines):
                    alllist.append(lines)
            num = Counter(errlist)
            logger.info('报错个数:{},总接口数:{},运行次数:{}'.format(len(errlist),len(linelist),len(alllist)))
            return len(errlist),len(linelist),len(alllist),dict(num)
    except Exception as e:
            logger.error(e)

if __name__ == '__main__':
    add_rtime()
    add_errnum()