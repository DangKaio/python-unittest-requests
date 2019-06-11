#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/6/13 18:25
# @Email   : 1370465454@qq.com
# @File    :
# @Description:发送数据组合
import json
import sys
sys.path.append('../')
from config.globalparam import domain_name_server
from case_excel.read_excel import ExcelUtil
from case_excel.copy_excel import Write_excel
from common.get_token import get_token
from config.globalparam import result_path,data_path_name,phone
from interface.interface_method import run_main
from common.log import Log
logger=Log()


def send_requests(s, testdata):
    '''对请求的数据进行封装'''
    test_nub = testdata['API Purpose']
    logger.info("*******正在执行用例：-----  %s  -----**********" % test_nub)

    method = testdata["Request Method"]
    url = domain_name_server+testdata["Request URL"]
    logger.info("请求方式：%s, 请求url:%s" % (method, url))
    # 请求头部headers
    try:
        headers = eval(testdata["Headers"])
        headers['x-token'] = get_token(phone)
    except:
        headers={}
        headers['x-token'] = get_token(phone)
    # logger.info("请求头部：%s" % headers)
    # url后面的params参数
    try:
        params = eval(testdata["Params"])
        logger.info("请求params：%s" % params)
    except:
        params = None
    # body的类型
    type = testdata["Request Data Type"]
    # post请求Request Data内容
    try:
        if testdata["Request Body Data"]!='':
            bodydata = eval(testdata["Request Body Data"])
            # 判断传data数据还是json
            if type == "Data":
                body = bodydata
            elif type == "Json":
                body = json.dumps(bodydata)
        else:
            body=None
    except:
        body=None

    if method == "POST":
        logger.info("post请求body类型为：%s ,body内容为：%s" % (type, body))
    elif method =="PUT":
        logger.info("put请求body类型为：%s ,body内容为：%s" % (type, body))
    verify = True
    res = {}   # 接受返回数据
    try:
        r = s.request(method=method,
                      url=url,
                      headers=headers,
                      params=params,
                      data=body,
                      verify=verify
                      )  # headers=headers,params=params,,verify=verify
        logger.info("页面返回信息：%s" % r.text)  # .json()
        # print(type(r.content.decode('utf-8')))
        res['No.'] = testdata['No.']
        res['API Purpose'] = testdata['API Purpose']
        res["status_code"] = str(r.status_code)  # 状态码转成str
        res["text"] = r.content.decode("utf-8")
        res["response"] = str(r.json())
        res["times"] = str(r.elapsed.total_seconds())   # 接口请求时间转str
        if res["status_code"] != '200':
            res["error"] = res["text"]
        else:
            res["error"] = ""
        res["msg"] = ""
        try:
            # if testdata["Check Point"] in res["text"]:
            if testdata["Check Point"].replace("\n","").replace(" ","") == res["text"].replace("\n",""):
                res["result"] = "pass"
                logger.info("用例测试结果:   %s---->%s" % (test_nub, res["result"]))
            else:
                res["result"] = "fail"
        except:
            res["result"] = "uncheckpoint"
        # print(type(r.content.decode('utf-8')))
        return res
    except Exception as msg:
        res["msg"] = str(msg)
        return res


def wirte_result(result, filename=result_path):
    # 返回结果的行数row_nub
    # print(result)
    row_nub = result['No.']+1
    col_nub = 12 #开始的列
    # 写入statuscode
    wt = Write_excel(filename)
    wt.write(row_nub, col_nub, result['status_code'])       # 写入返回状态码statuscode,第13列
    wt.write(row_nub, col_nub+1, result['times'])            # 耗时
    wt.write(row_nub, col_nub+2, result['error'])            # 状态码非200时的返回信息
    wt.write(row_nub, col_nub+3, result['result'])           # 测试结果 pass 还是fail
    wt.write(row_nub, col_nub+4, result['response'])           # 返回结果
if __name__ == "__main__":
    data = ExcelUtil(data_path_name, "TestCase")
    # print(data.dict_data())
    # s = requests.session()
