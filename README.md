***
基于 python3 和 pytest 搭建的接口自动化测试框架

基于 APIObject 封装思想搭建

适用于易工品内部接口自动化流程测试

**项目目录结构**

- baseapi 调用的主要api接口文件
- common  封装好的方法
- test_data 测试数据存放
- tset_case 测试用例调用
- report 测试报告存放目录

**运行环境请看Wiki**

http://wiki.yigongpin.net/confluence/pages/viewpage.action?pageId=34509012

**常用命令**

一键安装依赖项目命令，如果有安装包安装失败，请单独执行“pip install 包名”

pip install -r requirements.txt 

**本地执行测试用例,并生产测试报告在allure中**

pytest 测试用例目录、文件 --alluredir ./report

**查看allure测试报告**

allure serve report

**提交注释格式**

常规提交,先拉最新代码，添加新代码，提交后，推送到git

git pull

git add .

git commit -m "更新内容"

git push


名称规范
***
测试用例文件夹：

- 采用短横线命名(test-CaseInterface),例如test_接口名称

测试.py文件：

- 采用短横线命名(test-CaseInterface),例如test_接口名称

测试类class：

- 大写Test开头加接口名称(TestInterface)，例如TestCooperationBusiness

测试函数def：

- 小写test开投短横线拼接(test_case),例如test_CooperationBusiness

使用
***
Run类-运行当前类所有测试用例

Run方法-运行当前方法对应测试用例

Run文件-运行当前项目全部测试用例

技术栈
***
- python3
- pytest
- allure
- pymysql
- pyyaml
- requests