#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-08-06 17:25:43
# @Last Modified time: 2019-04-30 15:05:42
# @E-mail: 1370465454@qq.com
# @Description:读取excel的方法封装
import xlrd


class ExcelUtil(object):

    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于等于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum - 1)):
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i + 2
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == '__main__':
    ExcelUtil = ExcelUtil("../data/TestCase.xlsx", "TestCase")
    print(ExcelUtil.dict_data())
