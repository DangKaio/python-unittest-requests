#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-12-21 18:41:59
# @Last Modified time: 2019-08-16 10:08:00
# @E-mail: 1370465454@qq.com
# @Description:
# import requests
# import unittest
# class TokenClass(unittest.TestCase):
#     def setUp
import requests
import re
import sys
sys.path.append('../')
import json
from interface.interface_method import run_main
from config.globalparam import domain_name_server, spark_url
from common.log import Log
logger = Log()

# response = requests.post(url, data=json.dumps(request_param), headers=headers)
# print(response.text)


class Spark(object):
    """docstring for Spark"""

    def __init__(self, domain=domain_name_server, spark_url=spark_url):
        super(Spark, self).__init__()
        self.header = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        self.domain = domain_name_server
        self.spark_url = spark_url
        self.s = requests.session()

    def get_token(phone):
        """获取灵宠的token"""
        url = domain_name_server + "/tequila/login"
        data = {
            "phone": str(phone),
            "password": "123456"
        }
        headers = {
            "Content-Type": "application/json",
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        }
        resp = requests.post(url=url, json=data, headers=headers)
        if resp.status_code != 200:
            logger.error("获取token失败!!! %s " % resp.text)
            return ""
        resp_json = json.loads(resp.content.decode('utf-8'))
        token = resp_json["token"]
        # print(token)
        return str(token)

    def get_auth_token(self, username, password):
        "用户登录获取auth-token"
        data = {
            "username": username,
            "phone": username,
            "password": password,
            "remember_me": 'false',
            "next": "/oauth2/question"
        }

        # 用户登录
        url_login = self.domain + "/user/signin"
        res = run_main(self.s, 'Post', url_login, headers=self.header,
                       data=data)
        # print(res)
        url_callback = self.domain + \
            data['next']
        res = run_main(self.s, 'get', url_callback,
                       headers=self.header, allow_redirects=False)
        # print(res)
        rs = re.findall(r'code=([a-zA-Z0-9]+)<', str(res.text), re.I | re.M)
        # print(rs)
        login_url = self.spark_url + "/login"
        params = {"code": rs}
        res = run_main(self.s, 'Post', login_url,
                       headers=self.header, params=params)
        # print(res['data']['token'])
        return res['data']['token']


    # print(response.json()['data']["token"])
if __name__ == '__main__':
    # r = get_token(16620424025)
    # print(r)
    Spark().get_auth_token("xhadmin", "2009xabc")
