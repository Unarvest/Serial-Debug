

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QVBoxLayout, QWidget
from ui.multi_send_ui import Ui_multi_send

def formatHex(hex_string):
	cnt = 0
	res_string = ""
	for c in hex_string:
		if cnt > 1:
			res_string += ' '
			cnt = 0
		if c != ' ':
			res_string += c
			cnt += 1
	return res_string

def hex_to_string(hex_string):
	text = hex_string.replace(' ', '')
	if len(text) != 0:
		if len(text) % 2:
			text += '0'
		res = b''
		for i in range(int(len(text)/2)):
			try:
				res += int(text[i*2:i*2+2], 16).to_bytes(1, 'little')
			except:
				continue
		return res
	return b''


class Multi_Send(QWidget):
	send_signal = Signal(str)
	def __init__(self, mainwindow, num):
		super(Multi_Send, self).__init__(mainwindow)
		self.ui = Ui_multi_send()
		self.ui.setupUi(self)
		self.num = num
		self.ui.pushButton.setText('发送{}'.format(num+1))
		
	def sendMsg(self):
		print(self.ui.lineEdit.text())
		self.send_signal.emit(self.ui.lineEdit.text())
	
	def add_to_widget(self, layout):
		layout.addWidget(self)
