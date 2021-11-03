from typing import Tuple
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *
from PySide6.QtWidgets import * # type: ignore
from PySide6.QtNetwork import QHostAddress, QTcpServer, QTcpSocket, QUdpSocket
from src.parse_data import HexShow
from ui.net_widget_ui import Ui_Form
import time


class NetworkThread(QThread):
	read_sig = Signal(str, str, int)	# 接收到的数据, 断帧标识
	curve_sig = Signal(tuple)
	msg_sig = Signal(str)
	connected_sig = Signal()
	connected_fail = Signal(str, str)
	update_list_sig = Signal(str)
	ip = ""
	port = 0
	mode = 0
	curve = False
	socket_name = ""
	send_cnt = 0
	recv_cnt = 0
	def __init__(self, mainWidget, show_print = False):
		super(NetworkThread, self).__init__(mainWidget)
		# self.tcp_server = QTcpServer()
		self.mainWidget = mainWidget
		self.run_flag = True
		self.net_socket = None
		self.show_print = show_print

	def run(self):
		for i in range(250):
			if self.run_flag != True:
				break
			if self.net_socket.state() == QTcpSocket.ConnectedState:
				self.connected_sig.emit()
				return
			self.msleep(10)
		self.net_socket.close()
		self.net_socket.deleteLater()
		if self.run_flag:
			self.connected_fail.emit("连接超时", self.socket_name)
		else:
			self.connected_fail.emit('', self.socket_name)
	
	def disconnected_action(self):
		self.msg_sig.emit('<{}:{}> 断开与 <{}:{}>的连接'.format(
			self.net_socket.localAddress().toString(), 
			self.net_socket.localPort(),
			self.net_socket.peerAddress().toString(),
			self.net_socket.peerPort()
		))
		self.update_list_sig.emit(self.socket_name)
		self.deleteLater()

	def setup_socket(self):
		self.net_socket.readyRead.connect(self.readAll_data)
		self.socket_name = "[{}] -> {}:{} ".format(
			self.net_socket.localPort(),
			self.net_socket.peerAddress().toString(), 
			self.net_socket.peerPort()
		)
		if self.mode == 0:
			self.socket_name += '<TCP>'
		else:
			self.socket_name += '<UDP>'
		self.net_socket.disconnected.connect(self.disconnected_action)
		# new_socket_thread.net_socket.disconnected.connect(self.check_socket)
		# new_socket_thread.connected.connect(lambda: self.set_connect_state(True))
		# new_socket_thread.disconnected.connect(lambda: self.set_connect_state(True))
		'''
		print('start thread')
		self.run_flag = True
		while self.net_socket.isOpen():
			try:
				res = self.net_socket.readBufferSize()
				if res == 0:
					self.msleep(1)
					continue
				print(res)
				res = self.net_socket.readAll().data()
				if self.show_print == True:
					print(res.decode('utf-8'), end='')
				if self.curve == True:
					self.curve_sig.emit((res, True, False))
			except Exception as e:
				print(e)
				break	
		print('close thread')
		self.net_socket.close()
		self.msg_sig.emit('连接\'{}:{}\'断开'.format(self.ip, self.port))
		'''

	def readAll_data(self):
		res = self.net_socket.readAll().data()
		if self.show_print == True:
			print(res.decode('utf-8'), end='')
		if self.curve == True:
			self.curve_sig.emit((res, True, False))
		self.decodeData(res)
		self.recv_cnt += len(res)

	def decodeData(self, data):
		try:
			decode_string = data.decode(self.mainWidget.config.load('decode'), errors='replace')
		except ValueError:
			decode_string = '□'*len(data)
		self.read_sig.emit(decode_string+'\n', self.net_socket.peerAddress().toString(), self.net_socket.peerPort())

	def Open_Start(self, mode=0, ip="", port=None, socket=None):
		if socket is None:
			address = QHostAddress()
			if address.setAddress(ip) == False:
				return False
			self.ip = ip
			self.port = port
			self.mode = mode
			self.socket_name = "{}:{} - ".format(ip, port)
			if mode == 0:
				self.socket_name += 'TCP'
			else:
				self.socket_name += 'UDP'
		else:
			self.net_socket = socket
		if self.mode == 0:
			self.net_socket = QTcpSocket()
			self.net_socket.connectToHost(self.ip, self.port)
			# self.net_socket.connected.connect(self.readAllMsg)
		elif self.mode == 1:
			self.net_socket = QUdpSocket()
			self.net_socket.connectToHost(self.ip, self.port)
		else:
			self.connected_fail.emit('参数错误', self.socket_name)
		self.start()

		# self.net_socket.disconnected.connect(self.on_socket_disconnected)
		return True
	
	def Close_Port(self):
		if self.isRunning():
			self.run_flag = False
		self.net_socket.close()
		self.net_socket.deleteLater()
		self.net_socket = None

	def Send_Msg(self, data):
		self.send_cnt += self.net_socket.write(data)
	


