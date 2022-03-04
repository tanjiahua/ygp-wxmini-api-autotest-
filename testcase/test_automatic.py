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

@allure.epic("营业执照认证")
class Test_Automatic(Base_Api):

    @allure.story("营业执照识别")
    @allure.title("营业执照识别")
    @allure.severity("critical")
    @pytest.mark.parametrize("phone", [yaml.safe_load(open('./test_data/account.yaml', 'r', encoding="utf-8"))["phone"]])
    def test_automatic(self,phone):

        with allure.step("step1：上传营业执照，识别"):
            res = self.automatic(phone)
            assert res['msg'] == '请求/操作成功'
            assert res['data']['infoMap'] ['taxNumber']== '92231102MA1BF55493'
            assert res['data']['infoMap'] ['enterpriseName']== '爱辉区杜燕的黑糖网店'