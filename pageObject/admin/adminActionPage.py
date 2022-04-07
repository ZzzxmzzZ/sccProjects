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

class AdminActionPage(BasePage):
    """创建活动"""
    '''从excel表格中读取元素定位方式'''
    chooseCSEle = (By.XPATH, eleData.readExcel(6, 3))
    #创建活动
    adminCreateActionEle = (By.XPATH, eleData.readExcel(22, 3))
    adminCreateActionMessageEle = (By.XPATH, eleData.readExcel(23, 3))
    adminActionStartEle = (By.XPATH, eleData.readExcel(24, 3))
    adminActionEndEle = (By.XPATH, eleData.readExcel(25, 3))
    adminActionChooseEle = (By.XPATH, eleData.readExcel(26, 3))
    actionNameEle = (By.XPATH, eleData.readExcel(27, 3))
    actionClassroomEle = (By.XPATH, eleData.readExcel(28, 3))
    actionNumEle = (By.XPATH, eleData.readExcel(29, 3))
    actionCreditsEle = (By.XPATH, eleData.readExcel(30, 3))
    actionRemarks = (By.XPATH, eleData.readExcel(31, 3))
    actionCreatBtnEle = (By.XPATH, eleData.readExcel(32, 3))

    # 点击创建活动按钮
    def clickAdminCreateActionTipBtn(self):
        self.locator_element(*self.adminCreateActionEle).click()

    #获取创建活动页面文案
    def createActionPageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.adminCreateActionMessageEle).text
        return element_text

    #点击活动开始日期选择框
    def clickTimeStartBtn(self,startTime):
        # selectStartTime = Select(self.locator_element(*self.adminActionStartEle))  # select标签
        # selectStartTime.click()
        # #获得选项
        # # 1.根据值来选择
        # year = selectStartTime.select_by_xpth("//select[@name='year']")
        # year.select_by_value(str(2023))
        #
        # month = selectStartTime.select_by_xpth("//select[@name='month']")
        # year.select_by_value(str(3))
        #去掉日期控件中的readonly，使得可以以send_keys的方式传入时间
        # js = "$('input[id=actionDateLocal]').attr('readonly','')"
        # self.executeScript(js)
        # self.locator_element(*self.adminActionStartEle).send_keys(startTime)
        self.locator_element(*self.adminActionStartEle).send_keys(startTime)

        # input_datetime = driver.find_element_by_xpath('/html/body/div[1]/form/fieldset/div/div[1]/input[1]')
        # input_datetime.send_keys("2017-09-21")
        # input_datetime.click()
        # time.sleep(5)
    #点击活动结束日期选择框
    def clickTimeEndBtn(self,endTime):
        #去掉日期控件中的readonly，使得可以以send_keys的方式传入时间
        # js = "$('input[id=stopDateLocal]').attr('readonly','')"
        # self.executeScript(js)
        # self.locator_element(*self.adminActionEndEle).send_keys(endTime)
        self.locator_element(*self.adminActionEndEle).send_keys(endTime)


    #点击活动开放选择日期选择框
    def clickTimeChooseBtn(self,chooseTime):

        # #去掉日期控件中的readonly，使得可以以send_keys的方式传入时间
        # js = "$('input[id=selectedTime]').attr('readonly','')"
        # self.executeScript(js)
        # self.locator_element(*self.adminActionChooseEle).send_keys(chooseTime)
        self.locator_element(*self.adminActionChooseEle).send_keys(chooseTime)


    # 填写活动信息
    def createActionInfo(self, actionName, classroom, startTime, endTime,chooseTime,number,credit,remarks):
        self.locator_element(*self.actionNameEle).send_keys(actionName)
        self.locator_element(*self.actionClassroomEle).send_keys(classroom)
        self.clickTimeStartBtn(startTime)
        sleep(0.8)
        self.clickTimeEndBtn(endTime)
        sleep(0.8)
        self.locator_element(*self.actionNumEle).send_keys(number)
        self.locator_element(*self.actionCreditsEle).send_keys(credit)
        self.locator_element(*self.actionRemarks).send_keys(remarks)
        self.pageDown()
        sleep(0.5)
        self.clickTimeChooseBtn(chooseTime)
        sleep(0.8)



    # 点击创建活动按钮
    def clickCreateActionBtn(self):
        # self.driver.find_element_by_css_selector('#accordionSidebar > li:nth-child(6) > a').click()
        self.locator_element(*self.actionCreatBtnEle).click()
        print("定位创建活动成功")

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



#页面下滑
    def pageDown(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')




if __name__ == '__main__':
    pass