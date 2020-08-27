#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/6/10 17:25
# @Email   : 1370465454@qq.com
# @File    :
# @Description:将测试用例初始化分离出来
import requests
import unittest
import sys
sys.path.append('../')
from config import globalparam
from common.log import Log
import ddt
from interface.interface_method import run_main
from config.globalparam import data_path_name, read_excel_sheetname, now
from case_excel.read_excel import ExcelUtil
from case_excel.copy_excel import copy_excel
from common.get_token import Spark
testdata = ExcelUtil(data_path_name, read_excel_sheetname).dict_data()


@ddt.ddt
class My_Test(unittest.TestCase):
    """docstring for My_Test"""
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        copy_excel(globalparam.data_path_name,
                   globalparam.result_path)
        cls.logger = Log()
        cls.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        cls.headers["auth-token"] = Spark.get_auth_token("xhadmin", "2009xabc")
        cls.logger.info(
            '############################### START ###############################')
    # @ddt.data(*testdata)
    # def test_api(self,data):
    #     print(data['Request URL'])
    #     print(data['Request Method'])
    #     print(data['Request Data'])
    #     # 先复制excel数据到report
    #     res = send_requests(self.s, data)
    #     wirte_result(res, filename=globalparam.result_path)

    # # 检查点 checkpoint
    # check = data["checkpoint"]
    # print("检查点->：%s"%check)
    # # 返回结果
    # res_text = res["text"]
    # print("返回实际结果->：%s"%res_text)
    # # 断言
    # self.assertTrue(check in res_text)
    @classmethod
    def tearDownClass(cls):
        cls.logger.info(
            '############################### END ###############################')


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(My_Test)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main(verbosity=2)
