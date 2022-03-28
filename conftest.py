# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/22 20:09
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import base64
import pytest
import requests
import yaml
from common.common import MD5, write_data

@pytest.fixture(scope="session", autouse=True)
def app_login():
    base_url = yaml.safe_load(open('./test_data/env.yaml', 'r', encoding="utf-8"))["uat_url"]
    url = base_url + '/api/uc/god/login/distributor/useAccountOrPhone'
    phone = yaml.safe_load(open('./test_data/account.yaml', 'r', encoding="utf-8"))["phone"]
    password = MD5("ygp123456")
    headers = {"Content-Type": "application/json",
               "appName": "com.ygp.mro"}
    data = {"accountOrMobile": phone,
            "password": password}
    res = requests.post(url, headers=headers, json=data)
    token_data = res.json()["data"]["token"]
    write_data(token_data)
    yield token_data

# def test_md5():
#     # 加密过程
#     # 1.将data(JSON字符串)、appSecret按顺序拼接好
#     # 2.将第一步得到的字符串使用MD5Hex加密得到32位16进制的小写字符串
#     # 3.将第二步得到的32位字符串转为UTF - 8编码的byte数组
#     # 4.将得到的byte数组使用BASE64加密算法计算，最终得到sign值
#     data="ygp"
#     appSecret="123456"
#     bytes_data = MD5(data+appSecret).encode("utf-8")
#     resb64 = base64.b64encode(bytes_data)
#     print(resb64)
#     bef = base64.b64decode(resb64).decode("utf-8")
#     print(bef)
#     # import random, string
#     # num = string.ascii_letters + string.digits
#     # # print("".join(random.sample(num, 15)))
#     # i=0
#     # while i<10:
#     #     print("".join(random.sample(num, 7)))
#     #     i+=i
#     #     # print("".join(random.sample(num, 15)))