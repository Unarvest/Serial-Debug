'''
@Author: your name
@Date: 2020-05-07 10:46:24
@LastEditTime: 2020-05-27 11:43:33
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Calculation\graph.py
'''

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:dell
from pyqtgraph import setConfigOption, GraphicsLayoutWidget, InfiniteLine, SignalProxy, setConfigOptions#, LabelItem
from pyqtgraph import exporters
from re import search
from datetime import datetime
import weakref


class MyGraphWindow():
	def __init__(self, window, BackColor='f0f0f4', antialias=True, showXY=True, showGrid=True, showPos=True, showPoint=True, showLegend=True):
		self.window = window
		self.grid = True
		self.logMode = False
		self.legend = True
		self.Max = None
		self.Min = None
		self.Times = 0
		self.allPen = {}        #key为color  红r, 绿g, 蓝b, 青c, 粉m, 黄y, 白w
		self.allName = []
		self.Pencolor = ''
		self.outFlag = ';'
		self.newWin = None
		self.antialias = antialias
		self.showXY = showXY
		self.showGrid = showGrid
		self.showPos = showPos
		self.showPoint = showPoint
		self.limit = 200
		self.showLegend = showLegend
		self.set_graph_ui(BackColor)  # 设置绘图窗口

	class pen():
		def __init__(self, name, color, data = [], Times = [], limit = 200):
			self.name = name
			self.show = 1
			self.countTime = 0
			self.data = []
			self.Times = []
			self.limit = limit
		def addNum(self, value, time):
			if self.limit != None:
				if len(self.data) < self.limit + 1:
					self.data.append(value)
					self.Times.append(self.countTime)
					self.countTime += time
				elif len(self.data) == self.limit + 1:
					self.data[:-1] = self.data[1:]
					self.data[-1] = value
				else:
					self.data = self.data[(lens - self.limit - 1):]
					self.Times = self.Times[:self.limit + 1]
					self.countTime = time * self.limit
			else:
				self.data.append(value)
				self.Times.append(self.countTime)
				self.countTime += time
			#print(time)

			#self.curve.setData(y = self.data, x = self.Times, pen = color)
		def clearNum(self):
			self.countTime = 0
			self.data.clear()
			self.Times.clear()

	def set_graph_ui(self, BackColor = 'f0f0f4'):
		setConfigOption('background', BackColor)
		if (BackColor == 'e3f9fd')|(BackColor == 'f0f0f4')|(BackColor == 'ffffff')|(BackColor == 'e0f0e9'):
			setConfigOption('foreground', 'k')
		setConfigOptions(antialias=self.antialias)  # pyqtgraph全局变量设置函数，antialias=True开启曲线抗锯齿
		self.graphWin = GraphicsLayoutWidget()
		self.window.addWidget(self.graphWin)
		self.graph = self.graphWin.addPlot(title="数据可视化", enableMenu=True)   # 添加第一个绘图窗口
		# self.view = weakref.ref(self.graph.vb)
		# self.view().setYRange(1.0, 100.0)
		#self.graph.addItem(self.smallShowLabel)
		#self.graph.setLabel('left', text='value')               # y轴设置函数
		if self.showXY:
			self.graph.setLabel('bottom', text='[ - , - ]')             # x轴设置函数
		if self.showGrid:
			self.graph.showGrid(x = self.grid, y = self.grid)       # 栅格设置函数
		self.graph.setLogMode(x = self.logMode, y = self.logMode)
		if self.showLegend:
			self.Legend = self.graph.addLegend()                    # 添加图例

		self.vLine = InfiniteLine(angle=90, movable=False)
		self.hLine = InfiniteLine(angle=0, movable=False)

		self.graph.addItem(self.vLine, ignoreBounds=True)
		self.graph.addItem(self.hLine, ignoreBounds=True)
		if self.showXY | self.showPos:
			self.proxy = SignalProxy(self.graph.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)

	def setY(self, Min, Max):
		self.graph.vb.setYRange(Min, Max)

	def setX(self, Min, Max):
		self.graph.vb.setXRange(Min, Max)

	def outputGraph(self, path = '.'):
		try:
			ex = exporters.ImageExporter(self.graphWin.scene())
			name = datetime.now().strftime("%Y%m%d-%H%M%S.png")
			ex.export(fileName= (path + '\\' + name))
			return name
		except Exception as e:
			print('错误：', e)
			return False

	def addPen(self, color, name, data = [], Times = [], limit = 200):
		self.limit = limit
		canadd = 1
		if search(color, self.Pencolor) == None:
			for i in self.Pencolor:
				if self.allPen[i].name == name:
					canadd = 0
			if canadd:
				self.allPen[color] = self.pen(name, color, data, Times, limit = self.limit)
				self.Pencolor += color
				if self.showPoint:
					self.allPen[color].plot = self.graph.plot(pen=color, name=name,symbolBrush=(141,75,187))
				else:
					self.allPen[color].plot = self.graph.plot(pen=color, name=name)
				for color_ in self.Pencolor:
					if color_ != color:
						print(1)
						#self.allPen[color_].plot.setData(y = self.allPen[color_].data, x = self.allPen[color_].Times, pen = color_)
				self.graph.addItem(self.vLine, ignoreBounds=True)
				self.graph.addItem(self.hLine, ignoreBounds=True)
				return True
			else:
				print('名字重复')
				return None
		else:
			print('颜色已存在')
			return False

	def appendNum(self, color, num, time):
		if search(color, self.Pencolor) == None:
			print('颜色不存在')
		else:
			self.allPen[color].addNum(num, time)
			self.allPen[color].plot.setData(x = self.allPen[color].Times, y = self.allPen[color].data, pen = color)

	def updateData(self):
		for color in self.Pencolor:
			self.allPen[color].plot.clear()
		for color in self.Pencolor:
			self.allPen[color].plot.setData(x = self.allPen[color].Times, y = self.allPen[color].data, pen = color)

	def changeLimit(self, limit):
		for color in self.Pencolor:
			self.allPen[color].limit = limit
			self.limit = limit
			if limit != None:
				lens = len(self.allPen[color].data)
				if lens > limit + 1:
						self.allPen[color].countTime = int(self.allPen[color].countTime*(limit + 1)/len(self.allPen[color].data))
						self.allPen[color].data = self.allPen[color].data[(lens - self.limit - 1):]
						self.allPen[color].Times = self.allPen[color].Times[:self.limit + 1]
						#self.allPen[color].data = self.allPen[color].data[:self.limit + 1]
						#self.allPen[color].Times = self.allPen[color].Times[:self.limit + 1]
				self.updateData()



	def clearAll(self):
		for i in self.Pencolor:
			self.allPen[i].clearNum()
			self.allPen[i].plot.clear()

	def killPen(self, color):
		pos = search(color, self.Pencolor)
		if pos == None:
			print('颜色不存在')
		else:
			self.allPen[color].plot.clear()
			self.Legend.removeItem(self.allPen[color].name)
			for color_ in self.Pencolor:
				if color_ != color:
					print(1)
					#self.allPen[color_].plot.setData(y = self.allPen[color_].data, x = self.allPen[color_].Times, pen = color_)
			pos = pos.span()
			self.Pencolor = self.Pencolor[:pos[0]] + self.Pencolor[pos[1]:]
			self.allPen[color].clearNum()

	def hindPen(self, color):
		if search(color, self.Pencolor) == None:
			print('颜色不存在')
			return None
		else:
			self.allPen[color].plot.clear()
			self.Legend.removeItem(self.allPen[color].name)
			for color_ in self.Pencolor:
				if color_ != color:
					self.allPen[color_].plot.setData(y = self.allPen[color_].data, x = self.allPen[color_].Times, pen = color_)
			return True

	def showPen(self, color):
		if search(color, self.Pencolor) == None:
			print('颜色不存在')
		else:
			self.Legend.addItem(self.allPen[color].plot, self.allPen[color].name)
			self.allPen[color_].plot.setData(y = self.allPen[color].data, x = self.allPen[color].Times, pen = color)


	def moreWin(self, window):
		if self.newWin == None:
			self.newWin = MyGraphWindow(window)

	def inputData(self, color):
		pass

	def outputData(self, color):
		pass

	def formatData(self, data = '', time = 1):
		data = data.replace(' ', '')
		while len(data) > 0:
			pos = search("\w*=\d\.*\d*;", data)
			if pos != None:
				pos = pos.span()
				part = data[pos[0]:pos[1]]
				name = search("\w*=", part)
				value = search("=\d\.*\d*", part)
				if (name != None) & (value != None):
					name = part[name.span()[0]:name.span()[1]-1]
					value = part[value.span()[0] + 1:value.span()[1]]
					for color in self.Pencolor:
						if name == self.allPen[color].name:
							try:
								if value.isdigit():
									self.appendNum(color = color, num = int(value), time = time)
								else:
									self.appendNum(color = color, num = float(value), time = time)
							except Exception as e:
								print('错误:', e)
			else:
				return None
			data = data[pos[1]:]
		return True


		# self.Times += time
		# dataflag = True
		# flag = False
		# data = data.replace(' ', '')
		# while(dataflag):
		#     name = ''
		#     dataflag = False
		#     for color in self.Pencolor:
		#         flag = False
		#         num = ''
		#         name = self.allPen[color].name
		#         pos = search(name + '=', data)
		#         if pos != None:
		#             pos = pos.span()
		#             for i in data[pos[1]:]:
		#                 if i == self.outFlag:
		#                     flag = True
		#                     break
		#                 else:
		#                     num += i
		#             if flag == True:
		#                 try:
		#                     if num.isdigit():
		#                         self.appendNum(color = color, num = int(num), time = time)
		#                     else:
		#                         self.appendNum(color = color, num = float(num), time = time)
		#                 except Exception as e:
		#                     print('错误:', e)
		#                     flag =  False    #数据转换错误
		#             else:
		#                 flag =  None   #无截止符
		#             data = data[:pos[0]] + data[pos[1]:] + str(num) + ';'
		#             dataflag = True

		# if flag == False:
		#     return None  #无所需数据

	def mouseMoved(self, evt):
		vb = self.graph.vb
		pos = evt[0]  ## using signal proxy turns original arguments into a tuple
		if self.graph.sceneBoundingRect().contains(pos):
			try:
				mousePoint = vb.mapSceneToView(pos)
				pos_x = mousePoint.x()
				pos_y = mousePoint.y()
				if self.showXY:
					self.graph.setLabel('bottom', text='[ {:.2f} , {:.2f} ]'.format(pos_x, pos_y))
				if self.showPos:
					self.vLine.setPos(mousePoint.x())
					self.hLine.setPos(mousePoint.y())
			except Exception as e:
				print('错误: ', e)
				pass


