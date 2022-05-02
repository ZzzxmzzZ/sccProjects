import os, time, unittest
from time import sleep

# from common.BeautifulReport.BeautifulReport import BeautifulReport
from ddt import ddt, data
import xlrd

from common.log import Logger
from common.myUnit import TeaUnittest
from config.conf import baseUrl, casePath
from config.doExcel import ReadExcel
#from common.report import Logger


from pageObject.teacher.teaActionPage import TeaActionPage
from pageObject.teacher.teaActionSearchPage import TeaActionSearchPage

log = Logger(__name__)
testAdminActionData = ReadExcel('elementDate.xlsx', 'createActionData')  # 登录模块测试数据
actionData = testAdminActionData.readData()

createActionUrl = baseUrl + "activities/create"
searchCourseUrl = baseUrl + "activities/history"
homeUrl = baseUrl + "index"


@ddt
class TestTeaCreateAction(TeaUnittest):

    @data(*actionData)
    def test_01_teacher_createAction(self, actionData):
        '''创建活动测试用例'''
        '''判断教师是否进入了活动创建页面'''

        self.teacherAction = TeaActionPage(self.driver)
        print("点击选课系统按钮")
        self.teacherAction.clickChooseCSBtn()
        sleep(0.3)
        #点击新增课程标签
        self.teacherAction.clickAdminCreateActionTipBtn()
        # 获取创建活动页面文案
        if self.teacherAction.getUrl() == createActionUrl:
            message = self.teacherAction.createActionPageText()
            try:
                self.assertEqual(message, "创建活动")
            except Exception as F:
                print("创建活动测试用例：进入创建活动页面失败！")
                log.logger.error('创建活动：%s 未通过！未进入创建活动页面' % actionData["caseId"])
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                failScreenShot = "fail_" + times + "_" + actionData["caseId"] + ".png"
                self.teacherAction.screenShot(failScreenShot)
                raise F
            else:
                log.logger.info('创建活动：%s 成功进入创建活动页面！' % actionData["caseId"])
                print("创建活动：测试用例进入创建活动页面成功！")

        '''创建活动测试用例'''
        self.teacherAction.createActionInfo(actionData["actionName"], actionData["classroom"], actionData["startTime"], actionData["endTime"], actionData["chooseTime"], actionData["number"], actionData["credit"], actionData["remarks"])

        self.teacherAction.clickCreateActionBtn()
        sleep(0.8)
        message = self.teacherAction.alertInfo()
        if message:
            try:
                self.assertIn(actionData["expected"], message)
            except Exception as F:
                print('创建活动：%s 创建活动失败！' % actionData["caseId"])
                log.logger.error('创建活动：%s 创建活动失败！' % actionData["caseId"])
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                failScreenShot = "fail_" + times + "_" + actionData["caseId"] + ".png"
                self.teacherAction.screenShot(failScreenShot)
                raise F
            else:
                log.logger.info('创建活动：%s 通过！' % actionData["caseId"])
                print("创建活动：测试用例创建活动成功！")
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                successScreenShot = "pass_" + times + "_" + actionData["caseId"] + ".png"
                self.teacherAction.screenShot(successScreenShot)

class TestTeaSearchAction(TeaUnittest):
    def test_02_admin_searchAction(self):
        '''查询活动测试用例'''
        '''判断教师是否进入了查询课程页面'''

        self.teacherSearchAction = TeaActionSearchPage(self.driver)
        print("点击选课系统按钮")
        self.teacherSearchAction.clickChooseCSBtn()
        sleep(0.3)
        #点击查询课程标签
        self.teacherSearchAction.clickSearchCourseTipBtn_teacher()
        # 获取创建课程页面文案
        if self.teacherSearchAction.getUrl() == searchCourseUrl:
            message = self.teacherSearchAction.historyActionPageText()
            try:
                self.assertEqual("活动·历史记录", message)
            except Exception as F:
                print("查询活动：进入查询活动页面失败！")
                log.logger.error('查询活动：进入查询活动页面失败！')
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                failScreenShot = "fail_" + times + "_" + "searchActionTest-01" + ".png"
                self.teacherSearchAction.screenShot(failScreenShot)
                raise F
            else:
                log.logger.info('查询活动：成功进入创建活动页面！')
                print("查询活动：测试用例进入查询活动页面成功！")
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                successScreenShot = "pass_" + times + "_" + "searchActionTest-01" + ".png"
                self.teacherSearchAction.screenShot(successScreenShot)
        sleep(1)
        self.teacherSearchAction.getActionNameFromSql()
        # beforeSearch = self.adminSearchCourse.beforeSearchCourseList()
        # sleep(1)
        # print("查询前行数：",beforeSearch)
        #输入关键字
        self.teacherSearchAction.searchActionNameKeyword()
        #点击查询
        self.teacherSearchAction.clickSearchBtn()
        sleep(2)
        #查询后的列表
        self.teacherSearchAction.getActionNameFromSql()
        try:
            self.teacherSearchAction.isSearchCorrect() == True

        except Exception as F:
            print("查询活动测试用例：查询功能异常！")
            log.logger.error('查询活动：searchActionTest-01 查询功能异常！')
            times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
            failScreenShot = "fail_" + times + "_" + "searchActionTest-01" + ".png"
            self.teacherSearchAction.screenShot(failScreenShot)
            raise F
        else:
            print("查询活动成功！")
            log.logger.info('查询活动：searchActionTest-01 通过！')
            times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
            successScreenShot = "pass_" + times + "_" + "searchActionTest-01" + ".png"
            self.teacherSearchAction.screenShot(successScreenShot)


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
    suite.addTest(loader.loadTestsFromTestCase(TestTeaSearchAction))

    # fp = open(report_path + '-test_login_result.html', 'wb')
    # # 测试报告的标题与描述
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='登录功能测试报告:',
    #                                        description='脚脚本从用例表读取要登录的用户数，然后执行相应次数的登录操作，'
    #                                                    '根据登陆后页面的用户名进行断言，把结果记录在用例表中')
    # runner.run(suite)