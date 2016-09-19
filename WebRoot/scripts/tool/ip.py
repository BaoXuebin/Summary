#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-19 15:18:34
# @Author  : BaoXuebin (baoxbin@hotmail.com)
# @Link    : ${link}
# @Version : $Id$

import uuid
import socket
from urllib import request
#获取本机电脑名
def getComName():
    return socket.getfqdn(socket.gethostname())

#获取本机ip
def getInnerIP():
    return socket.gethostbyname(getComName())

# 获取本机mac地址
def get_mac_address():  
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]  
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

def getByBrowser(url):
    result = ''
    req = request.Request(url)
    # 伪装浏览器
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36')
    with request.urlopen(req) as f:
        if f.status == 200:
            try:
                result = f.read().decode('utf-8')
            except Exception as e:
                result = 'error: ' + "UnicodeEncodeError"
        else:
            result = '网络断开'
    return result
    
def getOuterIP():
    query_url = 'http://1212.ip138.com/ic.asp'
    result = getByBrowser(query_url)
    print(result)
    return result

getOuterIP()