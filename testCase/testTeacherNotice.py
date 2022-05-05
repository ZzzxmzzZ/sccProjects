import time, unittest
from time import sleep

# from common.BeautifulReport.BeautifulReport import BeautifulReport
from ddt import ddt, data

# from common.HTMLTestRunner import HTMLTestRunner
#from common.myUnit import MyUnittest
# from config.conf import reportPath, casePath, baseUrl, hwUrl
from selenium.webdriver.support.wait import WebDriverWait

from common.BeautifulReport import BeautifulReport
from common.log import Logger
from common.myUnit import TeaUnittest
from config.conf import baseUrl, casePath, reportPath
from config.doExcel import ReadExcel
#from common.report import Logger
from selenium.webdriver.support import expected_conditions as EC

from pageObject.teacher.teaNoticePage import TeaNoticePage

log = Logger(__name__)
testSendNoticeData = ReadExcel('elementDate.xlsx', 'sendNoticeData')  # 登录模块测试数据
noticeData = testSendNoticeData.readData()

createNoticeUrl = baseUrl + "notice/create"
homeUrl = baseUrl + "index"


@ddt
class TestTeacherNotice(TeaUnittest):
    def tearDown(self):
        """
        每个测试用例执行之后会执行
        :return:
        """
        self.teacherNotice.clickStuClose()

    @data(*noticeData)
    def test_01_teacher_createNotice(self, noticeData):
        '''教师向学生发布公告'''
        '''判断教师是否进入了发布公告页面'''

        self.teacherNotice = TeaNoticePage(self.driver)
        print("点击公告通知按钮")
        sleep(0.5)
        self.teacherNotice.clickNoticeBtn()
        time.sleep(0.5)
        self.teacherNotice.clickSendNoticeTipBtn()
        #获取公告页面文案
        message = self.teacherNotice.sendNoticePageText()
        try:
            self.assertIn("公告通知", message)
        except Exception as F:
            print("教师向学生发布公告测试用例：进入发布公告页面未通过！")
            log.logger.error('发布公告：%s 未通过！未进入发布公告页面' % noticeData["caseId"])
            times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
            failScreenShot = "fail_" + times + "_" + noticeData["caseId"] + ".png"
            self.teacherNotice.screenShot(failScreenShot)
            self.teacherNotice.clickStuClose()
            raise F
        else:
            log.logger.info('发布公告：%s 成功进入发布公告页面！' % noticeData["caseId"])
            print("发布公告：测试用例发布公告成功！")

        self.teacherNotice.clickSendNoticeToStuBtn()
        print("点击向教师发布公告成功")
        time.sleep(0.5)
        # To 教师文案
        toTeaText = self.teacherNotice.sendNoticeToStuPageText()
        try:
            self.assertEqual("To 学生", toTeaText)
        except Exception as F:
            print("教师向学生发布公告测试用例：进入向学生发布公告小窗未通过！")
            log.logger.error('发布公告：%s 未通过！进入向学生发布公告小窗失败' % noticeData["caseId"])
            times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
            failScreenShot = "fail_" + times + "_" + noticeData["caseId"] + ".png"
            self.teacherNotice.screenShot(failScreenShot)
            self.teacherNotice.clickStuClose()
            raise F
        else:
            log.logger.info('教师向学生发布公告：%s 成功进入对应发布公告小窗！' % noticeData["caseId"])
            print("教师向学生发布公告测试用例进入向学生发布公告小窗成功！")

        '''创建公告测试用例'''
        self.teacherNotice.sendStuNoticeInfo(noticeData["title"], noticeData["content"])
        self.teacherNotice.clickStuTreeBtn()
        self.teacherNotice.pageDown()
        # sleep(0.3)
        self.teacherNotice.clickSureSendStuNoticeBtn()
        message = self.teacherNotice.alertInfo()
        print("message:",message)
        # self.adminNotice.alertInfo()
        if message:
            try:
                # self.assertIn(noticeData["expected"], message)
                self.assertIn("东莞理工学院", message)
            except Exception as F:
                print("教师向学生发布公告测试用例：学院选择失败！")
                log.logger.error('教师向学生发布公告测试用例：%s 未通过！学院选择失败！' % noticeData["caseId"])
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                failScreenShot = "fail_" + times + "_" + noticeData["caseId"] + ".png"
                self.teacherNotice.screenShot(failScreenShot)
                self.teacherNotice.clickStuClose()
                raise F
            else:
                print('学院选择成功！')
                # self.adminNotice.clickClose()
                wait = WebDriverWait(self.driver, 10)
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
                        log.logger.error('教师向学生发布公告测试用例：%s 未通过！发布失败！' % noticeData["caseId"])
                        times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                        failScreenShot = "fail_" + times + "_" + noticeData["caseId"] + ".png"
                        self.teacherNotice.screenShot(failScreenShot)
                        self.teacherNotice.clickStuClose()
                        raise F
                    else:
                        log.logger.info('管理员向学生发布公告：%s 发布成功！' % noticeData["caseId"])
                        print('发布公告成功！')
                        # self.teacherNotice.clickStuClose()


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    reportTitle = "教师用户发布公告测试报告" + now + ".html"
    # nowPath = os.path.join(reportPath, reportTitle)
    caseName = "教师发布公告模块测试用例"

    # discover = unittest.defaultTestLoader.discover(casePath, pattern="testTeacherNotice.py", top_level_dir=None)
    #
    # suite = unittest.TestSuite()
    # loader = unittest.TestLoader()
    # suite.addTest(loader.loadTestsFromTestCase(TestTeacherNotice))
    #
    # runner = BeautifulReport(suite)
    # runner.report(filename=reportTitle,description=caseName,report_dir=reportPath)



    # fp = open(report_path + '-test_login_result.html', 'wb')
    # # 测试报告的标题与描述
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='登录功能测试报告:',
    #                                        description='脚脚本从用例表读取要登录的用户数，然后执行相应次数的登录操作，'
    #                                                    '根据登陆后页面的用户名进行断言，把结果记录在用例表中')
    # runner.run(suite)


    # testcase = unittest.TestLoader().loadTestsFromTestCase(TestTeacherNotice)
    #
    # BeautifulReport.BeautifulReport(testcase).report(filename=reportTitle, description=caseName, report_dir=reportPath)