# -*- coding: utf-8 -*-
"""
@Time ： 2022/3/14 11:27
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import allure

from baseapi.base_api.base_api import Base_Api


@allure.epic("订单测试流程")
class Test_Order_From_Cart(Base_Api):

    @allure.story("购物车购买产品，下单，微信支付")
    @allure.title("购物车购买产品，下单，微信支付")
    @allure.severity("critical")
    def test_order_pay(self):
        with allure.step("step1：在商品详情页，加入购物车，点击确定按钮"):
            res = self.from_cart_order_submit()
            assert res['msg'] == '请求/操作成功'
            orderNo=res["data"]["orderNo"]
            trxreserved = orderNo
        with allure.step("step1：微信支付"):
            res = self.order_pay(orderNo)
            assert res['msg'] == '请求/操作成功'
            cusorderid=self.order_pay(trxreserved)["data"]["reqsn"]
            trxid=self.order_pay(trxreserved)["data"]["trxid"]
        with allure.step("step1：微信支付回调成功"):
            res = self.pay_call_back(cusorderid,trxid,trxreserved)
            assert res.status_code ==200
        with allure.step("step1：查看代发货列表"):
            res = self.get_order_detail(orderNo)
            assert res['msg'] == '请求/操作成功'