import os, time, unittest
from time import sleep

# from common.BeautifulReport.BeautifulReport import BeautifulReport
from ddt import ddt, data
import xlrd

from selenium import webdriver

from common.BeautifulReport import BeautifulReport
from common.log import Logger
from config.conf import baseUrl, casePath, reportPath
from config.doExcel import ReadExcel
#from common.report import Logger
from pageObject.loginPage import LoginPage

log = Logger(__name__)
# 读取登录模块测试数据
testLoginData = ReadExcel('elementDate.xlsx', 'loginData')
userData = testLoginData.readData()
login_path = baseUrl + "login"
homeUrl = baseUrl + "index"


@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # 隐性等待时间为30秒

    def tearDown(self):
        sleep(4)
        self.sp.quit()
    @data(*userData)
    def test_login(self, userData):
        """登录模块测试用例"""
        self.sp = LoginPage(self.driver, login_path)
        self.sp.open()
        self.sp.loginFunc(userData["userId"], userData["password"])
        if self.sp.getUrl() == homeUrl:
            message = self.sp.assert_by_text()
            print("message:", message)
            try:
                self.assertIn(userData["expected"], message)
            except Exception as F:
                print('登录：%s 未通过！' % userData["caseId"])
                log.logger.error('登录：%s 未通过！，首页信息不符合预期' % userData["caseId"])
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                failScreenShot = "fail_" + times + "_" + userData["caseId"] + ".png"
                self.sp.screenShot(failScreenShot)
                raise F
            else:
                log.logger.info('登录：%s 通过！' % userData["caseId"])
                print('登录：%s 成功！' % userData["caseId"])
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                successScreenShot = "pass_" + times + "_" + userData["caseId"] + ".png"
                self.sp.screenShot(successScreenShot)

        elif self.sp.getUrl() == login_path:
            # 判断登陆失败
            message = self.sp.getFailedText()
            try:
                self.assertIn(userData["expected"], message)
            except Exception as F:
                print("登录：%s 登录失败，提示信息不合预期" % userData["caseId"])
                log.logger.info('登录：%s 未通过！' % userData["caseId"])
                log.logger.exception("登录：%s 登录失败，提示信息不合预期" % userData["caseId"])
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                failScreenShot = "fail_" + times + "_" + userData["caseId"] + ".png"
                self.sp.screenShot(failScreenShot)
                raise F
            else:
                print('登录：%s 通过！' % userData["caseId"])
                log.logger.info('登录：%s 通过！' % userData["caseId"])
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                successScreenShot = "pass_" + times + "_" + userData["caseId"] + ".png"
                self.sp.screenShot(successScreenShot)
        else:
            print('登录：%s 未通过！' % userData["caseId"])
            log.logger.error("登录跳转错误，请检查Url")
            log.logger.info('登录测试用例：%s 未通过！' % userData["caseId"])
            times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
            failScreenShot = "fail_" + times + "_" + userData["caseId"] + ".png"
            self.sp.screenShot(failScreenShot)


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))

    reportTitle = "登录系统功能测试报告" + now + ".html"
    desc = "登录模块测试用例"
    # nowPath = os.path.join(reportPath, reportTitle)
    # caseName = "登录模块测试用例"

    # discover = unittest.defaultTestLoader.discover(casePath, pattern="testLogin.py", top_level_dir=None)

    # suite = unittest.TestSuite()
    # suite.addTest(discover)
    # runner = BeautifulReport(suite)
    # runner.report(filename=reportTitle,description=caseName,report_dir=reportPath)
    #unittest.main()
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestLogin))
    runner = BeautifulReport(suite)
    runner.report(filename=reportTitle, description=desc, report_dir=reportPath)

    # fp = open(report_path + '-test_login_result.html', 'wb')
    # # 测试报告的标题与描述
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='登录功能测试报告:',
    #                                        description='脚脚本从用例表读取要登录的用户数，然后执行相应次数的登录操作，'
    #                                                    '根据登陆后页面的用户名进行断言，把结果记录在用例表中')
    # runner.run(suite)
