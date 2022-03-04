# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/28 18:45
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import allure
import pytest
import yaml
from baseapi.base_api.base_api import Base_Api

@allure.epic("登录")
class Test_Login(Base_Api):

    @allure.story("手机号码密码登录")
    @allure.title("手机号码密码登录")
    @allure.severity("critical")
    @pytest.mark.parametrize("phone", [yaml.safe_load(open('./test_data/account.yaml', 'r', encoding="utf-8"))["phone"]])
    @pytest.mark.skip("微信小程序，无法获取微信code,暂时无法实现接口，自动登录")
    def test_login(self,phone):
        with allure.step("step1：输入手机号码和密码"):
            res = self.login(phone)
            assert res['msg'] == '请求/操作成功'

