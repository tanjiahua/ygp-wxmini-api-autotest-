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

@allure.epic("注册模块")
class Test_Run_Register(Base_Api):

    @allure.feature("注册流程")
    @allure.story("流程测试用例")
    @allure.title("测试用例名称：注册")
    @allure.severity("critical")
    @pytest.mark.parametrize("phone", [yaml.safe_load(open('./test_data/account.yaml', 'r', encoding="utf-8"))["phone"]])
    def test_run(self,phone):
        '''
            用例描述：
            前置：登陆
            用例步骤：1.检查手机号是否注册 2.发送注册验证码  3.点击注册  4.上传营业执照 5.营业执照识别 6.提交验证
        '''
        with allure.step("step1：检查手机号是否注册"):
            self.is_register(phone)
        with allure.step("step1：发送注册验证码"):
            # 注册验证码：type=2，登录验证码：type=1
            self.send_sms(phone,2)
        with allure.step("step1：点击注册"):
            self.register(phone)
        with allure.step("step1：营业执照识别"):
            self.automatic(phone)
        with allure.step("step1：提交验证"):
            self.distributionsubmit(phone)




if __name__ == '__main__':
    pytest.main(['--alluredir', '../report', 'test_main.py'])