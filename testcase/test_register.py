# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/28 18:45
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import time

import allure
import pytest
import yaml

from baseapi.base_api.base_api import Base_Api

@allure.epic("注册")
class Test_Register(Base_Api):

    @allure.story("验证码注册")
    @allure.title("验证码注册")
    @allure.severity("critical")
    @pytest.mark.parametrize("phone", ['157' + str(int(time.time()))[2:]])
    def test_register(self,phone):
        with allure.step("step1：验证码发送"):
            res = self.send_sms(phone,2)
            assert res['msg'] == '请求/操作成功'
        with allure.step("step1：验证码注册"):
            res = self.register(phone)
            assert res['msg'] == '请求/操作成功'