import sys
from PySide6 import QtWidgets, QtCore

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from PySide6.QtCharts import *
from ui.draw_widget_ui import Ui_Draw_Widget
import math, time

import multiprocessing
MAX_POINT = 1000

'''

def Cal_Process(buffer_map, points_map, args_pipe):
	while True:
		(step, x_max, max_diff, max_len) = args_pipe[1].recv()

		for line_name in buffer_map.keys():
			buffer = buffer_map[line_name]
			points = points_map[line_name]
			points.clear()
			buffer_len = len(buffer)
			index = int(buffer_len - max_diff)
			diff = max_len - buffer_len
			while index < x_max:
				if index < 0:
					# line._points.append(QPointF(index, 0))
					pass
				elif index >= buffer_len:
					break
				else:
					points.append(QPointF(index+diff, buffer[index]))
				index += step
			if index < buffer_len:
				points.append(QPointF(index+diff, buffer[index]))
		args_pipe[0].send(True)
'''
class My_Chart_View(QChartView):
	f = 0
	def __init__(self, mainwindow):
		super(My_Chart_View, self).__init__(mainwindow)
		# self.raise_()
		self.setContentsMargins(0,0,0,0)
		self.mainwindow = mainwindow
		self.auto_Stretch = True
		self.line_map = {}
		'''
		self.buffer_map = multiprocessing.Manager().dict()
		self.points_map = multiprocessing.Manager().dict()
		self.arg_pipe = multiprocessing.Pipe()
		self.cal_process = multiprocessing.Process(target=Cal_Process, args=(self.buffer_map, self.points_map, self.arg_pipe))
		self.cal_process.start()
		'''
		self.max_len = 0
		self.max_value = float('inf')
		self.min_value = float('-inf')
		self.y_limit = [-1, 1, False]
		self.x_limit = [0, 1, False]
		self.slider_flag = True
		self._chart = QChart()  # 创建折线视图
		self._chart.setAnimationOptions(QChart.NoAnimation)
		self._chart.setContentsMargins(0,0,0,0)
		self._chart.setBackgroundVisible(visible=False)      # 背景色透明
		self._chart.setBackgroundBrush(QBrush(QColor("#000FFF")))     # 改变图背景色
		#  图形项默认无法接收悬停事件，可以使用QGraphicsItem的setAcceptHoverEvents()函数使图形项可以接收悬停事件。
		# self._chart.setAcceptHoverEvents(True)
		self._axis_x = QValueAxis()
		self._axis_x.setRange(self.x_limit[0], self.x_limit[1])
		self._axis_x.setLabelFormat("%d")
		
		self._axis_x.setTickCount(10)
		self._axis_y = QValueAxis()
		self._axis_y.setRange(self.y_limit[0], self.y_limit[1])
		self._axis_y.setTickCount(10)
		# self._axis_y.setTitleText("value")
		self._chart.setAxisX(self._axis_x)
		self._chart.setAxisY(self._axis_y)

		self.setChart(self._chart)
		self.show_thread = Show_Data_Thread(self)

	def create_series(self):
		t = time.time()
		v = self.max_len / 50
		dataTable = pow(math.sin(v), 2) * math.cos(v)
		# dataTable = self.i
		# if self.max_len < 2000:
		self.append_data('test1', dataTable)
		self.append_data('test2', dataTable + 1)
		self.append_data('test3', dataTable + 0.5)
		self.append_data('test4', dataTable -0.5)
		
		# self.f = time.time() - t
		# self.series.append(self.i, dataTable)
		# self.series2.append(self.i, dataTable+20)
		# self.i += 0.1

		# # 当时间轴大于现有时间轴，进行更新坐标轴，并删除之前数据
		# if self.i>=5 :
		# 	self.chart._chart.axisX().setRange(0, self.i)
		# if self.series.count() > 3000:
		#     self.series.removePoints(0, self.series.count() - 100)
		# if self.series2.count() > 3000:
		#     self.series2.removePoints(0, self.series2.count() - 100)
		pass
	
	def append_series(self, series_name):
		line = Line(self)
		line.setName(series_name)
		self.line_map[series_name] = line
		# self.buffer_map[series_name] = multiprocessing.Manager().list()
		# print('test:', self.buffer_map[series_name])
		# self.points_map[series_name] = []
		line._points = []
		line.append(line._points)
		self._chart.addSeries(line)
		self._chart.setAxisX(self._axis_x, line)
		self._chart.setAxisY(self._axis_y, line)

	def append_data(self, name, value):
		try:
			current_line = self.line_map[name]
		except KeyError:
			return False
		current_line._buffer.append(value)
		# self.buffer_map[name].append(value)
		# print(self.buffer_map[name])
		buffer_len = len(current_line._buffer)
		
		if self.auto_Stretch:
			if (value < self._axis_y.min()) & (value > self.min_value):
				self.y_limit[0] = value
				self.y_limit[2] = True
			if (value > self._axis_y.max()) & (value < self.max_value):
				self.y_limit[1] = value
				self.y_limit[2] = True
			
			if self.max_len > MAX_POINT:
				if buffer_len > self.max_len:
					self.x_limit[0] += 1
			self.x_limit[1] = self.max_len
			self.x_limit[2] = True
			# else:
			# 	self._axis_x.setRange(x_min, self.max_len)
			# self.show_data()
		if buffer_len > self.max_len:
			self.max_len = buffer_len
		if self.slider_flag:
			self.mainwindow.ui.graphScrollBar.setValue(self.x_limit[0])
			self.mainwindow.ui.graphScrollBar.setMaximum(self.max_len-self.x_limit[1]+self.x_limit[0])
		# except Exception as e:
		# 	print(e, x_max, x_min, len(current_line._buffer))
	
	def show_data2(self):
		if self.x_limit[2]:
			x_min = self.x_limit[0]
			x_max = self.x_limit[1]
		else:
			x_min = int(self._axis_x.min())
			x_max = int(self._axis_x.max())
		
		# self.mainwindow.ui.graphScrollBar.setPageStep(x_max-x_min)
		max_diff = self.max_len - x_min
		step = int((x_max - x_min) / MAX_POINT)
		if step == 0:
			step = 1
		t = time.time()
		self.arg_pipe[0].send((step, x_max, max_diff, self.max_len))
		print('send time: {}'.format(time.time() - t))
		if self.y_limit[2]:
			self.y_limit[2] = False
			self._axis_y.setRange(self.y_limit[0], self.y_limit[1])

		if self.x_limit[2]:
			self.x_limit[2] = False
			self._axis_x.setRange(x_min, x_max)
		print('setrange :{}'.format(time.time() - t))
		t = time.time()
		self.arg_pipe[1].recv()
		for line_name in self.line_map:
			line = self.line_map[line_name]
			line.replace(self.points_map[line_name])
			if line.scatter != None:
				line.scatter.replace(self.points_map[line_name])
				cnt = 0
				for p in self.points_map[line_name]:
					cnt += p.y()
				if len(self.points_map[line_name]) > 0:
					line.scatter.setName('avg:' + str(round(cnt/len(self.points_map[line_name]), 2)))
		self.f += 1
		print('replace all: {}'.format(time.time() - t))


	
	def show_data(self):
		if self.x_limit[2]:
			x_min = self.x_limit[0]
			x_max = self.x_limit[1]
		else:
			x_min = int(self._axis_x.min())
			x_max = int(self._axis_x.max())
		
		# self.mainwindow.ui.graphScrollBar.setPageStep(x_max-x_min)
		max_diff = self.max_len - x_min
		step = int((x_max - x_min) / MAX_POINT)
		if step == 0:
			step = 1
		# t = time.time()
		for line_name in self.line_map:
			line = self.line_map[line_name]
			line._points.clear()
			# line.clear()
			buffer_len = len(line._buffer)
			index = int(buffer_len - max_diff)
			diff = self.max_len - buffer_len
			while index < x_max:
				if index < 0:
					# line._points.append(QPointF(index, 0))
					pass
				elif index >= buffer_len:
					break
				else:
					line._points.append(QPointF(index+diff, line._buffer[index]))
				index += step
			if index < buffer_len:
				line._points.append(QPointF(index+diff, line._buffer[index]))
		# print('cal {}:{}'.format(line_name, time.time() - t))
		# t = time.time()
		if self.y_limit[2]:
			self.y_limit[2] = False
			self._axis_y.setRange(self.y_limit[0], self.y_limit[1])

		if self.x_limit[2]:
			self.x_limit[2] = False
			self._axis_x.setRange(x_min, x_max)
		# print('setrange :{}'.format(time.time() - t))
		# t = time.time()
		for line_name in self.line_map:
			line = self.line_map[line_name]
			line.replace(line._points)
			if line.scatter != None:
				line.scatter.replace(line._points)
				cnt = 0
				for p in line._points:
					cnt += p.y()
				if len(line._points) > 0:
					line.scatter.setName('avg:' + str(round(cnt/len(line._points), 2)))
		self.f += 1
		# print('replace all: {}'.format(time.time() - t))


