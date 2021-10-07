from typing import Tuple
from PySide6.QtCore import *  # type: ignore
import serial
from serial.serialwin32 import Serial
import serial.tools.list_ports as list_ports
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

class SerialPort(serial.Serial):
	sleep_time = 0.001
	send_cnt = 0
	encode = "UTF-8"
	decode = "UTF-8"
	port_list = []
	def __init__(self):
		super(SerialPort, self).__init__()
		self.set_bps(115200)
		self.set_byte_size('8')
		self.set_parity('None')
		self.set_stop_bits('1')
	def set_bps(self, bps:int):
		try:
			self.baudrate = bps
			return True
		except Exception as e:
			return False
	
	def set_byte_size(self, byte_size:str):
		try:
			if byte_size == '5':
				self.bytesize = serial.FIVEBITS
			elif byte_size == '6':
				self.bytesize = serial.SIXBITS
			elif byte_size == '7':
				self.bytesize = serial.SEVENBITS
			else:
				self.bytesize = serial.EIGHTBITS
			return True	
		except Exception as e:
			return str(e)
		
	def set_parity(self, parity:str):
		try:
			if parity == 'Mark':
				self.parity = serial.PARITY_MARK
			elif parity == 'Odd':
				self.parity = serial.PARITY_ODD
			elif parity == 'Even':
				self.parity = serial.PARITY_EVEN
			elif parity == 'Names':
				self.parity = serial.PARITY_NAMES
			elif parity == 'Space':
				self.parity = serial.PARITY_SPACE
			else:
				self.parity = serial.PARITY_NONE
			return True	
		except Exception as e:
			return str(e)
	
	def set_stop_bits(self, stop_bits:str):
		try:
			if stop_bits == '1.5':
				self.stopbits = serial.STOPBITS_ONE_POINT_FIVE
			elif stop_bits == '2':
				self.stopbits = serial.STOPBITS_TWO
			else:
				self.stopbits = serial.STOPBITS_ONE
			return True
		except Exception as e:
			return str(e)
	
	def Search_ports(self):
		port_info = list(list_ports.comports())
		port_list = []
		if len(port_info) == 0:
			return []
		else:
			for i in port_info:
				port_list.append((i.name, i.description))
		return port_list
	
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
				portName = i[0]
				if target in i[1]:
					self.port = portName
					print("成功找到目标", target, "位于", portName)
					return True
			else :
				print("未找到目标：", target)
				return None
	
	def Open_port(self, portName = ""):
		if self.is_open:
			self.close()
		if portName != "":
			self.port = portName
		self.open()
	
	def Send_msg(self, msg):
		if self.is_open:
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
		self.trans_done.connect(self.trans_done_slot)
	def run(self):
		try:
			self.mainwindow.show_msg.emit('正在后台进行转换')
			res = HexShow(self.old_data, self.split_symbel, self.line_break)
			self.trans_done.emit(res)
		except Exception as e:
			print(e)
			return False

	def openStart(self, data):
		if self.isRunning():
			return False
		self.old_data = data
		self.old_string = self.new_string = ""
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
	def __init__(self, mainwindow) -> None:
		super(SerialThread, self).__init__()
		self.mainwindow = mainwindow
		self.ser = SerialPort()
		self.ser.writeTimeout = 3
	
	def run(self):
		t = None
		self.run_flag = False
		if self.connect_target():
			self.connect_sig.emit(True)
		else:
			self.connect_sig.emit(False)
			return
		self.run_flag = True
		while self.ser.is_open:
			try:
				recv_len = self.ser.in_waiting
			except:
				self.ser.close()
				self.connect_sig.emit(False)
				self.msg_sig.emit('串口\'{}\'断开'.format(self.ser.port))
				return 
			while recv_len > 0:
				try:
					res = self.ser.read_until(expected=self.split_symbol, size=recv_len)
					recv_len -= len(res)

					if self.show_print == True:
						print(res.decode('utf-8'), end='')
					if recv_len > 0:
						self.recv_data += res
						self.frame += 1
						self.decodeData(res, self.add_line_break)
						# self.read_sig.emit((res, False))
						continue
					else:
						self.recv_data += res
						self.decodeData(res, False)
						if (res[-1] != 10) & (res[-1] != 13):
							t = time.time()

				except Exception as e:
					print(e)
				break
			if self.run_flag:
				if t != None:
					if ((time.time() - t) > 0.01):
						self.frame += 1
						self.decodeData(b'', self.auto_cut)
						# print(time.time() - t)
						t = None
				self.msleep(1)
			else:
				self.ser.close()
				break
		
		self.connect_sig.emit(False)
		self.msg_sig.emit('关闭串口\'{}\''.format(self.ser.port))

	def connect_target(self):
		if self.ser.isOpen():
			self.ser.close()
		try:
			self.ser.open()
		except Exception as e:
			err = str(e)
			if 'PermissionError' in err:
				self.msg_sig.emit("连接串口'{}'失败, 可能是串口被占用".format(self.ser.port))
			else:
				self.msg_sig.emit(str(e))
			return False
		return self.ser.is_open

	def Open_Start(self, portName = "", target = "CH340", port_list = None):
		if portName != "":
			self.ser.port = portName
		elif self.ser.port == None:
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

	def set_split(self, split_str, encode):
		try:
			self.split_symbol = serial.to_bytes(split_str.encode(encode))
			return True
		except:
			return False

# s = SerialThread()

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
 