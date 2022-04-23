# -*-coding:utf-8-*-
import time
import unittest

from common.BeautifulReport import BeautifulReport
from common.log import Logger
from config.conf import reportPath
from testCase.testAdminAction import TestAdminAction, TestAdminSearchAction
from testCase.testLogin import TestLogin
from testCase.testLoginOut import TestAdminLoginOut, TestTeaLoginOut, TestStuLoginOut

log = Logger(__name__)
##登录
# def testFirst():
#     now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
#     reportTitle = "登录系统功能测试报告" + now + ".html"
#     desc = "登录测试用例"
#
#     suite = unittest.TestSuite()
#     lorder1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
#     suite.addTest(lorder1)
#     runner = BeautifulReport(suite)
#     runner.report(filename=reportTitle, description=desc, report_dir=reportPath)
#
##退出登录
# def testSecond():
#     now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
#     reportTitle = "退出登录功能测试报告" + now + ".html"
#     desc = "退出测试用例"
#
#     suite = unittest.TestSuite()
#     lorder1 = unittest.TestLoader().loadTestsFromTestCase(TestAdminLoginOut)
#     lorder2 = unittest.TestLoader().loadTestsFromTestCase(TestTeaLoginOut)
#     lorder3 = unittest.TestLoader().loadTestsFromTestCase(TestStuLoginOut)
#     suite.addTest(lorder1)
#     suite.addTest(lorder2)
#     suite.addTest(lorder3)
#     runner = BeautifulReport(suite)
#     runner.report(filename=reportTitle, description=desc, report_dir=reportPath)
#管理员活动
def testThird():
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    reportTitle = "管理员活动管理功能测试报告" + now + ".html"
    desc = "创建活动测试用例+搜索活动测试用例"

    suite = unittest.TestSuite()
    lorder1 = unittest.TestLoader().loadTestsFromTestCase(TestAdminAction)
    lorder2 = unittest.TestLoader().loadTestsFromTestCase(TestAdminSearchAction)
    suite.addTest(lorder1)
    suite.addTest(lorder2)
    runner = BeautifulReport(suite)
    runner.report(filename=reportTitle, description=desc, report_dir=reportPath)



if __name__=="__main__":
    #执行各功能点用例
    # testFirst()
    # testSecond()
    testThird()