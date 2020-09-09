'''
Author: your name
Date: 2020-05-09 16:32:49
LastEditTime: 2020-08-09 15:34:38
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Serial_debugger\test.py
'''
import time
import serial
ser = serial.Serial()
def com():
    i=1
    while i<255:            #轮询COM口
        name='COM'+str(i)
        #ser.open
        try:
            #ser.is_open
            ser = serial.Serial(name)
            ser.baudrate=9600
            ser.timeout=0.5  # 读超时设置
            print(name)
 
            '''
            data = []
            # 接收返回的信息
            while True:
                count = 1
                while count <= 20:
                    ser.write('MEASure:CURRent?\n'.encode())  # 向端口写指令
                    print(count)
                    recv = ser.readline()
                    a = eval(recv)  # 将字符串str当成有效的表达式来求值并返回计算结果。
                    print("实时值：", a)
                    data.append(a)
                    print(data)
                    time.sleep(1)
                    count = count + 1
                break
            '''
 
        except serial.serialutil.SerialException:
            print("找不到设备或不能配置")
            #pass
 
        i+=1
com()