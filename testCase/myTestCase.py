# -*-coding:utf-8-*-
import unittest
from selenium import webdriver
from time import sleep


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 创建web服务
        cls.driver = webdriver.Chrome()  # 注意  这里前边加cls. 使driver可以在类的其他方法中使用
        # 打开浏览器
        cls.driver.get('https://www.baidu.com')
        cls.title = None

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器
        cls.driver.quit()  # 这里使用driver 前边是使用cls.

    def test_01(self):
        input_ = self.driver.find_element('id', "kw")  # 这里使用driver 前边是使用self.
        input_.clear()
        input_.send_keys('自动化学习')
        self.driver.find_element('id', "su").click()
        sleep(3)
        print(self.title)
        # 如果要修改cls.title的值,在全局生效的话,使用 MyTestCase.title （类名.对象）
        MyTestCase.title = self.driver.title
        print(self.title)

    def test_02(self):

        input_ = self.driver.find_element('id', "kw")  # 这里使用driver 前边是使用self.
        input_.clear()
        input_.send_keys('自动化学习2')
        self.driver.find_element('id', "su").click()
        sleep(3)
        print(self.title)
        # 如果要修改cls.title的值,在全局生效的话,使用 MyTestCase.title  （类名.对象）
        MyTestCase.title = self.driver.title
        print(self.title)


if __name__ == '__main__':
    unittest.main()
