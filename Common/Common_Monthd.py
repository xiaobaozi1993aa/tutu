#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:Common_Monthd.py
@time:2020年8月28日
'''
import requests
import json
from Common.Common_Log import MeiyinLog
from Common.Common_Conf import host,print_func

logger = MeiyinLog().get_log()


# 定义一个方法，传入需要的参数url和data
class RunMain:
    def send_post(self, url, data, headers):
        result = requests.request("POST", url, data = data, headers = headers)
        return result

    def send_get(self, url, data,headers):
        result = requests.get(url = url, data = data,headers = headers)
        res = json.dumps(result, ensure_ascii = False, sort_keys = True, indent=2)
        return res

    def run_main(self, method, url = None, data = None, headers = None):
        result = None
        if method == 'post':
            result = self.send_post(url, data, headers)
            logger.info('请求头:{}'.format(headers))
            logger.info('请求url:{},{}'.format(url,result.elapsed.total_seconds()))
            logger.info('请求数据:{}'.format(data))
            logger.info('接口响应:{}'.format(result.json()))
            logger.info('耗时%ss' % result.elapsed.total_seconds())
            logger.info(result.headers)

        elif method == 'get':
            result = self.send_get(url, data, headers)
            logger.info('请求头:{}'.format(headers))
            logger.info('请求url:{}'.format(url))
            logger.info('请求数据:{}'.format(data))
            logger.info('接口响应:{}'.format(result.json()))
            logger.info('耗时%ss' % result.elapsed.total_seconds())
        else:
            logger.error('%s 错误' % method)
        return result


