# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element
functions = Element('search')
from common.readconfig import ReadConfig
import yaml
import pytest
import allure



class FunctionPage(WebPage,ReadConfig):
    """配管功能流程"""
    def login(self):
        """登录"""
        # url = ReadConfig.read_inifile(self,head="HOST",hand="HOST")
        url = ReadConfig.read_inifile(self,hand='HOST',head='HOST')
        WebPage.get_url(self,url)
        # functios指元素，调用serach.yaml的列表元素
        self.input_text(functions['账号'], 'jy_zyic')
        sleep()
        self.input_text(functions['密码'], '123456')
        sleep()
        self.is_click(functions['登录'])
        sleep()
        """
        延保配管用的代码
        self.input_text(functions['账号'],'suihaonan')
        sleep()
        self.input_text(functions['密码'],'Abc123456')
        sleep()
        self.input_text(functions['验证码'],'FUCK')
        sleep()
        self.is_click(functions['登录按钮'])
        sleep()
        """
        return self

    def entry(self):
        """定损进入"""
        self.is_click(functions['运维管理'])
        sleep()
        self.is_click(functions['定损模拟'])
        sleep()
        self.is_frame()
        sleep()
        self.input_text(functions['来源'],'ZYIC')
        sleep()
        self.input_text(functions['单号'],'202206271')
        sleep()
        self.input_text(functions['报案号'],'202206271')
        sleep()
        self.input_text(functions['分公司代码'],'88')
        sleep()
        self.input_text(functions['中公司代码'],'88')
        sleep()
        self.is_click(functions['定损进入'])
        sleep()
        return self

    def Entry_Information(self):
        """录入信息"""
        # 获取当前页面源代码
        sleep()
        self.refresh()
        self.is_frames()
        sleep()
        # 定型
        self.input_texts(functions['定型VIN码'], 'LVGDC46A0CG191914')
        sleep()
        self.is_click(functions['开始定型'])
        sleep()
        self.is_click(functions['查询'])
        sleep()
        self.is_click(functions['确定'])
        sleep()
        self.yes_confirm()
        sleep()


