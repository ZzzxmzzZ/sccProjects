# -*-coding:utf-8-*-
import time
import unittest

from common import BeautifulReport
from config.conf import casePath, reportPath
from testCase.testLogin import TestLogin
from testCase.testTeacherNotice import TestTeacherNotice


now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    # reportTitle = "教师用户发布公告测试报告" + now + ".html"
    # # nowPath = os.path.join(reportPath, reportTitle)
    # caseName = "教师发布公告模块测试用例"
reportTitle = "登录系统柜测试报告" + now + ".html"
    # nowPath = os.path.join(reportPath, reportTitle)
caseName = "登录系统测试用例"

testcase = unittest.TestLoader().loadTestsFromTestCase(TestLogin)

BeautifulReport.BeautifulReport(testcase).report(filename=reportTitle, description=caseName, report_dir=reportPath)
