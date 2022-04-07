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

class TeaCoursePage(BasePage):
    """账号，密码，登录按钮，错误提示，登录成功提示"""
    '''从excel表格中读取元素定位方式'''
    chooseCSEle = (By.XPATH, eleData.readExcel(6, 3))
    createCourseTipEle = (By.XPATH, eleData.readExcel(7, 3))

    createCourseText = (By.XPATH, eleData.readExcel(8, 3))
    courseNameEle = (By.XPATH, eleData.readExcel(9, 3))
    classroomEle = (By.XPATH, eleData.readExcel(10, 3))
    startweekEle = (By.ID, eleData.readExcel(11, 3))
    endweekEle = (By.ID, eleData.readExcel(12, 3))
    dayEle = (By.ID, eleData.readExcel(13, 3))
    startsectionEle = (By.ID, eleData.readExcel(14, 3))
    endsectionEle = (By.ID, eleData.readExcel(15, 3))
    courseNumEle = (By.XPATH, eleData.readExcel(16, 3))
    courseCreditEle = (By.XPATH, eleData.readExcel(17, 3))
    remarkEle = (By.XPATH, eleData.readExcel(18, 3))
    academyEle = (By.XPATH, eleData.readExcel(19, 3))
    fenzhiEle = (By.XPATH, eleData.readExcel(20, 3))
    creatCourseBtn = (By.XPATH, eleData.readExcel(21, 3))
    # print(endweekEle)


    # 填写课程信息
    def createCourseInfo(self, courseName, classroom, startweek, endweek,day,startsection,endsection,courseNum, courseCredit, remark):
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


    def academyChoose(self):
        self.locator_element(*self.academyEle).click()
        sleep(0.5)
        self.locator_element(*self.fenzhiEle).click()





    # 点击创建课程按钮
    def clickCreateCourseBtn(self):
        # self.driver.find_element_by_css_selector('#accordionSidebar > li:nth-child(6) > a').click()
        self.locator_element(*self.creatCourseBtn).click()
        print("定位成功")

    #系统弹窗
    def alertInfo(self):
        # wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        message = alert.text
        alert.accept()
        return message
    #点击选课系统按钮
    def clickChooseCSBtn(self):
        # self.driver.find_element_by_css_selector('#accordionSidebar > li:nth-child(6) > a').click()
        self.locator_element(*self.chooseCSEle).click()
        print("定位成功")

    # 点击新增课程标签
    def clickCreateCourseTipBtn(self):
        self.locator_element(*self.createCourseTipEle).click()

    def createCoursePageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.createCourseText).text
        return element_text

#页面下滑
    def pageDown(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')




if __name__ == '__main__':
    pass