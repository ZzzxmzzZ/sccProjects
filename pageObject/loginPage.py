# -*-coding:utf-8-*-
from time import sleep

from selenium.webdriver.common.by import By
import xlrd
from config.conf import baseUrl
from config.doExcel import ReadExcel
from pageObject.basePage import BasePage, log

eleData = ReadExcel() # 存储系统所有的元素数据

homeUrl = baseUrl + "index"

class LoginPage(BasePage):
    """账号，密码，登录按钮，错误提示，登录成功提示"""
    '''从excel表格中读取元素定位方式'''
    userIdEle = (By.ID, eleData.readExcel(1, 3))
    passWordEle = (By.ID, eleData.readExcel(2, 3))
    loginBtnEle = (By.XPATH, eleData.readExcel(3, 3))
    errorMessage = (By.XPATH, eleData.readExcel(4, 3))
    welcomeText = (By.XPATH, eleData.readExcel(5, 3))
    # xiala = (By.ID, eleData.readExcel(6, 3))
    # tuichu = (By.XPATH, eleData.readExcel(7, 3))
    # tuiquedinganniu = (By.XPATH, eleData.readExcel(8, 3))


    # #获取登录成功欢迎词
    # def getWelcomeText(self):
    #     text = self.getVal(*self.welcomeText)
    #     return text
    #
    # # 获取登录失败时提示
    # def getFailedText(self):
    #     try:
    #         info = self.getVal(*self.errorMessage)
    #     except Exception as e:
    #         report.logger.info("无登录失败提示信息")
    #         raise e
    #     else:
    #         return info

    # 统一登录函数
    def loginFunc(self, userId='admin', password='123456'):
        self.locator_element(*self.userIdEle).send_keys(userId)
        self.locator_element(*self.passWordEle).send_keys(password)
        sleep(0.3)
        self.clickLoginBtn()
        sleep(0.5)
    # def loginFunc(self, userId='admin', password='123456'):
    #     self.input(self.userIdEle, userId)
    #     self.input(self.passWordEle, password)
    #     sleep(0.3)
    #     self.clickLoginBtn()
    #     sleep(0.5)
    # 点击登录按钮
    def clickLoginBtn(self):
        self.locator_element(*self.loginBtnEle).click()

    # 获取元素文本内容进行断言
    def assert_by_text(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.welcomeText).text
        return element_text

    #获取登录成功信息
    def isLoginSucceed(self):
        message = self.assert_by_text()
        try:
            assert '个人信息' in message
        except Exception as e:
            print("用户登录失败")
            raise e
        else:
            print("用户登录成功")


    # 获取登录失败时提示
    def getFailedText(self):
        try:
            self.driver.implicitly_wait(10)
            element_text = self.locator_element(*self.errorMessage).text
            # info = self.getVal(*self.errorMessage)
        except Exception as e:
            print("无登录失败提示信息")
            # report.logger.info("无登录失败提示信息")
            raise e
        else:
            return element_text

    # #断言欢迎词是否包含用户名
    # def isUserNameInWelcomeText(self,userName):
    #     message = self.getWelcomeText()
    #     try:
    #         assert userName in message
    #     except Exception as e:
    #         report.logger.info('用户：%s 登录失败' % userName)
    #         raise e
    #     else:
    #         report.logger.info("用户：%s 登录成功" % userName)

    def stuLogin(self,userId='admin', password='123456'):
        self.loginFunc(userId, password)
        self.isLoginSucceed()
    # def clickXialaBtn(self):
    #     self.click(*self.xiala)
    #
    #
    # def clickTuichuBtn(self):
    #     self.click(*self.tuichu)
    # def queding(self):
    #     self.click(*self.tuiquedinganniu)
    def adminLogin(self,userId='admin', password='123456'):
        self.loginFunc(userId, password)
        self.isLoginSucceed()



    def teaLogin(self,userId='2013007', password='0',userName='敖欣'):
        self.loginFunc(userId, password)
        self.isUserNameInWelcomeText(userName)

    def mock_stuLogin(self, userId='201741414235', pwd ='123456'):
        self.open()
        self.loginFunc(userId, pwd)
        sleep(0.8)
        while self.driver.current_url != homeUrl:
            log.logger.info("重新登录")
            self.loginFunc(userId, pwd)
            sleep(0.8)
        self.isLoginSucceed()
    #
    def mock_teaLogin(self, userId='21231231', pwd ='123456'):
        self.open()
        self.loginFunc(userId, pwd)
        sleep(0.8)
        while self.driver.current_url != homeUrl:
            log.logger.info("重新登录")
            self.loginFunc(userId, pwd)
            sleep(0.8)
        self.isLoginSucceed()
    #
    def mock_adminLogin(self, userId='admin', pwd ='123456'):
        self.open()
        self.loginFunc(userId, pwd)
        sleep(0.8)
        while self.driver.current_url != homeUrl:
            log.logger.info("重新登录")
            self.loginFunc(userId, pwd)
            sleep(0.8)
        self.isLoginSucceed()


    #
    # def retryingLogin(self,userId,pwd,userName,testUrl,homeUrl):
    #     self.open(testUrl)
    #     self.loginFunc(userId, pwd)
    #     sleep(0.5)
    #     while self.driver.current_url != homeUrl:
    #         report.logger.info("重新登录")
    #         self.loginFunc(userId, pwd)
    #     self.isUserNameInWelcomeText(userName)

if __name__ == '__main__':
    pass