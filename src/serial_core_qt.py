from typing import Tuple
from PySide6.QtCore import *  # type: ignore
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
'''port=None,
baudrate=9600,
bytesize=EIGHTBITS,
parity=PARITY_NONE,
stopbits=STOPBITS_ONE,
timeout=None,
xonxoff=False,
rtscts=False,
write_timeout=None,
dsrdtr=False,
inter_byte_timeout=None,
exclusive=None,'''



class SerialPort(QSerialPort):
	sleep_time = 0.001
	send_cnt = 0
	encode = "UTF-8"
	decode = "UTF-8"
	port_list = []
	_port = None
	def __init__(self):
		super(SerialPort, self).__init__()
		self.set_bps(115200)
		self.set_byte_size('8')
		self.set_parity('None')
		self.set_stop_bits('1')

	def set_bps(self, bps:int):
		try:
			self.setBaudRate(bps)
			return True
		except Exception as e:
			return False
	
	def set_byte_size(self, byte_size:str):
		try:
			if byte_size == '5':
				self.setDataBits(QSerialPort.Data5)
			elif byte_size == '6':
				self.setDataBits(QSerialPort.Data6)
			elif byte_size == '7':
				self.setDataBits(QSerialPort.Data7)
			else:
				self.setDataBits(QSerialPort.Data8)
			return True	
		except Exception as e:
			return str(e)
		
	def set_parity(self, parity:str):
		try:
			if parity == 'Mark':
				self.setParity(QSerialPort.MarkParity)
			elif parity == 'Odd':
				self.setParity(QSerialPort.OddParity)
			elif parity == 'Even':
				self.setParity(QSerialPort.EvenParity)
			elif parity == 'Space':
				self.setParity(QSerialPort.SpaceParity)
			else:
				self.setParity(QSerialPort.NoParity)
			return True	
		except Exception as e:
			return str(e)
	
	def set_stop_bits(self, stop_bits:str):
		try:
			if stop_bits == '1.5':
				self.setStopBits(QSerialPort.OneAndHalfStop)
			elif stop_bits == '2':
				self.setStopBits(QSerialPort.TwoStop)
			else:
				self.setStopBits(QSerialPort.OneStop)
			return True
		except Exception as e:
			return str(e)
	
	def Search_ports(self):
		return QSerialPortInfo.availablePorts()
		
	
	'''
	@description: 在串口列表中查找目标
	@param target{str}: 目标的关键词，默认为CH340 
	@return: 目标串口，错误返回None;
	'''
	def Find_target(self, target = "CH340", port_list = None):
		if port_list is None:
			self.port_list = self.Search_ports()
		else:
			self.port_list = port_list
		if len(self.port_list) == 0:
			print('无可用串口')
			return None
		else:
			for i in self.port_list:
				portName = i.portName()
				if target in i.description():
					self._port = portName
					# self.setPort(i)
					self.setPortName(portName)
					print("成功找到目标", target, "位于", portName)
					return True
			else :
				print("未找到目标：", target)
				return None
	
	def Open_port(self, portName = ""):
		# if self.isOpen():
		# 	self.close()
		# 	self.setPortName(portName)
		self.open(QSerialPort.ReadWrite)

	def Send_msg(self, msg):
		if self.isOpen():
			res = self.write(msg)
			self.send_cnt += res
		else:
			return None
	
	def Start_read(self):
		pass

	def Clear_send_cnt(self):
		self.send_cnt = 0
	
	def Clear_recv_cnt(self):
		
		self.recv_cnt = 0
	

def HexShow(string = b'', split_symbel = ' ', line_break = b'\n'):
	hex_string = ""
	if line_break == b'':
		parts = [string]
	else:
		parts = string.split(line_break)
	for part in parts[:-1]:
		hex_string += part.hex(split_symbel) + ' 0a\n'
	return hex_string + parts[-1].hex(split_symbel)

import time

import multiprocessing 
from multiprocessing.connection import Connection

def hex_show_process(args_pipe, done_pipe):
	while True:
		arg = args_pipe[1].recv()
		print(arg)
		res = HexShow(arg[0], arg[1], arg[2])
		done_pipe[0].send(res)

