# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/3 16:39
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import allure

from baseapi.base_api.base_api import Base_Api


@allure.epic("首页获取定位接口测试")
class Test_Get_Location(Base_Api):
    @allure.story("首页获取定位接口测试")
    @allure.title("首页获取定位接口测试")
    @allure.severity("critical")
    def test_get_location(self):
        with allure.step("step1：查看首页获取定位信息"):
            res = self.get_location()
            assert res['status'] == 0
            assert res['message'] == 'query ok'
            assert res['result']['address'] == '广东省广州市海珠区广州大道南999号'

