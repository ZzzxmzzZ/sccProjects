# -*-coding:utf-8-*-
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# import selenium.webdriver import ActionChains
import xlrd
from selenium.webdriver.support.select import Select

from config.conf import baseUrl
from config.doExcel import ReadExcel
from pageObject.basePage import BasePage, log

eleData = ReadExcel() # 存储系统所有的元素数据

homeUrl = baseUrl + "index"
class HomePage(BasePage):
    #选课系统元素
    print("选课系统元素定位：", eleData.readExcel(6, 3))
    chooseCSEle = (By.XPATH, eleData.readExcel(6, 3))
    createCourseEle = (By.XPATH, eleData.readExcel(7, 3))

    createCourseText = (By.XPATH, eleData.readExcel(8, 3))
    #
    #创建活动
    adminCreateActionEle = (By.XPATH, eleData.readExcel(22, 3))
    adminCreateActionMessageEle = (By.XPATH, eleData.readExcel(23, 3))
    adminActionStartEle = (By.XPATH, eleData.readExcel(24, 3))
    adminActionEndEle = (By.XPATH, eleData.readExcel(25, 3))
    adminActionChooseEle = (By.XPATH, eleData.readExcel(26, 3))



    #公告通知
    noticeEle = (By.XPATH, eleData.readExcel(33, 3))
    sendNoticeEle = (By.XPATH, eleData.readExcel(34, 3))
    stuNoticeEle = (By.XPATH, eleData.readExcel(35, 3))
    teaNoticeEle = (By.XPATH, eleData.readExcel(36, 3))
    noticePageMessageEle = (By.XPATH, eleData.readExcel(37, 3))
    toTeacherEle = (By.XPATH, eleData.readExcel(38, 3))
    toStudentEle = (By.XPATH, eleData.readExcel(39, 3))
    teaNoticeTitleEle = (By.XPATH, eleData.readExcel(40, 3))
    teaNoticeContentEle = (By.XPATH, eleData.readExcel(41, 3))
    stuNoticeTitleEle = (By.XPATH, eleData.readExcel(42, 3))
    stuNoticeContentEle = (By.XPATH, eleData.readExcel(43, 3))

    teaTreeEle = (By.XPATH, eleData.readExcel(44, 3))
    teaComputerEle = (By.XPATH, eleData.readExcel(45, 3))
    cancelSendTeaNoticeEle = (By.XPATH, eleData.readExcel(46, 3))
    sureSendTeaNoticeEle = (By.XPATH, eleData.readExcel(47, 3))
    stuComputerEle = (By.XPATH, eleData.readExcel(48, 3))
    cancelSendStuNoticeEle = (By.XPATH, eleData.readExcel(49, 3))
    sureSendStuNoticeEle = (By.XPATH, eleData.readExcel(50, 3))

    #教师公告管理
    teaNoticeEle = (By.XPATH, eleData.readExcel(51, 3))
    sendNotice_teaEle = (By.XPATH, eleData.readExcel(52, 3))
    stuNoticeEle = (By.XPATH, eleData.readExcel(53, 3))


    #学院机构
    schoolTreeEle = (By.XPATH, eleData.readExcel(54, 3))
    schoolTreePageTextEle = (By.XPATH, eleData.readExcel(55, 3))
    wanganEle = (By.XPATH, eleData.readExcel(56, 3))
    addTreeEle = (By.XPATH, eleData.readExcel(57, 3))
    editTreeEle = (By.XPATH, eleData.readExcel(58, 3))
    deleteTreeEle = (By.XPATH, eleData.readExcel(59, 3))
    #教师管理模块
    teaManageEle = (By.XPATH, eleData.readExcel(61, 3))
    teaManaPageTextEle = (By.XPATH, eleData.readExcel(62, 3))
    #学生管理模块
    stuManageEle = (By.XPATH, eleData.readExcel(69, 3))
    stuManaPageTextEle = (By.XPATH, eleData.readExcel(70, 3))

    #管理员查询课程
    adminSearchCourseEle = (By.XPATH, eleData.readExcel(78, 3))
    historyCourseTextEle = (By.XPATH, eleData.readExcel(79, 3))
    keyCourseNameEle = (By.XPATH, eleData.readExcel(80, 3))
    searchBtnEle = (By.XPATH, eleData.readExcel(81, 3))

    # 查询课程按钮
    def clickSearchCourseTipBtn_admin(self):
        self.locator_element(*self.adminSearchCourseEle).click()


    # 获取查询课程页面文案
    def historyCoursePageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.historyCourseTextEle).text
        return element_text



    #教师公告管理

    # 点发布新公告按钮
    def clickSendNoticeTipBtn_teacher(self):
        self.locator_element(*self.sendNotice_teaEle).click()


    # 点击公告通知按钮
    def clickNoticeBtn_teacher(self):
        # self.driver.find_element_by_css_selector('#accordionSidebar > li:nth-child(6) > a').click()
        self.locator_element(*self.teaNoticeEle).click()
        print("定位成功")


    # 获取发布公告页面文案
    def sendNoticePageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.noticePageMessageEle).text
        return element_text

    #管理员管理学生模块

    # 点击学生管理模块按钮
    def clickStuManageBtn(self):
        self.locator_element(*self.stuManageEle).click()

    # 获取学生管理系统页面文案
    def stuManagePageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.stuManaPageTextEle).text
        return element_text


    # 点击教师管理模块按钮
    def clickTeaManageBtn(self):
        self.locator_element(*self.teaManageEle).click()

    # 获取教师管理系统页面文案
    def teaManagePageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.teaManaPageTextEle).text
        return element_text


    # 学院机构按钮
    def clickSchoolTreeBtn(self):
        self.locator_element(*self.schoolTreeEle).click()

    # 获取学院机构页面文案
    def schoolTreePageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.schoolTreePageTextEle).text
        return element_text
    #鼠标悬停导航
    def move(self):
        el = self.locator_element(*self.wanganEle)
        ActionChains(self.driver).move_to_element(el).perform()


    #网安学院
    def clickAddWanganBtn(self):
        self.move()
        self.locator_element(*self.addTreeEle).click()


    #系统弹窗
    def alertInfo(self):
        # wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        message = alert.text
        alert.accept()
        # alert.accept()
        # alert1 = self.driver.switch_to.alert
        # sendNoticeText = alert1.text
        # alert1.accept()
        return message

    # 发布新公告按钮
    def clickSendNoticeTipBtn(self):
        self.locator_element(*self.sendNoticeEle).click()

    # 点发布新公告按钮
    def clickSendNoticeTipBtn(self):
        self.locator_element(*self.sendNoticeEle).click()

    # 点击公告通知按钮
    def clickNoticeBtn(self):
        # self.driver.find_element_by_css_selector('#accordionSidebar > li:nth-child(6) > a').click()
        self.locator_element(*self.noticeEle).click()
        print("定位成功")

    # 点发布新公告按钮
    def clickSendNoticeTipBtn(self):
        self.locator_element(*self.sendNoticeEle).click()

    # 获取发布公告页面文案
    def sendNoticePageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.noticePageMessageEle).text
        return element_text
    # 向教师发布公告
    def clickSendNoticeToTeaBtn(self):
        self.locator_element(*self.teaNoticeEle).click()

    # 向学生发布公告
    def clickSendNoticeToStuBtn(self):
        self.locator_element(*self.stuNoticeEle).click()

    # 教师公告小窗文案
    def sendNoticeToTeaPageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.toTeacherEle).text
        return element_text

    # 学生公告小窗文案
    def sendNoticeToStuPageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.toStudentEle).text
        return element_text


    # 填写发布公告信息
    def sendNoticeInfo(self, courseName, classroom, startweek, endweek,day,startsection,endsection,courseNum, courseCredit, remark):
        self.locator_element(*self.courseNameEle).send_keys(courseName)
        self.locator_element(*self.classroomEle).send_keys(classroom)
        # self.locator_element(*self.startweekEle).find_element_by_xpath("//option[@value="+startweek+"]").click()

        #startweek
        selectStartWeek = Select(self.locator_element(*self.startweekEle))  # select标签
        # 获得选择项
        # 1.根据值来选择
        selectStartWeek.select_by_value(str(startweek))

        # endweek
        selectEndWeek = Select(self.locator_element(*self.endweekEle))  # select标签
        selectEndWeek.select_by_value(str(endweek))

        #day
        selectDay = Select(self.locator_element(*self.dayEle))  # select标签
        selectDay.select_by_value(str(day))

        #startsection
        selectStartSection = Select(self.locator_element(*self.startsectionEle))  # select标签
        selectStartSection.select_by_value(str(startsection))
        #endsection
        selectEndSection = Select(self.locator_element(*self.endsectionEle))  # select标签
        selectEndSection.select_by_value(str(endsection))


        # a = self.locator_element(*self.endweekEle)
        # a.click()
        # a.find_element_by_xpath("//option[@value=" + endweek + "]").click()
        # # sleep(1)
        # self.locator_element(*self.dayEle).find_element_by_xpath("//option[@value=" + day + "]").click()
        # sleep(0.5)
        # self.locator_element(*self.startsectionEle).find_element_by_xpath("//option[@value=" + startsection + "]").click()
        # sleep(0.5)
        # self.locator_element(*self.endsectionEle).find_element_by_xpath("//option[@value=" + endsection + "]").click()
        # sleep(0.5)
        self.locator_element(*self.courseNumEle).send_keys(courseNum)
        self.locator_element(*self.courseCreditEle).send_keys(courseCredit)
        self.locator_element(*self.remarkEle).send_keys(remark)



    # 输入教师公告标题
    def inputTeaNoticeTitleBtn(self):
        self.locator_element(*self.teaNoticeTitleEle).click()

    # 输入教师公告内容
    def inputTeaNoticeContentBtn(self):
        self.locator_element(*self.teaNoticeContentEle).click()

    # 输入学生公告标题
    def inputStuNoticeTitleBtn(self):
        self.locator_element(*self.stuNoticeTitleEle).click()

    # 输入学生公告内容
    def inputStuNoticeContentBtn(self):
        self.locator_element(*self.stuNoticeContentEle).click()

    # 选择发布教师公告的学院分支
    def clickTeaTreeBtn(self):
        self.locator_element(*self.teaTreeEle).click()
        sleep(0.5)
        self.locator_element(*self.teaComputerEle).click()


    # 选择发布学生公告的学院分支
    def clickStuTreeBtn(self):
        self.locator_element(*self.stuTreeEle).click()
        sleep(0.5)
        self.locator_element(*self.stuComputerEle).click()

    # 页面下滑
    def pageDown(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')



    #点击日期选择框
    def clickTimeStartBtn(self):

        self.locator_element(*self.adminActionStartEle).send_keys('2022/3/15 15:25')

    # 点击退出登录选项
    def clickStartTimeBtn(self):
        self.locator_element(*self.adminActionStartEle)



    #退出登录
    avatarEle = (By.ID, eleData.readExcel(27, 3))
    logoffEle = (By.XPATH, eleData.readExcel(28, 3))
    sureLogoffEle = (By.XPATH, eleData.readExcel(29, 3))
    cancelLogoffEle = (By.XPATH, eleData.readExcel(30, 3))
    loginTextEle = (By.XPATH, eleData.readExcel(31, 3))

    #点击小头像按钮
    def clickAvatarBtn(self):
        self.find_element_by_link_text('陶老师').click()
        # self.locator_element(*self.avatarEle).click()

    #点击退出登录选项
    def clickLogoffBtn(self):
        self.locator_element(*self.logoffEle).click()

    #点击确定退出按钮
    def clickSureLogoffBtn(self):
        self.locator_element(*self.sureLogoffEle).click()

    # 点击取消退出按钮
    def clickCancleLogoffBtn(self):
        self.locator_element(*self.cancelLogoffEle).click()
    #获取登录页面文案
    def loginPageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.loginTextEle).text
        return element_text

    #点击选课系统按钮
    def clickChooseCSBtn(self):
        # self.driver.find_element_by_css_selector('#accordionSidebar > li:nth-child(6) > a').click()
        self.locator_element(*self.chooseCSEle).click()
        print("定位成功")

    # 点击新增课程按钮
    def clickCreateCourseTipBtn(self):
        self.locator_element(*self.createCourseEle).click()

    #获取创建课程页面文案
    def createCoursePageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.createCourseText).text
        return element_text

    # 点击创建活动按钮
    def clickAdminCreateActionTipBtn(self):
        self.locator_element(*self.adminCreateActionEle).click()

    #获取创建活动页面文案
    def createActionPageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.adminCreateActionMessageEle).text
        return element_text


    #点击导航栏中的公告通知
    def clickNoticeBtn(self):
        # self.driver.find_element_by_css_selector('#accordionSidebar > li:nth-child(6) > a').click()
        self.locator_element(*self.noticeEle).click()
        print("定位成功")

    # 点击发布新公告按钮
    def clickSendNoticeTipBtn(self):
        self.locator_element(*self.sendNoticeEle).click()

    #获取发布公告页面文案
    def sendNoticePageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.noticePageMessageEle).text
        return element_text
    # 点击向教师发布新公告按钮
    def clickSendNoticeToTeaBtn(self):
        self.locator_element(*self.teaNoticeEle).click()
    # 点击向学生发布新公告按钮
    def clickSendNoticeToStupBtn(self):
        self.locator_element(*self.stuNoticeEle).click()

