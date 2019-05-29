#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/6/10 17:25
# @Email   : 1370465454@qq.com
# @File    :
# @Description:接口的方法封装

import requests

class Run_Method:


    def post_main(self,url,headers,data=None):
        '''参数必须按照url、data顺序传入'''
        res=None
        res=requests.post(url=url, headers=headers, data=json.dumps(data))
        return res
    def get_main(self,url,headers,data=None):
        '''get接口主入口'''
        res=None
        res=requests.get(url=url, headers=headers,params=data)
        return res
    def put_main(self,url,headers,data=None):
        """put接口主入口"""
        res=None
        res = requests.put(url=url, headers=headers,data=json.dumps(data))
        result = r.json()
        return result

    #调用
    def run_main(self,method,url=None,headers=None,data=None):
        res=None
        if method=='Post':
            res=self.post_main(url, headers, data)

        elif method=='Put':
            res=self.put_main(url, headers, data)

        else:
            res=self.get_main(url, headers, data)
        return res



if __name__ == '__main__':
    data = {"username":"****","password":"**","verify":"", "referer":"http://m.imooc.com"}
    t = Run_Method()
