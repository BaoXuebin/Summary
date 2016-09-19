#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-17 20:49:32
# @Author  : BaoXuebin

import os
from tkinter import *
import re
sys.path.append('extension')
import dict_
import binary

class CommandHandler(object):

	def __init__(self, model_dict={}):
		self.model_dict = model_dict
		self.model = '\dict'
		self.handle_func = model_dict.get('\dict')

	def handle_next(self, word):
		if word in self.model_dict.keys():
			self.model = word
			self.handle_func = self.model_dict.get(word)
			return('已切换至%s模式' % word)
		else:
			return("未知指令：" + word)

	def handle(self, word):
		regex = re.compile('^\\\\')
		if regex.match(word): # 指令
			action = word.lstrip('\\')
			meth = getattr(self, "do_" + action.upper(), None)
			try:
				return meth()
			except TypeError:
				return self.handle_next(word)
		else:
			return self.handle_func(word)

	def do_HELP(self):
		return '''[help]\n\\state 查看当前查询模式\n''' + dict_.desc + binary.desc

	def do_STATE(self):
		return '当前模式：' + self.model



class GUI(CommandHandler):
	def __init__(self, model_dict):
		CommandHandler.__init__(self, model_dict)
		self.root = Tk()
		self.root.attributes("-alpha", 1)
		self.root.title("Tool 1.0")
		self.root.geometry("500x360")
		self.root.resizable(width=False, height=False)
		self.search_image = PhotoImage(file='res/search.png').subsample(x='2', y='2')
		self.reset_image = PhotoImage(file='res/reset.png').subsample(x='2', y='2')

		self.query = Entry(self.root, font="Arial 12")
		self.searchBtn = Button(self.root, image=self.search_image, text="search")
		self.resetBtn = Button(self.root, image=self.reset_image, text="reset")
		self.result = Text(self.root, state='normal', font="12")

		self.query.pack()
		self.searchBtn.pack()
		self.result.pack()

		self.query.place(x=10, y=5, width=420, height=25)
		self.searchBtn.place(x=435, y=5, height=25, width=25)
		self.resetBtn.place(x=465, y=5, height=25, width=25)
		self.result.place(width=480, height=310, x=10, y=40)

	# 输出执行结果
	def logResult(self, log):
		self.result.delete(0.0, END)
		self.result.insert(END, log)

	# 显示GUI
	def show(self):
		self.query.focus_set()
		# 事件的绑定
		self.resetBtn.bind('<Button-1>', self.clearQuery)
		self.searchBtn.bind('<Button-1>', self.queryResult)
		self.query.bind('<Key-Return>', self.queryResult)
		self.root.mainloop()

	def clearQuery(self, event):
			self.query.delete(0, END)
			self.query.insert(END, '')

	def queryResult(self, event):
		word = self.query.get().strip()
		if word:
			self.result.delete(0.0, END)
			self.result.insert(END, self.handle(word))
			# self.result.insert(END, '')
			self.query.delete(0, END)

def main():
	model_dict = {}
	model_dict[dict_.model] = dict_.handle_func
	model_dict[binary.model] = binary.handle_func
	
	gui = GUI(model_dict)
	gui.show()

if __name__ == '__main__':
	main()