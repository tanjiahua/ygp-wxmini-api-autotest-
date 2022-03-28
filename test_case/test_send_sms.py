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

@allure.epic("发送验证码")
class Test_Send_Sms(Base_Api):

    @allure.story("发送登录验证码")
    @allure.title("发送登录验证码")
    @allure.severity("critical")
    @pytest.mark.parametrize("phone",
                             [yaml.safe_load(open('./test_data/account.yaml', 'r', encoding="utf-8"))["phone"]])
    def test_send_login_sms(self,phone):
        # 注册验证码：type=2，登录验证码：type=1
        type=1
        with allure.step("step1：发送登录验证码"):
            res = self.send_sms(phone,type)
            assert res['msg'] == '请求/操作成功'

    @allure.story("发送注册验证码")
    @allure.title("发送注册验证码")
    @allure.severity("critical")
    @pytest.mark.parametrize("phone", ['157' + str(int(time.time()))[2:]])
    def test_send_register_sms(self,phone):
        # 注册验证码：type=2，登录验证码：type=1
        type=2
        with allure.step("step1：发送注册验证码"):
            res = self.send_sms(phone,type)
            assert res['msg'] == '请求/操作成功'
