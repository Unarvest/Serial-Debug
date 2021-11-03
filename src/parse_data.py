
from PySide6.QtCore import *  # type: ignore
import multiprocessing, time, re

def parse_once_process(data_pipe, decoded_pipe):
	values = {}
	begin = 0
	# pattern = re.compile(b'\w+\s*=\s*\d\.*\d*;')
	data = b''
	while True:
		(recv_data, labels) = data_pipe[1].recv()
		send_flag = False
		if len(data) - begin > 50:
			data = data[-50:] + recv_data
		else:
			data = data[begin:] + recv_data
		begin = 0
		if (labels != None) & (type(labels) == list):
			values.clear()
			for n in labels:
				values[n] = []
		
		for n in values:
			values[n].clear()
		while True:
			pos = re.search(b'\w+\s*=\s*[-]*\d\.*\d*;', data[begin:])
			if pos != None:
				pos = pos.span()
				part = data[pos[0]+begin:pos[1]+begin]
				part.replace(b' ', b'')
				begin += pos[1]
				equ_pos = part.index(b'=')
				name = part[:equ_pos].decode('utf-8')
				value = part[equ_pos+1:-1]
				try:
					l = values[name]
					send_flag = True
					l.append(float(value))
				except:
					pass
			else:
				break
		if send_flag:
			decoded_pipe[0].send(values)
			# print('s', values)


def HexShow(string = b'', split_symbel = ' ', line_break = b'\n'):
	hex_string = ""
	if line_break == b'':
		parts = [string]
	else:
		parts = string.split(line_break)
	for part in parts[:-1]:
		hex_string += part.hex(split_symbel) + ' 0a\n'
	return hex_string + parts[-1].hex(split_symbel)

def hex_show_process(args_pipe, done_pipe):
	while True:
		arg = args_pipe[1].recv()
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
		self.trans_done.connect(self.trans_done_slot)
	def run(self):
		try:
			self.mainwindow.show_msg.emit('正在后台进行转换')
			res = HexShow(self.old_data, self.split_symbel, self.line_break)
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


class DecodeData(QThread):
	decoded_sig = Signal(str)	# 接收到的数据, 断帧标识
	data_list = []
	labels = []
	def __init__(self, mainwindow):
		super(DecodeData, self).__init__()
		self.mainwindow = mainwindow
		self.run_flag = True
		self.data_pipe = multiprocessing.Pipe()
		self.decoded_pipe = multiprocessing.Pipe()
		self.parse_progress = multiprocessing.Process(target=parse_once_process, args=(self.data_pipe,self.decoded_pipe))
		self.parse_progress.start()

	def run(self):
		while self.run_flag:
			if len(self.data_list) > 0:
				data_tuple = self.data_list.pop(0)
				self.data_pipe[0].send((data_tuple[0], None))
				if data_tuple[2]:
					self.decodeData(data_tuple[0], data_tuple[1])
			else:
				self.usleep(100)

	def appendData(self, data_tuple):
		self.data_list.append(data_tuple)

	def add_label(self, name):
		self.labels.append(name)
		self.data_pipe[0].send((b'', self.labels))
	
	def del_label(self, name):
		if name in self.labels:
			self.labels.pop(self.labels.index(name))
		self.data_pipe[0].send((b'', self.labels))

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
			self.decoded_sig.emit(HexShow(data))
			self.mainwindow.trans_hex_thread.new_string += decode_string
		else:
			self.decoded_sig.emit(decode_string)