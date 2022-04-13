# -*- coding: utf-8 -*-
import unittest
from functools import wraps
from time import sleep

from common.driver import WbDriver
from pageObject.loginPage import LoginPage
from common.log import Logger

log = Logger(__name__)


def skip_dependon(depend=""):
    """
    :param depend: 依赖的用例函数名，默认为空
    :return: wraper_func
    """
    def wraper_func(test_func):
        @wraps(test_func)  # @wraps：避免被装饰函数自身的信息丢失
        def inner_func(self):
            if depend == test_func.__name__:
                raise ValueError("{} cannot depend on itself".format(depend))
            # print("self._outcome", self._outcome.__dict__)
            # 此方法适用于python3.4 +
            # 如果是低版本的python3，请将self._outcome.result修改为self._outcomeForDoCleanups
            # 如果你是python2版本，请将self._outcome.result修改为self._resultForDoCleanups
            failures = str([fail[0] for fail in self._outcome.result.failures])
            errors = str([error[0] for error in self._outcome.result.errors])
            # skipped = str([error[0] for error in self._outcome.result.skipped])
            flag = (depend in failures) or (depend in errors)
            if failures.find(depend) != -1:
                # 输出结果 [<__main__.TestDemo testMethod=test_login>]
                # 如果依赖的用例名在failures中，则判定为失败，以下两种情况同理
                # find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回 - 1
                test = unittest.skipIf(flag, "{} failed".format(depend))(test_func)
            elif errors.find(depend) != -1:
                test = unittest.skipIf(flag, "{} error".format(depend))(test_func)
            # elif skipped.find(depend) != -1:
            #     test = unittest.skipIf(flag, "{} skipped".format(depend))(test_func)
            else:
                test = test_func
            return test(self)
        return inner_func
    return wraper_func

class MyUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #只打开一次浏览器
        # cls.driver = WbDriver().firefox()
        print("执行了setupclass1")
        cls.driver = WbDriver().chrome()
        print("执行了setupclass2")
        log.logger.info('打开浏览器')
        print("执行了setupclass3")


    # def setUp(self) :
    #     self.login = LoginPage(self.driver)
    #     self.login.open()
    #     self.mock_stuLogin()
    #     report.logger.info('************************ 开始执行测试用例 ************************')

    def setUp(self) :
        print("执行了setup")
        self.login = LoginPage(self.driver)
        log.logger.info('************************ 开始执行测试用例 ************************')

    def tearDown(self) :
        sleep(0.7)
        log.logger.info('************************ 测试用例执行结束 ************************')
        # self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls) :
        cls.driver.delete_all_cookies()
        cls.driver.quit()
        log.logger.info('退出浏览器')

class StuUnittest(MyUnittest):
    @classmethod
    def setUpClass(cls):
        #只打开一次浏览器
        # cls.driver = WbDriver().firefox()
        cls.driver = WbDriver().chrome()
        log.logger.info('打开浏览器')
        login = LoginPage(cls.driver)
        login.mock_stuLogin()

class TeaUnittest(MyUnittest):
    @classmethod
    def setUpClass(cls):
        #只打开一次浏览器
        # cls.driver = WbDriver().firefox()
        cls.driver = WbDriver().chrome()
        log.logger.info('打开浏览器')
        login = LoginPage(cls.driver)
        login.mock_teaLogin()

    def getUrl(self):
        currUrl = self.driver.current_url  # 获取当前的url地址
        return currUrl

    # 页面下滑
    def pageDown(self):
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')


class AdminUnittest(MyUnittest):
    @classmethod
    def setUpClass(cls):
        #只打开一次浏览器
        # cls.driver = WbDriver().firefox()
        cls.driver = WbDriver().chrome()
        log.logger.info('打开浏览器')
        login = LoginPage(cls.driver)
        login.mock_adminLogin()

    def getUrl(self):
        currUrl = self.driver.current_url  # 获取当前的url地址
        return currUrl


    #页面下滑
    def pageDown(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')


if __name__ == '__main__':
    unittest.main()