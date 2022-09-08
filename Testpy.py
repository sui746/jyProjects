# -*- coding:utf-8 -*-

"""
    练习pytest使用方法
"""

import pytest  # 导入pytest包

def test_a(): # test开头的测试函数
    print("------->test_a")
    assert 1 # 断言成功
# def test_b():
#     print("------->test_b")
#     assert 0 # 断言失败
if __name__ == '__main__':
    pytest.main("-s  Testpy.py") # 调用pytest的main函数执行测试
