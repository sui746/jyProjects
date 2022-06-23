# -*- coding:utf-8 -*-
import configparser
# ConfigParser 是用来读取配置文件的包
from config.conf import cm
# 继承config文件夹下conf文件cm方法
HOST = 'HOST'


class ReadConfig(object):
    """配置文件"""

    def __init__(self):
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(cm.ini_file, encoding='utf-8')
        # 读取了config.ini文件
    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(cm.ini_file, 'w',encoding='utf-8') as f:
            self.config.write(f)

    # def read_url(self,hand,head):
    #     return self.config.get(hand,head)


    @property
    def url(self):
        return self._get(HOST, HOST)


    def read_inifile(self,head,hand):
        """读取ini文件内容"""
    # file1 = "D:\PycharmProjects\config\config.ini"

        conf = configparser.ConfigParser()
        conf.read('../config/config.ini')
        content = conf.get(head,hand)
        return content   # -- 将读取的文件内容返回供调用


ini = ReadConfig()

if __name__ == '__main__':
    print(ini.read_inifile('HOST','HOST'))


