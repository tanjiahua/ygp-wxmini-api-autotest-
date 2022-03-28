# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/10 10:12
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""

import allure
import pytest

from baseapi.base_api.base_api import Base_Api


@allure.epic("购物车删除商品")
class Test_Delete_Cart(Base_Api):

    @allure.story("测试购物车删除商品")
    @allure.title("测试购物车删除商品")
    @allure.severity("critical")
    @pytest.mark.parametrize("skuCodes_list",[["EFF00013"]])
    def test_delete_cart(self,skuCodes_list):
        with allure.step("step1：商品详情，点击加入购物车的按钮"):
            add_cart_res = self.add_cart(1,skuCodes_list[0])
            assert add_cart_res['msg'] == '请求/操作成功'
        with allure.step("step1：购物车里，删除商品"):
            res = self.delete_cart(skuCodes_list)
            assert res['msg'] == '请求/操作成功'