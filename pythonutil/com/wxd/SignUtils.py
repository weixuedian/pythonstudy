#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
import http.client
from urllib import request, parse
import time
import base64
import json
import random
import string

# 定义一些常量
APP_ID = '1106456615'
APP_KEY = 'iL8SJihPV0EmQz5q'
HOST = 'api.ai.qq.com'
TEXT_CHAT_URL = '/fcgi-bin/nlp/nlp_textpolar'

# MD5加密方法
def md5_str(str):
    hash = hashlib.md5()  # md5对象，md5不能反解，但是加密是固定的，就是关系是一一对应，所以有缺陷，可以被对撞出来
    hash.update(bytes(str, encoding='utf-8'))  # 要对哪个字符串进行加密，就放这里
    return hash.hexdigest().upper();


# 生成签名相关算法
def get_param_sign_str(param_arr):
    sb = '';
    for k in sorted(param_arr.keys()):
        if (0 < len(sb)):
            sb += '&' + k + '=' + parse.quote_plus(param_arr[k]);
        else:
            sb += k + '=' + parse.quote_plus(param_arr[k])
    sign_str = md5_str(sb + '&app_key=' + APP_KEY)
    return sign_str


# 获取Unix时间戳
def get_unix_time_str():
    t = time.time()
    return str(int(t))


# 获取随机字符窜
def get_nonce_str():
    return ''.join(random.sample(string.ascii_letters + string.digits, 10))


# 获取请求的url 以及参数组装
def get_request_url(param_arr):
    ret_str = TEXT_CHAT_URL + '?' + parse.urlencode(param_arr)
    return ret_str


# 情感分析
def get_textpolar(text):
    param_arr = {'app_id': APP_ID, 'nonce_str': get_nonce_str(), 'time_stamp': get_unix_time_str()};
    param_arr['text'] = text
    sign_str = get_param_sign_str(param_arr)
    param_arr['sign'] = sign_str
    all_url = get_request_url(param_arr)
    conn = http.client.HTTPSConnection(HOST)
    conn.request("POST", all_url)
    r1 = conn.getresponse()
    _retText = ''
    if (r1.status == 200):
        b = json.loads(r1.read())
        if (b['ret'] == 0):
            _retText = b
        else:
            print("接口请求错误，参数异常")
    else:
        print("出错了")
    return _retText

def ptu_facemerge(imageStr):
    param_arr = {'app_id': APP_ID, 'nonce_str': get_nonce_str(), 'time_stamp': get_unix_time_str()};
    param_arr['model'] = 1
    param_arr['image'] = imageStr
    sign_str = get_param_sign_str(param_arr)
    param_arr['sign'] = sign_str
    all_url = get_request_url(param_arr)
    conn = http.client.HTTPSConnection(HOST)
    conn.request("POST", all_url)
    r1 = conn.getresponse()
    _retText = ''
    if (r1.status == 200):
        b = json.loads(r1.read())
        if (b['ret'] == 0):
            _retText = b
        else:
            print("接口请求错误，参数异常")
    else:
        print("出错了")
    return _retText

ret_text_polar = get_textpolar('我儿子哭了')
print(ret_text_polar)


# with open("C:\\fbb.jpg","rb") as f:
#     # b64encode是编码，b64decode是解码
#     base64_data = base64.b64encode(f.read())
#     # base64.b64decode(base64data)
#     print(base64_data)
#     strs = ptu_facemerge(base64_data);
#     print(strs)



