# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/7 19:27
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import allure
import pytest

from baseapi.base_api.base_api import Base_Api


@allure.epic("查看购物车列表")
class Test_Cart(Base_Api):

    @allure.story("测试首页点击购物车")
    @allure.title("测试首页点击购物车")
    @allure.severity("critical")
    @pytest.mark.parametrize("lat,lng",[("23.054853","113.368675")])
    def test_cart(self,lat,lng):
        with allure.step("step1：首页，点击购物车的按钮，查看购物车列表"):
            res = self.cart(lat,lng)
            assert res['msg'] == '请求/操作成功'