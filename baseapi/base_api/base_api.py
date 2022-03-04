# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/28 18:45
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import requests
import yaml
from common.common import link_redis, write_yaml, query
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootpath=str(curPath)
syspath=sys.path
depth = rootpath.count("\\") - 1
sys.path=[]
sys.path.append(rootpath)#将工程根目录加入到python搜索路径中
sys.path.extend([rootpath+i for i in os.listdir(rootpath) if i[depth]!="."])#将工程目录下的一级目录添加到python搜索路径中
sys.path.extend(syspath)

class Base_Api():

    base_url=yaml.safe_load(open('./test_data/env.yaml', 'r', encoding="utf-8"))["test1_url"]
    token=yaml.safe_load(open('./test_data/wxmini_token.yaml', 'r', encoding="utf-8"))["wxmini_token"]

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
        verifyCode=link_redis(phone,"test1")
        url = self.base_url + '/api/uc/god/register/distributor/getRegisterCertificate'
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
                    "unrecognized":False,
                    "delta":4,
                    "canSkip":False,
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
        password = query("select `password` from uc_user where mobile='%d';"%phone,"test1")
        headers = {"Content-Type": "application/json"}
        data={"accountOrMobile":phone,
              "password":password,
              "code":"063LrJkl2TseI84Xldol2dsbxX1LrJkl"}
        print(data)
        res = requests.post(url,headers=headers,json=data)
        print(res.json())
        token_data=res.json()["data"]["token"]
        if os.path.exists("./test_data/wxmini_token") == False:
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
        if os.path.exists("./test_data/wxmini_token") == False:
            write_yaml("./test_data/wxmini_token.yaml", token_data)
        return res.json()

    def productsearch(self,keyword):
        url= self.base_url+'/api/sc/search/appSearch/v2'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":self.token}
        data={"word":"测试店",
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
        url= self.base_url+'/api/sc/shop/search/listShop/V2'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":self.token}
        data = {"word": "测试店",
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
        url= self.base_url+'/api/pay/pay/mall/userAccount/balance'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":self.token}
        res = requests.get(url,headers=headers)
        return res.json()

    def get_location(self):
        url= self.base_url+'https://apis.map.qq.com/ws/geocoder/v1/?coord_type=5&get_poi=0&output=json&key=TWNBZ-PULL3-YZF35-YUIMQ-WBR5Q-7FBT2&location=23.08331%2C113.3172'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":self.token}
        res = requests.get(url,headers=headers)
        return res.json()

    def get_level1(self):
        url= self.base_url+'/api/pms/category/info/level1'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":self.token}
        res = requests.get(url,headers=headers)
        return res.json()

    def get_level34(self):
        url= self.base_url+'/api/pms/category/info/level34'
        headers = {"Content-Type": "application/json",
                   "appName":"wx9b8740e10bb42de5",
                   "token":self.token}
        res = requests.get(url,headers=headers)
        return res.json()


if __name__ == '__main__':
    base_api = Base_Api()
    base_api.register()




