# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import *
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QThread, QObject, QTimer
from serial_core_qt import SerialPort

class SerialWork(QObject):
	def __init__(self):
		super().__init__()

	def init(self):
		self.com = SerialPort()
		self.com.setPortName('COM12')
		self.com.setBaudRate(115200)
		if self.com.open(QSerialPort.ReadWrite) == False:
			return
		self.com.setRequestToSend(False)
		self.com.setDataTerminalReady(False)
		# self.com.readyRead.connect(self.readData)
		self.readtimer = QTimer()
		self.readtimer.timeout.connect(self.readData)
		self.readtimer.start(100) 

	def readData(self):
		revData = self.com.readAll()
		revData = bytes(revData)
		print('read', revData)

class PyQt_Serial(QWidget):
	def __init__(self):
		super().__init__()
		self.serialthread = QThread()
		self.serialwork = SerialWork()
		self.serialwork.moveToThread(self.serialthread)
		self.serialthread.started.connect(self.serialwork.init)
		self.serialthread.start()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  win = PyQt_Serial()
  win.show()
  sys.exit(app.exec_()) 
