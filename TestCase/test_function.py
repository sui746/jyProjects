# -*- coding:utf-8 -*-
import pytest
import allure
import os
from page_object.functionpage import FunctionPage
from roles.role import YanBao



class TestFuction:

    def test_001(self, JYtest):
        # 配管登录
        JYtest.function.login()
        # 配管--运维管理--进入定损
        JYtest.function.one_entry()
        # 定型页面（定型、碰撞部位、修理厂）
        JYtest.function.Entry_Information()
        # 损失页面（添加配件）
        JYtest.function.Add_loss()

    def test_002(self, JYtest):
        # 配管登录
        JYtest.function.login()
        # 配管--运维管理--进入核价
        JYtest.function.two_entry()
        # 核价页面（同意定损--暂存）
        JYtest.function.Add_check()

    def test_003(self, JYtest):
        # 配管登录
        JYtest.function.login()
        # 配管--运维管理--进入核损
        JYtest.function.three_entry()
        # 核损页面（同意核损--暂存）
        JYtest.function.Add_audit()






if __name__ == '__main__':
    # pytest.main(['D:/PycharmProjects/TestCase/test_function.py','--alluredir','./temp'])
    # os.system('allure generate ./temp -o ./report --clean')

    pytest.main(['D:/PycharmProjects/TestCase/test_function.py', '--alluredir', './allure'])
    # os.system('allure serve allure')
    # 配合allure使用
    # pytest.main(['D:/PycharmProjects/TestCase/','--alluredir','D:/PycharmProjects/allure'])
    # os.system('allure serve allure')
