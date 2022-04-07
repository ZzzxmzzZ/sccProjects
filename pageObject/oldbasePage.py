# -*-coding:utf-8-*-

#本地部署
import base64
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.log import Logger
from config.conf import baseUrl, conf

log = Logger(__name__)



'''

HTML_IMG_TEMPLATE = """
    <a href="data:image/png;base64, {}">
    <img src="data:image/png;base64, {}" max-width=40% height=40%/>
    </a>
    <br></br>
"""
'''
testUrl = baseUrl + "login"


def open_browser(name, url):
    if name == 'chrome':
        # 设置下载路径
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

    if name == 'ff':
        driver = webdriver.Firefox()

    if name == 'ie':
        driver = webdriver.IE()
    driver.maximize_window()
    driver.get(url)
    return driver


class BasePage(object):

#本地部署
    def __init__(self, driver, url=testUrl):
        self.driver = open_browser(driver
        self.url = url
    '''
    def _open(self,url):
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            self.driver.refresh()
            print("输入了url")
        except Exception as e:
            # log.logger.exception(e, exc_info=True)
            raise ValueError('登入 %s 失败，请检查！' % url)
        else:
            log.logger.info('成功进入%s ' % url)
            self.driver.maximize_window()

    def open(self,url = testUrl):
        self._open(url)
        # log.logger.info('%s 加载成功!' % url)
        return self.driver

    '''
    #执行js代码
    def executeScript(self,js):
        self.driver.execute_script(js)

    #把display:none显示出来
    def display(self,className):
        js = 'document.getElementsByClassName({})[0].style.display="block"'.format(str(className))
        #js = 'document.getElementsByClassName(\"ivu-select-dropdown\")[0].style.display="block";'
        self.executeScript(js)
        log.logger.info("成功将隐藏元素回显")

    def findElement(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            log.logger.exception('元素定位超时：%s' % (loc,) ,exc_info=True)
            raise e
        else:
            # log.logger.info('成功定位元素：%s' % (loc,))
            return self.driver.find_element(*loc)

    def findElements(self,*loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            log.logger.exception('元素组定位超时：%s' % (loc,), exc_info=True)
            raise e
        else:
            # log.logger.info('成功定位元素组： %s' % (loc,))
            return self.driver.find_elements(*loc)

    def click(self,*loc):
        text = self.getVal(*loc)
        try:
            el = self.findElement(*loc)
            el.click()
        except Exception as e:
            log.logger.info('未成功点击%s' % text)
            raise e
        else:
            log.logger.info('点击%s' % text)
            # self.driver.implicitly_wait(10)

    def input(self, loc, val):
        el = self.findElement(*loc)
        # 清空输入框中的值，并输入需要搜索的值
        try:
            el.clear()
            el.send_keys(val)
        except Exception as e:
            log.logger.exception('键入值错误!', exc_info=True)
            raise e
        else:
            log.logger.info('输入 [%s]' % val)
   #上传文件
    # def uploadFile(self, browser: str, file: str):
    #     browser_type = {
    #         "firefox": "文件上传",
    #         "chrome": "打开",
    #         "ie": "选择要加载的文件"
    #     }
    #     sleep(2)
    #     dialog = win32gui.FindWindow("#32770", browser_type[browser])  # 火狐浏览器为”文件上传“，谷歌为”打开“
    #     combobox_ex32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
    #     combobox = win32gui.FindWindowEx(combobox_ex32, 0, 'ComboBox', None)
    #     edit = win32gui.FindWindowEx(combobox, 0, 'Edit', None)
    #     button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
    #     win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file)
    #     win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
    #
    #     log.logger.info("文件上传完毕")

    def getVal(self, *loc):
        element = self.findElement(*loc)
        try:
            value = element.text
        except Exception:
            value = element.get_attribute('value')
            # log.logger.info('获取元素 [%s] 的值 [%s] 失败' % (loc, value))
            return value
        except:
            log.logger.exception('获取元素 [%s] 的值 [%s] 失败', exc_info=True)
            raise Exception
        else:
            # log.logger.info('获取元素 [%s] 的值 [%s]' % (loc,value))
            return value

    def getVals(self,*loc):
        val_list = []
        try:
            for element in self.findElements(*loc):
                value = element.text
                val_list.append(value)
        except Exception as e:
            log.logger.exception('获取失败', exc_info=True)
            raise e
        else:
            # log.logger.info('获取元素组 [%s] 的值 [%s]' % (loc, val_list))
            return val_list

    def getValue(self,*loc):
        list =[]
        try:
            list.append(self.findElement(*loc).text)
        except Exception as e:
            try:
                for element in self.findElements(*loc):
                    value = element.text
                    list.append(value)
            except:
                log.logger.exception('获取失败', exc_info=True)
                raise e
            else:
                return list
        else:
            # log.logger.info('获取元素组 [%s] 的值 [%s]' % (loc, val_list))
            return list


    def isElementExist(self,element):
        try:
            # WebDriverWait(driver, 超时时长, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(element))
        except:
            return False
        else:
            return True

    # 清空输入框数据
    def clearValue(self, element):
        empty = self.findElement(*element)
        empty.clear()

    def judgeType(self,testObj):
        if isinstance(testObj, str):  # 判断是否为字符串类型
            print("It's str.")
        elif isinstance(testObj, list):  # 判断是否为列表
            print("It's list.")
        elif isinstance(testObj, tuple):  # 判断是否为元组
            print("It's tuple.")
        elif isinstance(testObj, dict):  # 判断是否为字典
            print("It's dict.")
        elif isinstance(testObj, set):  # 判断是否为集合
            print("It's set.")
        elif isinstance(testObj, int):  # 判断是否为整型数字
            print("It's int.")
        elif isinstance(testObj, float):  # 判断是否为浮点型数字
            print("It's float.")

    def getUrl(self):
        currUrl = self.driver.current_url  # 获取当前的url地址
        return currUrl

    def endToEle(self,*loc):
        script = "return arguments[0].scrollIntoView();"
        element = self.findElement(*loc)
        self.driver.execute_script(script, element)

    #向下翻页
    def pageDown(self,*loc):
        # a = self.findElement(*loc)
        # ActionChains(self.driver).key_down(Keys.CONTROL).perform()
        # a.click()
        # self.click(*loc)
        t = self.findElement(*loc)
        t.send_keys(Keys.PAGE_DOWN)
        log.logger.info("页面下滑成功")

    # def getClippedImageFromCanvas(self, browser, canvas, x, y, w, h):
    #    
    #     data = self.execute_script("\
    #         var canvas= arguments[0];\
    #         var x=arguments[1];\
    #         var y=arguments[2];\
    #         var w=arguments[3];\
    #         var h=arguments[4];\
    #         var context = canvas.getContext('2d');\
    #         var dataObj= context.getImageData(x, y, w, h);\
    #         var data = dataObj.data;\
    #         return data;"
    #                                   , canvas, x, y, w, h)
    #     data_bytes = array.array('B', data).tostring()
    #     im = Image.fromstring("RGBA", (w, h), data_bytes)
    #     return im

    def end(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.END)
        log.logger.info("页面下滑到底部")

    def getMessage(self):
        messageEle = (By.XPATH, "//*[@class='ivu-message']")
        if self.isElementExist(messageEle):
            log.logger.info("提示信息：%s" % self.getVal(*messageEle))
            return self.getVal(*messageEle)
        else:
            log.logger.info("无提示信息")
            return "无提示信息"
    #转base64
    @staticmethod
    def img2base(img_path: str, file_name: str) -> str:
        """
            接受传递进函数的filename 并找到文件转换为base64格式
        :param img_path: 通过文件名及默认路径找到的img绝对路径
        :param file_name: 用户在装饰器中传递进来的问价匿名
        :return:
        """

        with open(img_path + "\\" + file_name, 'rb') as file:
            data = file.read()
        return base64.b64encode(data).decode()

    #保存截图并保存到报告
    # def saveScreenShot(self,filename):
    #     list_value = []
    #     list =filename.split('.')
    #     for value in list:
    #         list_value.append(value)
    #     if list_value[1] == "png" or list_value[1] == "PNG" or list_value[1] == "jpg" or list_value[1] == "JPG" :
    #         if "fail" in list_value[0].split("_"):
    #             try:
    #                 self.driver.save_screenshot(os.path.join(conf.failImagePath,filename))
    #                 img = self.img2base(conf.failImagePath,filename)
    #                 print(HTML_IMG_TEMPLATE.format(img,img))
    #             except Exception :
    #                 log.logger.exception("未能保存失败截图",exc_info=True)
    #             else:
    #                 log.logger.info(
    #                     '成功保存失败截图 [%s]' % filename)
    #         elif "pass" in list_value[0].split("_"):
    #             try:
    #                 self.driver.save_screenshot(os.path.join(conf.passImagePath,filename))
    #             except Exception:
    #                 log.logger.exception("未能保存通过截图",exc_info=True)
    #             else:
    #                 log.logger.info(
    #                     '成功保存通过截图 [%s]' % filename)
    #         else:
    #             #格式不包含fail/pass
    #             log.logger.info('[%s]截图保存失败，格式名不包含fail/pass' %filename)
    #     else:
    #         #非png/jpg格式
    #         log.logger.info(
    #             '[%s]截图保存失败，非png/jpg格式' % filename)

'''

if __name__ == '__main__':
    pass
