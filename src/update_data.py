
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
# from Serial_Debugger2 import DebuggerMainWindow

class UpdateTimer(QTimer):
	mstime = 5
	second_cnt = 0
	def __init__(self, mainwindow):
		super(UpdateTimer, self).__init__()
		self.mainwindow = mainwindow
		self.timeout.connect(self.operate)
	def operate(self):
		# print(1)
		self.second_cnt += self.mstime
		if self.second_cnt > 1000:
			self.second_cnt = 0
			self.mainwindow.ui.frameLCD.display(self.mainwindow.serial_thread.frame)
			self.mainwindow.serial_thread.frame = 0
		recv_data_len = len(self.mainwindow.serial_thread.recv_data)
		self.mainwindow.ui.receiveCountLCD.display(recv_data_len)
		self.mainwindow.ui.sendCountLCD.display(self.mainwindow.serial_thread.ser.send_cnt)
	
	def open_start(self, time = 5):
		self.mstime = time
		self.start(self.mstime)

