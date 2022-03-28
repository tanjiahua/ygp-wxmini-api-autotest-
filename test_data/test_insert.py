# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/15 17:45
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
from common.common import insert


def test_insert():
    i=200
    while i > 0:
        insert("INSERT INTO `ygp_udc`.`shop_collection`(`user_code`, `shop_code`, `create_time`, `update_time`, `active`, `creator`, `creator_code`, `updater`, `updater_code`) VALUES ('UC1496317675387289601', 'SH00011038', '2022-03-15 19:31:03.717', '2022-03-15 19:32:22.592', 0, '15700001001', 'UC1496317675387289601', '15700001001', 'UC1496317675387289601');"
,"test1")
        i = i-1;
