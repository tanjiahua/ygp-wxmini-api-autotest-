# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/28 18:45
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import time

import pytest
import requests
import yaml
from common.common import link_redis, write_yaml, query
import os
path = os.path.dirname(os.path.abspath(__file__))

class Base_Api():

    base_url=yaml.safe_load(open('./test_data/env.yaml', 'r', encoding="utf-8"))["uat_url"]
    env_mark=yaml.safe_load(open('./test_data/env.yaml', 'r', encoding="utf-8"))["uat"]

    def is_register(self,phone):
        url= self.base_url+'/api/uc/god/login/check/phone?accountOrPhone=%d&type=2&tenantId=1'%phone
        headers = {"Content-Type": "application/json"}
        res = requests.get(url,headers=headers)
        return res.json()

    def send_sms(self,phone,type):
        url = self.base_url + '/api/uc/god/login/sendSMSCode'
        data={"phone":phone,"purpose":type}
        headers={"Content-Type": "application/json"}
        res = requests.post(url,headers=headers,json=data)
        return res.json()

    def register(self,phone):
        verifyCode=link_redis(phone,"uat")
        url = self.base_url + '/api/uc/god/register/distributor/getRegisterCertificate'
        print(verifyCode)
        data={"mobile":phone,
              "tenantId":1,
              "purpose":2,
              "verifyCode":verifyCode}
        headers={"Content-Type": "application/json"}
        res = requests.post(url,headers=headers,json=data)
        return res.json()

    def automatic(self,phone):
        url = self.base_url + '/api/crm/enterprise/approval/automaticRecognition'
        data ={"imgUrl":"https://qiniu-cdn-private-test.yigongpin.net/private/uat/miniprogramMallBusinessLicense/2022-02-25/dd421b738cbb1c67bb8b18b6b9d2e666.png",
               "bizCode":phone}
        headers = {"Content-Type": "application/json"}
        res = requests.post(url, headers=headers, json=data)
        return res.json()

    def distributionsubmit(self,phone):
        url = self.base_url + '/api/uc/god/enterprise/approval/distributionSubmit'
        data = {"total":3,
                    "residueDegree":2,
                    "filePath":"http://tmp/qfufpEdgePQJ9b5bb560048d4ba15d3718322566c80f.jpg",
                    "enterpriseName":"爱辉区杜燕的黑糖网店",
                    "taxNumber":"92231102MA1BF55493",
                    "automaticToken":"d3604ef0c74712cc3cdd573cbe1eb517",
                    "businessLicensePhoto":"https://qiniu-cdn-private-test.yigongpin.net/private/miniprogramMallBusinessLicense/2022-03-02/56534972a9665559f83b2b335419c138.png",
                    "unrecognized":"false",
                    "delta":4,
                    "canSkip":"false",
                    "mobile":phone,
                    "password":"57a233608bd7e809789f5a25443cd77e",
                    "onceToken":"bd01f24de72c443c8ecfd6229ad24374",
                    "__webviewId__":24,
                    "inviteSource":"",
                    "inviteScene":"",
                    "inviteMobile":""}
        headers = {"Content-Type": "application/json"}
        res = requests.post(url, headers=headers, json=data)
        return res.json()

    def login(self,phone):
        url = self.base_url +'/api/uc/login/adminLogin'
        password = query("select `password` from uc_user where mobile='%d';"%phone,"uat")
        headers = {"Content-Type": "application/json"}
        data={"accountOrMobile":phone,
              "password":password,
              "code":"063LrJkl2TseI84Xldol2dsbxX1LrJkl"}
        print(data)
        res = requests.post(url,headers=headers,json=data)
        print(res.json())
        token_data=res.json()["data"]["token"]
        if os.path.exists("./test_data/wxmini_token") == "false":
            write_yaml("./test_data/wxmini_token.yaml", token_data)
        return res.json()

    def login_verifycode(self,phone):
        url = self.base_url +'/api/uc/god/login/distributor/userWithMobile'
        verifyCode=link_redis(phone)
        headers = {"Content-Type": "application/json"}
        data={
            "code": "013Pfoll2QbPJ84Kv8nl2WOAXf0Pfol6",
            "loginMobile": phone,
            "verifyCode": verifyCode
            }
        res = requests.post(url,headers=headers,json=data)
        token_data = res.json()["data"]["token"]
        if os.path.exists("./test_data/wxmini_token") == "false":
            write_yaml("./test_data/wxmini_token.yaml", token_data)
        return res.json()

    def productsearch(self,keyword):
        token = yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]
        url= self.base_url+'/api/sc/search/appSearch/v2'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":token}
        data={"word":keyword,
                     "keyword":keyword,
                     "searchType":3,
                     "categoryIds":[],
                     "brandCodes":[],
                     "attrs":[],
                     "sort":"",
                     "pageNum":1,
                     "pageSize":10,
                     "channel":"applet",
                     "userCode":"UC1496317675387289601",
                     "userOpenId":"oJ9Gc5XXiHpbJ_LIfU8uFpGNJcWI",
                     "userUnionId":"null"}
        res = requests.post(url,headers=headers,json=data)
        return res.json()

    def shopsearch(self,keyword):
        token = yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]
        url= self.base_url+'/api/sc/shop/search/listShop/V2'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":token}
        data = {"word": keyword,
                "keyword": keyword,
                "searchType": 3,
                "categoryIds": [],
                "brandCodes": [],
                "attrs": [],
                "sort": "",
                "pageNum": 1,
                "pageSize": 10,
                "channel": "applet",
                "userCode": "UC1496317675387289601",
                "userOpenId": "oJ9Gc5XXiHpbJ_LIfU8uFpGNJcWI",
                "userUnionId": "null"}
        res = requests.post(url, headers=headers, json=data)
        return res.json()

    def balance(self):
        token = yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]
        url= self.base_url+'/api/pay/pay/mall/userAccount/balance'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":token}
        res = requests.get(url,headers=headers)
        return res.json()

    def get_location(self):
        token = yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]
        url= 'https://apis.map.qq.com/ws/geocoder/v1/?coord_type=5&get_poi=0&output=json&key=TWNBZ-PULL3-YZF35-YUIMQ-WBR5Q-7FBT2&location=23.08331%2C113.3172'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":token}
        res = requests.get(url,headers=headers)
        return res.json()

    def get_level1(self):
        token = yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]
        url= self.base_url+'/api/pms/category/info/level1'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":token}
        res = requests.get(url,headers=headers)
        return res.json()

    def get_level34(self):
        token = yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]
        url= self.base_url+'/api/pms/category/info/level34'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":token}
        res = requests.get(url,headers=headers)
        return res.json()

    def cart(self,lat,lng):
        token = yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]
        url= self.base_url+'/api/oms/mall/cart/list'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":token}
        data = {"lat":23.054853,"lng":113.368675}
        res = requests.post(url,headers=headers, json=data)
        return res.json()

    def add_cart(self,num,skuCode):
        token = yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]
        url= self.base_url+'/api/oms/mall/cart'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":token}
        data = {"cartItemDTOList":[{"num":num,"skuCode":skuCode}]}
        res = requests.post(url,headers=headers, json=data)
        return res.json()

    def delete_cart(self,skuCodes_list):
        token = yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]
        url= self.base_url+'/api/oms/mall/cart'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":token}
        data = {"skuCodes":skuCodes_list}
        res = requests.delete(url,headers=headers, json=data)
        return res.json()

    def get_user_info(self,id):
        token = yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]
        url= self.base_url+f'/api/uc/ucuser/get/{id}'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":token}
        res = requests.get(url,headers=headers)
        return res.json()

    def order_submit(self):
        token = yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]
        url = self.base_url + '/api/oms/mall/order/submit'
        headers = {"Content-Type": "application/json",
                   "appName": "wx9b8740e10bb42de5",
                   "token": token}
        data = {
                "orderShopRequestList": [
                    {
                        "shopCode": "SH00000YGP",
                        "orderSkuRequestList": [
                            {
                                "skuCode": "A0000127800001",
                                "skuType": "null",
                                "selfRun": 1,
                                "shopType": 1,
                                "brandCode": "41802425",
                                "brandName": "正美",
                                "categoryCode": "4100189",
                                "imageUrl": "https://qiniu-cdn-test.yigongpin.net/file/temporary/1645772404688-C2.jpg",
                                "modelCode": "C-01",
                                "skuAttr": "null",
                                "skuAttrValueList": "null",
                                "skuLadderPriceVO": "null",
                                "allowInvoice": "true",
                                "purchaseType": "非备货",
                                "salesUomId": "张",
                                "baseUomId": "张",
                                "salesUnitQty": 1,
                                "supplierCode": "null",
                                "leadTime": 1,
                                "outputTaxRate": 0.13,
                                "onSale": "true",
                                "salesMinIncrement": 1,
                                "salesMinOrderQty": 1,
                                "spuCode": "A00001278",
                                "spuName": "正美牌家华测试产品",
                                "skuName": "正美牌家华测试产品",
                                "shopCode": "SH00000YGP",
                                "shopName": "易工品官方旗舰店",
                                "merchantCode": "BU0000000000YGP",
                                "merchantName": "广州市易工品贸易有限公司",
                                "activitySkuVOList": [],
                                "activityLabel": "null",
                                "productPrice": 268,
                                "activityDiscountPrice": "null",
                                "vipPrice": "null",
                                "subtotalPrice": 268,
                                "subVipPrice": "null",
                                "num": 1,
                                "isCashOnDelivery": "false",
                                "supportCashOnDelivery": "false",
                                "activityTotalPrice": 0,
                                "salesUnitLength": 120,
                                "salesUnitWidth": 100,
                                "salesUnitHeight": 80,
                                "salesUnitGrossWeight": 50,
                                "shopBusinessType": "MRO",
                                "actId": "null",
                                "actCode": "null",
                                "isCashBack": "null",
                                "noStock": "false",
                                "skuLabelList": [
                                    {
                                        "labelName": "开票",
                                        "labelRuleDescription": "null"
                                    }
                                ],
                                "productLocationId": "1",
                                "elementContent": "搜索结果页",
                                "searchKeyword": "家华",
                                "skuTrackData": {
                                    "recommend_product_type": 0,
                                    "shop_element_content": "",
                                    "shop_location_id": "",
                                    "category_four": "",
                                    "use_coupon_name": "",
                                    "last_sku_id": "",
                                    "first_sku": "A0000127800001",
                                    "input_type": "文字输入"
                                }
                            }
                        ],
                        "isNeedInsteadDelivery": "false",
                        "isNeedInvoice": "true",
                        "transportType": 1,
                        "actId": "null",
                        "actCode": "null",
                        "isCashBack": "null"
                    }
                ],
                "orderType": 1,
                "payManner": 14,
                "payPeriod": "微信支付",
                "platformType": 13,
                "receiptId": "7827691",
                "spreaderMobile": "",
                "spreadSourceType": "",
                "spreadCode": "",
                "shareCode": "",
                "validStartTime": "",
                "validEndTime": "",
                "shareId": "no-share-id",
                "entrance": "/pages/product-detail/product-detail",
                "durationId": "d_1648447860534",
                "purchaseType": "直接购买",
                "transportType": "有货即发",
                "trackData": {
                    "identity_version": "",
                    "element_content": ""
                },
                "couponInstanceCode": "1506952781430956035",
                "promoteMobile": "",
                "isRedPacket": "true"
            }
        res = requests.post(url, headers=headers, json=data)
        return res.json()
    def from_cart_order_submit(self):
        token = yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]
        url = self.base_url + '/api/oms/mall/order/submit'
        headers = {"Content-Type": "application/json",
                   "appName": "wx9b8740e10bb42de5",
                   "token": token}
        data = {
                "orderShopRequestList": [
                    {
                        "shopCode": "SH00000YGP",
                        "orderSkuRequestList": [
                            {
                                "skuCode": "A0001148400001",
                                "skuType": "null",
                                "selfRun": 1,
                                "shopType": 1,
                                "brandCode": "41800340",
                                "brandName": "大意测试",
                                "categoryCode": "4100668",
                                "imageUrl": "https://qiniu-cdn-test.yigongpin.net/pms/product/img/2022-03-26/98846543b018f9226be794fd3f9819ac.jpg",
                                "modelCode": "H001",
                                "skuAttr": "null",
                                "skuAttrValueList": "null",
                                "skuLadderPriceVO": "null",
                                "allowInvoice": "true",
                                "purchaseType": "非备货",
                                "salesUomId": "台",
                                "baseUomId": "台",
                                "salesUnitQty": 1,
                                "supplierCode": "null",
                                "leadTime": 1,
                                "outputTaxRate": 0.13,
                                "onSale": "true",
                                "salesMinIncrement": 1,
                                "salesMinOrderQty": 1,
                                "spuCode": "A00011484",
                                "spuName": "家华呼吸机测试",
                                "skuName": "呼吸机一台",
                                "shopCode": "SH00000YGP",
                                "shopName": "易工品官方旗舰店",
                                "merchantCode": "BU0000000000YGP",
                                "merchantName": "广州市易工品贸易有限公司",
                                "activitySkuVOList": [],
                                "activityLabel": "null",
                                "productPrice": 368,
                                "activityDiscountPrice": "null",
                                "vipPrice": "null",
                                "subtotalPrice": 368,
                                "subVipPrice": "null",
                                "num": 1,
                                "isCashOnDelivery": "false",
                                "supportCashOnDelivery": "false",
                                "activityTotalPrice": 0,
                                "salesUnitLength": 40,
                                "salesUnitWidth": 20,
                                "salesUnitHeight": 25,
                                "salesUnitGrossWeight": 5,
                                "shopBusinessType": "MRO",
                                "actId": "null",
                                "actCode": "null",
                                "isCashBack": "null",
                                "noStock": "false",
                                "skuLabelList": [
                                    {
                                        "labelName": "开票",
                                        "labelRuleDescription": "null"
                                    }
                                ],
                                "productLocationId": "",
                                "elementContent": "",
                                "searchKeyword": "",
                                "skuTrackData": {
                                    "recommend_product_type": 0,
                                    "shop_element_content": "",
                                    "shop_location_id": "",
                                    "category_four": "",
                                    "use_coupon_name": "",
                                    "last_sku_id": "",
                                    "first_sku": "A0001148400001",
                                    "input_type": ""
                                }
                            }
                        ],
                        "isNeedInsteadDelivery": "false",
                        "isNeedInvoice": "true",
                        "transportType": 1,
                        "actId": "null",
                        "actCode": "null",
                        "isCashBack": "null"
                    }
                ],
                "orderType": 1,
                "payManner": 14,
                "payPeriod": "微信支付",
                "platformType": 13,
                "receiptId": "7827691",
                "spreaderMobile": "",
                "spreadSourceType": "",
                "spreadCode": "",
                "shareCode": "",
                "validStartTime": "",
                "validEndTime": "",
                "shareId": "no-share-id",
                "entrance": "/pages/shopping-cart/shopping-cart",
                "durationId": "d_1648447860534",
                "purchaseType": "常规加购",
                "transportType": "有货即发",
                "trackData": {
                    "identity_version": "",
                    "element_content": ""
                },
                "couponInstanceCode": "1506952781430956037",
                "promoteMobile": "",
                "isRedPacket": "true"
            }
        res = requests.post(url, headers=headers, json=data)
        return res.json()

    def order_pay(self,orderNo):
        token = yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]
        url= self.base_url+'/api/oms/payment/orderPay'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":token
                   }
        data = {"orderNo":orderNo,
                "payManner":"on_line",
                "openId":"oJ9Gc5XXiHpbJ_LIfU8uFpGNJcWI"}
        res = requests.post(url,headers=headers, json=data)
        return res.json()

    def pay_call_back(self,cusorderid,trxid,trxreserved):
        token = yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]
        url= self.base_url+'/api/oms/payment/orderPay/callBack'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":token
                   }
        data = {
                "acct": "null",
                "bizOrderNo": "null",
                "chnldata": "null",
                "chnltrxid": "null",
                "cusorderid": cusorderid,
                "fee": 0,
                "outtrxid": "null",
                "paytime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                "termauthno": "null",
                "termbatchid": "null",
                "termno": "null",
                "termrefnum": "null",
                "termtraceno": "null",
                "trxamt": 1,
                "trxcode": "VSP501",
                "trxdate": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                "trxid": trxid,
                "trxreserved":"{\"biz_order_no\":\"%s\",\"env\":\"test3\"}"%trxreserved,
                "trxstatus": "null"
            }
        res = requests.post(url,headers=headers, json=data)
        return res

    def get_order_detail(self,orderNo):
        token = yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]
        url= self.base_url+f'/api/oms/mall/order/detailPageV2?orderNo={orderNo}'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":token}
        res = requests.get(url,headers=headers)
        return res.json()

if __name__ == '__main__':
    base_api = Base_Api()
    base_api.register()




