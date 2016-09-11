#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-11 17:03:08
# @Author  : BaoXuebin

import os
import re
import json
from urllib import request
from urllib import parse
from tkinter import *

class CommandHandler(object):

	def __init__(self):
		pass

	def unknown(self, gui, command):
		gui.logResult("未知指令：" + command)

	def handle(self, gui, dic, command):
		if command.strip():
			action = command.lstrip('\\')
			meth = getattr(self, "do_" + action.upper(), None)
			try:
				meth(gui, dic)
			except TypeError:
				self.unknown(gui, command)

	def do_HELP(self, gui, dic):
		log = '''[help]\n\\dict 切换至字典模式\n\\translate 切换至翻译模式\n\\state 查看当前查询模式\n'''
		gui.logResult(log)

	def do_DICT(self, gui, dic):
		gui.logResult('已经切换至字典模式')
		dic.change2Dict()

	def do_TRANSLATE(self, gui, dic):
		gui.logResult('已经切换至翻译模式')
		dic.change2Translate()

	def do_STATE(self, gui, dic):
		gui.logResult('当前模式：' + dic.only)

class GUI(CommandHandler):

	def __init__(self):
		CommandHandler.__init__(self)
		self.root = Tk()
		self.root.attributes("-alpha", 1)
		self.root.title("Dict")
		self.root.geometry("200x190")
		self.root.resizable(width=False, height=False)
		self.search_image = PhotoImage(file='res/search.png').subsample(x='2', y='2')
		self.reset_image = PhotoImage(file='res/reset.png').subsample(x='2', y='2')

		self.query = Entry(self.root)
		self.searchBtn = Button(self.root, image=self.search_image, text="search")
		self.resetBtn = Button(self.root, image=self.reset_image, text="reset")
		self.result = Text(self.root)

		self.query.pack()
		self.searchBtn.pack()
		self.result.pack()

		self.query.place(x=2, y=3, width=140)
		self.searchBtn.place(x=146, y=1, height=25, width=25)
		self.resetBtn.place(x=173, y=1, height=25, width=25)
		self.result.place(width=196, height=150, x=2, y=29)

	# 输出执行结果
	def logResult(self, log):
		self.result.delete(0.0, END)
		self.result.insert(END, log)

	# 显示GUI
	def show(self, dic):
		def clearQuery(event):
			self.query.delete(0, END)
			self.query.insert(END, '')

		def query(event):
			word = self.query.get().strip()
			regex = re.compile('^\\\\')
			if regex.match(word): # 指令
				self.handle(self, dic, word)
			else: # 查询
				if word:
					self.result.delete(0.0, END)
					self.result.insert(END, dic.translate(word))
			self.query.delete(0, END)


		# 事件的绑定
		self.resetBtn.bind('<Button-1>', clearQuery)
		self.searchBtn.bind('<Button-1>', query)
		self.query.bind('<Key-Return>', query)
		self.root.mainloop()

class Dict(object):

	def __init__(self):
		self.key = '588759537'
		self.keyfrom = 'python-self-app'
		self.url = 'http://fanyi.youdao.com/openapi.do?'
		self.only = 'translate' # dict
		self.errors = {
			0: '正常',
			20: '要翻译的文本过长',
			30: '无法进行有效的翻译',
			40: '不支持的语言类型',
			50: '无效的key',
			60: '无词典结果'
		}

	def change2Dict(self):
		self.only = 'dict'

	def change2Translate(self):
		self.only = 'translate'

	def getByBrowser(self, url):
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
		
	def translate(self, word):
		query_url = '%skeyfrom=%s&key=%s&type=data&doctype=json&version=1.1&only=%s&q=%s' % (self.url, self.keyfrom, self.key, self.only, parse.quote(word))
		result = self.getByBrowser(query_url)
		strs = json.loads(result)
		errorCode = strs.get('errorCode')

		if errorCode != 0: # 查询出现异常
			result = word + "：\n" + self.errors.get(errorCode)
		elif self.only == 'translate': # 翻译
			result = word + "：\n" + "\n".join(strs.get('translation'))
		elif self.only == 'dict': # 字典
			result = word + "：\n" + "\n".join(strs.get('basic').get('explains'))

		return result

def main():
	gui = GUI()
	dic = Dict()

	gui.show(dic)

if __name__ == '__main__':
	main()