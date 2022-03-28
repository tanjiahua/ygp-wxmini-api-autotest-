# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/10 17:52
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import allure

from baseapi.base_api.base_api import Base_Api

@allure.epic("获取个人信息")
class Test_Get_User_Info(Base_Api):

    @allure.story("获取个人信息")
    @allure.title("获取个人信息")
    @allure.severity("critical")
    def test_get_user_info(self):
        with allure.step("step1：登录，个人中心,个人信息"):
            res = self.get_user_info(93107)
            assert res['msg'] == '请求/操作成功'
            assert res['data']['id'] == '93107'
            assert res['data']['userCode'] == 'UC1496413700959674370'
