# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element
from common.readconfig import ReadConfig
search = Element('search')


class LoginPage(WebPage,ReadConfig):
    """搜索类"""

    def rurl(self):

        url = ReadConfig.read_inifile(self,hand='HOST',head='HOST')
        WebPage.get_url(self,url)
        sleep()
        return self
    def input_name(self, content):
        """输入帐号"""
        self.input_text(search['账号'], txt=content)
        sleep()
        return self

    def input_password(self, content):
        """输入密码"""
        self.input_text(search['密码'], txt=content)
        sleep()
        return self

    def input_verify(self, content):
        """输入验证码"""
        self.input_text(search['验证码'], txt=content)
        sleep()
        return self

    def click_search(self):
        """点击登录按钮"""
        self.is_click(search['登录按钮'])