class Show_Data_Thread(QThread):
	set_axis_y = Signal(float, float)
	set_axis_x = Signal(float, float)

	def __init__(self, parent:My_Chart_View):
		super(Show_Data_Thread, self).__init__(parent)
		self._parent = parent
		self.continue_flag = False
		self.set_axis_x.connect(self._parent._axis_x.setRange)
		self.set_axis_y.connect(self._parent._axis_y.setRange)
		self.start()
	
	def run(self):
		while True:
			while self.continue_flag != True:
				self.msleep(1)
			self.continue_flag = False
			if self._parent.x_limit[2]:
				x_min = self._parent.x_limit[0]
				x_max = self._parent.x_limit[1]
			else:
				x_min = int(self._parent._axis_x.min())
				x_max = int(self._parent._axis_x.max())
			
			# self._parent.mainwindow.ui.graphScrollBar.setPageStep(x_max-x_min)
			max_diff = self._parent.max_len - x_min
			step = int((x_max - x_min) / MAX_POINT)
			if step == 0:
				step = 1
			for line_name in self._parent.line_map:
				line = self._parent.line_map[line_name]
				line._points.clear()
				# line.line_clear_sig.emit()
				buffer_len = len(line._buffer)
				index = int(buffer_len - max_diff)
				diff = self._parent.max_len - buffer_len
				while index < x_max:
					if index < 0:
						# line._points.append(QPointF(index, 0))
						pass
					elif index >= buffer_len:
						break
					else:
						line._points.append(QPointF(index+diff, line._buffer[int(index)]))
					index += step
				if index < buffer_len:
					line._points.append(QPointF(index+diff, line._buffer[index]))
			
			if self._parent.y_limit[2]:
				self._parent.y_limit[2] = False
				self.set_axis_y.emit(self._parent.y_limit[0], self._parent.y_limit[1])

			if self._parent.x_limit[2]:
				self._parent.x_limit[2] = False
				self.set_axis_x.emit(x_min, x_max)

			
			for line_name in self._parent.line_map:
				line = self._parent.line_map[line_name]
				line.line_replace_sig.emit(line._points)
				line.scatter_replace_sig.emit()
				
			self._parent.f += 1

	def set_continue(self):
		self.continue_flag = True

