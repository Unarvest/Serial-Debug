'''
@Author: your name
@Date: 2020-04-20 23:02:46
@LastEditTime: 2020-05-17 16:17:28
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Serial_debugger\File_loader.py
'''
import os
import json

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
    'parameter': '8N1', 
    'timeout': 1,
    'Is_cut': 1,
    'sleep_time': 0.01,
    'showHex': 0, 
    'sendHex': 0, 
    'setTimeSend': 500,
    'autoConnect': 0,
    'showSend': 0,
    'limit': 1,
    'limitLen': 200,
    'lineChange': '\r\n',
    'path': '.\\data',
    'autoTarget': 'CH340',
    'fastConnect': None,
    'curveColor': '红色',
    'curveName': 'Curve',
    'backColor': '铅白',
    'findUpdate': 0,
    'font': '等线',
    'fontSize': 13,
    'limitMsgLen': 0,
    'MsgLen': 5000,
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
    'decode': 'UTF-8'
}

class Config():
    def __init__(self):
        self.default = default_data
        self.data = self.Load_config()

    def Save_data(self, name, value):
        try:
            with open(".\config.json", 'r+') as config:
                data = dict(json.load(config))
                data[name] = value
                config.close()
                config = open(".\config.json", 'w')
                json.dump(data, config)
                config.close()
                self.data[name] = value
        except Exception as e:
            print('错误', e)

    def data_init(self):
        try:
            os.mkdir('data')
        except FileExistsError:
            pass
        with open(".\config.json", 'w') as config:
            json.dump(default_data, config)
            config.close()
    
    def Load_config(self):
        try:
            with open(".\config.json", 'r') as config:
                data = json.load(config)
                config.close()
            return data
        except Exception:
            self.data_init()
            return default_data
 
    def Load_data(self, name):
        try:
            return self.data[name]
        except KeyError:
            print('key error: ', name)
            return default_data[name]
            try:
                self.Save_data(name, default_data[name])
                return default_data[name]
            except:
                print("值错误")
                return False



