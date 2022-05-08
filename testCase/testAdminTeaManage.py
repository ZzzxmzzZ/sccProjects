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
from pageObject.admin.adminTeaManagePage import AdminTeaManagePage
from selenium.webdriver.support import expected_conditions as EC

log = Logger(__name__)
testTeaManageData = ReadExcel('elementDate.xlsx', 'uploadFileData')  # 登录模块测试数据
fileData = testTeaManageData.readData()

createNoticeUrl = baseUrl + "notice/create"
homeUrl = baseUrl + "index"


@ddt
class TestAdminTeaManage(AdminUnittest):

    @data(*fileData)
    def test_01_admin_teaManage(self, fileData):
        ''' 管理员教师管理模块'''
        '''判断管理员是否进入了教师管理模块页面'''
        '''判断管理员能够上传文件成功.'''

        self.adminTeaManage = AdminTeaManagePage(self.driver)
        print("点击教师管理模块按钮")
        self.adminTeaManage.clickTeaManageBtn()
        time.sleep(0.5)
        #获取教师管理系统页面文案
        message = self.adminTeaManage.teaManagePageText()
        try:
            self.assertEqual("教师管理系统", message)
        except Exception as F:
            print("管理员教师管理模块：进入教师管理页面未通过！")
            log.logger.error('管理员教师管理模块：%s 未通过！未进入教师管理页面' % fileData["caseId"])
            times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
            failScreenShot = "fail_" + times + "_" + fileData["caseId"] + ".png"
            self.adminTeaManage.screenShot(failScreenShot)
            raise F
        else:
            log.logger.info('管理员教师管理模块：%s 成功进入教师管理页面！' % fileData["caseId"])
            print("管理员教师管理模块：成功进入教师管理页面！")

        self.adminTeaManage.clickOpenTreeBtn()
        print("展开树成功")
        time.sleep(0.5)
        self.adminTeaManage.clickComputerBtn()
        self.adminTeaManage.clickUploadFileBtn(fileData["filePath"])
        sleep(1)
        self.adminTeaManage.clickTransportBtn()
        message = self.adminTeaManage.alertInfo()
        print("message:",message)
        # self.adminNotice.alertInfo()
        if message:
            try:
                # self.assertIn(noticeData["expected"], message)
                self.assertIn("Excel文件", message)
            except Exception as F:
                print('点击录入按钮失败！')
                log.logger.error('管理员教师管理模块：%s 点击录入失败！' % fileData["caseId"])
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                failScreenShot = "fail_" + times + "_" + fileData["caseId"] + ".png"
                self.adminTeaManage.screenShot(failScreenShot)
                raise F
            else:
                print('点击录入按钮成功！')
                log.logger.info('管理员教师管理模块：%s 点击录入按钮成功！' % fileData["caseId"])
                # self.adminNotice.clickClose()
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                addTeaText = alert.text
                print(addTeaText)
                alert.accept()
                if message:
                    try:
                        # self.assertIn(noticeData["expected"], message)
                        self.assertIn(fileData["expected"], addTeaText)
                    except Exception as F:
                        print('失败！')
                        log.logger.error('管理员教师管理模块：%s 录入教师用户失败！' % fileData["caseId"])
                        times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                        failScreenShot = "fail_" + times + "_" + fileData["caseId"] + ".png"
                        self.adminTeaManage.screenShot(failScreenShot)
                        raise F
                    else:
                        print('成功！')
                        log.logger.info('管理员教师管理模块：%s 录入教师用户通过！' % fileData["caseId"])
                        times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                        successScreenShot = "pass_" + times + "_" + fileData["caseId"] + ".png"
                        self.adminTeaManage.screenShot(successScreenShot)

class TestAdminTeaManageNoFile(AdminUnittest):
    def test_02_admin_teaManage(self):
        '''判断管理员未选择文件的时候点击录入'''

        self.adminTeaManage = AdminTeaManagePage(self.driver)
        print("点击教师管理模块按钮")
        self.adminTeaManage.clickTeaManageBtn()
        time.sleep(0.5)
        #获取教师管理系统页面文案
        message = self.adminTeaManage.teaManagePageText()
        try:
            self.assertEqual("教师管理系统", message)
        except Exception as F:
            print("管理员教师管理模块：进入教师管理页面未通过！")
            log.logger.error('管理员教师管理模块: 未通过！未进入教师管理页面')
            times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
            failScreenShot = "fail_" + times + "_" + "TestAdminTeaManageNoFile1" + ".png"
            self.adminTeaManage.screenShot(failScreenShot)
            raise F
        else:
            log.logger.info('管理员教师管理模块：成功进入教师管理页面！')
            print("管理员教师管理模块：成功进入教师管理页面！")

        self.adminTeaManage.clickOpenTreeBtn()
        print("展开树成功")
        time.sleep(0.5)
        self.adminTeaManage.clickComputerBtn()
        self.adminTeaManage.clickTransportBtn()
        message = self.adminTeaManage.alertInfo()
        print("message:",message)
        # self.adminNotice.alertInfo()
        if message:
            try:
                # self.assertIn(noticeData["expected"], message)
                self.assertIn("Excel文件", message)
            except Exception as F:
                print('点击录入按钮失败！')
                log.logger.error('管理员教师管理模块：%s 点击录入失败！' % fileData["caseId"])
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                failScreenShot = "fail_" + times + "_" + "TestAdminTeaManageNoFile3" + ".png"
                self.adminTeaManage.screenShot(failScreenShot)
                raise F
            else:
                print('点击录入按钮成功！')
                # self.adminNotice.clickClose()
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                addTeaText = alert.text
                print(addTeaText)
                alert.accept()
                if message:
                    try:
                        # self.assertIn(noticeData["expected"], message)
                        self.assertEqual("请选择文件", addTeaText)
                    except Exception as F:
                        print('用例失败！')
                        log.logger.error('管理员教师管理模块：录入教师用户失败！')
                        times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                        failScreenShot = "fail_" + times + "_" + "TestAdminTeaManageNoFile2" + ".png"
                        self.adminTeaManage.screenShot(failScreenShot)
                        raise F
                    else:
                        print('用例成功！')
                        log.logger.error('管理员教师管理模块：录入教师用户成功！')
                        times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                        successScreenShot = "pass_" + times + "_" + "TestAdminTeaManageNoFile" + ".png"
                        self.adminTeaManage.screenShot(successScreenShot)





if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    # reportTitle = "登录功能测试报告" + now + ".html"
    # nowPath = os.path.join(reportPath, reportTitle)
    caseName = "教师管理模块测试用例"

    # discover = unittest.defaultTestLoader.discover(casePath, pattern="testLogin.py", top_level_dir=None)

    # suite = unittest.TestSuite()
    # suite.addTest(discover)
    # runner = BeautifulReport(suite)
    # runner.report(filename=reportTitle,description=caseName,report_dir=reportPath)
    #unittest.main()
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestAdminTeaManage))

    # fp = open(report_path + '-test_login_result.html', 'wb')
    # # 测试报告的标题与描述
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='登录功能测试报告:',
    #                                        description='脚脚本从用例表读取要登录的用户数，然后执行相应次数的登录操作，'
    #                                                    '根据登陆后页面的用户名进行断言，把结果记录在用例表中')
    # runner.run(suite)