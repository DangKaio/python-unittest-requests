#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-08-07 16:33:11
# @Last Modified time: 2018-08-07 16:39:39
# @E-mail: 1370465454@qq.com
# @Description:
import sys
import unittest
sys.path.append('../')
from interface.interface_senddata import send_requests

# dic={'API Purpose': 'POST无参数', 'rowNum': 3, 'statuscode': '200', 'response': "{'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Content-Length': '0', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.19.1'}, 'json': None, 'origin': '119.145.82.230', 'url': 'https://httpbin.org/post'}", 'times': '1.950892', 'error': '', 'msg': '', 'result': 'uncheckpoint'}
# data={'rowNum': 3, 'No.': 2.0, 'API Purpose': 'POST无参数', 'Request URL': 'https://httpbin.org/post', 'Request Method': 'POST', 'Request Data Type': '', 'Request Data': '', 'Encryption': '', 'Check Point': 200.0, 'isCheckStatusCode': '', 'status_code': '', 'times': '', 'error': '', 'result': '', 'response': '', 'exception': ''}
class Interface_Senddata_Test(unittest.TestCase):
    """转换操作包测试类"""

    def setUp(self):
        """初始化测试环境"""
        print('------init------')

    def tearDown(self):
        """清理测试环境"""
        print('------clear------')

    def test_Interface_Senddata(self,dic,data):
        send_requests(dic, data)
if __name__ == '__main__':
    unittest.main()