class Network_Widget(QWidget):
	# view 总窗口
	sendMsg_sig = Signal(str)
	append_msg_sig = Signal(str)
	msg_sig = Signal(str)
	thread_map = {}
	server_ip = QHostAddress()
	listen_state = False
	current_socket = None
	
	def __init__(self, mainwindow):
		super(Network_Widget, self).__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.config = mainwindow.config
		self.decodethread_appender = mainwindow.decode_thread.appendData
		self.connect_state = True
		self.set_current_socket(None)
		self.tcp_server = QTcpServer(self)
		self.tcp_server.newConnection.connect(self.newConnectionComing)

	def newConnectionComing(self):
		new_socket = self.tcp_server.nextPendingConnection()
		new_socket_thread = self.setup_new_socket_thread()
		new_socket_thread.net_socket = new_socket
		new_socket_thread.connected_sig.emit()

	def append_connection(self, socket_thread:NetworkThread):
		socket_thread.setup_socket()
		self.set_connect_state(True)
		self.thread_map[socket_thread.socket_name] = socket_thread
		self.ui.connectListWidget.addItem(socket_thread.socket_name)
		self.set_current_socket(socket_thread)

	def connect_fail(self, msg, socket_name):
		if socket_name in self.thread_map:
			self.thread_map.pop(socket_name)
			print(self.thread_map)
		self.set_connect_state(False)
		self.set_current_socket(None)
		if msg != '':
			QMessageBox.critical(self, '连接错误', msg)

	def check_socket(self, socket_name=None):
		socket_name = "{}:{}".format(self.ui.IPEdit.text(), self.ui.PortEdit.value())
		for key in self.thread_map.keys():
			if socket_name in key:
				return True
		return False

	def modeSet(self, mode):
		self.set_current_socket(None)
		self.set_connect_state(False)

	def setIP(self, ip):
		self.set_current_socket(None)
		self.set_connect_state(False)

	def setPort(self, port):
		self.set_current_socket(None)
		self.set_connect_state(False)

	def setConnDraw(self, v):
		if self.current_socket != None:
			self.current_socket.curve = v

	def setup_new_socket_thread(self):
		new_socket_thread = NetworkThread(self, False)
		new_socket_thread.curve = self.ui.connectRraw.isChecked()
		new_socket_thread.msg_sig.connect(self.msg_sig)
		new_socket_thread.curve_sig.connect(self.decodethread_appender)
		new_socket_thread.read_sig.connect(self.add_header)
		# new_socket_thread.finished.connect(self.check_socket)
		new_socket_thread.update_list_sig.connect(self.update_list_view)
		new_socket_thread.connected_fail.connect(self.connect_fail)
		new_socket_thread.connected_sig.connect(lambda: self.append_connection(new_socket_thread))
		return new_socket_thread

	def startConnect(self):
		if self.current_socket != None:
			
			if self.current_socket.mode == 0:
				socket_type = QTcpSocket
			else:
				socket_type = QUdpSocket
			if type(self.current_socket.net_socket) != socket_type:
				if self.current_socket.Open_Start(
					mode = self.ui.modeComboBox.currentIndex(),
					ip = self.ui.IPEdit.text(),
					port = self.ui.PortEdit.value()
				) == False:
					QMessageBox.critical(self, '错误', '连接错误,，可能是部分参数有误')
				else:
					self.set_connect_state(None)
			elif self.current_socket.net_socket.state() == socket_type.ConnectingState:
				if QMessageBox.information(self, '警告', '正在连接中\n是否取消连接？', QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
					self.current_socket.run_flag = False
			elif self.current_socket.net_socket.state() == socket_type.ConnectedState:
				self.current_socket.Close_Port()
			return
		if self.check_socket():
			if QMessageBox.information(self, '警告', '该服务器已在连接列表中\n是否建立另一个连接？', QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
				return
		new_socket_thread = self.setup_new_socket_thread()
		if new_socket_thread.Open_Start(
			mode = self.ui.modeComboBox.currentIndex(),
			ip = self.ui.IPEdit.text(),
			port = self.ui.PortEdit.value()
		) == False:
			QMessageBox.critical(self, '错误', '连接错误,，可能是部分参数有误')
		else:
			self.set_connect_state(None)
		self.set_current_socket(new_socket_thread)

	def showIP(self, v):
		pass

	def showPort(self, v):
		pass

	def timeSend(self, v):
		pass

	def timerTime(self, value):
		pass

	def clearAllConnection(self):
		pass

	def listenStart(self):
		if self.listen_state:
			self.listen_state = False
		else:
			self.listen_state = True
		self.set_listen_state()
		
	
	def set_listen_state(self, state = None):
		icon_state = QIcon()
		if state != None:
			self.listen_state = state
		if self.listen_state == True:
			ip = QHostAddress()
			i = self.ui.serverIPBox.currentIndex()
			if i == self.ui.serverIPBox.count() - 1:
				QMessageBox.warning(self, '警告', 'ip地址不可为<自定义>')
			else:
				if i == 0:
					ip.setAddress(QHostAddress.AnyIPv4)
				elif i == 1:
					ip.setAddress(QHostAddress.LocalHost)
				else:
					ip.setAddress(self.ui.serverIPBox.currentText())
				if self.tcp_server.listen(ip, self.ui.serverPortEdit.value()):
					icon_state.addPixmap(QPixmap(':/Mainico/ico/正在监听.ico'))
					self.ui.listenButton.setIcon(icon_state)
					return
				else:
					
					QMessageBox.critical(self, '错误', '监听失败\n' + self.tcp_server.errorString())
		icon_state.addPixmap(QPixmap(':/Mainico/ico/未监听.ico'))
		self.ui.listenButton.setIcon(icon_state)
		self.tcp_server.close()

	def setServerIP(self, index):
		if index == self.ui.serverIPBox.count() - 1:
			res = QInputDialog.getText(self, '设置地址', '请输入一个有效地址 可能需要设备支持')
			if res[1]:
				value = QHostAddress()
				if value.setAddress(res[0]):
					self.ui.serverIPBox.setItemText(self.ui.serverIPBox.count() - 1, res[1])
					self.ui.serverIPBox.addItem("<自定义>")
				else:
					QMessageBox.warning(self, '警告', '输入的地址有误')
					self.ui.serverIPBox.setCurrentIndex(0)
			else:
				self.ui.serverIPBox.setCurrentIndex(0)
		self.set_listen_state(state = False)
		self.tcp_server.close()

	def setServerPort(self, port):
		pass

	def listClicked(self, item:QListWidgetItem):
		if item.text() in self.thread_map:
			self.set_current_socket(self.thread_map[item.text()])
			print(item.text())

	def setThreadNum(self):
		i = QInputDialog.getInt(self, '设置最大服务器连接数', '请输入一个整数', 10)
		if i[1]:
			value = i[0]
			if value > 0:
				self.tcp_server.setMaxPendingConnections(value)
			else:
				QMessageBox.warning(self, '数值有误', '输入了错误值{}'.format(value))

	def set_current_socket(self, socket):
		if type(socket) != NetworkThread:
			self.current_socket = None
			self.ui.selectLabel.setText('未选择')
		else:
			self.current_socket = socket
			if socket.net_socket.localAddress().toString() == '':
				self.ui.selectLabel.setText('连接中...')
			else:	
				self.ui.selectLabel.setText('[{}]'.format(socket.net_socket.localPort()))
				self.msg_sig.emit(socket.socket_name)
				self.ui.connectRraw.setChecked(socket.curve)

	def set_connect_state(self, state):
		icon_state = QIcon()
		self.connect_state = state
		if state == True:
			icon_state.addPixmap(QPixmap(':/Mainico/ico/断开 (2).ico'))
			self.ui.connectButton.setCheckable(True)
		elif state == False:
			icon_state.addPixmap(QPixmap(':/Mainico/ico/连接.ico'))
			self.ui.connectButton.setCheckable(True)
		else:
			icon_state.addPixmap(QPixmap(':/Mainico/ico/连接 (1).ico'))
			self.ui.connectButton.setCheckable(False)
		self.ui.connectButton.setIcon(icon_state)
	
	def add_header(self, msg, ip, port):
		if self.ui.showIPBox.isChecked() & self.ui.showPortBox.isChecked():
			header = "{}:{} ->".format(ip, port)
		elif self.ui.showIPBox.isChecked():
			header = "{} ->".format(ip)
		elif self.ui.showPortBox.isChecked():
			header = "{} ->".format(port)
		else:
			header = "->"
		self.append_msg_sig.emit(header + msg)
	
	def update_list_view(self, socket_name = None):
		if socket_name is not None:
			if socket_name in self.thread_map:
				if self.current_socket == self.thread_map.pop(socket_name):
					self.set_current_socket(None)
					self.set_connect_state(False)
			
		self.ui.connectListWidget.clear()
		for name in self.thread_map:
			self.ui.connectListWidget.addItem(name)



	
