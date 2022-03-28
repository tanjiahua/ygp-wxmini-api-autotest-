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
class Test_DistributionSubmit(Base_Api):

    @allure.story("提交营业执照认证")
    @allure.title("提交营业执照认证")
    @allure.severity("critical")
    @pytest.mark.parametrize("phone", [yaml.safe_load(open('./test_data/account.yaml', 'r', encoding="utf-8"))["phone"]])
    def test_distributionsubmit(self,phone):

        with allure.step("step1：上传营业执照，识别，提交营业执照认证"):
            res = self.distributionsubmit(phone)
            assert res['msg'] == '该企业已认证，如有疑问，可以联系客服进行申诉处理'