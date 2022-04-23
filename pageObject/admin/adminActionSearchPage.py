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

class AdminActionSearchPage(BasePage):
    """管理员查询课程"""
    '''从excel表格中读取元素定位方式'''
    chooseCSEle = (By.XPATH, eleData.readExcel(6, 3))


    #管理员查询活动
    searchActionEle = (By.XPATH, eleData.readExcel(84, 3))
    historyActionTextEle = (By.XPATH, eleData.readExcel(85, 3))
    keyActionNameEle = (By.XPATH, eleData.readExcel(86, 3))
    searchBtnEle = (By.XPATH, eleData.readExcel(87, 3))
    actionTableEle = (By.XPATH, eleData.readExcel(88, 3))

    #点击选课系统按钮
    def clickChooseCSBtn(self):
        # self.driver.find_element_by_css_selector('#accordionSidebar > li:nth-child(6) > a').click()
        self.locator_element(*self.chooseCSEle).click()
        print("定位成功")
    # 活动记录按钮
    def clickSearchCourseTipBtn_admin(self):
        self.locator_element(*self.searchActionEle).click()


    # 获取查询活动页面文案
    def historyActionPageText(self):
        self.driver.implicitly_wait(10)
        element_text = self.locator_element(*self.historyActionTextEle).text
        return element_text

    #查询活动名关键字
    def searchActionNameKeyword(self):
        inputValue = "学"
        self.locator_element(*self.keyActionNameEle).send_keys(inputValue)
        print("输入成功")
        # return inputValue

    # 点击查询按钮
    def clickSearchBtn(self):
        self.locator_element(*self.searchBtnEle).click()

    # 获取查询前的行数
    def beforeSearchCourseList(self):
        pax = []
        att = []
        # 定位到table，并获得table中所有得tr元素
        course_table = self.locator_element(*self.actionTableEle)
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

    #从数据库中获取数据
    def getActionNameFromSql(self):
        sql = "select activity_name from sys_activities where activity_name like '%学%';"
        # sql = "select activity_name from sys_activities where activity_name like '%s'" % selectName
        res = Mysql().sql(sql)
        print("数据库：",res)
        # 数据库： (('jvm原理',), ('Java EE',))
        print("元组1：",res[0][0])
        # 元组1： jvm原理
        print("元组2：", res[1][0])
        # 元组2： Java EE
        print("数据库中返回值的长度：",len(res))
        return len(res)


    # 获取活动名列的值
    def getActionNameValue(self):
        pax = []
        att = []
        number = 0
        inputValue = "学"
        print("查询后行数：")

        # 定位到table，并获得table中所有得tr元素
        course_table = self.locator_element(*self.actionTableEle)
        # 通过标签名获取表格的所有行
        table_tr_list = course_table.find_elements_by_tag_name('tr')

        #  按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
        for tr in table_tr_list:
            att = (tr.text).split(" ")
            pax.append(att)
        print(pax)

        # 循环列表中的元素列表
        for i in range(1,len(pax)):
            # 获取每个元素列表中的第二个元素
            ta = pax[i][2]

            # 判断关键字是否在该字段里边
            if inputValue in ta:
                number = number + 1


            print("搜索结果：", i, ta)
            # 搜索结果： 1 Java
            # 搜索结果： 2 jvm原理
        print("数字：",number)
        # 数字： 2
        return number

        # 判断数据库中取到的值是否跟页面显示的值一样
    def isSearchCorrect(self):
        if self.getActionNameFromSql() == self.getActionNameValue():
            return True
        else:
            return False

        # # python 得len()函数返回对象（字符、列表、元组）得长度或者元素得个数
        #
        # numbers = len(rows)
        #
        # print(type(numbers))  # 打印类型，输入为int
        # print(numbers)  # 打印行数
        #
        # courseInfo_list = []  # 定义数组来存取遍历得到的应用名称值
        # for i in range(numbers):
        # # i 默认从0开始，而定位元素是从1开始，所以需i+1
        # # i 是int类型，元素定位中的tr[i] 是string 类型，所以需进行类型转换
        # # 使用str()将int转换为String
        # # 此元素定位是获取表格中的应用名称的值，需注意后面的text
        #     course_names = \
        #     #获取某一列数据
        #     # self.driver.find_elements_by_xpath('//table[@class="el-table__body"][1]//tr[' + str(i + 1) + ']//td[3]//div')[0].text
        #     #获取某一行数据
        #     self.driver.find_elements_by_xpath('//*[@id="mytab"]/tbody/tr/td[3]')[0].text
        #     courseInfo_list.append(course_names)  # 遍历一次，就加入数组中
        # print(courseInfo_list)  # 打印出遍历完成的数组



#页面下滑
    def pageDown(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')




if __name__ == '__main__':
    pass