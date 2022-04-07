# -*-coding:utf-8-*-
from time import sleep

from numpy import random
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import xlrd
from selenium.webdriver.common.keys import Keys

from common.driver import WbDriver
from config.conf import baseUrl
from config.doExcel import ReadExcel
from pageObject.basePage import BasePage, log
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

eleData = ReadExcel() # 存储系统所有的元素数据

homeUrl = baseUrl + "index"

class AdminSchoolTreePage(BasePage):
    """学院机构"""
    '''从excel表格中读取元素定位方式'''
    #学院机构
    schoolTreeEle = (By.XPATH, eleData.readExcel(54, 3))
    schoolTreePageTextEle = (By.XPATH, eleData.readExcel(55, 3))
    wanganEle = (By.XPATH, eleData.readExcel(56, 3))
    addTreeEle = (By.XPATH, eleData.readExcel(57, 3))
    editTreeEle = (By.XPATH, eleData.readExcel(58, 3))
    deleteTreeEle = (By.XPATH, eleData.readExcel(59, 3))


    deleteBranchEle = (By.XPATH, eleData.readExcel(60, 3))
    renameBranchEle = (By.XPATH, eleData.readExcel(61, 3))
    inputNameEle = (By.XPATH, eleData.readExcel(62, 3))
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

    # 网安学院分支
    def clickAddWanganBtn(self):
        self.move()
        sleep(0.5)
        self.locator_element(*self.addTreeEle).click()

    # 删除分支
    def clickDeleteTreeBtn(self):
        el = self.locator_element(*self.deleteBranchEle)
        ActionChains(self.driver).move_to_element(el).perform()
        self.locator_element(*self.deleteTreeEle).click()

    # 重命名
    def clickRenameBtn(self):
        el = self.locator_element(*self.renameBranchEle)
        ActionChains(self.driver).move_to_element(el).perform()
        self.locator_element(*self.editTreeEle).click()
        # self.input = self.locator_element(*self.inputNameEle)
        inputValue = self.locator_element(*self.inputNameEle).get_attribute('value')
        print(inputValue)
        for i in range(len(inputValue)):
            self.locator_element(*self.inputNameEle).send_keys(Keys.BACK_SPACE)
            print(i)
        self.locator_element(*self.inputNameEle).send_keys(random.randint(100,5000))
        self.locator_element(*self.inputNameEle).send_keys(Keys.ENTER)

    # 重命名定位
    def renameBtn(self):
        # self.input = self.locator_element(*self.inputNameEle)
        # self.input.clear()
        sleep(0.5)
        self.input.send_keys("chongmingming")
        # print("dianjihuiche")
        # self.input.submit()
        # # self.input.send_keys(Keys.ENTER)
        # sleep(0.5)
        # print("dianjihuiche2")


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