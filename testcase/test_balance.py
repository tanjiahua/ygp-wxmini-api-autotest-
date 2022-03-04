# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/28 18:45
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import allure

from baseapi.base_api.base_api import Base_Api

@allure.epic("红包账户")
class Test_Balance(Base_Api):

    @allure.story("查询红包账账户余额")
    @allure.title("查询红包账账户余额")
    @allure.severity("critical")
    def test_balance(self):
        with allure.step("step1：登录，个人中心查询"):
            res = self.balance()
            assert res['msg'] == '请求/操作成功'