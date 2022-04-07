# -*-coding:utf-8-*-
from time import sleep

from selenium.webdriver.common.by import By
import xlrd

from common.driver import WbDriver
from common.mysql import Mysql
from config.conf import baseUrl
from config.doExcel import ReadExcel
from pageObject.basePage import BasePage, log
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

eleData = ReadExcel() # 存储系统所有的元素数据

homeUrl = baseUrl + "index"

class AdminCourseAuditPage(BasePage):
    """管理员查询课程"""
    '''从excel表格中读取元素定位方式'''
    chooseCSEle = (By.XPATH, eleData.readExcel(6, 3))


    #管理员查询课程
    adminSearchCourseEle = (By.XPATH, eleData.readExcel(78, 3))
    historyCourseTextEle = (By.XPATH, eleData.readExcel(79, 3))
    firstRowEle = (By.XPATH, eleData.readExcel(90, 3))
    auditCourseEle = (By.XPATH, eleData.readExcel(91, 3))
    auditTextEle = (By.XPATH, eleData.readExcel(92, 3))
    sureAuditEle = (By.XPATH, eleData.readExcel(93, 3))
    cancelAuditEle = (By.XPATH, eleData.readExcel(94, 3))
    startChooseTimeEle = (By.XPATH, eleData.readExcel(95, 3))
    endChooseTimeEle = (By.XPATH, eleData.readExcel(96, 3))
    firstRowCourseNameEle = (By.XPATH, eleData.readExcel(97, 3))

    #点击选课系统按钮
    def clickChooseCSBtn(self):
        # self.driver.find_element_by_css_selector('#accordionSidebar > li:nth-child(6) > a').click()
        self.locator_element(*self.chooseCSEle).click()
        print("定位成功")
    # 查询课程按钮
    def clickSearchCourseTipBtn_admin(self):
        self.locator_element(*self.adminSearchCourseEle).click()


    # 获取查询课程页面文案
    def historyCoursePageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.historyCourseTextEle).text
        return element_text

    # 点击第一行课程信息按钮
    def clickFirstRow(self):
        self.locator_element(*self.firstRowEle).click()
    # 获取第一行的课程名
    def firstCourseName(self):
        # self.driver.find_element_by_xpath('//*[@id="mytab"]')
        element_text = self.locator_element(*self.firstRowCourseNameEle).text
        return element_text

    # 点击审核课程按钮
    def clickAuditBtn(self):
        self.locator_element(*self.auditCourseEle).click()

    # 获取审核课程页面文案
    def auditCourseText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.auditTextEle).text
        return element_text

    #点击选课开始时间选择框
    def clickTimeStartBtn(self,startTime):
        self.locator_element(*self.startChooseTimeEle).send_keys(startTime)

    #点击选课结束时间选择框
    def clickTimeEndBtn(self,endTime):
        self.locator_element(*self.endChooseTimeEle).send_keys(endTime)


    # 点击确定按钮
    def clickSureBtn(self):
        self.locator_element(*self.sureAuditEle).click()
    # 点击取消按钮
    def clickCancelBtn(self):
        self.locator_element(*self.cancelAuditEle).click()

    #系统弹窗
    def alertInfo(self):
        # wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        message = alert.text
        alert.accept()
        return message




    # 获取查询前的行数
    def beforeSearchCourseList(self):
        pax = []
        att = []
        # 定位到table，并获得table中所有得tr元素
        course_table = self.locator_element(*self.courseTableEle)
        # 通过标签名获取表格的所有行
        table_tr_list = course_table.find_elements_by_tag_name('tr')

        # python 得len()函数返回对象（字符、列表、元组）得长度或者元素得个数
        for tr in table_tr_list:
            att = (tr.text).split(" ")
            pax.append(att)

        print(pax)
        numbers = len(table_tr_list)
        print(table_tr_list)

        print(type(numbers))  # 打印类型，输入为int
        print(numbers)  # 打印行数
        return numbers

    #从数据库中获取审核前的第一行数据的id
    def getFirstRowCourseIDFromSql(self,firstCourseName):
        sql = "select course_id from sys_course where course_name = '" + firstCourseName + "' order by course_id desc limit 1"
        res = Mysql().sql(sql)
        print("数据库：",res)
        # 数据库： (('jvm原理',), ('Java EE',))
        print("id：",res[0][0])
        # 元组1： jvm原理
        print(type(res[0][0]))
        #
        return res[0][0]

    #从数据库中获取数据
    def getCourseNameFromSql(self,courseID):
        sql = 'select status from sys_course where course_id = %s'
        res = Mysql().sql2(sql,courseID)
        print("数据库：",res)
        # 数据库： (('jvm原理',), ('Java EE',))
        print("元组1：",res[0][0])
        print(type(res[0][0]))
        # 元组1： jvm原理

        return res[0][0]



if __name__ == '__main__':
    pass