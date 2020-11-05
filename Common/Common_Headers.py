#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:Common_Headers.py
@time:2020年8月28日
'''
import time
import random
import requests
from Common.Common_Conf import host
from Common.Common_Log import MeiyinLog
logger = MeiyinLog().get_log()




def test_login(mobile):
    header = {"deviceId": "android"}
    path = '/api/common/login/loginByPhone'
    api = ''.join([host, path])
    data = {"phone": mobile, "pwd": "e10adc3949ba59abbe56e057f20f883e", "areaCode": 86, "loginType": 0}
    r = requests.post(url=api, data=data,headers = header)
    logger.info(r.json())
    logger.error('耗时%ss' %r.elapsed.total_seconds())
    return (r.json().get('data').get('token'))

def common_hd(mobile):
    header = {"deviceId": "android"}
    path = '/api/common/login/loginByPhone'
    api = ''.join([host, path])
    data = {"phone": mobile, "pwd": "e10adc3949ba59abbe56e057f20f883e", "areaCode": 86, "loginType": 0}
    r = requests.post(url=api, data=data, headers=header)
    token = r.json().get('data').get('token')
    headers = { "appId": "wxe36d354edaff0317",
               "deviceId": "android",
               "macId": "juLoEbCTWJwtB/qI1MRNW52fYaUb9Bb0K6WZFzy4FE7OlFRd5QCxT6uCXUVRyulMWUOrDgbVPsa2On0oRLtzN5k9GGAMVP+UKNyp26yZimPpvhcRA5BEQfbOI/9lVdByFEXBn5YRMt1nYdD9h4TgGNCW8zmjHY5bJggL8mf7uTo=",
               "h-nonce": "4a91903c-bbc6-4b9d-a976-8aabd0501c06",
               "h-system-code": "android",
               "versionName": "1.6.2.2"}
    headers['random'] = str(random.randint(1000000000, 9000000000))
    headers['timestamp'] = str(round(time.time() * 1000))
    headers['X-TOKEN'] = token
    logger.info(headers)
    return headers

def get_hd(token):
    headers = {"appId": "wxe36d354edaff0317",
               "deviceId": "android",
               "macId": "juLoEbCTWJwtB/qI1MRNW52fYaUb9Bb0K6WZFzy4FE7OlFRd5QCxT6uCXUVRyulMWUOrDgbVPsa2On0oRLtzN5k9GGAMVP+UKNyp26yZimPpvhcRA5BEQfbOI/9lVdByFEXBn5YRMt1nYdD9h4TgGNCW8zmjHY5bJggL8mf7uTo=",
               "h-nonce": "4a91903c-bbc6-4b9d-a976-8aabd0501c06",
               "h-system-code": "android",
               "versionName": "1.6.2.2"}
    headers['random'] = str(random.randint(1000000000, 9000000000))
    headers['timestamp'] = str(round(time.time() * 1000))
    headers['X-TOKEN'] = token
    logger.info(headers)
    return headers


header = {"deviceId": "android"}
headers = {"appId": "wxe36d354edaff0317",
           #"Content - Type":"text / plain;charset = UTF - 8",
           "deviceId": "android",
           "macId": "juLoEbCTWJwtB/qI1MRNW52fYaUb9Bb0K6WZFzy4FE7OlFRd5QCxT6uCXUVRyulMWUOrDgbVPsa2On0oRLtzN5k9GGAMVP+UKNyp26yZimPpvhcRA5BEQfbOI/9lVdByFEXBn5YRMt1nYdD9h4TgGNCW8zmjHY5bJggL8mf7uTo=",
           "h-nonce": "4a91903c-bbc6-4b9d-a976-8aabd0501c06",
           "h-system-code": "android",
           "versionName": "1.6.2.2",
           'random':str(random.randint(1000000000, 9000000000)),
           'timestamp':str(round(time.time() * 1000))
           }


if __name__ == '__main__':
    mobile = 13066909086
    test_login(mobile)