import requests

# 封装get方法
# def request_get(url,headers=None,data=None):
#     r = requests.get(url,headers=headers,json=data)
# # 发送request请求
#     code =r.status_code
#     try:
#         body = r.json()
#     except:
#         body = r.text
#     d = dict()
#     d["code"] = code
#     d["body"] = body
#     return d
#
# def request_post(url,headers=None,data=None):
#     r = requests.post(url,headers=headers,json=data)
#     code = r.status_code
#     try:
#         body = r.json()
#     except:
#         body = r.text
#     d = dict()
#     d["code"] = code
#     d["body"] = body
#     return d

class RequestsUtil:

    def requests_api(self,url,method="get",headers=None,json=None):
        method = method.lower()
        r = None
        if method=="get":
            r = requests.get(url, headers=headers, json=json)
        if method=="post":
            r = requests.post(url, headers=headers, json=json)
        code = r.status_code
        try:
            body = r.json()
        except:
            body = r.text
        res = dict()
        res["code"] = code
        res["body"] = body
        return res

