import time, unittest
from time import sleep

# from common.BeautifulReport.BeautifulReport import BeautifulReport
from ddt import ddt

# from common.HTMLTestRunner import HTMLTestRunner
#from common.myUnit import MyUnittest
# from config.conf import reportPath, casePath, baseUrl, hwUrl
from selenium.webdriver.support.wait import WebDriverWait

from common.log import Logger
from common.myUnit import AdminUnittest
#from common.report import Logger
from pageObject.admin.adminSchoolTreePage import AdminSchoolTreePage
from selenium.webdriver.support import expected_conditions as EC

log = Logger(__name__)
# testSchoolTreeData = ReadExcel('elementDate.xlsx', 'schoolTreeData')  # 登录模块测试数据
# schoolTreeData = testSchoolTreeData.readData()
#
# createNoticeUrl = baseUrl + "notice/create"
# homeUrl = baseUrl + "index"


@ddt
class TestAdminSchoolTree(AdminUnittest):

    def test_01_admin_add_schoolTree(self):
        '''判断管理员是否进入了学院机构页面'''
        '''这里的login是myunittest.py中定义的login = LoginPage()中的login'''
        self.adminSchoolTree = AdminSchoolTreePage(self.driver)
        print("点击学院机构按钮")
        self.adminSchoolTree.clickSchoolTreeBtn()
        time.sleep(0.5)
        #获取学院机构页面文案
        message = self.adminSchoolTree.schoolTreePageText()
        try:
            self.assertIn("学校机构", message)
        except Exception as F:
            print("登录测试用例：进入学校机构页面未通过！")
            raise F
        else:
            print("登录测试用例进入学校机构页面成功！")

        self.adminSchoolTree.clickAddWanganBtn()
        print("点击增加按钮成功")
        time.sleep(0.5)
        message = self.adminSchoolTree.alertInfo()
        print("message:", message)
        # self.adminNotice.alertInfo()
        if message:
            try:
                # self.assertIn(noticeData["expected"], message)
                self.assertIn("添加此结构", message)
            except Exception as F:
                print('添加学院分支失败！')
                raise F
            else:
                print('添加学院分支成功！')
                # self.adminNotice.clickClose()
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                alert.send_keys("网络工程")
                # addbranchText = alert.text
                alert.accept()
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.alert_is_present())
                addbranch = self.driver.switch_to.alert
                addbranchText = addbranch.text
                addbranch.accept()

                if message:
                    try:
                        # self.assertIn(noticeData["expected"], message)
                        self.assertEqual("添加成功", addbranchText)
                    except Exception as F:
                        print('添加分支失败！')
                        raise F
                    else:
                        print('添加分支成功！')

    def test_02_admin_delete_schoolTree(self):
        '''判断管理员是否进入了学院机构页面'''
        '''这里的login是myunittest.py中定义的login = LoginPage()中的login'''
        self.adminSchoolTree = AdminSchoolTreePage(self.driver)
        print("点击学院机构按钮")
        self.adminSchoolTree.clickSchoolTreeBtn()
        time.sleep(0.5)
        #获取学院机构页面文案
        message = self.adminSchoolTree.schoolTreePageText()
        try:
            self.assertIn("学校机构", message)
        except Exception as F:
            print("登录测试用例：进入学校机构页面未通过！")
            raise F
        else:
            print("登录测试用例进入学校机构页面成功！")

        self.adminSchoolTree.clickDeleteTreeBtn()
        print("点击删除按钮成功")
        time.sleep(0.5)
        message = self.adminSchoolTree.alertInfo()
        print("message:", message)
        # self.adminNotice.alertInfo()
        if message:
            try:
                # self.assertIn(noticeData["expected"], message)
                self.assertIn("确认删除", message)
            except Exception as F:
                print('删除学院分支失败！')
                raise F
            else:
                print('删除学院分支成功！')
                # self.adminNotice.clickClose()
                wait = WebDriverWait(self.driver, 10)
                wait.until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                deleteBranchText = alert.text
                alert.accept()
                sleep(2)

                if message:
                    try:
                        # self.assertIn(noticeData["expected"], message)
                        self.assertEqual("删除成功", deleteBranchText)
                    except Exception as F:
                        print('删除分支失败！')
                        raise F
                    else:
                        print('删除分支成功！')

    def test_03_admin_rename_schoolTree(self):
        '''判断管理员是否进入了学院机构页面'''
        '''这里的login是myunittest.py中定义的login = LoginPage()中的login'''
        self.adminSchoolTree = AdminSchoolTreePage(self.driver)
        print("点击学院机构按钮")
        self.adminSchoolTree.clickSchoolTreeBtn()
        time.sleep(0.5)
        #获取学院机构页面文案
        message = self.adminSchoolTree.schoolTreePageText()
        try:
            self.assertIn("学校机构", message)
        except Exception as F:
            print("登录测试用例：进入学校机构页面未通过！")
            raise F
        else:
            print("登录测试用例进入学校机构页面成功！")

        sleep(0.8)
        self.adminSchoolTree.clickRenameBtn()
        print("点击重命名按钮成功")
        time.sleep(0.5)
        # self.adminSchoolTree.renameBtn()

        # sleep(5)
        message = self.adminSchoolTree.alertInfo()
        print("message:", message)
        # self.adminNotice.alertInfo()
        if message:
            try:
                # self.assertIn(noticeData["expected"], message)
                self.assertEqual("您确认修改类别名称?", message)
                # self.assertEqual("您确认修改类别名称?", message)
            except Exception as F:
                print('重命名失败！')
                raise F
            else:
                print('重命名成功！')
                # self.adminNotice.clickClose()



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
    suite.addTest(loader.loadTestsFromTestCase(TestAdminSchoolTree))

    # fp = open(report_path + '-test_login_result.html', 'wb')
    # # 测试报告的标题与描述
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='登录功能测试报告:',
    #                                        description='脚脚本从用例表读取要登录的用户数，然后执行相应次数的登录操作，'
    #                                                    '根据登陆后页面的用户名进行断言，把结果记录在用例表中')
    # runner.run(suite)