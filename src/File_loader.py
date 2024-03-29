import os
import json
import ctypes, sys

'''
@param target{str}: 目标关键字
@param bps{int}: 串口波特率
@param parameter{str}: 串口参数
@param timeout{int}: 串口超时时间
@param port_list: 串口列表
@param ser: 串口类
@param Is_open: 串口开启标志位
@param Is_cut: 是否断帧
@param receive_data: 数据接收缓存
@param sleep_time: 接收缓冲间隔 默认为0.1s
'''

default_data = {
	'bps': 115200,
	'byte_size': '8',
	'parity': 'None',
	'stop_bits': '1',
	'timeout': 1,
	'auto_cut': True,
	'cut_time': 1,
	'enter_send': True,
	'auto_send_time': 500,
	'show_send_msg': False,
	'auto_connect': False,
	# 'show_send': True,
	'limit': 1,
	'limit_len': 200,
	'set_line_break': True,
	'line_break': 0,
	'path': os.getcwd() + '\data',
	'auto_target': 'CH340',
	'fastConnect': None,
	'curveColor': '红色',
	'curveName': 'Curve',
	'backColor': '铅白',
	'findUpdate': 0,
	'font': '等线',
	'fontSize': 13,
	'limitMsgLen': 1,
	'MsgLen': 10000,
	'antialias': 1,
	'mousePos': 1,
	'pointShow': 1,
	'showXY': 1,
	'showGrid': 1,
	'update': 1,
	'newVersion': None,
	'deleteVersion': 0,
	'DTR': 0,
	'RTS': 0,
	'decode': 'UTF-8',
	'encode': 'UTF-8',
	'showLegend': 1,
	'Cache': '',
	'multi_send': [
		'',
		'',
		'',
		'',
		'',
		'',
		'',
		'',
		'',
	]
}


def getAccess():
	try:
		with open('./testFIle', 'w') as f:
			f.close()
		os.remove('./testFile')
	except PermissionError:
		if ctypes.windll.shell32.IsUserAnAdmin():
			return
		else:
			print('获取权限')
			if sys.version_info[0] == 3:
				ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
			else:#in python2.x
				ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
			return 

class Config():
	def __init__(self):
		self.default = default_data
		self.data = self.Load_config()

	def save(self, name, value):
		if os.path.exists("config.json"):
			try:
				with open("./config.json", 'r+') as config:
					data = dict(json.load(config))
					data[name] = value
					config.close()
					config = open("./config.json", 'w')
					json.dump(data, config, sort_keys=True,indent=2, separators=(',', ': '))
					config.close()
					self.data[name] = value
			except Exception as e:
				print('错误', e)
		else:
			print('无配置文件!')
			self.data_init()


	def data_init(self):
		getAccess()
		if os.path.exists('data'):
			pass
		else:
			os.mkdir('data')
		with open("./config.json", 'w') as config:
			json.dump(default_data, config, sort_keys=True,indent=2, separators=(',', ': '))
			config.close()

	def Load_config(self):
		if os.path.exists('config.json'):
			try:
				with open("./config.json", 'r') as config:
					data = json.load(config)
					config.close()
				return data
			except Exception:
				self.data_init()
				return default_data
		else:
			print('无配置文件!')
			self.data_init()
			return default_data

	def load(self, name):
		try:
			return self.data[name]
		except KeyError:
			print('key error: ', name)
			try:
				self.save(name, default_data[name])
				return default_data[name]
			except:
				print("值错误")
				return False
			return default_data[name]
				


	