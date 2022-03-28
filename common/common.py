# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/28 18:45
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import base64
import hashlib
import pymysql
import redis
import rsa
import yaml
import os
path = os.path.dirname(os.path.abspath(__file__))

def link_redis(key,env_mark):
    dict = yaml.safe_load(open('./test_data/env.yaml', 'r', encoding="utf-8"))
    r=redis.StrictRedis(host=dict[env_mark]['redis_ip'],
                        password=dict[env_mark]['redis_password'],
                        port=6379,
                        db=dict[env_mark]['redis_db'],
                        decode_responses = True)
    res=r.get('uc:sms:smscode:FRONT:REGISTER:%s'%key)
    return res

def link_mysql(env_mark):
    dict = yaml.safe_load(open('./test_data/env.yaml', 'r', encoding="utf-8"))
    db = pymysql.connect(host=dict[env_mark]["host"],
                         user=dict[env_mark]["user"],
                         password=dict[env_mark]["password"],
                         database=dict[env_mark]["database"])

    return db

def insert(sql, env_mark):
    conn = link_mysql(env_mark)
    cur = conn.cursor()
    result = cur.execute(sql)
    conn.commit()
    cur.close()
    # conn.close()
    return result


def insert_args(sql, env_mark, args):
    conn = link_mysql(env_mark)
    cur = conn.cursor()
    result = cur.execute(sql, args)
    conn.commit()
    cur.close()
    conn.close()
    return result


def update_many(sql, env_mark, arg):
    conn = link_mysql(env_mark)
    cur = conn.cursor()
    result = cur.executemany(sql, arg)
    conn.commit()
    cur.close()
    # conn.close()
    return result


def update(sql, env_mark):
    conn = link_mysql(env_mark)
    cur = conn.cursor()
    result = cur.execute(sql)
    conn.commit()
    cur.close()
    # conn.close()
    return result


def query(sql, env_mark):
    conn = link_mysql(env_mark)
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchone()[0]
    cur.close()
    # conn.close()
    return result


def delete(sql, env_mark):
    conn = link_mysql(env_mark)
    cur = conn.cursor()
    result = cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    return result

def write_yaml(file, data, encoding="utf-8"):
    "写入Yaml"
    with open(file, encoding=encoding, mode="w") as f:
        yaml.dump(data, stream=f, allow_unicode=True)

def read_yaml(file, encoding="utf-8"):
    "读取Yaml"
    data=yaml.safe_load(open(file, 'r', encoding=encoding))
    return data

def MD5(data):
    md5 = hashlib.md5()
    md5.update(data.encode(encoding="utf-8"))
    res_data=md5.hexdigest()
    return res_data

def write_data(token):
    from ruamel import yaml
    data = {'wxmini_token': token}
    with open('./test_data/wxmini_token.yaml', 'r+', encoding="utf-8") as f:
        f.write(yaml.dump(data, Dumper=yaml.RoundTripDumper))

# link_mysql("test1")
# print(link_redis("15746289471","test1"))

# data={"wx_token":
#   "7cb2337e485cfae72d4deba1194d0061"}
# write_yaml("./test_data/wxmini_token.yaml",data)
# print(read_yaml('./test_data/wxmini_token.yaml'))
# print(rsa_encryp
#
# t("ygp123456"))


# phone=15700001001
# query("select `password` from uc_user where account='%d';"%phone,"test1")
# insert("INSERT INTO `ygp_udc`.`browsing_record`( `user_code`, `sku_code`, `date_value`, `create_time`, `update_time`, `active`, `creator`, `creator_code`, `updater`, `updater_code`) VALUES ( 'UC1496317675387289601', 'MFD00021', '2022-03-15', '2022-03-15 17:39:58.000', '2022-03-15 17:39:58.000', 1, '15700001001', 'UC1496317675387289601', '15700001001', '15700001001');"
#     ,"test1")