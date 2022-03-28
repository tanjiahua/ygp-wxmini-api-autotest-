# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/8 17:23
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import allure
import pytest
from baseapi.base_api.base_api import Base_Api

@allure.epic("添加商品到购物车")
class Test_Add_Cart(Base_Api):

    @allure.story("添加商品到购物车")
    @allure.title("添加商品到购物车")
    @allure.severity("critical")
    @pytest.mark.parametrize("num,skuCode",[(1,"EFF00013")])
    def test_add_cart(self,num,skuCode):
        with allure.step("step1：在商品详情页，点击加入购物车，点击确定按钮"):
            res = self.add_cart(num,skuCode)
            assert res['msg'] == '请求/操作成功'