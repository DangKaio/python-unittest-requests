#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-12-21 18:41:59
# @Last Modified time: 2019-01-23 20:14:59
# @E-mail: 1370465454@qq.com
# @Description:
# import requests
# import unittest
# class TokenClass(unittest.TestCase):
#     def setUp
import requests
import json
url = "https://****"
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
request_param = {
    "password": "***",
    "userName": "***"
}
response = requests.post(url, data=json.dumps(request_param), headers=headers)
print(response.text)
# print(response.json()['data']["token"])



# def login():
#     url = "https://zhytest.999.com.cn/zhyAdmin/v1/system/user/login"
#     headers = {
#         'Content-Type': 'application/json;charset=UTF-8',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
#     }
#     request_param = {
#         "password": "Abc123",
#         "userName": "admin"
#     }
#     response = requests.post(url, data=json.dumps(request_param), headers=headers)
#     # print(response.text)

#     return response.json()["object"]['token'],response.text
