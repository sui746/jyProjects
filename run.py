# -*- coding:utf-8 -*-
# @File ：run.py
# -*- ecoding: utf-8 -*-
# @Time: 2021/8/22 21:05
# @Author: niu run peng
import os
import sys

abspath = os.path.abspath(__file__)
if 'test_function' in abspath:
    sys.path.append(
        os.path.abspath(__file__).split('EasyEPC_3.0_UIAutomatiotTest')[0] + 'EasyEPC_3.0_UIAutomatiotTest/')
else:
    sys.path.append(os.path.abspath(__file__).split('EasyEPC')[0] + 'EasyEPC/')
import pytest
import shutil

# env = 'test'
# browser = 'Chrome'
# last_fails = '0'

# mark = ''
# from common.send_mail import MailSender

"""
Pytest运行入口
"""
if __name__ == '__main__':
    env = sys.argv[1]
    browser = sys.argv[2]
    last_fails = sys.argv[3]
    shutil.rmtree('../temp', ignore_errors=True)
    shutil.rmtree('../report', ignore_errors=True)
    os.mkdir('../temp')
    os.mkdir('../report')
    exec_li = ['-s', '-v', '../test_case/', '--reruns', '0', '--env', env, '--browser', browser,
               '--alluredir', '../temp/', '--clean-alluredir', '--html', 'report.html']
    if last_fails == '1':
        exec_li.append('--lf')
    pytest.main(exec_li)
    os.system('allure generate ../temp/ -o ../report/ --clean')
    # MailSender().send_allure_report('EasyEPC_3.0_UIAutomatiotTest',env=env)
