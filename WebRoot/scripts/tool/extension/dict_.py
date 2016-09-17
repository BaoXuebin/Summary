#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-17 22:58:03
# @Author  : BaoXuebin

import os
import json
from urllib import request
from urllib import parse

key = '588759537'
keyfrom = 'python-self-app'
url = 'http://fanyi.youdao.com/openapi.do?'
only = 'dict' # dict
errors = {
	0: '正常',
	20: '要翻译的文本过长',
	30: '无法进行有效的翻译',
	40: '不支持的语言类型',
	50: '无效的key',
	60: '无词典结果'
}
	
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
			result = 'error: ' + f.status

	return result
	
def translate(word):
	query_url = '%skeyfrom=%s&key=%s&type=data&doctype=json&version=1.1&only=%s&q=%s' % (url, keyfrom, key, only, parse.quote(word))
	result = getByBrowser(query_url)
	strs = json.loads(result)
	errorCode = strs.get('errorCode')

	if errorCode != 0: # 查询出现异常
		result = word + "：\n" + errors.get(errorCode)
	elif only == 'translate': # 翻译
		result = word + "：\n" + "\n".join(strs.get('translation'))
	elif only == 'dict': # 字典
		result = word + "：\n" + "\n".join(strs.get('basic').get('explains'))

	return result


model = '\dict'
handle_func = translate
