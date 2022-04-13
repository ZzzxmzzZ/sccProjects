#!/usr/bin/python
# -*- coding:utf8 -*-
import xlrd
import os
from common.log import Logger
from config import conf

log = Logger(__name__)

class ReadExcel(object):

    def __init__(self,fileName='Data.xlsx',sheetName='user'):
        try:
            # report.logger.info("开始获取[%s]的[%s]表" % (fileName,sheetName))
            self.dataFile = os.path.join(conf.dataPath, fileName)
            self.workBook = xlrd.open_workbook(self.dataFile)
            self.sheetName = self.workBook.sheet_by_name(sheetName) #获取名字为sheetName的工作表
            self.sheet = sheetName
        except Exception:
            log.logger.exception('获取工作表[%s]失败' % sheetName, exc_info=True)
            raise

    def readExcel(self,rownum,colnum):
        try:
            value = self.sheetName.cell(rownum,colnum).value
        except Exception:
            log.logger.exception('读取工作表[%s]数据失败' % self.sheet, exc_info=True)
            raise
        else:
            return value

    #用字典数组形式输出数据
    def readData(self):
        # 获取该sheet中的有效行数
        nrows = self.sheetName.nrows
        # 返回由第一行中所有单元格的数据组成的列表：即表头
        colNames = self.sheetName.row_values(0)
        # print(nrows)
        # 3
        # print(colNames)
        # ['用例id', '用户名', '密码']
        list = []
        #从第二行到有效行
        for rowNum in range(1,nrows):
            #将第rowNum行的数据保存在row列表中
            row = self.sheetName.row_values(rowNum)
            if row:
                app = {} #定义字典
                for i in range(len(colNames)):
                    #isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
                    if isinstance(row[i],float):
                        row[i] = int(row[i])

                    app[colNames[i]] = row[i]
                list.append(app) #追加
        # print(list)
        # [{'用例id': 1, '用户名': 123, '密码': 1234}, {'用例id': 2, '用户名': 345, '密码': 1234}]
        log.logger.info("创建表[%s]的数据字典" % self.sheet)
        return list

    def getCaseID(self,data):
        list = []
        for i in range(len(data)):
            # print(i)
            id = data[i]["用例id"]
            # print(id)
            # print(caseID)
            list.append(id)
        return list

if __name__ == '__main__':
    cellValue = ReadExcel().readExcel(1,2)
    # print((cellValue))
    # 1234.0
    userData = ReadExcel('data.xlsx', 'user')
    user = userData.readData()
    # print(user)
    # [{'用例id': 1, '用户名': 123, '密码': 1234}, {'用例id': 2, '用户名': 345, '密码': 1234}]==list
    # print(user[0]["用例id"])
    # 1
    # print(str(user[1]["用户名"]))
    # 345
    # # print(user)
    # t = userData.getCaseID(user)
    # print(t)