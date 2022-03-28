# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/1 19:02
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import os

import requests
import yaml
from common.common import write_yaml


class Spm_Api():
    base_url = yaml.safe_load(open('./test_data/spm_env.yaml', 'r', encoding="utf-8"))["uat_url"]

    def login(self, phone, password):
        url = self.base_url + '/api/uc/login/adminLogin'
        headers = {"Content-Type": "application/json"}
        data = {
            "accountOrMobile": phone,
            "password": password
        }
        res = requests.post(url, headers=headers, json=data)
        token = res.json()["data"]["token"]
        token_data = {"token": token}
        if os.path.exists("./test_data/token.yaml") == False:
            write_yaml("./test_data/token.yaml", token_data)
        return res.json()