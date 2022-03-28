# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/22 19:06
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import json
from ruamel import yaml

def test_write_data():
    aproject = {'cardBalance': 18851}
    aproject2 = {"cardNumber": "22222223"}
    with open('test.yaml', 'r+', encoding="utf-8") as f:
        f.write(yaml.dump(aproject, Dumper=yaml.RoundTripDumper))

