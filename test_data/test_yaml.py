# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/28 18:45
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import time

import yaml

def test_yaml():
    data = yaml.safe_load(open('account.yaml', 'r', encoding="utf-8"))
    print(data['phone'])
    print(time.strftime("%Y-%m-%d", time.localtime()))

def test_data():
    for num in range(1, 10):
        for i in range(1, num):
            print(num)
            sum=i*num
            print('%d * %d = %d' % (i, num, sum))