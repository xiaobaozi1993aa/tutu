#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:get_rtime.py
@time:2020年9月17日
'''
import time,re,os,xlrd
from Common.Common_Excel import get_nrows,get_xls
from Common.Common_Conf import end_path
from Common.Common_Log import MeiyinLog
from collections import Counter
from Common.Common_Conf import path
logger = MeiyinLog().get_log()

name =  time.strftime("%Y_%m_%d_")+'test'+'.log'
file = path+name
# 筛选列表
portlist = ['usercenter/sign', 'editUserInfo','getMessageGroup','productSearch',
            'getProductInfo','checkCodeIsOk','getMineWallet','addAlbum','delAlbumBatch','editAddressNew',
            ]

def add_rtime():
    xlsc, shtc = get_xls(0)
    number = get_nrows(0)
    try:
        with open(file, 'r', encoding='utf-8') as f:
            for lines in f.readlines():
                lines = lines.replace("\n", "").split(",")
                if 'loginByPhone' in str(lines):
                    a = str(lines)[3:22] + ',' + str(lines)[26:29]
                    shtc.write(number, 0, a)
                    shtc.write(number, 1, lines[2])
                    xlsc.save(r'%s' % end_path)
                for i in portlist:
                    if i in str(lines):
                        b = portlist.index(i) + 2
                        shtc.write(number, b, lines[2])
                        xlsc.save(r'%s' % end_path)
            logger.info('响应时间EXCEL保存完毕')
    except Exception as e:
        logger.error(e)

'''
全部接口总数
总报错接口数
接口运行次数
'''

def add_errnum():
    linelist = []
    errlist = []
    alllist = []
    try:
        subdir = os.listdir(path)
        for f in subdir:            # 遍历文件夹下的文件
            filename, extension = os.path.splitext(f)  # 将文件名拆分为文件名与后缀
            if (extension == '.log'):
                text = open(path+f, 'r', encoding='utf-8')
                for lines in text.readlines():
                    lines = lines.replace("\n", "").split(",")
                    if 'ERROR' in str(lines):
                        if 'test_' in str(lines):
                            errlist.append(re.findall(r"] (.+?).py", str(lines))[0])
                    if 'line:33' in str(lines):
                        linelist.append(lines)
                    if '接口运行完毕' in str(lines):
                        alllist.append(lines)
        num = Counter(errlist)
        logger.info('报错个数:{},总接口数:{},运行次数:{}'.format(len(errlist), len(linelist), len(alllist)))
        return len(errlist), len(linelist), len(alllist), dict(num)
    except Exception as e:
        logger.error(e)

def add_gtime():
    gtime_list = []         # 超时列表
    xls = xlrd.open_workbook(end_path)
    a = xls.sheets()[0]
    for i in range(1,11):
        glist = (a.col_values(i))[1::]
        new_glist = [i for i in glist if i != '']
        for ii in new_glist:
            if float(ii) >= 1.0:            # 超时接口时间定义
                gtime_list.append((a.col_values(i))[0])
    num = Counter(gtime_list)
    logger.info('超时数据统计完毕,共:{}个'.format(len(gtime_list)))
    return dict(num),len(gtime_list)

def get_real_time():
    today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return today

if __name__ == '__main__':
    add_rtime()
    add_errnum()
    add_gtime()