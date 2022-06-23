# -*- coding:utf-8 -*-

from page_object.searchpage import SearchPage
from page_object.functionpage import FunctionPage


class TestSearch:
    # @pytest.fixture(scope='function', autouse=True)
    # def open_baidu(self, drivers):
    #     """打开地址"""
    #     search = SearchPage(drivers)
    #     search.get_url(ini.url)

    def test_001(self, drivers):
        """登录"""

        functions = FunctionPage(drivers)
        functions.login()



    # def test_002(self, drivers):
    #     """测试搜索候选"""
    #     search = SearchPage(drivers)
    #     search.input_search("selenium")
    #     log.info(list(search.imagine))
    #     assert all(["selenium" in i for i in search.imagine])
#
#
# if __name__ == '__main__':
#     pytest.main(['PycharmProjects/TestCase/'])





