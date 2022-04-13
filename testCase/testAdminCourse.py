import time, unittest
from time import sleep

# from common.BeautifulReport.BeautifulReport import BeautifulReport
from ddt import ddt, data

# from common.HTMLTestRunner import HTMLTestRunner
#from common.myUnit import MyUnittest
# from config.conf import reportPath, casePath, baseUrl, hwUrl

from common.log import Logger
from common.myUnit import AdminUnittest
from config.conf import baseUrl
from config.doExcel import ReadExcel
#from common.report import Logger
from pageObject.admin.adminCourseAuditPage import AdminCourseAuditPage
from selenium.webdriver.common.action_chains import ActionChains
from pageObject.admin.adminCourseCreatePage import AdminCoursePage
from pageObject.admin.adminCourseSearchPage import AdminCourseSearchPage

log = Logger(__name__)
testCreateCourseData = ReadExcel('elementDate.xlsx', 'createCourseData')  # 登录模块测试数据
courseData = testCreateCourseData.readData()

testSearchData = ReadExcel('elementDate.xlsx', 'searchData')  # 搜索测试数据
searchData = testSearchData.readData()

testAuditData = ReadExcel('elementDate.xlsx', 'auditCourseData')  # 审核课程测试数据
auditData = testAuditData.readData()

createCourseUrl = baseUrl + "course/create"
searchCourseUrl = baseUrl + "course/history"

homeUrl = baseUrl + "index"


@ddt
class TestAdminCourse(AdminUnittest):

    # @data(*courseData)
    # def test_01_admin_createCourse(self, courseData):
    #     '''创建课程测试用例'''
    #     '''判断管理员是否进入了课程创建页面'''
    #
    #     self.adminCourse = AdminCoursePage(self.driver)
    #     print("点击选课系统按钮")
    #     self.adminCourse.clickChooseCSBtn()
    #     sleep(0.3)
    #     #点击新增课程标签
    #     self.adminCourse.clickCreateCourseTipBtn()
    #     # 获取创建课程页面文案
    #     if self.adminCourse.getUrl() == createCourseUrl:
    #         message = self.adminCourse.createCoursePageText()
    #         try:
    #             self.assertEqual(message, "创建课程")
    #         except Exception as F:
    #             print("登录测试用例：进入创建课程页面未通过！")
    #             raise F
    #         else:
    #             print("登录测试用例进入创建课程页面成功！")
    #
    #     '''创建课程测试用例'''
    #     self.adminCourse.createCourseInfo(courseData["courseName"], courseData["classroom"], courseData["startweek"], courseData["endweek"], courseData["day"], courseData["startsection"], courseData["endsection"], courseData["number"], courseData["credits"], courseData["remarks"])
    #     self.adminCourse.academyChoose()
    #     self.pageDown()
    #     sleep(0.5)
    #     self.adminCourse.clickCreateCourseBtn()
    #     sleep(0.8)
    #     message = self.adminCourse.alertInfo()
    #     if message:
    #         try:
    #             self.assertIn(courseData["expected"], message)
    #         except Exception as F:
    #             print('登录测试用例：%s 未通过！' % courseData["caseId"])
    #             raise F
    #         else:
    #             print('登录测试用例：%s 成功！' % courseData["caseId"])


    # def test_02_admin_searchCourse(self):
    #     '''查询课程测试用例'''
    #     '''判断管理员是否进入了查询课程页面'''
    #
    #     self.adminSearchCourse = AdminCourseSearchPage(self.driver)
    #     print("点击选课系统按钮")
    #     self.adminSearchCourse.clickChooseCSBtn()
    #     sleep(0.3)
    #     #点击查询课程标签
    #     self.adminSearchCourse.clickSearchCourseTipBtn_admin()
    #     # 获取创建课程页面文案
    #     if self.adminSearchCourse.getUrl() == searchCourseUrl:
    #         message = self.adminSearchCourse.historyCoursePageText()
    #         try:
    #             self.assertEqual("课程·历史记录", message)
    #         except Exception as F:
    #             print("登录测试用例：进入查询课程页面未通过！")
    #             raise F
    #         else:
    #             print("登录测试用例进入查询课程页面成功！")
    #     sleep(1)
    #     self.adminSearchCourse.getCourseNameFromSql()
    #     # beforeSearch = self.adminSearchCourse.beforeSearchCourseList()
    #     # sleep(1)
    #     # print("查询前行数：",beforeSearch)
    #     #输入关键字
    #     self.adminSearchCourse.searchCourseNameKeyword()
    #     #点击查询
    #     self.adminSearchCourse.clickSearchBtn()
    #     sleep(2)
    #     #查询后的列表
    #     self.adminSearchCourse.getCourseNameValue()
    #     try:
    #         self.adminSearchCourse.isSearchCorrect() == True
    #
    #     except Exception as F:
    #         print("登录测试用例：查询功能异常！")
    #         raise F
    #     else:
    #         print("查询课程成功！")

    @data(*auditData)
    def test_03_admin_auditCourse(self, auditData):
        '''管理员审核课程测试用例'''
        '''判断管理员是否进入了查询课程页面'''

        self.adminSearchCourse = AdminCourseAuditPage(self.driver)
        print("点击选课系统按钮")
        self.adminSearchCourse.clickChooseCSBtn()
        sleep(0.3)
        #点击查询课程标签
        self.adminSearchCourse.clickSearchCourseTipBtn_admin()
        # 获取创建课程页面文案
        if self.adminSearchCourse.getUrl() == searchCourseUrl:
            message = self.adminSearchCourse.historyCoursePageText()
            try:
                self.assertEqual("课程·历史记录", message)
            except Exception as F:
                print("登录测试用例：进入查询课程页面未通过！")
                raise F
            else:
                print("登录测试用例进入查询课程页面成功！")
        sleep(1)
        firstCourseName = self.adminSearchCourse.firstCourseName()

        print("第一行名字：",firstCourseName)
        courseID = self.adminSearchCourse.getFirstRowCourseIDFromSql(firstCourseName)
        self.adminSearchCourse.clickFirstRow()
        #点击审核课程
        self.adminSearchCourse.clickAuditBtn()
        sleep(0.5)
        self.adminSearchCourse.clickTimeStartBtn(auditData["startTime"])
        sleep(1)
        action = ActionChains(self.driver)
        action.move_by_offset(200, 100).click().perform()  # 200，100是坐标
        self.adminSearchCourse.clickTimeEndBtn(auditData["endTime"])
        sleep(1)

        self.adminSearchCourse.clickSureBtn()
        sleep(0.8)

        message = self.adminSearchCourse.alertInfo()
        #课程状态
        status = self.adminSearchCourse.getCourseNameFromSql(courseID)
        print(status)



        try:
            if message == "设置成功":
                #审核通过
                self.assertEqual(status, "1")
            else:
                self.assertEqual(auditData["expected"], message)
                self.adminSearchCourse.clickCancelBtn()
                sleep(0.8)
                firstCourseName2 = self.adminSearchCourse.firstCourseName()
                self.assertEqual(firstCourseName, firstCourseName2)


        except Exception as F:
            print("审核课程测试用例失败！")
            raise F
        else:
            print("审核课程测试用例成功！")



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
    suite.addTest(loader.loadTestsFromTestCase(TestAdminCourse))

    # fp = open(report_path + '-test_login_result.html', 'wb')
    # # 测试报告的标题与描述
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='登录功能测试报告:',
    #                                        description='脚脚本从用例表读取要登录的用户数，然后执行相应次数的登录操作，'
    #                                                    '根据登陆后页面的用户名进行断言，把结果记录在用例表中')
    # runner.run(suite)