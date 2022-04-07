# -*-coding:utf-8-*-
import traceback
from time import sleep

import win32con
import win32gui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import xlrd

from common.driver import WbDriver
from config.conf import baseUrl
from config.doExcel import ReadExcel
from pageObject.basePage import BasePage, log
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

eleData = ReadExcel() # 存储系统所有的元素数据

homeUrl = baseUrl + "index"

class AdminStuManagePage(BasePage):
    """学生管理模块"""
    '''从excel表格中读取元素定位方式'''
    # 教师管理
    stuManageEle = (By.XPATH, eleData.readExcel(71, 3))
    stuManaPageTextEle = (By.XPATH, eleData.readExcel(72, 3))
    computerEle = (By.XPATH, eleData.readExcel(73, 3))
    uploadFileEle = (By.XPATH, eleData.readExcel(74, 3))
    transportEle = (By.ID, eleData.readExcel(75, 3))

    exportPersonEle = (By.XPATH, eleData.readExcel(76, 3))
    downloadFileEle = (By.XPATH, eleData.readExcel(77, 3))

    # 点击学生管理模块按钮
    def clickStuManageBtn(self):
        self.locator_element(*self.stuManageEle).click()

    # 获取学生管理系统页面文案
    def stuManagePageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.stuManaPageTextEle).text
        return element_text


    # 点击计算机学院
    def clickComputerBtn(self):
        return self.locator_element(*self.computerEle).click()


    # 点击上传文件按钮
    def clickUploadFileBtn(self, file_path):
        # self.driver.find_element_by_css_selector('#accordionSidebar > li:nth-child(6) > a').click()
        # upload = self.locator_element(*self.uploadFileEle)
        # ActionChains(self.driver).click(upload).perform()
        upload = self.locator_element(*self.uploadFileEle)
        sleep(1)
        upload.send_keys(file_path)  # send_keys
        print(upload.get_attribute('value')) # check value
        print("点击上传文件成功")
        # upload = driver.find_element_by_id('file')
        # time.sleep(12)
        # upload.send_keys('d:\\all_money.wmv')  # send_keys
        # print(upload.get_attribute('value'))
        # browser_type = {
        #     "firefox": "文件上传",
        #     "chrome": "打开",
        #     "ie": "选择要加载的文件"
        # }

        # # 一级顶层窗口，此处title为上传窗口名称，浏览器不一样上传窗口名称不一样
        # print(file_path)
        # dialog = win32gui.FindWindow("#32770", u"打开“")
        # # 二级窗口
        # ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        # # 三级窗口
        # comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
        # # 四级窗口
        # edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)
        # button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
        # # 执行操作 输入文件路径
        # win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
        # sleep(1)
        # # 点击打开上传文件
        # win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        # print("上传文件成功")

    # 点击计算机学院
    def clickTransportBtn(self):
        return self.locator_element(*self.transportEle).click()




    # 页面下滑
    def pageDown(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')


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