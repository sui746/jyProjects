# -*- coding:utf-8 -*-
# 创建角色用的文件，可以操作不同流程和功能，便于调用
from page_object.functionpage import FunctionPage
from page_object.login import LoginPage


class YanBao:
    def __init__(self,driver):
        self.function=FunctionPage(driver)
        # self.search=FunctionPage(driver)
        # self.factory=LoginPage(driver)


    # def logins(self):
    #     self.function.login()
    #
    # def damage(self):
    #     self.function.test_damage()
