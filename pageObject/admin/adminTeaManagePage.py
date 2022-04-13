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

class AdminTeaManagePage(BasePage):
    """教师管理模块"""
    '''从excel表格中读取元素定位方式'''
    # 教师管理
    teaManageEle = (By.XPATH, eleData.readExcel(63, 3))
    teaManaPageTextEle = (By.XPATH, eleData.readExcel(64, 3))
    openTreeEle = (By.XPATH, eleData.readExcel(65, 3))
    computerEle = (By.XPATH, eleData.readExcel(66, 3))
    uploadFileEle = (By.ID, eleData.readExcel(67, 3))

    transportEle = (By.XPATH, eleData.readExcel(68, 3))
    exportPersonEle = (By.XPATH, eleData.readExcel(69, 3))
    downloadFileEle = (By.XPATH, eleData.readExcel(70, 3))

    # 点击教师管理模块按钮
    def clickTeaManageBtn(self):
        self.locator_element(*self.teaManageEle).click()

    # 获取教师管理系统页面文案
    def teaManagePageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.teaManaPageTextEle).text
        return element_text

    # 点击展开树按钮
    def clickOpenTreeBtn(self):
        self.locator_element(*self.openTreeEle).click()

    # 点击计算机学院
    def clickComputerBtn(self):
        return self.locator_element(*self.computerEle).click()

    # def action_click(self):
    #     temp = 1
    #     # report = self._log
    #     element = self.locator_element(*self.uploadFileEle)
    #     while temp < 5:
    #         try:
    #             element = WebDriverWait(self.driver, 5, 1).until(expected_conditions.element_to_be_clickable(*self.uploadFileEle))
    #             # element.click()
    #             ActionChains(self.driver).click(element).perform()
    #         except Exception as e:
    #             sleep(0.5)
    #             temp += 1
    #             # traceback.print_exc()
    #             report.logger.debug(traceback.print_exc())
    #         else:
    #             break
    #         # 尝试5次仍失败，则终止
    #         if temp == 5:
    #             # self.save_screen()
    #             raise Exception("Fail to click")
    #         return element


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


    # # 教师公告小窗文案
    # def sendNoticeToTeaPageText(self):
    #     self.driver.implicitly_wait(10)
    #     element_text = self.locator_element(*self.toTeacherEle).text
    #     return element_text
    #
    # # 学生公告小窗文案
    # def sendNoticeToStuPageText(self):
    #     self.driver.implicitly_wait(10)
    #     element_text = self.locator_element(*self.toStudentEle).text
    #     return element_text
    #
    #
    # # 输入教师公告内容
    # def inputTeaNoticeContentBtn(self):
    #      return self.locator_element(*self.teaNoticeContentEle)
    #
    # # 填写向教师发布公告信息
    # def sendTeaNoticeInfo(self, title, content):
    #     self.inputTeaNoticeTitleBtn().send_keys(title)
    #
    #     self.inputTeaNoticeContentBtn().send_keys(content)
    #
    # # 输入学生公告标题
    # def inputStuNoticeTitleBtn(self):
    #     return self.locator_element(*self.stuNoticeTitleEle)
    #
    # # 输入学生公告内容
    # def inputStuNoticeContentBtn(self):
    #     return self.locator_element(*self.stuNoticeContentEle)
    #
    # # 填写向学生发布公告信息
    # def sendStuNoticeInfo(self, title, content):
    #     self.inputStuNoticeTitleBtn().send_keys(title)
    #     self.inputStuNoticeContentBtn().send_keys(content)
    #
    #
    # # 选择发布教师公告的学院分支
    # def clickTeaTreeBtn(self):
    #     self.locator_element(*self.teaTreeEle).click()
    #     sleep(0.5)
    #     self.locator_element(*self.teaComputerEle).click()
    #
    #
    # # 选择发布学生公告的学院分支
    # def clickStuTreeBtn(self):
    #     # self.locator_element(*self.stuTreeEle).click()
    #     # sleep(0.5)
    #     self.locator_element(*self.stuComputerEle).click()
    # # 点击关闭按钮
    # def clickClose(self):
    #     self.locator_element(*self.cancelSendTeaNoticeEle).click()

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