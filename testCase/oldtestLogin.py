import os, time, unittest
from time import sleep

# from common.BeautifulReport.BeautifulReport import BeautifulReport
from ddt import ddt, data

# from common.HTMLTestRunner import HTMLTestRunner
from common.myUnit import MyUnittest
# from config.conf import reportPath, casePath, baseUrl, hwUrl
from config.conf import baseUrl, casePath
from config.doExcel import ReadExcel
from common.log import Logger

log = Logger(__name__)
testLoginData = ReadExcel('elementDate.xlsx', 'loginData')  # 登录模块测试数据
userData = testLoginData.readData()

testUrl = baseUrl + "login"
homeUrl = baseUrl + "index"


@ddt
class TestLogin(MyUnittest):

    @data(*userData)
    def test_login(self, userData):

        """登录模块测试用例"""

        self.login.open(testUrl)
        print("打开了login页面")
        log.logger.info("   *** 登录测试用例：%s %s ***", userData["caseId"], userData["用例描述"])
        self.login.loginFunc(userData["userId"], userData["password"])
        sleep(1)

        if self.login.getUrl() == homeUrl:
            message = self.login.getWelcomeText()
            print("message:", message)
            try:
                result = self.assertIn(userData["expected"], message)
                print("结果：result=", result)
                # 第一步同样要定位到select框
                self.login.clickXialaBtn()
                time.sleep(2)
                # 第二步通过xpath定位到要点击的list集合
                # options = driver.find_elements_by_xpath("//ul[@class='list-test']/li")
                self.login.clickTuichuBtn()
                time.sleep(1)
                self.login.queding()
                # 第三步通过for循环找到要点击的具体选项
                # for li in options:
                #     if "autotest" in li.text:  # 这里用text属性寻找，也可选id或class
                #         i.click()
                #         break

            except Exception as F:
                log.logger.info('登录测试用例：%s 未通过！' % userData["caseId"])
                log.logger.exception("登录测试用例：%s 成功进入首页，但未成功登录")
                # failPic = "fail_" + userData["caseId"] + ".png"
                self.login.saveScreenShot(failPic)
                raise F
            else:
                log.logger.info(
                    '登录测试用例 %s 测试用例通过！' % userData["caseId"])
                # passPic = "pass_" + userData["caseId"] + ".png"
                # self.login.saveScreenShot(passPic)

        elif self.login.getUrl() == testUrl:
            # 判断登陆失败
            text = self.login.getFailedText()
            try:
                self.assertEqual(text, userData["expected"])
            except Exception as F:
                log.logger.info('登录测试用例：%s 未通过！' % userData["caseId"])
                log.logger.exception("登录测试用例：%s 登录失败，提示信息错误" % userData["caseId"])
                # failPic = "fail_" + userData["caseId"] + ".png"
                # self.login.saveScreenShot(failPic)
                raise F
            else:
                log.logger.info(
                    '登录测试用例：%s 通过！' % userData["caseId"])
                # passPic = "pass_" + userData["caseId"] + ".png"
                # self.login.saveScreenShot(passPic)
        else:
            log.logger.error("网页地址发生错误")
            log.logger.info('登录测试用例：%s 未通过！' % userData["caseId"])
            # failPic = "fail_" + userData["caseId"] + ".png"
            # self.login.saveScreenShot(failPic)


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    # reportTitle = "登录功能测试报告" + now + ".html"
    # nowPath = os.path.join(reportPath, reportTitle)
    caseName = "登录模块测试用例"

    discover = unittest.defaultTestLoader.discover(casePath, pattern="oldtestLogin.py", top_level_dir=None)
    suite = unittest.TestSuite()
    suite.addTest(discover)
    # runner = BeautifulReport(suite)
    # runner.report(filename=reportTitle,description=caseName,report_dir=reportPath)
