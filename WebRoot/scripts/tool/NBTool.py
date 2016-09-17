#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-17 20:49:32
# @Author  : BaoXuebin

import os
from tkinter import *
import re
sys.path.append('extension')
import dict_

class CommandHandler(object):

	def __init__(self, model_dict={}):
		self.model_dict = model_dict
		self.model = model_dict.get(0)
		self.handle_func = model_dict.get('\dict')

	def handle(self, word):
		regex = re.compile('^\\\\')
		if regex.match(word): # 指令
			if word in self.model_dict.keys():
				self.model = word
				self.handle_func = self.model_dict.get(word)
				print('model: ' + self.model)
				print(self.handle_func)
				return('已切换至%s模式' % word)
			else:
				return("未知指令：" + word)
		else:
			return self.handle_func(word)

class GUI(CommandHandler):
	def __init__(self, model_dict):
		CommandHandler.__init__(self, model_dict)
		self.root = Tk()
		self.root.attributes("-alpha", 1)
		self.root.title("Tool 1.0")
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
	def show(self):
		def clearQuery(event):
			self.query.delete(0, END)
			self.query.insert(END, '')

		def query(event):
			word = self.query.get().strip()
			self.result.delete(0.0, END)
			self.result.insert(END, self.handle(word))
			self.query.delete(0, END)

		# 事件的绑定
		self.resetBtn.bind('<Button-1>', clearQuery)
		self.searchBtn.bind('<Button-1>', query)
		self.query.bind('<Key-Return>', query)
		self.root.mainloop()

def main():
	model_dict = {}
	model_dict[dict_.model] = dict_.handle_func

	gui = GUI(model_dict)
	gui.show()

if __name__ == '__main__':
	main()