# -*-coding:utf-8-*-
import time
import unittest

from selenium.webdriver.support.wait import WebDriverWait

from common.myUnit import MyUnittest
from pageObject.homePage import HomePage
from selenium.webdriver.support import expected_conditions as EC


class TestHome(MyUnittest):

    def test_01_admin_enter_createCourse(self):
        '''判断管理员是否进入了课程创建页面'''
        '''这里的login是myunittest.py中定义的login = LoginPage()中的login'''
        self.login.mock_adminLogin()
        self.home = HomePage(self.driver)
        print("点击选课系统按钮")
        self.home.clickChooseCSBtn()
        time.sleep(0.5)
        self.home.clickCreateCourseTipBtn()
        #h获取创建课程页面文案
        message = self.home.createCoursePageText()
        try:
            self.assertEqual(message, "创建课程")
        except Exception as F:
            print("登录测试用例：进入创建课程页面未通过！")
            raise F
        else:
            print("登录测试用例进入创建课程页面成功！")

        '''管理员发布公告'''
    def test_02_admin_enter_createNoticePage(self):
        '''判断管理员是否进入了公告发布创建页面'''
        self.login.mock_adminLogin()
        self.home = HomePage(self.driver)
        print("点击公告通知按钮")
        self.home.clickNoticeBtn()
        time.sleep(0.5)
        self.home.clickSendNoticeTipBtn()
        # 获取发布公告页面文案
        message = self.home.sendNoticePageText()
        try:
            self.assertIn("发布",message)
        except Exception as F:
            print("登录测试用例：进入发布公告页面未通过！")
            raise F
        else:
            print("登录测试用例进入发布公告页面成功！")

    def test_03_admin_enter_createAction(self):
        '''判断管理员是否进入了活动创建页面'''
        '''这里的login是myunittest.py中定义的login = LoginPage()中的login'''
        self.login.mock_adminLogin()
        self.home = HomePage(self.driver)
        print("点击选课系统按钮")
        self.home.clickChooseCSBtn()
        time.sleep(0.5)
        self.home.clickAdminCreateActionTipBtn()
        #获取创建活动页面文案
        message = self.home.createActionPageText()
        try:
            self.assertEqual(message, "创建活动")
        except Exception as F:
            print("登录测试用例：进入创建活动页面未通过！")
            raise F
        else:
            print("登录测试用例进入创建活动页面成功！")

        self.home.clickTimeStartBtn()
        print("点击日期成功")
        time.sleep(1)

    def test_04_admin_enter_createNotice(self):
        '''判断管理员是否进入了发布公告页面'''
        '''这里的login是myunittest.py中定义的login = LoginPage()中的login'''
        self.login.mock_adminLogin()
        self.home = HomePage(self.driver)
        print("点击公告通知按钮")
        self.home.clickNoticeBtn()
        time.sleep(0.5)
        self.home.clickSendNoticeTipBtn()
        #获取创建活动页面文案
        message = self.home.sendNoticePageText()
        try:
            self.assertIn("公告通知", message)
        except Exception as F:
            print("登录测试用例：进入发布公告页面未通过！")
            raise F
        else:
            print("登录测试用例进入发布公告页面成功！")

        self.home.clickSendNoticeToTeaBtn()
        print("点击向教师发布公告成功")
        time.sleep(0.5)
        # To 教师文案
        toTeaText = self.home.sendNoticeToTeaPageText()
        try:
            self.assertEqual("To 教师", message)
        except Exception as F:
            print("登录测试用例：进入向教师发布公告小窗未通过！")
            raise F
        else:
            print("登录测试用例进入向教师发布公告小窗成功！")

    def test_05_admin_enter_schoolTree(self):
        '''判断管理员是否进入了教师管理页面'''
        '''这里的login是myunittest.py中定义的login = LoginPage()中的login'''
        self.login.mock_adminLogin()
        self.home = HomePage(self.driver)
        print("点击学院机构按钮")
        self.home.clickSchoolTreeBtn()
        time.sleep(0.5)
        #获取学院机构页面文案
        message = self.home.schoolTreePageText()
        try:
            self.assertIn("学校机构", message)
        except Exception as F:
            print("登录测试用例：进入学校机构页面未通过！")
            raise F
        else:
            print("登录测试用例进入学校机构页面成功！")
    def test_06_admin_enter_teaMagage(self):
        '''判断管理员是否成功进入教师管理模块页面'''

        self.login.mock_adminLogin()
        self.home = HomePage(self.driver)
        print("点击教师管理模块按钮")
        self.home.clickTeaManageBtn()
        time.sleep(0.5)
        #获取教师管理系统页面文案
        message = self.home.teaManagePageText()
        try:
            self.assertEqual("教师管理系统", message)
        except Exception as F:
            print("登录测试用例：进入教师管理系统页面未通过！")
            raise F
        else:
            print("登录测试用例进入教师管理系统页面成功！")

    def test_07_admin_enter_stuMagage(self):
        '''判断管理员是否成功进入学生管理模块页面'''

        self.login.mock_adminLogin()
        self.home = HomePage(self.driver)
        print("点击教师管理模块按钮")
        self.home.clickStuManageBtn()
        time.sleep(0.5)
        #获取学生管理系统页面文案
        message = self.home.stuManagePageText()
        try:
            self.assertEqual("学生管理系统", message)
        except Exception as F:
            print("登录测试用例：进入学生管理系统页面未通过！")
            raise F
        else:
            print("登录测试用例进入学生管理系统页面成功！")


    def test_08_teacher_enter_notice(self):

        '''判断教师是否进入了发布公告页面'''
        self.login.mock_teaLogin()

        self.teacherNotice = HomePage(self.driver)
        print("点击公告通知按钮")
        time.sleep(0.5)
        self.teacherNotice.clickNoticeBtn_teacher()
        time.sleep(0.5)
        self.teacherNotice.clickSendNoticeTipBtn_teacher()
        # 获取公告页面文案
        message = self.teacherNotice.sendNoticePageText()
        try:
            self.assertIn("公告通知", message)
        except Exception as F:
            print("登录测试用例：进入发布公告页面未通过！")
            raise F
        else:
            print("登录测试用例进入发布公告页面成功！")

    def test_09_admin_enter_historyCoursePage(self):
        '''判断管理员是否成功进入查询课程页面'''

        self.login.mock_adminLogin()
        self.home = HomePage(self.driver)
        print("点击选课系统按钮")
        self.home.clickChooseCSBtn()
        time.sleep(0.5)
        self.home.clickSearchCourseTipBtn_admin()
        time.sleep(0.5)
        #获取教师管理系统页面文案
        message = self.home.historyCoursePageText()
        try:
            self.assertEqual("课程·历史记录", message)
        except Exception as F:
            print("登录测试用例：进入查询课程页面未通过！")
            raise F
        else:
            print("登录测试用例进入查询课程页面成功！")







    # def test_03_tea_loginOffFunc(self):
    #     '''判断管理员是否进入了公告发布创建页面'''
    #     self.login.mock_teaLogin()
    #     self.home = HomePage(self.driver)
    #     print("点击头像小标")
    #
    #     self.home.clickAvatarBtn()
    #     time.sleep(0.5)
    #
    #     # self.click('xpath', './/*[@id=\'type\']/div/div')
    #     # self.click('xpath', './/*[@id="userDropdown"]')
    #     print("定位头像成功")
    #     time.sleep(1)
    #     self.click('xpath', './/*[@id="content"]/div[1]/nav/ul/li[2]/div/a[4]')
    #     time.sleep(2)
    #     print("定位登出成功")
    #
    #
    #     #
    #     # # 找到dropdown-menu父元素
    #     # WebDriverWait(self.home.driver,10).until(lambda the_driver:the_driver.find_element_by_class_name('dropdown-menu dropdown-menu-right shadow animated--grow-in show').is_displayed())
    #     #
    #     # # 找到better than
    #     # tuichu = self.home.driver.find_element_by_class_name('dropdown-menu dropdown-menu-right shadow animated--grow-in show').find_element_by_link_text('登出')
    #     #
    #     # tuichu.click()
    #     #
    #     # time.sleep(1)
    #     #
    #     # #点击退出登录按钮
    #     # self.home.clickLogoffBtn()
    #     # time.sleep(0.5)
    #     # #点击确定退出
    #     self.home.clickSureLogoffBtn()
    #     # 获取发布公告页面文案
    #     message = self.home.loginPageText()
    #     try:
    #         self.assertEqual(message,'请登录')
    #     except Exception as F:
    #         print("登录测试用例：退出登录未通过！")
    #         raise F
    #     else:
    #         print("登录测试用例退出登录成功！




if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestHome))

