#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-18 23:06:14
# @Author  : BaoXuebin

import os
import re

def handle(word):
	if word.isdigit(): # 是数字
		num = int(word)
		mid = []
		while True:
			if num == 0: break
			num,rem = divmod(num, 2)
			mid.append(rem)
		return ''.join([str(x) for x in mid[::-1]])
	else: # 不是数字
		return "%s 不是数字类型" % word

def toString():
	return '\\binary: 十进制转二进制\n'

model = r'\binary'
handle_func = handle