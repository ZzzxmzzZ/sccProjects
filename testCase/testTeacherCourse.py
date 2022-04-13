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
from common.myUnit import MyUnittest, TeaUnittest
from config.conf import baseUrl, casePath
from config.doExcel import ReadExcel
#from common.report import Logger
from pageObject.loginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC

from pageObject.teacher.teaCoursePage import TeaCoursePage
from pageObject.teacher.teaCourseSearchPage import TeaCourseSearchPage

log = Logger(__name__)
testCreateCourseData = ReadExcel('elementDate.xlsx', 'createCourseData')  # 登录模块测试数据
courseData = testCreateCourseData.readData()

createCourseUrl = baseUrl + "course/create"
searchCourseUrl = baseUrl + "course/history"
homeUrl = baseUrl + "index"


@ddt
class TestTeacherCourse(TeaUnittest):

    @data(*courseData)
    def test_01_tea_createAction(self, courseData):
        '''创建课程测试用例'''
        '''判断教师是否进入了课程创建页面'''

        self.teaCourse = TeaCoursePage(self.driver)
        print("点击选课系统按钮")
        self.teaCourse.clickChooseCSBtn()
        sleep(0.3)
        #点击新增课程标签
        self.teaCourse.clickCreateCourseTipBtn()
        # 获取创建课程页面文案
        if self.teaCourse.getUrl() == createCourseUrl:
            message = self.teaCourse.createCoursePageText()
            try:
                self.assertEqual(message, "创建课程")
            except Exception as F:
                print("登录测试用例：进入创建课程页面未通过！")
                raise F
            else:
                print("登录测试用例进入创建课程页面成功！")

        '''创建课程测试用例'''
        self.teaCourse.createCourseInfo(courseData["courseName"], courseData["classroom"], courseData["startweek"], courseData["endweek"], courseData["day"], courseData["startsection"], courseData["endsection"], courseData["number"], courseData["credits"], courseData["remarks"])
        self.teaCourse.academyChoose()
        self.pageDown()
        sleep(0.5)
        self.teaCourse.clickCreateCourseBtn()
        sleep(0.8)
        message = self.teaCourse.alertInfo()
        if message:
            try:
                self.assertIn(courseData["expected"], message)
            except Exception as F:
                print('登录测试用例：%s 未通过！' % courseData["caseId"])
                raise F
            else:
                print('登录测试用例：%s 成功！' % courseData["caseId"])


    def test_02_teacher_searchCourse(self):
        '''查询课程测试用例'''
        '''判断管理员是否进入了查询课程页面'''

        self.teaSearchCourse = TeaCourseSearchPage(self.driver)
        print("点击选课系统按钮")
        self.teaSearchCourse.clickChooseCSBtn()
        sleep(0.3)
        #点击查询课程标签
        self.teaSearchCourse.clickSearchCourseTipBtn_teacher()
        # 获取创建课程页面文案
        if self.teaSearchCourse.getUrl() == searchCourseUrl:
            message = self.teaSearchCourse.historyCoursePageText()
            try:
                self.assertEqual("课程·历史记录", message)
            except Exception as F:
                print("登录测试用例：进入查询课程页面未通过！")
                raise F
            else:
                print("登录测试用例进入查询课程页面成功！")
        sleep(1)
        self.teaSearchCourse.getCourseNameFromSql()
        # beforeSearch = self.adminSearchCourse.beforeSearchCourseList()
        # sleep(1)
        # print("查询前行数：",beforeSearch)
        #输入关键字
        self.teaSearchCourse.searchCourseNameKeyword()
        #点击查询
        self.teaSearchCourse.clickSearchBtn()
        sleep(2)
        #查询后的列表
        self.teaSearchCourse.getCourseNameValue()
        try:
            self.teaSearchCourse.isSearchCorrect() == True

        except Exception as F:
            print("登录测试用例：查询功能异常！")
            raise F
        else:
            print("查询课程成功！")


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
    suite.addTest(loader.loadTestsFromTestCase(TestTeacherCourse))

    # fp = open(report_path + '-test_login_result.html', 'wb')
    # # 测试报告的标题与描述
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='登录功能测试报告:',
    #                                        description='脚脚本从用例表读取要登录的用户数，然后执行相应次数的登录操作，'
    #                                                    '根据登陆后页面的用户名进行断言，把结果记录在用例表中')
    # runner.run(suite)