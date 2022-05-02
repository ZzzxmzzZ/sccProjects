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
class TestTeacherCreateCourse(TeaUnittest):

    @data(*courseData)
    def test_01_tea_createAction(self, courseData):
        '''创建课程测试用例'''
        #判断教师是否进入了课程创建页面
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
                log.logger.info('成功进入创建课程页面')
            except Exception as F:
                print("创建课程测试用例：进入创建课程页面未通过！")
                log.logger.error('创建课程：%s 未通过！未进入创建课程页面' % courseData["caseId"])
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                failScreenShot = "fail_" + times + "_" + courseData["caseId"] + ".png"
                self.teaCourse.screenShot(failScreenShot)
                raise F
            else:
                log.logger.info('创建课程：%s 成功进入创建课程页面！' % courseData["caseId"])
                print("创建课程测试用例：进入创建课程页面成功！")
                # 输入课程信息
                self.teaCourse.createCourseInfo(courseData["courseName"], courseData["classroom"],
                                                courseData["startweek"], courseData["endweek"], courseData["day"],
                                                courseData["startsection"], courseData["endsection"],
                                                courseData["number"], courseData["credits"], courseData["remarks"])
                # 选择学院分支
                self.teaCourse.academyChoose()
                # 页面下滑以防定位不到元素
                self.pageDown()
                sleep(0.5)
                # 点击【申请】按钮创建我课程
                self.teaCourse.clickCreateCourseBtn()
                sleep(0.8)
                # 获取弹窗信息
                message = self.teaCourse.alertInfo()
                if message:
                    try:
                        # 判断是否与Excel文档中的预期结果一致
                        self.assertIn(courseData["expected"], message)
                    except Exception as F:
                        print('创建课程测试用例：%s 未通过！' % courseData["caseId"])
                        log.logger.exception("创建课程：%s 失败，弹窗信息不合预期" % courseData["caseId"])
                        failScreenShot = "fail_" + courseData["caseId"] + ".png"
                        self.teaCourse.screenShot(failScreenShot)
                        raise F
                    else:
                        print('创建课程测试用例：%s 成功！' % courseData["caseId"])
                        log.logger.info('创建课程：%s 通过！' % courseData["caseId"])
                        successScreenShot = "pass_" + courseData["caseId"] + ".png"
                        self.teaCourse.screenShot(successScreenShot)
        else:
            print('创建课程：%s 未通过！' % courseData["caseId"])
            log.logger.error("创建课程跳转错误，请检查Url")
            log.logger.info('创建课程测试用例：%s 未通过！' % courseData["caseId"])
            times = time.strftime("%(asctime)s")
            failScreenShot = "fail_" + times + courseData["caseId"] + ".png"
            self.teaCourse.screenShot(failScreenShot)



        # else:
        #     print('创建课程：%s 未通过！' % courseData["caseId"])
        #     log.logger.error("创建课程跳转错误，请检查Url")
        #     log.logger.info('创建课程测试用例：%s 未通过！' % courseData["caseId"])
        #     times = time.strftime("%(asctime)s")
        #     failScreenShot = "fail_" + times + courseData["caseId"] + ".png"
        #     self.teaCourse.screenShot(failScreenShot)
        # #输入课程信息
        # self.teaCourse.createCourseInfo(courseData["courseName"], courseData["classroom"], courseData["startweek"], courseData["endweek"], courseData["day"], courseData["startsection"], courseData["endsection"], courseData["number"], courseData["credits"], courseData["remarks"])
        # #选择学院分支
        # self.teaCourse.academyChoose()
        # #页面下滑以防定位不到元素
        # self.pageDown()
        # sleep(0.5)
        # #点击【申请】按钮创建我课程
        # self.teaCourse.clickCreateCourseBtn()
        # sleep(0.8)
        # #获取弹窗信息
        # message = self.teaCourse.alertInfo()
        # if message:
        #     try:
        #         #判断是否与Excel文档中的预期结果一致
        #         self.assertIn(courseData["expected"], message)
        #     except Exception as F:
        #         print('创建课程测试用例：%s 未通过！' % courseData["caseId"])
        #         log.logger.exception("创建课程：%s 失败，弹窗信息不合预期" % courseData["caseId"])
        #         failScreenShot = "fail_" + courseData["caseId"] + ".png"
        #         self.teaCourse.screenShot(failScreenShot)
        #         raise F
        #     else:
        #         print('创建课程测试用例：%s 成功！' % courseData["caseId"])
        #         log.logger.info('创建课程：%s 通过！' % courseData["caseId"])
        #         successScreenShot = "pass_" + courseData["caseId"] + ".png"
        #         self.teaCourse.screenShot(successScreenShot)

class TestTeacherSeachCourse(TeaUnittest):
    def test_02_teacher_searchCourse(self):
        '''查询课程测试用例'''
        '''判断教师是否进入了查询课程页面'''

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
                print("查询课程：进入查询课程页面失败！")
                log.logger.error('查询课程： 进入查询课程页面失败！')
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                failScreenShot = "fail_" + times + "_" + "searchCourseTest-01" + ".png"
                self.teaSearchCourse.screenShot(failScreenShot)
                raise F
            else:
                log.logger.info('查询课程：成功进入创建课程页面！')
                print("查询课程：测试用例进入查询课程页面成功！")
                times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
                successScreenShot = "pass_" + times + "_" + "searchCourseTest-01" + ".png"
                self.teaSearchCourse.screenShot(successScreenShot)
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
            print("查询课程测试用例：查询功能异常！")
            log.logger.error('查询课程：searchCourseTest-01 查询功能异常！')
            times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
            failScreenShot = "fail_" + times + "_" + "searchCourseTest-01" + ".png"
            self.teaSearchCourse.screenShot(failScreenShot)
            raise F
        else:
            print("查询课程成功！")
            log.logger.info('查询课程：searchCourseTest-01 通过！')
            times = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
            successScreenShot = "pass_" + times + "_" + "searchCourseTest-01" + ".png"
            self.teaSearchCourse.screenShot(successScreenShot)


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