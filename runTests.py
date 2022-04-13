# -*-coding:utf-8-*-
import time
import unittest

from common.BeautifulReport import BeautifulReport
from common.log import Logger
from config.conf import reportPath
from testCase.testLogin import TestLogin

log = Logger(__name__)
def testFirst():
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    reportTitle = "登录系统功能测试报告" + now + ".html"
    desc = "登录测试用例"

    suite = unittest.TestSuite()
    lorder1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    suite.addTest(lorder1)
    runner = BeautifulReport(suite)
    runner.report(filename=reportTitle, description=desc, report_dir=reportPath)

if __name__=="__main__":
    #执行各功能点用例
    testFirst()