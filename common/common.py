# -*- coding: utf-8 -*-
"""
@Time ： 2022/2/28 18:45
@Auth ： tanjiahua
@Email : tanjiahua@gongpin.com
"""
import pymysql
import redis
import rsa
import yaml
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
    print(result)
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


def rsa_encrypt(message):
    with open('rsa_public_key.pem','r') as f:
        pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
        text = rsa.encrypt(message.encode(), pubkey)
    return text

def write_yaml(file, data, encoding="utf-8"):
    "写入Yaml"
    with open(file, encoding=encoding, mode="w") as f:
        yaml.dump(data, stream=f, allow_unicode=True)

def read_yaml(file, encoding="utf-8"):
    "读取Yaml"
    data=yaml.safe_load(open(file, 'r', encoding=encoding))
    return data


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
