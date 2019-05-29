# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Email : 1370465454@qq.com
# @Date:   2019-03-21 18:09:55
# @Last Modified time: 2019-04-26 14:48:59

import unittest
import sys
import os
from report.Runner.HTMLTestRunner3 import HTMLTestRunner
import time
sys.path.append('../')
from common import sendmail
curpath = os.path.dirname(os.path.realpath(__file__))
case_path = os.path.join(curpath, "case")


def create_suite():
    TestSuite = unittest.TestSuite()  # 测试集
    test_dir = os.getcwd() + '\\test_case\\'
    suite = unittest.defaultTestLoader.discover(
        start_dir=test_dir, pattern='test*.py', top_level_dir=None)
    for test_case in suite:
        TestSuite.addTests(test_case)
    return TestSuite


def report():
    if len(sys.argv) > 1:
        report_name = os.getcwd() + '\\report\\test_report\\' + \
            sys.argv[1] + '_result.html'
    else:
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        report_name = os.getcwd() + '\\report\\test_report\\' + now + 'result.html'
    return report_name


f = open(report(), 'wb')
runner = HTMLTestRunner(stream=f, title=u'测试报告',
                        description=u'测试用例执行情况',
                        verbosity=2,
                        )

if __name__ == '__main__':
    TestSuite = create_suite()
    runner.run(TestSuite)
    # 发送邮件
    # mail = sendmail.Send_Mail()
    # mail.send()
    f.close()
