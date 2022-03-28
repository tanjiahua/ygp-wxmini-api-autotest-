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

@allure.epic("注册")
class Test_Is_Register(Base_Api):

    @allure.feature("注册流程")
    @allure.story("检查手机号是否注册接口")
    @allure.title("测试用例名称：注册")
    @allure.severity("critical")
    @pytest.mark.parametrize("phone", [yaml.safe_load(open('./test_data/account.yaml', 'r', encoding="utf-8"))["phone"]])
    def test_is_register(self,phone):
        with allure.step("step1：检查手机号是否注册"):
            res = self.is_register(phone)
            assert res['msg'] == '请求/操作成功'

# if __name__ == '__main__':
#     pytest.main([ '--alluredir', '../report', 'test_is_register.py'])