class Line(QLineSeries):
	line_replace_sig = Signal(list)
	line_clear_sig = Signal()
	scatter_replace_sig = Signal()
	def __init__(self, parent=None):
		super(Line, self).__init__(parent)
		self.setUseOpenGL(True)
		self._buffer = []
		self._points = []
		self.show_buffer = []
		self.line_diff = 0
		self.scatter = None
		self.scatter_replace_sig.connect(self.update_scatter)
		self.line_replace_sig.connect(self.replace)
		self.line_clear_sig.connect(self.clear)
	
	def update_scatter(self):
		if self.scatter != None:
			self.scatter.replace(self._points)
			cnt = 0
			for p in self._points:
				cnt += p.y()
			if len(self._points) > 0:
				self.scatter.setName('avg:' + str(round(cnt/len(self._points), 2)))

	def delete_scatter(self):
		if self.scatter is not None:
			self.scatter.deleteLater()
			self.scatter = None
	
	def append_scatter(self, chart):
		if self.scatter == None:
			self.scatter = QScatterSeries()
			self.scatter.setColor(self.color())
			chart._chart.addSeries(self.scatter)
			chart._chart.setAxisX(chart._axis_x, self.scatter)
			chart._chart.setAxisY(chart._axis_y, self.scatter)
			

class Graph_View(QWidget):
	# view 总窗口
	def __init__(self):
		super(Graph_View, self).__init__()
		self.ui = Ui_Draw_Widget()
		# self.setupUi(self)
		# self.setGeometry(QtCore.QRect(0, 0, 980, 480))
		
		self.i=0
		self.scatter_num = 100
		self.limit_points = [200, 1000]
		self.showfps = True
		self.auto_set_point = True
		# self.fi = 0
		# self.f_list = []
		# 执行折线视图函数

		self.setup()
		self.create_chart()
		

	def setup(self):
		self.ui.setupUi(self)
		self.setContentsMargins(0,0,0,0)
		graphSplitterV = QSplitter(Qt.Vertical)
		graphSplitterV.addWidget(self.ui.graphFrame)
		graphSplitterV.addWidget(self.ui.graphSetFrame)
		self.ui.verticalLayout.addWidget(graphSplitterV)

		self.chart = My_Chart_View(self)
		
		self.chart.setRubberBand(QChartView.VerticalRubberBand)
		# self.chart.setGeometry(QtCore.QRect(0, 0, 980, 480))
		self.chart.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
		self.ui.graphLayout.addWidget(self.chart)
		self.setup_timer()

	def setup_timer(self):
		self.update_timer = QTimer(self)#更新时间戳，
		self.update_timer.start(10)#每隔0.01秒刷新数据
		self.update_timer.timeout.connect(self.chart.create_series)
		self.show_timer = QTimer(self)
		self.show_timer.start(16)
		# self.show_timer.timeout.connect(self.chart.show_thread.set_continue)
		self.show_timer.timeout.connect(self.chart.show_data)
		self.timer2 = QTimer(self)
		self.timer2.start(250)
		self.timer2.timeout.connect(self.printFps)

	def moveGraph(self, value):
		self.chart.x_limit[1] = value + self.chart.x_limit[1] - self.chart.x_limit[0]
		self.chart.x_limit[0] = value
		self.chart.x_limit[2] = True
		self.chart.show_data()
	
	def stopUpdate(self):
		self.chart.slider_flag = False
		self.chart.auto_Stretch = False
	
	def continueUpdate(self):
		self.chart.slider_flag = True

	def resetGraph(self):
		i = 0.1
		for line_name in self.chart.line_map:
			line = self.chart.line_map[line_name]
			line._buffer += [0.1+i, 0.2+i, 0.3+i, 0.4+i, 0.5+i, 0.6+i, 0.7+i, 0.8+i, 0.9+i, 0.1+i]*1000000
			i -= 0.1
		self.chart.show_data()

	def wheelEvent(self, event:QWheelEvent):
		x_min = int(self.chart._axis_x.min())
		x_max = int(self.chart._axis_x.max())

		if event.angleDelta().toTuple()[1] > 0:
			fact = 0.9
		else:
			fact = 1.1
		if self.chart.auto_Stretch:
			x_min = int(x_max - (x_max-x_min)*fact)
		else:
			pos_p = event.position().toTuple()[0] / self.width()
			pos = (x_max-x_min)*pos_p + x_min
			x_min = int(pos - (pos - x_min)*fact)
			x_max = int(pos + (x_max-pos)*fact)
			if fact > 1:
				x_max += 1
			if (x_max - x_min) < self.scatter_num:
				for line_name in self.chart.line_map:
					line = self.chart.line_map[line_name]
					line.append_scatter(self.chart)
			else:
				for line_name in self.chart.line_map:
					line = self.chart.line_map[line_name]
					line.delete_scatter()

		if x_max > self.chart.max_len:
			x_max = self.chart.max_len

		if x_min < 0:
			x_min = 0

		if x_min == x_max:
			x_max = x_min + 1

		if (x_min != int(self.chart._axis_x.min())) | (x_max != int(self.chart._axis_x.max())):
			self.chart.x_limit = [x_min, x_max, True]
			# self.chart._axis_x.setRange(x_min, x_max)
			# self.series.
		if self.chart.auto_Stretch != True:
			self.chart.show_data()
			# QWidget.wheelEvent(event)

	def mousePressEvent(self, event:QMouseEvent):
		if event.button() == Qt.MiddleButton:
			if self.chart.auto_Stretch:
				self.chart.auto_Stretch = False
				self.show_timer.stop()
				if (self.chart._axis_x.max() - self.chart._axis_x.min()) < self.scatter_num:
					for line_name in self.chart.line_map:
						self.chart.line_map[line_name].append_scatter(self.chart)
					self.chart.show_data()
			else:
				self.chart.auto_Stretch = True
				self.show_timer.start(16)
				for line_name in self.chart.line_map:
					self.chart.line_map[line_name].delete_scatter()
		# elif event.button() == Qt.LeftButton:
		# 	pos = event.windowPos()
		# 	print(pos.toTuple())


	def printFps(self):
		global MAX_POINT

		if self.auto_set_point & self.chart.auto_Stretch:
		# print(self.chart.max_len)
			if (self.chart.f < 10) & (MAX_POINT > self.limit_points[0]):
				MAX_POINT = int(MAX_POINT * 0.95)
			elif (self.chart.f > 15) & (MAX_POINT < self.limit_points[1]):
				MAX_POINT = int(MAX_POINT * 1.05)
		if self.showfps:
			self.ui.progressBar_2.setValue(int(self.chart.f*4))
		# self.chart._axis_x.setTitleText("fps\t{} | point\t{}".format(self.chart.f*0.4, MAX_POINT))
		self.chart.f = 0

	def create_chart(self):
		# 创建折线视图窗口

		
		self.chart.append_series("test1")
		self.chart.append_series("test2")
		self.chart.append_series("test3")
		self.chart.append_series("test4")

	
