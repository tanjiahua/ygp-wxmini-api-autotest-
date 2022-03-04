# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/28 18:45
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import allure
import pytest

from baseapi.base_api.base_api import Base_Api

@allure.epic("搜索模块")
class Test_Search(Base_Api):
    @allure.story("商品搜索")
    @allure.title("商品搜索测试用例")
    @allure.severity("critical")
    @pytest.mark.parametrize("keyword",["扳手"])
    def test_productsearch(self,keyword):
        with allure.step("step1：输入搜索关键词，点击搜索"):
            res = self.productsearch(keyword)
            assert res['msg'] == '请求/操作成功'
            assert res['data'] ['data'][0]['skuName']=="5号测试"
            assert res['data'] ['total']== 6

    @allure.story("店铺搜索")
    @allure.title("店铺搜索测试用例")
    @allure.severity("critical")
    @pytest.mark.parametrize("keyword",["测试店"])
    def test_shopsearch(self,keyword):
        with allure.step("step1：输入搜索关键词，点击搜索"):
            res = self.shopsearch(keyword)
            assert res['msg'] == '请求/操作成功'
            assert res['data'] ['data'][0]['shopName']== "测试店铺xxxxxxx"
            assert res['data'] ['total']== 47