class TransHexThread(QThread):
	trans_done = Signal(str)
	old_data = b""
	old_string = ""
	new_string = ""
	split_symbel = ' '
	line_break = b'\n'
	hex_flag = False
	def __init__(self, mainwindow):
		super(TransHexThread, self).__init__()
		self.mainwindow = mainwindow
		self.args_pipe = multiprocessing.Pipe()
		self.done_pipe = multiprocessing.Pipe()
		self.trans_done.connect(self.trans_done_slot)
		self.p = multiprocessing.Process(target=hex_show_process, args=(self.args_pipe, self.done_pipe)) 
		self.p.start()
	def run(self):
		try:
			self.mainwindow.show_msg.emit('正在后台进行转换')
			self.args_pipe[0].send((self.old_data, self.split_symbel, self.line_break))
			res = self.done_pipe[1].recv()
			self.trans_done.emit(res)
			# res = HexShow(self.old_data, self.split_symbel, self.line_break)
		except Exception as e:
			print(e)
			return False

	def openStart(self, data):
		if self.isRunning():
			return False
		self.old_data = data
		self.old_string = self.new_string = ""
		# self.args_pipe[0].send((self.old_data, self.split_symbel, self.line_break))
		# self.mainwindow.show_msg.emit('正在后台进行转换')
		self.start()

	def trans_done_slot(self, data):
		if self.mainwindow.is_show_hex:
			self.old_string = self.mainwindow.ui.receiveBox.toPlainText()
			self.mainwindow.ui.receiveBox.setPlainText(data)
			self.mainwindow.ui.recvBox_reset_cursor()
			self.hex_flag = True
			self.mainwindow.show_msg.emit('十六进制转换完毕')
	
	def return_back(self):
		if self.hex_flag:
			self.mainwindow.ui.receiveBox.setPlainText(self.old_string + self.new_string)
			self.mainwindow.ui.recvBox_reset_cursor()
			self.mainwindow.show_msg.emit('已还原')
	
	

class SerialThread(QThread):
	read_sig = Signal(str)	# 接收到的数据, 断帧标识
	connect_sig = Signal(bool)	#
	msg_sig = Signal(tuple)
	frame = 0
	split_symbol = b'\n'
	target = "CH340"
	sleep_time = 0.001
	recv_data = b""
	show_print = False
	run_flag = False
	add_line_break = True
	auto_cut = False
	def __init__(self, mainwindow=None) -> None:
		super(SerialThread, self).__init__()
		self.mainwindow = mainwindow
		self.ser = SerialPort()
		# self.ser.writeTimeout = 3
	
	def run(self):
		t = None
		self.run_flag = False
		if self.connect_target():
			self.connect_sig.emit(True)
		else:
			self.connect_sig.emit(False)
			return
		self.run_flag = True
		end_flag = False
		print(1)
		self.ser.setDataTerminalReady(True)
		self.ser.setRequestToSend(True)
		while self.ser.isOpen():
			'''
			try:
				
				self.ser.size()
			except:
				self.ser.close()
				self.connect_sig.emit(False)
				self.msg_sig.emit('串口\'{}\'断开'.format(self.ser.port))
				return 
			'''
			if end_flag:
				if self.auto_cut:
					self.frame += 1
					self.decodeData(b'', True)

			# if self.ser.waitForReadyRead(100) != True:
			# 	self.ser.close()
			# 	self.connect_sig.emit(False)
			# 	self.msg_sig.emit('串口\'{}\'断开'.format(self.ser.port))
			print(1)
			data = self.ser.readAll().data()
			print(data)
			if len(data) == 0:
				self.msleep(1)
				continue
			recv_len = len(data)
			# if self.show_print == True:
			print(data.decode('utf-8'), end='')
			self.recv_data += data
			# self.decodeData(data, False)
			if (data[-1] != 10) & (data[-1] != 13):
				end_flag = self.ser.waitForReadyRead(10)

		
		self.connect_sig.emit(False)
		self.msg_sig.emit('关闭串口\'{}\''.format(self.ser._port))

	def Read_once(self):
		data = self.ser.readAll()
		print(data.data().decode('utf-8'))

	def connect_target(self):
		# if self.ser.isOpen():
		# 	self.ser.close()
		try:
			self.ser.open(QSerialPort.ReadWrite)
		except Exception as e:
			err = str(e)
			if 'PermissionError' in err:
				self.msg_sig.emit("连接串口'{}'失败, 可能是串口被占用".format(self.ser.port))
			else:
				self.msg_sig.emit(str(e))
			return False
		return self.ser.isOpen()

	def Open_Start(self, portName = "", target = "CH340", port_list = None):
		if portName != "":
			self.ser._port = portName
		elif self.ser._port == None:
			if self.ser.Find_target(target, port_list) != True:
				return False
		self.start()
		return True

	def Close_Port(self):
		if self.isRunning():
			self.run_flag = False
			# QThread.msleep(10)
			# self.quit()

	def decodeData(self, data, line_break):
		t = time.time()
		try:
			if (data == b'') & line_break:
				decode_string = '\n'
			else:
				decode_string = data.decode(self.mainwindow.config.load('decode'), errors='replace')
				if line_break:
					if (decode_string[-1] != '\n') & (decode_string[-1] != '\r'):
						decode_string += '\n'
		except ValueError:
			decode_string = '□'*len(data)
		if self.mainwindow.is_show_hex:
			self.read_sig.emit(HexShow(data))
			self.mainwindow.trans_hex_thread.new_string += decode_string
		else:
			self.read_sig.emit(decode_string)

	# def set_split(self, split_str, encode):
	# 	try:
	# 		self.split_symbol = serial.to_bytes(split_str.encode(encode))
	# 		return True
	# 	except:
	# 		return False

