#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/6/10 17:25
# @Email   : 1370465454@qq.com
# @File    :
# @Description:

import sys
import time
import os
sys.path.append('../')
from config import globalparam
from PIL import ImageGrab


def get_img(dr, filename):
    '''对于网页进行截图,截图放到report下的img目录下'''
    path = get_path()
    path_filename = path + "\\" + \
        time.strftime('%Y-%m-%d_%H_%M_%S') + filename + '.png'
    dr.save_screenshot(path_filename)


def get_path():
    """保存截图"""
    path = globalparam.img_path + "\\" + \
        time.strftime("%Y-%m-%d", time.localtime(time.time()))
    path = new_file(path)
    return path


def new_file(path):
    """路径不存在时自动创建"""
    if os.path.exists(path):
        return path
    else:
        # 创建文件夹
        os.makedirs(path)
        return path


def window_screenshoot(filename):
    '''对于有弹窗的用window截图'''
    path = get_path()
    path_filename = path + "\\" + \
        time.strftime('%Y-%m-%d_%H_%M_%S') + filename + '.jpg'
    ImageGrab.grab().save(path_filename)


if __name__ == '__main__':
    get_img(dr, filename)
