'''
@Author: Yuzhi Tu
@Date: 2020-04-15 14:57:23
@LastEditTime: 2020-05-09 12:31:38
@LastEditors: Please set LastEditors
@Description: 与串口相关函数
@FilePath: \Serial_debugger\Serial_core.py
'''
from PyQt5.QtWidgets import QApplication, QMainWindow
import serial   
import serial.tools.list_ports
from threading import Thread
from time import time, sleep
from re import search


'''
@description: 串口收发主体
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
class Myserial(Thread):
    def __init__(self, target = 'CH340', bps = 115200, parameter = "8N1", timeout = 1, Is_cut = True, sleep_time = 0.1, DTR=0, RTS=0):
        Thread.__init__(self)
        self.target = target
        self.bps = 115200
        self.parameter = parameter
        self.timeout = timeout
        self.port_list = None
        self.portname = ""
        self.ser = None
        self.Is_open = False
        self.Is_cut = Is_cut
        self.receive_data = ""
        self.sleep_time = sleep_time
        self.Is_receive = 0
        self.receiveCount = 0
        self.data = ''
        self.DTR = DTR
        self.RTS = RTS
        #self.receive_data = self.receive_data.encode('utf-8')

    '''
    @description: 接收线程
    '''
    def run(self):
        try:
            loop = 0
            cut = True
            print ("开启线程接收数据, 来自->" + self.portname)
            while self.Is_open == True:
                sleep(self.sleep_time)     #接收间隔
                '''
                loop += 1
                if loop > 10:
                    print("\rwaiting...", end = '')
                    loop = 0
                '''
                #等待提示
                size = self.ser.inWaiting()     #获取数据长度
                if size:
                    cut = True      #设为未断帧
                    self.receiveCount += size
                    try:
                        self.data = self.ser.read(size).decode("UTF-8")
                        print(self.data)
                        self.receive_data +=self.data       #将数据保存至接收缓存
                    except Exception as e:
                        print("编码错误, 原因: ",e)
                    self.Is_receive = 1
                    
                elif self.Is_cut & cut:
                    cut = False
                    if len(self.receive_data) == 0:
                        pass
                    elif self.receive_data[-1] != '\n':
                        self.receive_data += "\n"       #自动断帧
            else:
                print("串口未打开")
                self.Is_open = False
        except Exception as e:
            print("串口断开, 原因：",e)
            self.Is_receive = 1
            self.Is_open = False
            
    '''
    @description: 列出串口列表
    '''
    
    def List_ports(self):
        self.port_list = list(serial.tools.list_ports.comports())
        #print(self.port_list)
        return self.port_list

    '''
    @description: 在串口列表中查找目标
    @param target{str}: 目标的关键词，默认为CH340 
    @return: 目标串口，错误返回None;
    '''
    def Find_target(self, target = "CH340"):
        if target != "CH340":
            self.target = target
        self.port_list = list(serial.tools.list_ports.comports())   
        #print(self.port_list)       #列出串口表
        if len(self.port_list) == 0:
            print('无可用串口')
            return None
        else:
            for i in range(0,len(self.port_list)):
                print(self.port_list[i])     #打印所有串口
                if search(self.target, str(self.port_list[i])) is not None:
                    Position = search(' ', str(self.port_list[i])).span()
                    self.portname = str(self.port_list[i])[:Position[0]]
                    #串口名
            if len(self.portname) > 0:
                print("成功找到目标", self.target, "位于", self.portname)
                return self.portname
            else :
                print("未找到目标：", self.target)
                return None

    '''
    @description: 向串口发送信息(应先打开串口)
    @param ser{serson类}: 已打开的串口
    @param msg{str}: 将发送的信息
    @param lineChange{str}: 换行符
    @return: 成功发送的字节数, 错误返回None
    '''
    def Send_data(self, msg = "", lineChange = '\r\n'):
        try:
            if self.Is_open == True:
                
                msg += lineChange
                result=self.ser.write(msg.encode())#写数据
                t = time()
                return result
                #返回成功发送的字节数
            else:
                print("串口未开启")
                return None
        except Exception as e:
            print("---异常---：",e)
            return None

    def Send_hex(self, msg = ""):
        try:
            if self.Is_open == True:
                result=self.ser.write(msg)#写数据
                t = time()
                return result
                #返回成功发送的字节数
            else:
                print("串口未开启")
                return None
        except Exception as e:
            print("---异常---：",e)
            return None
    '''
    @description: 打开串口
    @param portname{str}: 目标串口名
    @param bps{int}: 串口波特率(默认为115200)
    @param parameter{str}: 串口参数, 格式为：数据位+校验位+停止位
    @param timeout{int}: 串口超时时间, 单位为s
    @return: 成功打开返回True, 失败返回False
    '''
    def Open_port(self, portname = None, bps = 115200, parameter = "8N1", timeout = 1):
        '''
        parameter:
            数据位： FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS = (5, 6, 7, 8)
            校验位:  PARITY_NONE, PARITY_EVEN, PARITY_ODD, PARITY_MARK, PARITY_SPACE = 'N', 'E', 'O', 'M', 'S'
            停止位： STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO = (1, 1.5, 2)
        '''
        if self.Is_open == False:
            try:
                if portname == None:
                    portname = self.portname
                self.ser = serial.Serial(portname, self.bps, bytesize=int(self.parameter[0]), 
                                         parity=self.parameter[1], stopbits=float(self.parameter[2]), 
                                         timeout=self.timeout, rtscts = self.RTS, dsrdtr = self.DTR)
                self.Is_open = True
                self.start()
                return True
            except serial.serialutil.SerialException:
                print(portname+'拒绝访问, 可能是串口被占用')
                return False
        else:
            print("串口处于开启状态")

    '''
    @description: 关闭串口
    '''        
    def Close_port(self):
        try:
            self.ser.close()
            self.Is_open = False
            return True
        except Exception as e:
            print("串口关闭失败, 原因: ", e)
            return False

    '''
    @description: 将字符串格式化为16进制, 默认转接收缓存
    @param line{str}: 目标字符串
    @param part{str}: 16进制字符间的分隔符, 默认为' '
    '''
    def HexShow(self, line = '', part = ' '):
        result = ''
        LLen = len(line)
        if LLen == 0:
            line = self.receive_data
            LLen = len(self.receive_data) - 1
        for i in range(LLen + 1):
            hvol = ord(line[i])
            hhex = '%02x'%hvol
            result += hhex + part
        #print(result)
        return result

    '''
    @description: 将字符编码为16进制
    @param ch{char}: 目标字符  
    @return: 成功返回: 转换后的结果, 失败返回: None
    '''
    def Onehexcode(self, ch):
        if len(ch) == 2:
            return chr(int('02', 16))
        else:
            print('长度错误')
            return None
















