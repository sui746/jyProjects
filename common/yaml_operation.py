# -*- coding:utf-8 -*-
# @File ：yaml_operation.py
# -*- ecoding: utf-8 -*-
# @Time: 2021/8/21 20:01
# @Author: niu run peng
import json

import yaml


class YamlOperation:
    titles = []

    @staticmethod
    def load_case(file_path, n: list = None):
        """
        根据测试用例yml文件路径加载用例数据
        :param n: 第几条用例被加载 可以挑选某几个测试用例 便于报错的用例单独调试 不传就加载全部
        :param file_path:测试用例yml文件路径
        :return:[(),(),...]
        """
        li = []
        titles = []
        with open(file_path, mode='r', encoding='utf-8') as f:
            case_list = yaml.load(f, Loader=yaml.FullLoader)
        if n:
            for i in n:
                case_value_li = tuple(dict(case_list[i - 1]).values())
                titles.append(f'{i}.{case_value_li[0]}')
                li.append(case_value_li)
        else:
            i = 0
            for case in case_list:
                i += 1
                case_value_li = tuple(dict(case).values())
                titles.append(f'{i}.{case_value_li[0]}')
                li.append(case_value_li)
        # 把用例中的标题赋值给类变量 下边的case_title方法可以使用这个标题用作测试用例的ids
        YamlOperation.titles = titles
        return li

    @staticmethod
    def case_title():
        return YamlOperation.titles

    @staticmethod
    def load_config(file_path):
        with open(file_path, mode='r', encoding='utf-8') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        return config

    @staticmethod
    def write_config(path, data: dict):
        with open(path, 'w') as f:
            yaml.dump(data, f)


if __name__ == '__main__':
    print(YamlOperation.load_config('../case_data/yb_login.yml')['notice'])







