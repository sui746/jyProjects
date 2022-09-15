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

    def one_entry(self):
        """定损进入"""
        self.is_click(functions['运维管理'])
        sleep()
        self.is_click(functions['定损模拟'])
        sleep()
        self.is_frame()
        sleep()
        self.input_text(functions['来源'],'ZYIC')
        sleep()
        self.input_text(functions['单号'],'2022091317')
        sleep()
        self.input_text(functions['报案号'],'2022091317')
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
        self.is_frames(1)
        sleep()
        # 定型
        self.input_texts(functions['定型VIN码'], 'LJ1EEAUUXJ7704396')
        sleep()
        self.is_click(functions['开始定型'])
        sleep()
        self.is_click(functions['查询'])
        sleep()
        self.is_click(functions['问题判断'])
        sleep()
        self.is_click(functions['确定'])
        sleep()
        self.is_click(functions['弹窗确定'])
        sleep()
        self.is_click(functions['全车'])
        sleep()
        self.is_click(functions['内部'])    # 加个内部是因为外修关联了内部，不加内部有弹窗，加上可以规避弹窗
        sleep()
        self.is_click(functions['选择修理厂'])
        sleep()
        self.is_click(functions['点选修理厂'])
        sleep()
        self.is_click(functions['修理厂确定'])
        sleep()
        self.is_click(functions['修理厂弹窗确定'])
        sleep()

    def Add_loss(self):
        sleep()
        self.is_click(functions['选择损失'])
        sleep()
        self.is_click(functions['添加配件'])
        sleep()
        self.input_text(functions['配件录入'],'前保险杠皮')
        sleep(8)
        self.is_click(functions['配件查询'])
        sleep()
        self.is_click(functions['点选添加'])
        sleep()
        self.is_click(functions['辅料切换'])
        sleep()
        self.is_click(functions['辅料添加'])
        sleep()
        self.is_click(functions['外修切换'])
        sleep()
        self.is_click(functions['外修添加'])
        sleep()
        self.is_click(functions['关闭窗口'])
        sleep()
        self.input_text(functions['辅料价格'], '100')
        sleep()
        self.input_text(functions['修改配件价格'], '500')
        sleep()
        self.input_text(functions['修改外修价格'], '100')
        sleep(3)
        self.is_click(functions['完成'])
        sleep(5)
        self.is_click(functions['暂存'])
        sleep()
        # self.driver.close()
        return self


    def two_entry(self):
        """核价进入"""
        self.is_click(functions['运维管理'])
        sleep()
        self.is_click(functions['定损模拟'])
        sleep()
        self.is_frame()
        sleep()
        self.is_select(functions['请求类型'],'003')
        sleep(3)
        self.input_text(functions['核价来源'],'ZYIC')
        sleep()
        self.input_text(functions['核价单号'],'2022091317')
        sleep()
        self.input_text(functions['核价报案号'],'2022091317')
        sleep()
        self.input_text(functions['核价分公司代码'],'88')
        sleep()
        self.input_text(functions['核价中公司代码'],'88')
        sleep()
        self.is_click(functions['核价进入'])
        sleep(3)
    def Add_check(self):
        """核价审核"""
        # 切换标签页
        # self.driver.switch_to.window(self.driver.window_handles[2])
        sleep()
        # 获取当前页面源代码
        self.refresh()
        # 定位跳转的第三个页面
        self.is_frames(2)
        sleep()
        self.is_click(functions['配件全选'])
        sleep()
        self.is_click(functions['配件同意定损'])
        sleep()
        self.is_click(functions['外修全选'])
        sleep()
        self.is_click(functions['外修同意定损'])
        sleep()
        self.input_text(functions['备注意见'], '核价审核通过')
        sleep()
        self.is_click(functions['核价暂存'])
        sleep()

    def three_entry(self):
        """核损进入"""
        # 所有核价来源等信息 核损通用，配管核价核损页面元素一致
        self.is_click(functions['运维管理'])
        sleep()
        self.is_click(functions['定损模拟'])
        sleep()
        self.is_frame()
        sleep()
        self.is_select(functions['请求类型'],'005')
        sleep(3)
        self.input_text(functions['核价来源'],'ZYIC')
        sleep()
        self.input_text(functions['核价单号'],'2022091317')
        sleep()
        self.input_text(functions['核价报案号'],'2022091317')
        sleep()
        self.input_text(functions['核价分公司代码'],'88')
        sleep()
        self.input_text(functions['核价中公司代码'],'88')
        sleep()
        self.is_click(functions['核价进入'])
        sleep(3)
    def Add_audit(self):
        """核损审核"""
        sleep()
        # 获取当前页面源代码
        self.refresh()
        # 定位跳转的第四个页面
        self.is_frames(3)
        sleep()
        self.is_click(functions['一键审核'])
        sleep()
        self.is_click(functions['配件全选框'])
        sleep()
        self.is_click(functions['同意定损方案'])
        sleep()
        self.input_text(functions['核损意见'], '核损审核通过')
        sleep()
        self.is_click(functions['核损暂存'])
        sleep()