# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/28 18:45
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import allure
import pytest
import yaml
from baseapi.base_api.mws_api import Mws_Api

@allure.epic("登录mws")
class Test_Mws_Login():

    @allure.story("登录mws接口测试用例")
    @allure.title("登录mws接口测试用例")
    @allure.severity("critical")
    @pytest.mark.parametrize("dict", [yaml.safe_load(open('./test_data/account.yaml', 'r', encoding="utf-8"))])
    def test_login(self,dict):
        mws=Mws_Api()
        with allure.step("step1：账号密码登录"):
            res = mws.login(dict["account"],dict["password"])
            assert res['msg'] == '请求/操作成功'
            assert res['data']['mobile']== str(dict["account"])


