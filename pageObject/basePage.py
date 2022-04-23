#coding:utf-8
import os
import time

from selenium import webdriver
from time import sleep
from common.log import Logger
from config.conf import baseUrl, conf, proPath

log = Logger(__name__)
testUrl = baseUrl + "login"

#定义页面的基础类，所有的页面都需要继承这个基础类
class BasePage(object):

    #初始化基础类
    def __init__(self,driver,url=testUrl):
        self.driver=driver
        self.url=url

    #启动浏览器，访问指定页面
    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    #定位元素
    def locator_element(self,*locator):
        el = self.driver.find_element(*locator)
        return el

    #浏览器退出
    def quit(self):
        sleep(2)
        self.driver.quit()

    def getUrl(self):
        currUrl = self.driver.current_url  # 获取当前的url地址
        return currUrl

    #截图
    def screenShot(self,fileName):
        # timeAndName = now + fileName
        path = os.path.join(r'D:\Software\PycharmProjects\sccProjects\img', fileName)
        self.driver.get_screenshot_as_file(path)



    #页面下滑
    def pageDown(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')


    #执行js代码
    def executeScript(self,js):
        self.driver.execute_script(js)


    #把display:none显示出来
    def display(self,className):

        # js = 'document.getElementsByClassName({})[0].style.display="block"'.format(str(className))
        js = 'document.querySelector("#userDropdown")'.format(str(className))
        #js = 'document.getElementsByClassName(\"ivu-select-dropdown\")[0].style.display="block";'
        self.executeScript(js)
        print("成功将隐藏元素回显")
        # report.logger.info("成功将隐藏元素回显")
    #
    #
    # #鼠标悬停导航
    # def move(self):
    #     el = self.findElement(*self.menuEle)
    #     ActionChains(self.driver).move_to_element(el).perform()