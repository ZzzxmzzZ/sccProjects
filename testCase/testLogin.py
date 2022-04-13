import os, time, unittest
from time import sleep

# from common.BeautifulReport.BeautifulReport import BeautifulReport
from ddt import ddt, data
import xlrd

# from common.HTMLTestRunner import HTMLTestRunner
#from common.myUnit import MyUnittest
# from config.conf import reportPath, casePath, baseUrl, hwUrl
from selenium import webdriver

from common.BeautifulReport import BeautifulReport
from common.log import Logger
from config.conf import baseUrl, casePath, reportPath
from config.doExcel import ReadExcel
#from common.report import Logger
from pageObject.loginPage import LoginPage

log = Logger(__name__)
testLoginData = ReadExcel('elementDate.xlsx', 'loginData')  # 登录模块测试数据
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

        # self.login.open(login_path)

        self.sp = LoginPage(self.driver, login_path)
        self.sp.open()
        self.sp.loginFunc(userData["userId"], userData["password"])
        # 获取系统定位元素的关键字
        # message = self.sp.assert_by_text()
        #
        # print("message:", message)
        # self.name = str(self.name)
        # self.assertEqual(text, self.name)

        # print("打开了login页面")
        # report.logger.info("   *** 登录测试用例：%s %s ***", userData["caseId"], userData["用例描述"])
        # self.login.loginFunc(userData["userId"], userData["password"])
        # sleep(1)

        if self.sp.getUrl() == homeUrl:
            # message = self.login.getWelcomeText()
            message = self.sp.assert_by_text()
            print("message:", message)
            try:
                self.assertIn(userData["expected"], message)
            except Exception as F:
                print('登录测试用例：%s 未通过！' % userData["caseId"])
                raise F
            else:
                print('登录测试用例：%s 成功！' % userData["caseId"])

            # try:
            #     result = self.assertIn(userData["expected"], message)
            #     print("结果：result=", result)
            #     # # 第一步同样要定位到select框
            #     # self.login.clickXialaBtn()
            #     # time.sleep(2)
            #     # 第二步通过xpath定位到要点击的list集合
            #     # options = driver.find_elements_by_xpath("//ul[@class='list-test']/li")
            #     # self.login.clickTuichuBtn()
            #     # time.sleep(1)
            #     # self.login.queding()
            #     # 第三步通过for循环找到要点击的具体选项
            #     # for li in options:
            #     #     if "autotest" in li.text:  # 这里用text属性寻找，也可选id或class
            #     #         i.click()
            #     #         break
            #
            # except Exception as F:
            #     report.logger.info('登录测试用例：%s 未通过！' % userData["caseId"])
            #     report.logger.exception("登录测试用例：%s 成功进入首页，但未成功登录")
            #     # failPic = "fail_" + userData["caseId"] + ".png"
            #     self.login.saveScreenShot(failPic)
            #     raise F
            # else:
            #     report.logger.info(
            #         '登录测试用例 %s 测试用例通过！' % userData["caseId"])
            #     # passPic = "pass_" + userData["caseId"] + ".png"
            #     # self.login.saveScreenShot(passPic)

        elif self.sp.getUrl() == login_path:
            # 判断登陆失败
            message = self.sp.getFailedText()
            print("登录失败提示信息：", message)
            try:
                # self.assertEqual(text, userData["expected"])
                self.assertIn(userData["expected"], message)
            except Exception as F:
                print("登录测试用例：%s 登录失败，提示信息错误" % userData["caseId"])
                # report.logger.info('登录测试用例：%s 未通过！' % userData["caseId"])
                # report.logger.exception("登录测试用例：%s 登录失败，提示信息错误" % userData["caseId"])
                # failPic = "fail_" + userData["caseId"] + ".png"
                # self.login.saveScreenShot(failPic)
                raise F
            else:
                print('登录测试用例：%s 通过！' % userData["caseId"])
                # report.logger.info('登录测试用例：%s 通过！' % userData["caseId"])
                # passPic = "pass_" + userData["caseId"] + ".png"
                # self.login.saveScreenShot(passPic)
        else:
            print('登录测试用例：%s 未通过！' % userData["caseId"])
            # report.logger.error("网页地址发生错误")
            # report.logger.info('登录测试用例：%s 未通过！' % userData["caseId"])
            # failPic = "fail_" + userData["caseId"] + ".png"
            # self.login.saveScreenShot(failPic)


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
