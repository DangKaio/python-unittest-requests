#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-08-06 17:25:43
# @Last Modified time: 2019-08-16 09:15:26
# @E-mail: 1370465454@qq.com
# @Description:定义一些默认参数、路径等
import os
import time

now = time.strftime('%Y-%m-%d_%H_%M_%S')
# 项目参数设置
prj_path = os.path.dirname(os.path.dirname(__file__))
# 日志路径
log_path = os.path.join(prj_path, 'report', 'Log')

# 测试报告路径
report_path = os.path.join(prj_path, 'report', 'test_report')

# 测试excel结果路径
result_path = os.path.join(
    prj_path, 'report', 'test_result\\' + now + 'report.xlsx')
# 默认浏览器
browser = 'Chrome'
# 登录域名
# domain_name_server = 'https://test-api.xiao100.com'

domain_name_server = "https://logintest.xiaojiaoyu100.com"
# 服务器域名
spark_url = "http://test.tiku.xiaojiaoyu100.com/que_api"
# 测试数据路径
data_path = os.path.join(prj_path, 'data', 'test_data')
# 读取Excel数据
data_path_name = os.path.join(prj_path, 'data', "TestCase.xlsx")
# 读取表名
read_excel_sheetname = "TestCase"
# 登录用户
phone = 16620424025
# mysql数据库的连接信息
db_config = {
    'host': '119.23.229.140',
    'port': 5433,
    'user': 'waitress',
    'password': 'test646169ff75049b9bff53085717f5f0b7',
    'database': 'waitress'
}
