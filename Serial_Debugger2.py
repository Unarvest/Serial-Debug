import sys, os
from datetime import datetime
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from ui.Serial_MainWindow_ui import Ui_MainWindow                                       
#add(your program's name)  use :pyuic5 button.ui -o button.py to create.
from src.File_loader import Config
from src.serial_core import SerialThread
from src.parse_data import HexShow, TransHexThread, DecodeData
from src.update_data import UpdateTimer
from src.send_contrl import *
from src.graph_widget import Graph_View, My_Chart_View
from src.net_core import Network_Widget, NetworkThread
from src.download import findUpdate
from src.setCMD import *
import icoPack_rc


class DebuggerMainWindow(QMainWindow):
	show_msg = Signal(str)
	is_show_hex = False
	is_send_hex = False
	is_show = True
	def __init__(self, config):
		super(DebuggerMainWindow, self).__init__()
		self.ui = DebuggerWindowUi(self)
		self.config = config
		self.serial_thread = SerialThread(self)
		self.decode_thread = DecodeData(self)
		
		self.trans_hex_thread = TransHexThread(self)
		self.network = Network_Widget(self)
		self.graph_widget = Graph_View()
		self.net_widget = Network_Widget(self)
		self.autoSendTimer = QTimer(self)
		self.autoSendTimer.timeout.connect(self.autoSend)
		self.graph_widget.sendMsg_sig.connect(self.sendMsg)
		self.multi_send_list = []
		# self.serial_thread.show_print = True
		
	def setup(self):
		self.setupThread()
		self.ui.setupUi(self)
		self.ui.receiveBox.setAcceptDrops(False)
		self.ui.Init_data(config)
		self.ui.splitterSet()
		self.ui.draw_layout.addWidget(self.graph_widget)
		self.ui.network_layout.addWidget(self.net_widget)
		self.net_widget.ui.enterSendCheckBox.clicked.connect(self.setEnterSend)
		self.net_widget.ui.showSendMsgBox.clicked.connect(self.setShowSendMsg)
		self.net_widget.ui.sendHexCheckBox.clicked.connect(self.setSendHex)
		self.net_widget.ui.sendTimeRadioButton.clicked.connect(self.setAutoSend)
		self.net_widget.ui.sendTimeSpinBox.valueChanged.connect(self.autoSendTimeChanged)
		self.net_widget.append_msg_sig.connect(self.updateRecv)
		self.net_widget.msg_sig.connect(self.show_msg)
		text_list = self.config.load('multi_send')
		if type(text_list) != list:
			text_list = ['']
		for text in text_list:
			self.add_multi_send(text)
		self.CMDLine = CMDSendLine(self, self.cmdEnterSend)
		self.show_msg.connect(self.ui.toMessageBox)
		if self.config.load('auto_connect'):
			self.connectSerial()

	def setupThread(self):
		self.serial_thread.read_sig.connect(self.decode_thread.appendData)
		self.serial_thread.msg_sig.connect(self.ui.toMessageBox)
		self.serial_thread.connect_sig.connect(self.ui.connectState)
		self.decode_thread.decoded_sig.connect(self.updateRecv)
		self.decode_thread.start()
		self.trans_hex_thread.start()
		self.graph_widget.chart.append_thread.data_pipe = self.decode_thread.decoded_pipe
		self.graph_widget.add_label_sig.connect(self.decode_thread.add_label)
		# self.serial_thread.show_print = True
	
	def cmdEnterSend(self, msg):
		self.sendMsg(msg)

	def autoSend(self):
		if self.ui.mainLeftWidget.currentIndex() == 0:
			if self.serial_thread.ser.is_open != True:
				QMessageBox.warning(self, '警告', '串口未开启')
				self.ui.sendTimeRadioButton.setChecked(False)
				self.net_widget.ui.sendTimeRadioButton.setChecked(False)
				self.autoSendTimer.stop()
				return 
		elif self.ui.mainLeftWidget.currentIndex() == 1:
			if self.net_widget.current_socket == None:
				QMessageBox.warning(self, '警告', '未选择发送端口')
				self.autoSendTimer.stop()
				self.net_widget.ui.sendTimeRadioButton.setChecked(False)
				self.ui.sendTimeRadioButton.setChecked(False)
				return 
		self.sendMsg()

	def updateRecv(self, decode_data):
		self.ui.insertTextToRecvBox(decode_data)

	def bpsChanged(self, value:str):
		if value.isalnum():
			value = int(value)
			self.config.save('bps', value)
		else:
			res = QInputDialog.getInt(self, '设置波特率', '请输入一个整数 可能需要设备支持', 115200)
			if res[1]:
				value = res[0]
				self.ui.bpscomboBox.setItemText(self.ui.bpscomboBox.count() - 1, str(value))
				self.ui.bpscomboBox.addItem("<自定义>")
			else:
				self.ui.bpscomboBox.setCurrentText('115200')
		self.serial_thread.ser.set_bps(value)
			# self.config.save('bps', '115200')
		
	def byteSizeChanged(self, value):
		self.config.save('byte_size', value)
		self.serial_thread.ser.set_byte_size(value)
	
	def parityChanged(self, value):
		self.config.save('parity', value)
		self.serial_thread.ser.set_parity(value)
	
	def stopBitsChanged(self, value):
		self.config.save('stop_bits', value)
		self.serial_thread.ser.set_stop_bits(value)

	def connectSerial(self):
		if self.serial_thread.isRunning():
			if self.serial_thread.run_flag:
				self.serial_thread.Close_Port()
				self.ui.connectState(None)
		else:
			port_list = self.searchPort()
			if self.serial_thread.Open_Start(target = self.ui.autoConnectLineEdit.text(), port_list=port_list):
				self.ui.connectState(None)
			else:
				self.show_msg.emit('未找到目标: {}'.format(self.ui.autoConnectLineEdit.text()))
				self.ui.connectState(False)
			

	def setSendHex(self, value):
		self.ui.sendHexCheckBox.setChecked(value)
		self.net_widget.ui.sendHexCheckBox.setChecked(value)
		self.is_send_hex = value
		text = self.ui.sendBox.toPlainText()
		cursor = self.ui.sendBox.textCursor()
		if value == True:
			text = HexShow(text.encode(self.config.load('encode')), line_break = b'')
			self.ui.sendBox.setPlainText(text)
			self.ui.sendBox.setTextCursor(cursor)
		else:
			res = hex_to_string(text)
			try:
				self.ui.sendBox.setPlainText(res.decode(self.config.load('encode')))
			except Exception as e:
				self.ui.sendHexCheckBox.setChecked(True)
				self.ui.sendHexCheckBox_2.setChecked(True)
				QMessageBox.critical(self, '解码错误', str(e))

	
	def setEnterSend(self, value):
		self.ui.enterSendCheckBox.setChecked(value)
		self.net_widget.ui.enterSendCheckBox.setChecked(value)
		self.config.save('enter_send', value)
	
	def setShowHex(self, value):
		self.ui.showHexCheckBox.setChecked(value)
		self.net_widget.ui.showHexCheckBox.setChecked(value)
		self.is_show_hex = value
		if value == True:
			self.trans_hex_thread.openStart(self.serial_thread.recv_data)
		else:
			self.trans_hex_thread.return_back()
	
	def setShowSendMsg(self, value):
		self.ui.showSendMsgBox.setChecked(value)
		self.net_widget.ui.showSendMsgBox.setChecked(value)
		self.config.save('show_send_msg', value)
	
	def setDTR(self, value):
		if self.serial_thread.isRunning():
			self.serial_thread.ser.setDataTerminalReady(value)

	def setRTS(self, value):
		if self.serial_thread.isRunning():
			self.serial_thread.ser.setRequestToSend(value)

	def setAutoCut(self, value):
		self.config.save('auto_cut', value)
		self.serial_thread.auto_cut = value
	
	def cutTimeChanged(self, value):
		self.config.save('cut_time', value)
	
	def setAutoSend(self, value):
		self.ui.sendTimeRadioButton.setChecked(value)
		self.net_widget.ui.sendTimeRadioButton.setChecked(value)
		if value == True:
			self.autoSendTimer.start(self.ui.sendTimeSpinBox.value())
		else:
			self.autoSendTimer.stop()

	def autoSendTimeChanged(self, value):
		self.ui.sendTimeSpinBox.setValue(value)
		self.net_widget.ui.sendTimeSpinBox.setValue(value)
		if self.ui.sendTimeRadioButton.isChecked():
			self.autoSendTimer.start(value)
		self.config.save('auto_send_time', value)
	
	def setLineBreak(self, value):
		self.config.save('set_line_break', value)
	
	def LineBreakChanged(self, value):
		self.config.save('line_break', value)
		if value > 2:
			res = QInputDialog.getText(self, '设置换行符', '请输入一个换行符')

			if res[1]:
				value = res[0]
				self.ui.bpscomboBox.setItemText(self.ui.bpscomboBox.count() - 1, value)
				self.ui.bpscomboBox.addItem("<自定义>")
			else:
				self.ui.bpscomboBox.setCurrentIndex(0)
		print(value)
	
	def searchPort(self):
		port_list = self.serial_thread.ser.Search_ports()
		self.ui.serialListWidget.clear()
		for i in port_list:
			self.ui.serialListWidget.addItem("{} - {}".format(i[0], i[1]))
		self.show_msg.emit("发现{}个设备".format(len(port_list)))
		return port_list
		
	def portListClicked(self, item:QListWidgetItem):
		tail = item.text().index(' - ')
		port_name = item.text()[:tail]
		try:
			self.serial_thread.ser.setPortName(port_name)
		except Exception as e:
			self.serial_thread.Close_Port()
			self.show_msg.emit(str(e))
	
	def portListDoubleClicked(self, item:QListWidgetItem):
		tail = item.text().index(' - ')
		port_name = item.text()[:tail]
		try:
			self.serial_thread.ser.setPortName(port_name)
			self.connectSerial()
		except Exception as e:
			self.serial_thread.Close_Port()
			self.show_msg.emit(str(e))
	
	def setAutoConnect(self, value:bool):
		self.config.save('auto_connect', value)
	
	def autoConnectChanged(self, value:str):
		self.config.save('auto_target', value)

	def streamFlameSet(self):
		pass

	def clearRecvBox(self):
		self.ui.receiveBox.clear()
		self.serial_thread.frame = 0
		
	def saveRecvBox(self):
		try:
			name = datetime.now().strftime("%Y%m%d-%H%M%S.txt")
			Msg = self.ui.receiveBox.toPlainText()
			if len(Msg) == 0:
				if QMessageBox.warning(self, '警告', '接收信息为空, 是否继续保存?',QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
					getAccess()
					megfile = open(self.config.load('path') + '/' + name, 'w', encoding = 'UTF-8')
					megfile.write(Msg)
				else:
					return
			else:
				getAccess()
				megfile = open(self.config.load('path') + '/' + name, 'w', encoding = 'UTF-8')
				megfile.write(Msg)
			megfile.close()
			if QMessageBox.question(self, '提示', name + '\n保存成功!' + '\n是否打开文件?', QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
				os.startfile(self.config.load('path') + '/' + name)
			self.show_msg.emit('保存成功')

		except Exception as e:
			QMessageBox.warning(self, '警告', '保存文件错误, 可能需要管理员权限\n原因:' + str(e))

	def openPath(self):
		os.startfile(self.config.load('path'))

	def showRecvHex(self):
		pass

	def isShowMsg(self, value):
		self.is_show = value
	
	def sendBoxTextChange(self):
		text = self.ui.sendBox.toPlainText()
		cursor = self.ui.sendBox.textCursor()
		cursor_pos = cursor.position()
		if len(text) == 0:
			return
		if self.config.load('enter_send'):
			if text[cursor_pos - 1] == '\n':
				text = text[:cursor_pos - 1] + text[cursor_pos:]
				# text = HexShow(text.encode("UTF-8"), line_break=b'')
				self.ui.sendBox.setPlainText(text)
				QTextCursor.setPosition(cursor, cursor_pos - 1)
				self.ui.sendBox.setTextCursor(cursor)
				self.sendMsg()
		if self.is_send_hex:
			if cursor_pos == 0:
				return
			tail_flag = (cursor_pos == len(text))
			c = ord(text[cursor_pos - 1])
			if ((c>=48) & (c<=57)) | ((c>=65) & (c<=70)) | ((c>=97) & (c<=102)) | (c==32):
				text = formatHex(text)
			else:
				self.show_msg.emit('输入错误字符:' + text[cursor_pos - 1])
				text = text[:cursor_pos - 1] + text[cursor_pos:]
			self.ui.sendBox.setPlainText(text)
			if tail_flag != True:
				if len(text) > 1:
					if (len(text) - 2)%3 == 0:
						cursor_pos += 1
				QTextCursor.setPosition(cursor, cursor_pos)
			self.ui.sendBox.setTextCursor(cursor)

	def tabChanged(self, value): 
		if value == 1:
			self.graph_widget.start_timer()
		else:
			self.graph_widget.stop_timer()
	
	def scanPort(self):
		QMessageBox.warning(self, '警告', '暂不可用')
	
	def startServer(self):
		pass

	def setDecode(self, value):
		self.config.save('decode', value)
	
	def setDataDir(self):
		path = QFileDialog.getExistingDirectory()
		if path != '':
			self.config.save('path', path)
			self.ui.pathLabel.setText(path)

	def openDataDir(self):
		self.config.load('path')

	def changeMode(self, mode):
		# print(mode)
		pass

	def sendMsg(self, msg_string=None):
		tab_index = self.ui.mainLeftWidget.currentIndex()
		if type(msg_string) != str:
			msg_string = self.ui.sendBox.toPlainText()
		if self.is_send_hex:
			msg = hex_to_string(msg_string)
		try:
			msg = msg_string.encode(self.config.load('encode'))
		except Exception as e:
			QMessageBox.critical(self, '解码错误', str(e))
		if self.config.load('set_line_break'):
			line_break_index = self.ui.lineBreakComboBox.currentIndex()
			if line_break_index == 0:
				msg += b'\r\n'
				msg_string += '\\r\\n'
			elif line_break_index == 1:
				msg += b'\r'
				msg_string += '\\r'
			elif line_break_index == 2:
				msg += b'\n'
				msg_string += '\\n'
			else:
				msg += self.ui.lineBreakComboBox.itemText(line_break_index).encode(self.config.load('encode'))
		if tab_index == 0:
			if self.serial_thread.ser.isOpen() != True:
				QMessageBox.warning(self, '警告', '串口未开启')
				return 
			try:
				if self.serial_thread.send_msg(msg) == False:
					QMessageBox.warning(self, '发送失败', '串口正在发送其它消息')
					return
			except Exception as e:
				QMessageBox.critical(self, '发送失败', str(e))
				self.serial_thread.Close_Port()
				return

			if self.config.load('show_send_msg'):
				self.ui.receiveBox.appendPlainText(">>> " + msg_string + "\n")
		elif tab_index == 1:
			if type(self.net_widget.current_socket) == NetworkThread:
				self.net_widget.current_socket.Send_Msg(msg)
				if self.config.load('show_send_msg'):
					self.ui.receiveBox.appendPlainText("{}>>> ".format(
						self.net_widget.current_socket.net_socket.localPort()) + msg_string + "\n")
			else:
				QMessageBox.warning(self, '警告', '未选择发送端口')
	
	def openSetCmdWin(self):
		self.cmd = setCmdWindow()
		self.cmd.closeSignal.connect(self.CMDLine._setModel)
		self.cmd.show()

	def add_multi_send(self, default_text):
		if type(default_text) != str:
			default_text = ""
		m = Multi_Send(self, len(self.multi_send_list))
		m.add_to_widget(self.ui.multi_send_layout)
		m.ui.lineEdit.setText(default_text)
		m.send_signal.connect(self.sendMsg)
		self.multi_send_list.append(m)
	
	def openSetCmdWin(self):
		self.cmd = setCmdWindow()
		self.cmd.closeSignal.connect(self.CMDLine._setModel)
		self.cmd.show()

	def delete_multi_send(self):
		if len(self.multi_send_list) > 9:
			self.multi_send_list.pop().deleteLater()

	def closeEvent(self, event: QCloseEvent) -> None:

		multi_send_text_list = []
		for n in range(len(self.multi_send_list)):
			text = self.multi_send_list[n].ui.lineEdit.text()
			if n > 8:
				if text == '':
					continue
			multi_send_text_list.append(text)
		
		self.config.save('multi_send', multi_send_text_list)

		os._exit(0)
		return super().closeEvent(event)


class DebuggerWindowUi(Ui_MainWindow):
	def __init__(self, mainwindow:DebuggerMainWindow):
		super(DebuggerWindowUi, self).__init__()
		self.mainwindow = mainwindow
	
	def Init_data(self, config):
		bps = str(config.load('bps'))
		self.bpscomboBox.setCurrentText(bps)
		if self.bpscomboBox.currentIndex() == self.bpscomboBox.count() - 1:
			self.bpscomboBox.setItemText(self.bpscomboBox.count() - 1, bps)
			self.bpscomboBox.addItem("<自定义>")

		self.byteSizeComboBox.setCurrentText(str(config.load('byte_size')))
		self.parityComboBox.setCurrentText(config.load('parity'))
		self.stopBitsComboBox.setCurrentText(str(config.load('stop_bits')))
		config.load('enter_send')
		self.showSendMsgBox.setChecked(config.load('show_send_msg'))
		self.cutFrameCheckBox.setChecked(config.load('auto_cut'))
		# self..setValue(config.load('cut_time'))
		self.sendTimeRadioButton.setChecked(config.load('auto_send_time'))
		self.sendLineBreak.setChecked(config.load('set_line_break'))
		self.lineBreakComboBox.setCurrentIndex(config.load('line_break'))
		self.autoConnectCheckBox.setChecked(config.load('auto_connect'))
		self.autoConnectLineEdit.setText(config.load('auto_target'))
	
	def connectState(self, state):
		if state == True:
			icon_connect = QIcon()
			icon_connect.addPixmap(QPixmap(':/Mainico/ico/断开 (2).ico'))
			print('成功连接到\'{}\''.format(self.mainwindow.serial_thread.ser.portName()))
			self.toMessageBox('成功连接到\'{}\''.format(
				self.mainwindow.serial_thread.ser.portName(), ))
			self.openSerialButton.setIcon(icon_connect)
			self.openSerialButton.setCheckable(True)
			# self.connectStateRadioButton.setCheckable(True)
			# self.connectStateRadioButton.setChecked(True)
			self.openSerialButton.update()
		elif state == False:
			icon_disconnect = QIcon()
			icon_disconnect.addPixmap(QPixmap(':/Mainico/ico/连接.ico'))
			self.openSerialButton.setIcon(icon_disconnect)
			self.openSerialButton.setCheckable(True)
			# self.connectStateRadioButton.setChecked(False)
			self.openSerialButton.update()
		else:
			icon_connecting = QIcon()
			icon_connecting.addPixmap(QPixmap(':/Mainico/ico/连接 (1).ico'))
			self.toMessageBox('正在连接到{}'.format(self.mainwindow.serial_thread.ser.portName()), 1000)
			self.openSerialButton.setCheckable(False)
			self.openSerialButton.setIcon(icon_connecting)
			# self.connectStateRadioButton.setChecked(False)
			self.openSerialButton.update()
	
	def toMessageBox(self, msg, time=0):
		self.statusBar.showMessage(str(msg), time)
	
	def insertTextToRecvBox(self, decode_data):
		if self.mainwindow.is_show != True:
			return
		self.receiveBox.insertPlainText(decode_data)
		# self.ui.receiveCountLCD.display(len(self.serial_thread.recv_data))
		self.recvBox_reset_cursor()

	def recvBox_reset_cursor(self):
		cursor = self.receiveBox.textCursor()
		cursor.movePosition(QTextCursor.End)
		self.receiveBox.setTextCursor(cursor)


	def splitterSet(self):
		splitterRight = QSplitter(Qt.Vertical)
		splitterRight.addWidget(self.sendFrame)
		splitterRight.addWidget(self.toolBox)
		splitterRight.setSizes([1000,100])
		self.verticalLayout_16.addWidget(splitterRight)

		mainSplitterH = QSplitter(Qt.Horizontal)
		mainSplitterH.addWidget(self.mainLeftWidget)
		mainSplitterH.addWidget(self.mainRightFrame)
		self.horizontalLayout_2.addWidget(mainSplitterH)


	
import time
import multiprocessing
if __name__ == '__main__':
	multiprocessing.freeze_support()
	QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
	app = QApplication(sys.argv)
	config = Config()
	window = DebuggerMainWindow(config)
	window.setup()
	u = UpdateTimer(window)
	u.open_start()
	if window.config.load('update'):
		update = findUpdate(window)
		update.openStart()
	window.show()
	sys.exit(app.exec())
