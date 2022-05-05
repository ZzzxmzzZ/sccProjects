# -*-coding:utf-8-*-
import time
import unittest

from common.BeautifulReport import BeautifulReport
from common.log import Logger
from config.conf import reportPath
from testCase.testAdminAction import TestAdminAction, TestAdminSearchAction
from testCase.testAdminCourse import TestAdminCreateCourse, TestAdminAuditCourse, TestAdminSearchCourse
from testCase.testAdminSchoolTree import TestAdminAddSchoolTree, TestAdminDeleteSchoolTree, TestAdminRenameSchoolTree
from testCase.testAdminStuNotice import TestAdminStuNotice
from testCase.testAdminTeaNotice import TestAdminTeaNotice
from testCase.testLogin import TestLogin
from testCase.testLoginOut import TestAdminLoginOut, TestTeaLoginOut, TestStuLoginOut
from testCase.testStudentAction import TestStudentAction
from testCase.testStudentCourse import TestStudentCourse
from testCase.testTeacherAction import TestTeaCreateAction, TestTeaSearchAction
from testCase.testTeacherCourse import TestTeacherCreateCourse, TestTeacherSeachCourse
from testCase.testTeacherNotice import TestTeacherNotice

log = Logger(__name__)
#登录
def testFirst():
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    reportTitle = "登录系统功能测试报告" + now + ".html"
    desc = "登录测试用例"

    suite = unittest.TestSuite()
    lorder1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    suite.addTest(lorder1)
    runner = BeautifulReport(suite)
    runner.report(filename=reportTitle, description=desc, report_dir=reportPath)

#退出登录
def testSecond():
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    reportTitle = "退出登录功能测试报告" + now + ".html"
    desc = "退出测试用例"

    suite = unittest.TestSuite()
    lorder1 = unittest.TestLoader().loadTestsFromTestCase(TestAdminLoginOut)
    lorder2 = unittest.TestLoader().loadTestsFromTestCase(TestTeaLoginOut)
    lorder3 = unittest.TestLoader().loadTestsFromTestCase(TestStuLoginOut)
    suite.addTest(lorder1)
    suite.addTest(lorder2)
    suite.addTest(lorder3)
    runner = BeautifulReport(suite)
    runner.report(filename=reportTitle, description=desc, report_dir=reportPath)
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
#管理员课程
def testFourth():
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    reportTitle = "管理员课程管理功能测试报告" + now + ".html"
    desc = "创建课程测试用例+搜索课程测试用例+审核课程测试用例"

    suite = unittest.TestSuite()
    lorder1 = unittest.TestLoader().loadTestsFromTestCase(TestAdminCreateCourse)
    lorder2 = unittest.TestLoader().loadTestsFromTestCase(TestAdminSearchCourse)
    lorder3 = unittest.TestLoader().loadTestsFromTestCase(TestAdminAuditCourse)
    suite.addTest(lorder1)
    suite.addTest(lorder2)
    suite.addTest(lorder3)
    runner = BeautifulReport(suite)
    runner.report(filename=reportTitle, description=desc, report_dir=reportPath)

#教师活动
def testFifth():
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    reportTitle = "教师活动管理功能测试报告" + now + ".html"
    desc = "创建活动测试用例+搜索活动测试用例"

    suite = unittest.TestSuite()
    lorder1 = unittest.TestLoader().loadTestsFromTestCase(TestTeaCreateAction)
    lorder2 = unittest.TestLoader().loadTestsFromTestCase(TestTeaSearchAction)
    suite.addTest(lorder1)
    suite.addTest(lorder2)
    runner = BeautifulReport(suite)
    runner.report(filename=reportTitle, description=desc, report_dir=reportPath)

#教师课程
def testsixth():
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    reportTitle = "教师课程管理功能测试报告" + now + ".html"
    desc = "创建课程测试用例+搜索课程测试用例"

    suite = unittest.TestSuite()
    lorder1 = unittest.TestLoader().loadTestsFromTestCase(TestTeacherCreateCourse)
    lorder2 = unittest.TestLoader().loadTestsFromTestCase(TestTeacherSeachCourse)
    suite.addTest(lorder1)
    suite.addTest(lorder2)
    runner = BeautifulReport(suite)
    runner.report(filename=reportTitle, description=desc, report_dir=reportPath)
#学生活动
def testseventh():
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    reportTitle = "学生活动管理功能测试报告" + now + ".html"
    desc = "搜索活动测试用例"

    suite = unittest.TestSuite()
    lorder1 = unittest.TestLoader().loadTestsFromTestCase(TestStudentAction)
    suite.addTest(lorder1)
    runner = BeautifulReport(suite)
    runner.report(filename=reportTitle, description=desc, report_dir=reportPath)
#学生课程
def testeigth():
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    reportTitle = "学生课程管理功能测试报告" + now + ".html"
    desc = "搜索课程测试用例"

    suite = unittest.TestSuite()
    lorder1 = unittest.TestLoader().loadTestsFromTestCase(TestStudentCourse)
    suite.addTest(lorder1)
    runner = BeautifulReport(suite)
    runner.report(filename=reportTitle, description=desc, report_dir=reportPath)
#管理员学院机构管理
def testninth():
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    reportTitle = "管理员学院机构管理功能测试报告" + now + ".html"
    desc = "增加学院机构测试用例+删除学院机构测试用例+重命名学院机构测试用例"

    suite = unittest.TestSuite()
    lorder1 = unittest.TestLoader().loadTestsFromTestCase(TestAdminAddSchoolTree)
    lorder2 = unittest.TestLoader().loadTestsFromTestCase(TestAdminDeleteSchoolTree)
    lorder3 = unittest.TestLoader().loadTestsFromTestCase(TestAdminRenameSchoolTree)
    suite.addTest(lorder1)
    suite.addTest(lorder2)
    suite.addTest(lorder3)
    runner = BeautifulReport(suite)
    runner.report(filename=reportTitle, description=desc, report_dir=reportPath)
#管理员向学生发布公告
def testtenth():
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    reportTitle = "管理员向学生发布公告管理功能测试报告" + now + ".html"
    desc = "发布公告测试用例"

    suite = unittest.TestSuite()
    lorder1 = unittest.TestLoader().loadTestsFromTestCase(TestAdminStuNotice)
    suite.addTest(lorder1)
    runner = BeautifulReport(suite)
    runner.report(filename=reportTitle, description=desc, report_dir=reportPath)
#管理员向教师发布公告
def testeleventh():
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    reportTitle = "管理员向教师发布公告管理功能测试报告" + now + ".html"
    desc = "发布公告测试用例"

    suite = unittest.TestSuite()
    lorder1 = unittest.TestLoader().loadTestsFromTestCase(TestAdminTeaNotice)
    suite.addTest(lorder1)
    runner = BeautifulReport(suite)
    runner.report(filename=reportTitle, description=desc, report_dir=reportPath)
#教师向学生发布公告
def test12th():
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    reportTitle = "教师向学生发布公告管理功能测试报告" + now + ".html"
    desc = "发布公告测试用例"

    suite = unittest.TestSuite()
    lorder1 = unittest.TestLoader().loadTestsFromTestCase(TestTeacherNotice)
    suite.addTest(lorder1)
    runner = BeautifulReport(suite)
    runner.report(filename=reportTitle, description=desc, report_dir=reportPath)

if __name__=="__main__":
    #执行各功能点用例
    # testFirst()
    # testSecond()
    # testThird()
    # testFourth()
    # testFifth()
    # testsixth()
    # testseventh()
    # testeigth()
    # testninth()
    # testtenth()
    # testeleventh()
    test12th()
    # testseventh()