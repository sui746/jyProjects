# -*- coding:utf-8 -*-
"""
selenium基类
本文件存放了selenium基类的封装方法
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


from selenium import webdriver
from config.conf import cm
from utils.times import sleep
from utils.logger import log


class WebPage(object):
    """selenium基类"""

    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(cm.LOCATE_MODE[name], value)

    def find_element(self, locator):
        """寻找单个元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_element_located(args)), locator)

    def find_elements(self, locator):
        """查找多个相同的元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        log.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))


    def input_texts(self, locator, txt):
        """
        lear方法不起作用时，用此方法
        python语法中用 send_keys  用下划线，不用点
        """
        sleep()
        # ctrl+a 全选
        # self.find_element(locator).send_keys(Keys.CONTROL, 'a')
        # self.find_element(locator).send_keys(txt)
        el = self.find_element(locator)
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(txt)

    def is_click(self, locator):
        """点击"""
        self.find_element(locator).click()
        sleep()
        log.info("点击元素：{}".format(locator))

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        log.info("获取文本：{}".format(_text))
        return _text


    def is_frame(self):
        """定位内嵌页面"""
        self.driver.switch_to.frame(0)

    def alert_click(self):
        """页面弹出的alert弹窗时  自动点击确定（消息弹窗）"""
        self.driver.switch_to.alert.accept()

    def yes_confirm(self):
        sleep(2)
        # 点击ok按钮
        self.driver.switch_to.alert.accept()

    def no_confirm(self):
        sleep(2)
        # 点击no按钮
        self.driver.switch_to.alert.dismiss()

    def is_frames(self, num):
        """定位跳转的第二个页面"""
        self.driver.switch_to.window(self.driver.window_handles[num])

    def is_select(self,element, num):
        """带下拉列表元素定位的选择方法 element==元素，num==对应下拉列表的值"""
        Select(self.find_element(element)).select_by_value(num)


    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)