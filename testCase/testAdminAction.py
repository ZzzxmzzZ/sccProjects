import time, unittest
from time import sleep

# from common.BeautifulReport.BeautifulReport import BeautifulReport
from ddt import ddt, data

# from common.HTMLTestRunner import HTMLTestRunner

# from config.conf import reportPath, casePath, baseUrl, hwUrl

from common.log import Logger
from common.myUnit import AdminUnittest
from config.conf import baseUrl
from config.doExcel import ReadExcel
#from common.report import Logger
from pageObject.admin.adminActionPage import AdminActionPage
from pageObject.admin.adminActionSearchPage import AdminActionSearchPage

log = Logger(__name__)
testAdminActionData = ReadExcel('elementDate.xlsx', 'createActionData')  # 登录模块测试数据
actionData = testAdminActionData.readData()

createActionUrl = baseUrl + "activities/create"
searchCourseUrl = baseUrl + "activities/history"
homeUrl = baseUrl + "index"


@ddt
class TestAdminAction(AdminUnittest):

    @data(*actionData)
    def test_01_admin_createAction(self, actionData):
        '''创建活动测试用例'''
        '''判断管理员是否进入了活动创建页面'''

        self.adminAction = AdminActionPage(self.driver)
        print("点击选课系统按钮")
        self.adminAction.clickChooseCSBtn()
        sleep(0.3)
        #点击新增课程标签
        self.adminAction.clickAdminCreateActionTipBtn()
        # 获取创建活动页面文案
        if self.adminAction.getUrl() == createActionUrl:
            message = self.adminAction.createActionPageText()
            try:
                self.assertEqual(message, "创建活动")
            except Exception as F:
                print("登录测试用例：进入创建活动页面未通过！")
                raise F
            else:
                print("登录测试用例进入创建活动页面成功！")

        '''创建活动测试用例'''
        self.adminAction.createActionInfo(actionData["actionName"], actionData["classroom"], actionData["startTime"], actionData["endTime"], actionData["chooseTime"], actionData["number"], actionData["credit"], actionData["remarks"])

        self.adminAction.clickCreateActionBtn()
        sleep(0.8)
        message = self.adminAction.alertInfo()
        if message:
            try:
                self.assertIn(actionData["expected"], message)
            except Exception as F:
                print('登录测试用例：%s 未通过！' % actionData["caseId"])
                raise F
            else:
                print('登录测试用例：%s 成功！' % actionData["caseId"])

    def test_02_admin_searchAction(self):
        '''查询课程测试用例'''
        '''判断管理员是否进入了查询活动页面'''

        self.adminSearchAction = AdminActionSearchPage(self.driver)
        print("点击选课系统按钮")
        self.adminSearchAction.clickChooseCSBtn()
        sleep(0.3)
        #点击查询课程标签
        self.adminSearchAction.clickSearchCourseTipBtn_admin()
        # 获取创建课程页面文案
        if self.adminSearchAction.getUrl() == searchCourseUrl:
            message = self.adminSearchAction.historyActionPageText()
            try:
                self.assertEqual("活动·历史记录", message)
            except Exception as F:
                print("登录测试用例：进入查询活动页面未通过！")
                raise F
            else:
                print("登录测试用例进入查询活动页面成功！")
        sleep(1)
        self.adminSearchAction.getActionNameFromSql()
        # beforeSearch = self.adminSearchCourse.beforeSearchCourseList()
        # sleep(1)
        # print("查询前行数：",beforeSearch)
        #输入关键字
        self.adminSearchAction.searchActionNameKeyword()
        #点击查询
        self.adminSearchAction.clickSearchBtn()
        sleep(2)
        #查询后的列表
        self.adminSearchAction.getActionNameFromSql()
        try:
            self.adminSearchAction.isSearchCorrect() == True

        except Exception as F:
            print("登录测试用例：查询功能异常！")
            raise F
        else:
            print("查询活动成功！")




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
    suite.addTest(loader.loadTestsFromTestCase(TestAdminAction))

    # fp = open(report_path + '-test_login_result.html', 'wb')
    # # 测试报告的标题与描述
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='登录功能测试报告:',
    #                                        description='脚脚本从用例表读取要登录的用户数，然后执行相应次数的登录操作，'
    #                                                    '根据登陆后页面的用户名进行断言，把结果记录在用例表中')
    # runner.run(suite)