import time, unittest
from time import sleep

# from common.BeautifulReport.BeautifulReport import BeautifulReport
from ddt import ddt, data

# from common.HTMLTestRunner import HTMLTestRunner
#from common.myUnit import MyUnittest
# from config.conf import reportPath, casePath, baseUrl, hwUrl
from selenium.webdriver.support.wait import WebDriverWait

from common.log import Logger
from common.myUnit import AdminUnittest, TeaUnittest, StuUnittest
from config.conf import baseUrl
from config.doExcel import ReadExcel
#from common.log import Logger
from pageObject.admin.adminNoticePage import AdminNoticePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pageObject.loginOutPage import LoginOutPage
from selenium.webdriver.common.keys import Keys

log = Logger(__name__)
testSendNoticeData = ReadExcel('elementDate.xlsx', 'sendNoticeData')  # 登录模块测试数据
noticeData = testSendNoticeData.readData()

createNoticeUrl = baseUrl + "notice/create"
homeUrl = baseUrl + "index"


@ddt
class TestAdminLoginOut(AdminUnittest):

    def test_01_admin_loginOut(self):
        '''管理员退出登录'''

        self.adminLoginOut = LoginOutPage(self.driver)
        self.adminLoginOut.clickAvatareBtn()
        # submit = self.driver.find_element_by_id('userDropdown')  # 首先创建对象
        # submit = self.driver.find_element_by_xpath('//*[@id="userDropdown"]/svg')  # 首先创建对象
        self.driver.find_element_by_xpath('//*[@id="userDropdown"]').send_keys(Keys.ENTER)

        # ActionChains(self.driver).click(submit).perform()  # 左键
        sleep(1)


        print("点头像小标按钮")
        # self.driver.find_element_by_xpath('//*[@id="userDropdown"]').click()
        # self.adminLoginOut.clickAvatareBtn()

        print("点击头像成功")
        # WebDriverWait(self.driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('//*[@id="content"]/div[1]/nav/ul/li[2]/div').is_displayed())

        # self.driver.implicitly_wait(10)
        self.adminLoginOut.clickLoginOuteBtn()
        sleep(0.5)

        message = self.adminLoginOut.getLoginOutText()
        print("message:",message)
        # self.adminNotice.alertInfo()
        if message:
            try:
                # self.assertIn(noticeData["expected"], message)
                self.assertIn("Ready to Leave?", message)
            except Exception as F:
                print('点击登出按钮失败！')
                raise F
            else:
                print('点击登出按钮成功！')

                self.adminLoginOut.clickSureLoginOutBtn()

                sleep(0.5)
                loginText = self.adminLoginOut.getLoginPageText()
                try:
                    # self.assertIn(noticeData["expected"], message)
                    self.assertEqual("请登录", loginText)
                except Exception as F:
                    print('登出失败！')
                    raise F
                else:
                        print('登出成功！')

class TestTeaLoginOut(TeaUnittest):
    def test_02_teacher_loginOut(self):
        '''教师退出登录'''

        self.teacherLoginOut = LoginOutPage(self.driver)
        self.teacherLoginOut.clickAvatareBtn()
        # submit = self.driver.find_element_by_id('userDropdown')  # 首先创建对象
        # submit = self.driver.find_element_by_xpath('//*[@id="userDropdown"]/svg')  # 首先创建对象
        # self.driver.find_element_by_xpath('//*[@id="userDropdown"]').send_keys(Keys.ENTER)

        # ActionChains(self.driver).click(submit).perform()  # 左键
        # sleep(1)


        print("点头像小标按钮")
        # self.driver.find_element_by_xpath('//*[@id="userDropdown"]').click()
        # self.adminLoginOut.clickAvatareBtn()

        print("点击头像成功")
        # WebDriverWait(self.driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('//*[@id="content"]/div[1]/nav/ul/li[2]/div').is_displayed())

        # self.driver.implicitly_wait(10)
        self.teacherLoginOut.clickLoginOuteBtn()
        sleep(0.5)

        message = self.teacherLoginOut.getLoginOutText()
        print("message:",message)
        # self.adminNotice.alertInfo()
        if message:
            try:
                # self.assertIn(noticeData["expected"], message)
                self.assertIn("Ready to Leave?", message)
            except Exception as F:
                print('点击登出按钮失败！')
                raise F
            else:
                print('点击登出按钮成功！')

                self.teacherLoginOut.clickSureLoginOutBtn()

                sleep(0.5)
                loginText = self.teacherLoginOut.getLoginPageText()
                try:
                    # self.assertIn(noticeData["expected"], message)
                    self.assertEqual("请登录", loginText)
                except Exception as F:
                    print('登出失败！')
                    raise F
                else:
                        print('登出成功！')

class TestStuLoginOut(StuUnittest):
    def test_03_student_loginOut(self):
        '''学生退出登录'''

        self.studentLoginOut = LoginOutPage(self.driver)
        sleep(0.5)
        self.studentLoginOut.clickAvatareBtn()
        # submit = self.driver.find_element_by_id('userDropdown')  # 首先创建对象
        # submit = self.driver.find_element_by_xpath('//*[@id="userDropdown"]/svg')  # 首先创建对象
        # self.driver.find_element_by_xpath('//*[@id="userDropdown"]').send_keys(Keys.ENTER)

        # ActionChains(self.driver).click(submit).perform()  # 左键
        # sleep(1)


        print("点头像小标按钮")
        # self.driver.find_element_by_xpath('//*[@id="userDropdown"]').click()
        # self.adminLoginOut.clickAvatareBtn()

        print("点击头像成功")
        # WebDriverWait(self.driver, 10).until(lambda the_driver: the_driver.find_element_by_xpath('//*[@id="content"]/div[1]/nav/ul/li[2]/div').is_displayed())

        # self.driver.implicitly_wait(10)
        self.studentLoginOut.clickLoginOuteBtn()
        sleep(0.5)

        message = self.studentLoginOut.getLoginOutText()
        print("message:",message)
        # self.adminNotice.alertInfo()
        if message:
            try:
                # self.assertIn(noticeData["expected"], message)
                self.assertIn("Ready to Leave?", message)
            except Exception as F:
                print('点击登出按钮失败！')
                raise F
            else:
                print('点击登出按钮成功！')

                self.studentLoginOut.clickSureLoginOutBtn()

                sleep(0.5)
                loginText = self.studentLoginOut.getLoginPageText()
                try:
                    # self.assertIn(noticeData["expected"], message)
                    self.assertEqual("请登录", loginText)
                except Exception as F:
                    print('登出失败！')
                    raise F
                else:
                        print('登出成功！')



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
    suite.addTest(loader.loadTestsFromTestCase(TestAdminLoginOut))

    # fp = open(report_path + '-test_login_result.html', 'wb')
    # # 测试报告的标题与描述
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='登录功能测试报告:',
    #                                        description='脚脚本从用例表读取要登录的用户数，然后执行相应次数的登录操作，'
    #                                                    '根据登陆后页面的用户名进行断言，把结果记录在用例表中')
    # runner.run(suite)