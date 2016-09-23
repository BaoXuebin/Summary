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
def getHostName():
    return socket.gethostname()

def getComName():
    return socket.getfqdn(getHostName())

#获取本机ip
def getInnerIP():
    return socket.gethostbyname(getHostName())

# 获取本机mac地址
def getMacAddress():  
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]  
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

def getByBrowser(url):
    result = ''
    req = request.Request(url)
    # 伪装浏览器
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36')
    result = ""
    try:
        with request.urlopen(req) as f:
            if f.status == 200:
                result = f.read().decode('gbk')
            else:
                result = "1"
    except Exception as e:
        result = "2"
    
    return result
    
def getOuterIP():
    query_url = 'http://1212.ip138.com/ic.asp'
    result = getByBrowser(query_url)

    if result == "1":
        return "网络错误"
    elif result == "2":
        return "网络连接错误"
    else:
        # ['您的IP是：[116.226.120.26]', '来自：上海市徐汇区', '电信']
        result = ''.join(result.split('/')).split('<center>')[1].split(" ")

        outerIP = result[0].split('：')[1]
        local = result[1].split('：')[1] + " " + result[2]

        return outerIP + ' ' + local

def getComputerInfo():
    return '主机名:%s\nMAC地址:%s\n内网IP:[%s]\n外网IP:%s\n' % (getHostName(), getMacAddress(), getInnerIP(), getOuterIP())

desc = '\\ip: 查看电脑基本网络信息\n'
handle_func = getComputerInfo