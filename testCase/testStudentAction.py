import os, time, unittest
from time import sleep

# from common.BeautifulReport.BeautifulReport import BeautifulReport
from ddt import ddt, data
import xlrd

# from common.HTMLTestRunner import HTMLTestRunner
#from common.myUnit import MyUnittest
# from config.conf import reportPath, casePath, baseUrl, hwUrl
from selenium import webdriver

from common.log import Logger
from common.myUnit import StuUnittest
from config.conf import baseUrl, casePath
from config.doExcel import ReadExcel
#from common.report import Logger
from pageObject.loginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC

from pageObject.student.studentActionSearchPage import StudentActionSearchPage
from pageObject.student.studentCourseSearchPage import StudentCourseSearchPage

log = Logger(__name__)
testCreateCourseData = ReadExcel('elementDate.xlsx', 'createCourseData')  # 登录模块测试数据
courseData = testCreateCourseData.readData()

createCourseUrl = baseUrl + "course/create"
searchCourseUrl = baseUrl + "course/history"
homeUrl = baseUrl + "index"


@ddt
class TestStudentAction(StuUnittest):

    def test_01_student_searchAction(self):
        '''查询课程测试用例'''
        '''判断学生是否进入了查询课程页面'''

        self.stuSearchAction = StudentActionSearchPage(self.driver)
        print("点击选课系统按钮")
        self.stuSearchAction.clickChooseCSBtn()
        sleep(0.3)
        #点击查询课程标签
        self.stuSearchAction.clickSearchCourseTipBtn_student()
        # 获取创建课程页面文案
        if self.stuSearchAction.getUrl() == searchCourseUrl:
            message = self.stuSearchAction.historyActionPageText()
            try:
                self.assertEqual("活动·历史记录", message)
            except Exception as F:
                print("查询活动：进入查询活动页面失败！")
                log.logger.error('查询活动：进入查询活动页面失败！')
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                failScreenShot = "fail_" + times + "_" + "searchActionTest-01" + ".png"
                self.stuSearchAction.screenShot(failScreenShot)
                raise F
            else:
                log.logger.info('查询活动：成功进入创建活动页面！')
                print("查询活动：测试用例进入查询活动页面成功！")
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                successScreenShot = "pass_" + times + "_" + "searchActionTest-01" + ".png"
                self.stuSearchAction.screenShot(successScreenShot)
        sleep(1)
        self.stuSearchAction.getActionNameFromSql()
        # beforeSearch = self.adminSearchCourse.beforeSearchCourseList()
        # sleep(1)
        # print("查询前行数：",beforeSearch)
        #输入关键字
        self.stuSearchAction.searchActionNameKeyword()
        #点击查询
        self.stuSearchAction.clickSearchBtn()
        sleep(1)
        #查询后的列表
        self.stuSearchAction.getActionNameFromSql()
        try:
            self.stuSearchAction.isSearchCorrect() == True

        except Exception as F:
            print("查询活动测试用例：查询功能异常！")
            log.logger.error('查询活动：searchActionTest-01 查询功能异常！')
            times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
            failScreenShot = "fail_" + times + "_" + "searchActionTest-01" + ".png"
            self.stuSearchAction.screenShot(failScreenShot)
            raise F
        else:
            print("查询活动成功！")
            log.logger.info('查询活动：searchActionTest-01 通过！')
            times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
            successScreenShot = "pass_" + times + "_" + "searchActionTest-01" + ".png"
            self.stuSearchAction.screenShot(successScreenShot)


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
    suite.addTest(loader.loadTestsFromTestCase(TestStudentAction))

    # fp = open(report_path + '-test_login_result.html', 'wb')
    # # 测试报告的标题与描述
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='登录功能测试报告:',
    #                                        description='脚脚本从用例表读取要登录的用户数，然后执行相应次数的登录操作，'
    #                                                    '根据登陆后页面的用户名进行断言，把结果记录在用例表中')
    # runner.run(suite)