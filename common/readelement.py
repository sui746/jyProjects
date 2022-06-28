# -*- coding:utf-8 -*-
import os
# 对大量文件和大量路径进行操作，需要依赖于os模块
import yaml
# YAML是一种简洁的非标记语言。其以数据为中心，使用空白，缩进，分行组织数据，从而使得表示更加简洁
from config.conf import cm
# 此文件是读取page_element/search.yaml  下的元素信息用的

class Element(object):
    """获取元素"""

    def __init__(self, name):
        self.file_name = '%s.yaml' % name
        self.element_path = os.path.join(cm.ELEMENT_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取属性"""
        data = self.data.get(item)
        if data:
            name, value = data.split('==')
            return name, value
        raise ArithmeticError("{}中不存在关键字：{}".format(self.file_name, item))


if __name__ == '__main__':
    search = Element('search')
    print(search['帐号'])