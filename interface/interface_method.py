#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/6/10 17:25
# @Email   : 1370465454@qq.com
# @File    :
# @Description:接口的方法封装

import requests
import json

import requests
import json


def post_main(re, url, headers, params=None, data=None):
    '''参数必须按照url、data顺序传入'''
    res = None
    res = re.post(url=url, headers=headers,
                  params=params, data=json.dumps(data))
    result = res.json()
    return result


def get_main(re, url, headers, params=None, data=None, allow_redirects=None):
    '''get接口入口'''
    try:
        res = None
        res = re.get(url=url, headers=headers,
                     params=params, data=json.dumps(data), allow_redirects=allow_redirects)
        result = res.json()
    except:
        return res
    return result


def put_main(re, url, headers, params=None, data=None):
    """put接口主入口"""
    res = None
    res = re.put(url=url, headers=headers,
                 params=params, data=json.dumps(data))
    result = res.json()
    return result

# 调用

def run_main(re, method, url=None, headers=None, params=None, data=None, allow_redirects=None):
    res = None
    if method == 'Post' or method == 'post':
        res = post_main(re, url, headers, params, data)

    elif method == 'Put'or method == 'put':
        res = put_main(re, url, headers, params, data)

    else:
        res = get_main(re, url, headers, params, data, allow_redirects=None)
    return res


if __name__ == '__main__':
    data = {"username": "****", "password": "**",
            "verify": "", "referer": "http://m.imooc.com"}
