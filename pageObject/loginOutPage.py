# -*-coding:utf-8-*-
from time import sleep

from selenium.webdriver.common.by import By
import xlrd

from common.driver import WbDriver
from config.conf import baseUrl
from config.doExcel import ReadExcel
from pageObject.basePage import BasePage, log
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

eleData = ReadExcel() # 存储系统所有的元素数据

homeUrl = baseUrl + "index"

class LoginOutPage(BasePage):
    """退出登录"""
    '''从excel表格中读取元素定位方式'''
    # 公告通知
    avatarEle = (By.XPATH, eleData.readExcel(98, 3))
    logoffEle = (By.XPATH, eleData.readExcel(99, 3))
    loginOutText = (By.XPATH, eleData.readExcel(100, 3))
    sureLogoffEle = (By.XPATH, eleData.readExcel(101, 3))
    cancelLogoffEle = (By.XPATH, eleData.readExcel(102, 3))
    loginTextEle = (By.XPATH, eleData.readExcel(103, 3))


    # 点击头像小标按钮
    def clickAvatareBtn(self):
        self.locator_element(*self.avatarEle).click()
        sleep(1)

    # 点击登出按钮
    # #退出登录
    # def clickExitBtn(self):
    #     self.display('\"ivu-select-dropdown\"')
    #     self.click(*self.exitBtn)
    #

    def clickLoginOuteBtn(self):
        # self.display('\"ivu-select-dropdown\"')
        self.display('\"nav-link dropdown-toggle\"')
        # self.click(*self.exitBtn)
        self.locator_element(*self.logoffEle).click()

    # 获取退出登录文案
    def getLoginOutText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.loginOutText).text
        return element_text

    # 点击确定登出按钮
    def clickSureLoginOutBtn(self):
        self.locator_element(*self.sureLogoffEle).click()


    # 点击取消登出按钮
    def clickCancelLoginOutBtn(self):
        # self.driver.find_element_by_css_selector('#accordionSidebar > li:nth-child(6) > a').click()
        self.locator_element(*self.cancelLogoffEle).click()
        print("定位成功")


    # 获取登录页面文案
    def getLoginPageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.loginTextEle).text
        return element_text
    # 向教师发布公告
    def clickSureBtn(self):
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

    # 输入教师公告标题
    def inputTeaNoticeTitleBtn(self):
        return self.locator_element(*self.teaNoticeTitleEle)

    # 输入教师公告内容
    def inputTeaNoticeContentBtn(self):
         return self.locator_element(*self.teaNoticeContentEle)

    # 填写向教师发布公告信息
    def sendTeaNoticeInfo(self, title, content):
        self.inputTeaNoticeTitleBtn().send_keys(title)

        self.inputTeaNoticeContentBtn().send_keys(content)

    # 输入学生公告标题
    def inputStuNoticeTitleBtn(self):
        return self.locator_element(*self.stuNoticeTitleEle)

    # 输入学生公告内容
    def inputStuNoticeContentBtn(self):
        return self.locator_element(*self.stuNoticeContentEle)

    # 填写向学生发布公告信息
    def sendStuNoticeInfo(self, title, content):
        self.inputStuNoticeTitleBtn().send_keys(title)
        self.inputStuNoticeContentBtn().send_keys(content)


    # 选择发布教师公告的学院分支
    def clickTeaTreeBtn(self):
        self.locator_element(*self.teaTreeEle).click()
        sleep(0.5)
        self.locator_element(*self.teaComputerEle).click()


    # 选择发布学生公告的学院分支
    def clickStuTreeBtn(self):
        # self.locator_element(*self.stuTreeEle).click()
        # sleep(0.5)
        self.locator_element(*self.stuComputerEle).click()

    # 页面下滑
    def pageDown(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    # 点击关闭按钮
    def clickTeaClose(self):
        self.locator_element(*self.cancelSendTeaNoticeEle).click()

    # 点击关闭按钮
    def clickStuClose(self):
        self.locator_element(*self.cancelSendStuNoticeEle).click()

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



if __name__ == '__main__':
    pass