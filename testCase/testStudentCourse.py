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

from pageObject.student.studentCourseSearchPage import StudentCourseSearchPage

log = Logger(__name__)
testCreateCourseData = ReadExcel('elementDate.xlsx', 'createCourseData')  # 登录模块测试数据
courseData = testCreateCourseData.readData()

createCourseUrl = baseUrl + "course/create"
searchCourseUrl = baseUrl + "course/history"
homeUrl = baseUrl + "index"


@ddt
class TestStudentCourse(StuUnittest):

    def test_01_student_searchCourse(self):
        '''查询课程测试用例'''
        '''判断学生是否进入了查询课程页面'''

        self.stuSearchCourse = StudentCourseSearchPage(self.driver)
        print("点击选课系统按钮")
        self.stuSearchCourse.clickChooseCSBtn()
        sleep(0.3)
        #点击查询课程标签
        self.stuSearchCourse.clickSearchCourseTipBtn_student()
        # 获取创建课程页面文案
        if self.stuSearchCourse.getUrl() == searchCourseUrl:
            message = self.stuSearchCourse.historyCoursePageText()
            try:
                self.assertEqual("课程·历史记录", message)
            except Exception as F:
                print("查询课程：进入查询课程页面失败！")
                log.logger.error('查询课程： 进入查询课程页面失败！')
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                failScreenShot = "fail_" + times + "_" + "searchCourseTest-01" + ".png"
                self.stuSearchCourse.screenShot(failScreenShot)
                raise F
            else:
                log.logger.info('查询课程：成功进入创建课程页面！')
                print("查询课程：测试用例进入查询课程页面成功！")
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                successScreenShot = "pass_" + times + "_" + "searchCourseTest-01" + ".png"
                self.stuSearchCourse.screenShot(successScreenShot)
        sleep(1)
        self.stuSearchCourse.getCourseNameFromSql()
        # beforeSearch = self.adminSearchCourse.beforeSearchCourseList()
        # sleep(1)
        # print("查询前行数：",beforeSearch)
        #输入关键字
        self.stuSearchCourse.searchCourseNameKeyword()
        #点击查询
        self.stuSearchCourse.clickSearchBtn()
        sleep(2)
        #查询后的列表
        self.stuSearchCourse.getCourseNameValue()
        try:
            self.stuSearchCourse.isSearchCorrect() == True

        except Exception as F:
            print("查询课程测试用例：查询功能异常！")
            log.logger.error('查询课程：searchCourseTest-01 查询功能异常！')
            times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
            failScreenShot = "fail_" + times + "_" + "searchCourseTest-01" + ".png"
            self.stuSearchCourse.screenShot(failScreenShot)
            raise F
        else:
            print("查询课程成功！")
            log.logger.info('查询课程：searchCourseTest-01 通过！')
            times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
            successScreenShot = "pass_" + times + "_" + "searchCourseTest-01" + ".png"
            self.stuSearchCourse.screenShot(successScreenShot)


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
    suite.addTest(loader.loadTestsFromTestCase(TestStudentCourse))

    # fp = open(report_path + '-test_login_result.html', 'wb')
    # # 测试报告的标题与描述
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='登录功能测试报告:',
    #                                        description='脚脚本从用例表读取要登录的用户数，然后执行相应次数的登录操作，'
    #                                                    '根据登陆后页面的用户名进行断言，把结果记录在用例表中')
    # runner.run(suite)