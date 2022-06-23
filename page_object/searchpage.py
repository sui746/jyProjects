# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

search = Element('search')


class SearchPage(WebPage):
    """搜索类"""

    def input_name(self, content):
        """输入帐号"""
        self.input_text(search['账号'], txt=content)
        sleep()

    def input_password(self, content):
        """输入密码"""
        self.input_text(search['密码'], txt=content)
        sleep()

    def input_verify(self, content):
        """输入验证码"""
        self.input_text(search['验证码'], txt=content)
        sleep()


    @property
    def imagine(self):
        """搜索联想"""
        return [x.text for x in self.find_elements(search['候选'])]

    def click_search(self):
        """点击登录按钮"""
        self.is_click(search['登录按钮'])


