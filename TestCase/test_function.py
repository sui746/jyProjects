# -*- coding:utf-8 -*-
import pytest
import allure
import os
from page_object.functionpage import FunctionPage
from roles.role import YanBao



class TestFuction:

    def test_001(self, JYtest):

        JYtest.function.login()
        JYtest.function.entry()
        JYtest.function.Entry_Information()

        # message=yb.search.sea('eadas1')
        # assert message=="asdas"

    # def test_002(self, yb):
        """登录"""
        # self.yanbao.damage()




if __name__ == '__main__':
    # pytest.main(['D:/PycharmProjects/TestCase/test_function.py','--alluredir','./temp'])
    # os.system('allure generate ./temp -o ./report --clean')

    pytest.main(['D:/PycharmProjects/TestCase/test_function.py', '--alluredir', './allure'])
    # os.system('allure serve allure')
    # 配合allure使用
    # pytest.main(['D:/PycharmProjects/TestCase/','--alluredir','D:/PycharmProjects/allure'])
    # os.system('allure serve allure')
