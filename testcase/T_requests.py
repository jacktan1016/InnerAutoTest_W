import json

import requests
from utils.RequestsUtil import RequestsUtil
from config.Conf import ConfYaml
import os

request_util = RequestsUtil()
conf = ConfYaml()

def login():
    url = os.path.join(conf.get_yaml_data(),"authorizations/")
    # url = "http://211.103.136.242:8064/authorizations/"
    data = {"username": "python", "password": "12345678"}
    # r = requests.post(url, data=data)
    r = request_util.requests_api(url,method="post",json=data)
    return r

def info(token):
    url = os.path.join(conf.get_yaml_data(),"user/")
    # url = "http://211.103.136.242:8064/user/"
    headers = {
        "Authorization":"JWT "+token
    }
    return request_util.requests_api(url,headers=headers)
    # r = requests.get(url,headers=headers)
    # print(r.json())

def cate():
    url = os.path.join(conf.get_yaml_data(),"categories/115/skus/")
    # url = "http://211.103.136.242:8064/categories/115/skus/"
    data = {"page":"1","page_size":"10","ording":"create_time"}
    return request_util.requests_api(url,json=data)
    # r = requests.get(url,params=data)
    # print(r.json())

def cart(token):
    url = os.path.join(conf.get_yaml_data(),"cart/")
    # url = "http://211.103.136.242:8064/cart/"
    data = {"sku_id":"3","count":"1","selected":"true"}
    headers = {
        "Authorization": "JWT " + token
    }
    return request_util.requests_api(url,method="post",headers=headers,json=data)
    # r = requests.post(url,data=data,headers=headers)
    # print(r.json())

def order(token):
    url = "http://211.103.136.242:8064/orders/"
    data = {"address":"1","pay_method":"1"}
    headers = {
        "Authorization": "JWT " + token
    }
    r = requests.post(url,data=data,headers=headers)
    print(r.json())


if __name__=="__main__":
    # 首先登录，获取token
    r = login()
    print(r)
    # # 获取token
    str_token = r['body']['token']
    info_data = info(str_token)
    print(info_data)
    cate = cate()
    print("cate接口相关数据:{}".format(cate))
    # # 拿着token到用户中心
    cart = cart(str_token)
    print("cart接口相关数据:{}".format(cart))
    # order(str_token)