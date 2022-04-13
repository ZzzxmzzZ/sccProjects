import time, unittest
from time import sleep

# from common.BeautifulReport.BeautifulReport import BeautifulReport
from ddt import ddt, data

# from common.HTMLTestRunner import HTMLTestRunner
#from common.myUnit import MyUnittest
# from config.conf import reportPath, casePath, baseUrl, hwUrl
from selenium.webdriver.support.wait import WebDriverWait

from common.log import Logger
from common.myUnit import AdminUnittest
from config.conf import baseUrl
from config.doExcel import ReadExcel
#from common.report import Logger
from pageObject.admin.adminNoticePage import AdminNoticePage
from selenium.webdriver.support import expected_conditions as EC

log = Logger(__name__)
testSendNoticeData = ReadExcel('elementDate.xlsx', 'sendNoticeData')  # 登录模块测试数据
noticeData = testSendNoticeData.readData()

createNoticeUrl = baseUrl + "notice/create"
homeUrl = baseUrl + "index"


@ddt
class TestAdminTeaNotice(AdminUnittest):

    def tearDown(self):
        """
        每个测试用例执行之后会执行
        :return:
        """
        self.adminNotice.clickTeaClose()

    @data(*noticeData)
    def test_01_admin_createNoticeToTeacher(self, noticeData):
        '''判断管理员是否进入了发布公告页面'''

        self.adminNotice = AdminNoticePage(self.driver)
        print("点击公告通知按钮")
        sleep(0.5)
        self.adminNotice.clickNoticeBtn()
        time.sleep(0.5)
        self.adminNotice.clickSendNoticeTipBtn()
        #获取创建活动页面文案
        message = self.adminNotice.sendNoticePageText()
        try:
            self.assertIn("公告通知", message)
        except Exception as F:
            print("登录测试用例：进入发布公告页面未通过！")
            raise F
        else:
            print("登录测试用例进入发布公告页面成功！")

        self.adminNotice.clickSendNoticeToTeaBtn()
        print("点击向教师发布公告成功")
        time.sleep(0.5)
        # To 教师文案
        toTeaText = self.adminNotice.sendNoticeToTeaPageText()
        try:
            self.assertEqual("To 教师", toTeaText)
        except Exception as F:
            print("登录测试用例：进入向教师发布公告小窗未通过！")
            raise F
        else:
            print("登录测试用例进入向教师发布公告小窗成功！")

        '''创建公告测试用例'''
        self.adminNotice.sendTeaNoticeInfo(noticeData["title"], noticeData["content"])
        self.adminNotice.clickTeaTreeBtn()
        self.pageDown()
        sleep(0.8)
        self.adminNotice.clickSureSendTeaNoticeBtn()
        sleep(0.8)
        message = self.adminNotice.alertInfo()
        print("message:",message)
        # self.adminNotice.alertInfo()
        if message:
            try:
                # self.assertIn(noticeData["expected"], message)
                self.assertIn("计算机科学与技术学院", message)
            except Exception as F:
                print('学院选择失败！')
                raise F
            else:
                print('学院选择成功！')
                # self.adminNotice.clickClose()
                wait = WebDriverWait(self.driver, 2)
                wait.until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                sendNoticeText = alert.text
                alert.accept()
                if message:
                    try:
                        # self.assertIn(noticeData["expected"], message)
                        self.assertIn("发布成功", sendNoticeText)
                    except Exception as F:
                        print('发布失败！')
                        raise F
                    else:
                        print('发布公告成功！')
                        self.adminNotice.clickTeaClose()






if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    # reportTitle = "登录功能测试报告" + now + ".html"
    # nowPath = os.path.join(reportPath, reportTitle)
    caseName = "创建课程模块测试用例"

    # discover = unittest.defaultTestLoader.discover(casePath, pattern="testLogin.py", top_level_dir=None)

    # suite = unittest.TestSuite()
    # suite.addTest(discover)
    # runner = BeautifulReport(suite)
    # runner.report(filename=reportTitle,description=caseName,report_dir=reportPath)
    #unittest.main()
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestAdminTeaNotice))

    # fp = open(report_path + '-test_login_result.html', 'wb')
    # # 测试报告的标题与描述
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='登录功能测试报告:',
    #                                        description='脚脚本从用例表读取要登录的用户数，然后执行相应次数的登录操作，'
    #                                                    '根据登陆后页面的用户名进行断言，把结果记录在用例表中')
    # runner.run(suite)