# s = SerialThread()

# # # s.Open_Start(target = "USB")
# s.Open_Start(target = "USB")

# while s.isRunning():
# 	pass
'''
ser = SerialPort()
ser.Find_target('USB')
ser.open()
while ser.is_open:
	while ser.in_waiting > 0:
		try:
			res = ser.read_until(expected=b'\n', size=ser.in_waiting)
			if ser.in_waiting > 0:
				print(res, True)
				continue
			else:
				print(res, False)
				time.sleep(0.001)
				if ser.in_waiting > 0:
					continue
				else:
					print(b'', True)
		except Exception as e:
			print(e)
		break
	time.sleep(0.001)
'''

# class WorkerThread(QThread):
#     signal_str = Signal(str)
#     signal_int = Signal(int)
#     def __init__(self):
#         super(WorkerThread, self).__init__()
#         # Instantiate signals and connect signals to the slots
#         # self.signals = MySignals()
#     def run(self):
#         # Do something on the worker thread
#         a = 1 + 1
#         # Emit signals whenever you want
#         self.signal_int.emit(a)
#         self.signal_str.emit("This text comes to Main thread from our Worker thread.")
#         print(1)
 
 
# # if __name__ == "__main__":
# #     app = QApplication(sys.argv)
# #     window = MainForm()
# #     window.show()
#     # sys.exit(app.exec_())

# instanced_thread = WorkerThread()
# instanced_thread.signal_str.connect(res)
# instanced_thread.signal_int.connect(res)
# instanced_thread.start()
# while instanced_thread.isRunning():
#     pass
 
def printHexshow(name):
	t = time.time()
	HexShow(b'Hello world'*1000009)
	print(name, time.time() - t)

# if __name__ == "__main__": 
# 	p1 = multiprocessing.Process(target=printHexshow, args=('multi', )) 
# 	# p2 = multiprocessing.Process(target=print_cube, args=(10, )) 

# 	# starting process 1&2
# 	p1.start() 
# 	# p2.start() 

# 	# wait until process 1&2 is finished 
# 	p1.join()
# 	# p2.join() 
# 	t = time.time()
# 	printHexshow('defaultS')
# 	# both processes finished 
# 	print(time.time() - t)

	# printHexshow()