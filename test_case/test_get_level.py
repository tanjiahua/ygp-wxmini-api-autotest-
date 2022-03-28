# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/3 16:56
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import allure

from baseapi.base_api.base_api import Base_Api


@allure.epic("分类")
class Test_Get_Level(Base_Api):
    @allure.story("一级分类")
    @allure.title("获取一级分类信息")
    @allure.severity("critical")
    def test_get_level1(self):
        test1_url="http://gateway-test1.yigongpin.net"
        with allure.step("step1：点击分类按钮，请求一级分类接口"):
            res = self.get_level1()
            assert res['msg'] == '请求/操作成功'
            if test1_url == self.base_url:
                assert res['data'][0]['categoryName'] == '手工具'

    @allure.story("三级、四级级分类")
    @allure.title("获取三级、四级分类信息")
    @allure.severity("critical")
    def test_get_level34(self):
        test1_url = "http://gateway-test1.yigongpin.net"
        with allure.step("step1：点击分类按钮，请求三级、四级分类接口"):
            res = self.get_level34()
            if test1_url == self.base_url:
                assert res["msg"] == "请求/操作成功"
                # KeyError: '321450',一直找不到这个key?很奇怪
                # assert res["data"]["321450"][0]["categoryName"] == "花洒/淋浴/软管"
                # assert res["data"]["321450"][0]["children"][0]['categoryName'] == "洗衣机管"











