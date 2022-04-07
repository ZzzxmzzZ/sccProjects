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

class AdminNoticePage(BasePage):
    """公告通知"""
    '''从excel表格中读取元素定位方式'''
    # 公告通知
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

    # 点击确定发布公告按钮
    def clickSureSendTeaNoticeBtn(self):
        self.locator_element(*self.sureSendTeaNoticeEle).click()

    # 点击确定发布公告按钮
    def clickSureSendStuNoticeBtn(self):
        self.locator_element(*self.sureSendStuNoticeEle).click()

    # 点发布新公告按钮
    def clickSendNoticeTipBtn(self):
        self.locator_element(*self.sendNoticeEle).click()


    # 点击公告通知按钮
    def clickNoticeBtn(self):
        # self.driver.find_element_by_css_selector('#accordionSidebar > li:nth-child(6) > a').click()
        self.locator_element(*self.noticeEle).click()
        print("定位成功")


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