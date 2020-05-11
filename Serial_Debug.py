'''
@Author: your name
@Date: 2020-04-15 14:56:15
@LastEditTime: 2020-05-12 00:58:17
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Serial_debugger\Serial_debugger.py
'''
import sys
import os
from Serial_core import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QSplashScreen
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from Ui_Serial_MainWindow import Ui_MainWindow
#add(your program's name)  use :pyuic5 button.ui -o button.py to create.
from datetime import datetime
from re import search
import icoPack_rc

from File_loader import *
from HexFormat import *
from graph import *



class receiveTimer():
    def __init__(self):
        self.timer = QtCore.QTimer() #初始化一个定时器
        self.timer.timeout.connect(self.operate) #计时结束调用operate()方法
    def operate(self):
        global ser, window
        if ser.Is_receive:
            if data.showSend == 0:
                if data.showHex:
                    window.receiveBox.setPlainText(ser.HexShow())
                    window.graphReceiveBox.setPlainText(ser.HexShow())
                else:
                    Msg = ser.receive_data
                    window.receiveBox.setPlainText(Msg)
                    window.graphReceiveBox.setPlainText(Msg)
                cursor = window.receiveBox.textCursor()
                cursor.movePosition(QtGui.QTextCursor.End)
                window.receiveBox.setTextCursor(cursor)
                cursor = window.graphReceiveBox.textCursor()
                cursor.movePosition(QtGui.QTextCursor.End)
                window.graphReceiveBox.setTextCursor(cursor)
            graph.formatData(data = ser.data, time = 1)
            data.receiveCount += ser.receiveCount
            window.receiveCountLabel.setText(str(data.receiveCount))
            ser.receiveCount = 0
            ser.Is_receive = 0
            if ser.Is_open == False:
                try:
                    ser.Close_port()
                except Exception:
                    pass
                toMessageBox('串口断开')
                connectState(0)

class autoSendTimer():
    def __init__(self):
        self.timer = QtCore.QTimer() #初始化一个定时器
        self.timer.timeout.connect(self.operate) #计时结束调用operate()方法
        self.timer.start(10) #设置计时间隔并启动
    def operate(self):
        Back.sendButton_()
    def start(self, time):
        self.timer.start(time) #设置计时间隔并启动
    def stop(self):
        self.timer.stop()


class openPortThread(QtCore.QThread):
    def __init__(self):
        super(openPortThread, self).__init__()

    def run(self):
        No_find = 0
        if data.portname != None:
            ser.portname = data.portname
        else:
            if ser.Find_target() == None:
                No_find = 1
                toMessageBox('未找到设备')
        if No_find:
            toMessageBox('未找到设备')
            connectState(0)
        elif ser.Open_port() == False:
            toMessageBox('拒绝访问, 可能是串口被占用')
            connectState(0)
        else:
            window.messageBox.setText('连接成功')
            window.graphMsgBox.setText('连接成功')
            data.portname = ser.portname
            connectState(1)
        if ser.port_list != None:
            window.serialListWidget.clear()
        try:
            for i in range(len(ser.port_list)):
                window.serialListWidget.addItem(str(ser.port_list[i]))
        except Exception:
            pass
        self.quit()

    def openStart(self):
        self.start()
        self.exec_()

class autoConnectThread(QtCore.QThread):
    def __init__(self):
        super(autoConnectThread, self).__init__()

    def run(self):
        global ser, data, receiveT
        connectState(2)
        ser = Myserial(bps=data.bps, parameter=data.parameter, timeout=data.timeout, Is_cut=data.Is_cut, sleep_time=data.sleep_time)
        def auto():
            global ser
            window.messageBox.setText('正在自动连接' + data.autoTarget)
            window.graphMsgBox.setText('正在自动连接' + data.autoTarget)
            self.quit()
            #ser = Myserial(bps=data.bps, parameter=data.parameter, timeout=data.timeout, Is_cut=data.Is_cut, sleep_time=data.sleep_time)
            if ser.Find_target(target=data.autoTarget) == None:
                window.messageBox.setText('未找到' + data.autoTarget)
                window.graphMsgBox.setText('未找到' + data.autoTarget)
                connectState(0)
            else:
                if ser.Open_port() == False:
                    connectState(0)
                    window.messageBox.setText('连接失败, 串口可能被占用')
                    window.graphMsgBox.setText('连接失败, 串口可能被占用')
                else:
                    window.messageBox.setText('连接成功')
                    window.graphMsgBox.setText('连接成功')
                    connectState(1)
            if ser.port_list != None:
                window.serialListWidget.clear()
            try:
                data.opening = 1
                for i in range(len(ser.port_list)):
                    window.serialListWidget.addItem(str(ser.port_list[i]))
                data.opening = 0
            except Exception:
                pass
            
        
        if data.fastConnect != None:
            toMessageBox('快速连接中')
            ser.portname = data.fastConnect
            if ser.Open_port(portname=data.fastConnect) == False:
                toMessageBox('快速连接失败')
                data.fastConnect = None
                data.file.Save_data('fastConnect', None)
                window.fastConnectRadioButton.setChecked(0)
                if data.autoConnect:
                    auto()
            else:
                toMessageBox('快速连接成功, 已连接到' + data.fastConnect)
                connectState(1)
        elif data.autoConnect:
            auto()
        else:
            connectState(0)
    def openStart(self):
        self.start()
        

class listPortThread(QtCore.QThread):
    def __init__(self):
        super(listPortThread, self).__init__()

    def run(self):
        data.searching = 1
        window.searchSerialButton.setText('搜索中')
        port_list = list(serial.tools.list_ports.comports())
        window.serialListWidget.clear()
        for i in range(len(port_list)):
            window.serialListWidget.addItem(str(port_list[i]))
        data.searching = 0
        window.searchSerialButton.setText('搜索串口')
        toMessageBox('找到' + str(len(port_list)) + '个设备')
        self.quit()

    def openStart(self):
        self.start()
        self.exec_()
        
class callBack():
    def sendButton_(self):
        global ser, window, MainWindow, _translate
        if ser.Is_open:
            Msg = window.sendBox.toPlainText()
            if data.sendHex:
                if data.lineChange == '\r\n':
                    Msg += '0A 0D'
                elif data.lineChange == '\r':
                    Msg += '0A'
                elif data.lineChange == '\n':
                    Msg += '0D'
                res = ser.Send_hex(formatHex(Msg))
            else:
                if Text.enterSend:
                    if Msg[-1] == '\n':
                        Msg = Msg[:-1]
                    window.sendBox.setPlainText(Msg)
                res = ser.Send_data(Msg, lineChange=data.lineChange)
            data.sendCount += res
            window.sendCountLabel.setText(str(data.sendCount))
            if res != None:
                if data.lineChange == None:
                    pass
                elif data.sendHex == 0:
                    Msg += data.lineChange
                Msg = Msg.replace('\n', '\\n')
                Msg = Msg.replace('\r', '\\r')
                toMessageBox("[{}]-> ".format(res) + Msg)
            else:
                toMessageBox("None!")
        else:
            QMessageBox.warning(MainWindow, '警告', '串口未开启')
            connectState(0)

    def graphSendButton_(self):
        global ser, window, MainWindow, _translate
        if ser.Is_open:
            Msg = window.graphSendBox.toPlainText()
            if Text.enterSend:
                if Msg[-1] == '\n':
                    Msg = Msg[:-1]
                window.sendBox.setPlainText(Msg)
            res = ser.Send_data(Msg, lineChange=data.lineChange)
            data.sendCount += res
            window.sendCountLabel.setText(str(data.sendCount))
            if res != None:
                if data.lineChange == None:
                    pass
                elif data.sendHex == 0:
                    Msg += data.lineChange
                Msg = Msg.replace('\n', '\\n')
                Msg = Msg.replace('\r', '\\r')
                toMessageBox("[{}]->".format(res) + Msg)
            else:
                toMessageBox("None!")
        else:
            QMessageBox.warning(MainWindow, '警告', '串口未开启')
            connectState(0)
        
    def bpscomboBox_(self, value):
        data.bps = int(value)
        data.file.Save_data('bps', data.bps)

    def byteSizeComboBox_(self, value):
        data.parameter = value + data.parameter[1:]
        data.file.Save_data('parameter', data.parameter)

    def parityComboBox_(self, value):
        data.parameter = data.parameter[0]+ value[0] + data.parameter[2:]
        data.file.Save_data('parameter', data.parameter)

    def stopBitsComboBox_(self, value):
        data.parameter = data.parameter[:2] + value
        data.file.Save_data('parameter', data.parameter)

    def graphColorComboBox_(self, value):
        data.curveColor = value
        data.file.Save_data('curveColor', data.curveColor)
        if search(colorSelect(), graph.Pencolor) == None:
            window.addGraphColor.setText('添加曲线')
        else:
            window.addGraphColor.setText('删除曲线')
    
    def backColorComboBox_(self, value):
        data.backColor = value
        data.file.Save_data('backColor', data.backColor)
        toMessageBox('背景将在重新启动后更改！')
    
    def graphColorName_(self, value):
        data.curveName = value
        data.file.Save_data('curveName', data.curveName)

    def openSerialButton_(self):
        global ser, MainWindow, window, _translate
        if ser.Is_open:
            ser.Close_port()
            toMessageBox('串口已关闭')
            connectState(0)
        elif data.opening:
            QMessageBox.warning(MainWindow, '警告', '串口打开中...')
        else:
            #将数据载入ser
            ser = Myserial(bps=data.bps, parameter=data.parameter, timeout=data.timeout, Is_cut=data.Is_cut, sleep_time=data.sleep_time)
            connectState(2)
            t = openPortThread()
            t.exit()
            t.openStart()
            
    def sendHexCheckBox_(self, value):
        global Text, Back
        if value == 0:
            data.sendHex = 0
            enter = Text.enterSend
            Text = currentHex(window.sendBox, Back)
            Text.enterSend = enter
            window.sendBox.textChanged.connect(Text.default)
        else:
            data.sendHex = 1
            enter = Text.enterSend
            Text = currentHex(window.sendBox, Back)
            Text.enterSend = enter
            window.sendBox.textChanged.connect(Text.insertBlock)
        data.file.Save_data('showHex', data.showHex)
            
    def showHexCheckBox_(self, value):
        if value == 0:
            data.showHex = 0
        else:
            data.showHex = 1
        ser.Is_receive = 1
        data.file.Save_data('showHex', data.showHex)

    def cutFrameCheckBox_(self, value):
        if value == 0:
            data.Is_cut = 0
        else:
            data.Is_cut = 1
        data.file.Save_data('Is_cut', data.Is_cut)
        ser.Is_cut = data.Is_cut
    
    def cutTimeSpinBox_(self, value):
        data.sleep_time = value / 1000
        data.file.Save_data('sleep_time', data.sleep_time)
        ser.sleep_time = data.sleep_time

    def sendTimeSpinBox_(self, value):
        global autoSend, data, window
        data.setTimeSend = value
        data.file.Save_data('setTimeSend', data.setTimeSend)
        if window.sendTimeCheckBox.checkState() == 2:
            autoSend.stop()
            autoSend.start(data.setTimeSend)

    def saveMsgPushButton_(self):
        try:
            name = datetime.now().strftime("%Y%m%d-%H%M%S.txt")
            Msg = window.receiveBox.toPlainText()
            if len(Msg) == 0:
                if QMessageBox.warning(MainWindow, '警告', '接收信息为空, 是否继续保存?',QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
                    megfile = open(data.path + '\\' + name, 'w')
                    megfile.write(Msg)
                    QMessageBox.information(MainWindow, '提示', name + '\n保存成功!')
                    toMessageBox('保存成功')
                    megfile.close()
            else:
                megfile = open(data.path + '\\' + name, 'w')
                megfile.write(Msg)
                QMessageBox.information(MainWindow, '提示', name + '\n保存成功!')
                toMessageBox('保存成功')
                megfile.close()
            
        except Exception as e:
            QMessageBox.warning(MainWindow, '警告', '保存文件错误, 原因\n' + str(e))
    
    def cleanMsgPushButton_(self):
        window.receiveBox.setPlainText('')
        window.graphReceiveBox.setPlainText('')
        ser.receive_data = ''
    
    def autoConnectCheckBox_(self, value):
        if value == 0:
            data.autoConnect = 0
        else:
            data.autoConnect = 1
        data.file.Save_data('autoConnect', data.autoConnect)
    
    def fastConnectRadioButton_(self, value):
        if value == True:
            if data.portname == None:
                QMessageBox.warning(MainWindow, '警告', '当前未选中串口, 无法使用快速启动')
                window.fastConnectRadioButton.setChecked(0)
            else:
                data.fastConnect = data.portname
                data.file.Save_data('fastConnect', data.fastConnect)
                toMessageBox('下次启动将优先连接' + data.fastConnect)
        if value == False:
            data.fastConnect = None
            data.file.Save_data('fastConnect', data.fastConnect)
            toMessageBox('关闭快速连接')

    def autoConnectLineEdit_(self, value):
        data.autoTarget = value
        data.file.Save_data('autoTarget', data.autoTarget)
    

    def searchSerialButton_(self):
        '''
        global ser, data
        if ser.Is_open:
            QMessageBox.warning(MainWindow, '警告', '串口已打开, 请先关闭串口')
        elif data.opening:
            QMessageBox.warning(MainWindow, '警告', '串口正在打开')
        '''
        if data.searching:
            QMessageBox.warning(MainWindow, '警告', '串口搜索中')
        else:
            global t
            t = listPortThread()
            t.openStart()
            
    def serialListWidget_(self, value):
        global ser
        port = value.text()
        Position = search(' ', port).span()
        data.portname = port[:Position[0]]
        toMessageBox('选中: ' + data.portname)
        
    def showSendCheckBox_(self, value):
        if value == 0:
            data.showSend = 0
        else:
            data.showSend = 1
        data.file.Save_data('showSend', data.showSend)

    def lineChangeComboBox_(self, value):
        if value == 0:
            data.lineChange = '\r\n'
        elif value == 1:
            data.lineChange = '\r'
        elif value == 2:
            data.lineChange = '\n'
        else :data.lineChange = '' 
        data.file.Save_data('lineChange', data.lineChange)

    def enterSendCheckBox_(self, value):
        global Text
        if value == True:
            Text.enterSend = 1
        else:
            Text.enterSend = 0
    
    def sendTimeCheckBox_(self, value):
        global autoSend, data
        if value == True:
            if ser.Is_open:
                autoSend = autoSendTimer()
                autoSend.start(data.setTimeSend)
                toMessageBox('开启定时发送')
            else:
                QMessageBox.warning(MainWindow, '警告', '串口未开启!')
                toMessageBox('无法开启定时发送')
                window.sendTimeCheckBox.setChecked(0)
        else:
            autoSend.stop()
            toMessageBox('关闭定时发送')
    
    def customCheckBox_(self, value):
        window.customCheckBox.setChecked(0)
        QMessageBox.information(MainWindow, '提示', '暂时不可用')


    def addGraphColor_(self):
        #红r, 绿g, 蓝b, 青c, 粉m, 黄y, 白w
        color = colorSelect()
        if search(color, graph.Pencolor) == None:
            if data.limit == True:
                res = graph.addPen(color = color, name = data.curveName, limit = data.limitLen)
            else:
                res = graph.addPen(color = color, name = data.curveName, limit = None)
            if res == False:
                QMessageBox.warning(MainWindow, '警告', '颜色已存在')
                window.addGraphColor.setText('添加曲线')
            elif res == None:
                QMessageBox.warning(MainWindow, '警告', '标签重复')
                window.addGraphColor.setText('添加曲线')
            else:
                window.addGraphColor.setText('删除曲线')
                Index = window.graphColorComboBox.currentIndex() + 1
                if Index == 8:
                    Index = 0
                window.graphColorComboBox.setCurrentIndex(Index)            
            
        else:
            graph.killPen(color)
            window.addGraphColor.setText('添加曲线')
    
    def clearDataButton_(self):
        graph.clearAll()
    
    def limitCheckBox_(self, value):
        data.limit = value
        data.file.Save_data('limit', data.limit)
        if value == True:
            graph.changeLimit(limit = data.limitLen)
        else:
            graph.changeLimit(limit = None)

    def limitLenSpinBox_(self, value):
        data.limitLen = value
        data.file.Save_data('limitLen', data.limitLen)
        if data.limit == True:
            graph.changeLimit(limit = data.limitLen)
    
    def saveDataButton_(self):
        name = graph.outputGraph(path = data.path)
        if name != False:
            QMessageBox.information(MainWindow, '提示', '图片保存为' + name)
        else:
            QMessageBox.warning(MainWindow, '警告', '保存失败')
    
    def cleanMessageButton_(self):
        window.sendCountLabel.setText('--')
        window.receiveCountLabel.setText('--')
        toMessageBox('')
        if ok:
            '''
            f = open('./f', 'w')
            f.write(font)
            f.close()
            f = open('./f', 'r')
            font = f.read(font)
            window.searchSerialButton.setFont(font)
            f.close()
            '''
            print(font.getFamily())

def colorSelect():
    color = ''
    if data.curveColor == '红色':
        color = 'r'
    elif data.curveColor == '绿色':
        color = 'g'
    elif data.curveColor == '蓝色':
        color = 'b'
    elif data.curveColor == '青色':
        color = 'c'
    elif data.curveColor == '粉色':
        color = 'm'
    elif data.curveColor == '黄色':
        color = 'y'
    elif data.curveColor == '白色':
        color = 'w'
    elif data.curveColor == '黑色':
        color = 'k'
    else:
        color = 'r'
    return color

def backColorSelect():
    if data.backColor == '铅白':
        color = 'f0f0f4'
    elif data.backColor == '纯白':
        color = 'ffffff'
    elif data.backColor == '莹白':
        color = 'e3f9fd'
    elif data.backColor == '纯黑':
        color = 'k'
    elif data.backColor == '素':
        print(1)
        color = 'e0f0e9'
    elif data.backColor == '墨色':
        color = '50616d'
    else:
        color = 'k'
    return color


class dataInit():
    def __init__(self, window):
        #载入数据
        self.file = Config()
        self.bps = self.file.Load_data('bps')
        self.parameter = self.file.Load_data('parameter')
        self.timeout = self.file.Load_data('timeout')
        self.Is_cut = self.file.Load_data('Is_cut')
        self.sleep_time = self.file.Load_data('sleep_time')
        self.showHex = self.file.Load_data('showHex')
        self.sendHex = self.file.Load_data('sendHex')
        self.lineChange = self.file.Load_data('lineChange')
        self.setTimeSend = self.file.Load_data('setTimeSend')
        self.path = self.file.Load_data('path')
        self.autoConnect = self.file.Load_data('autoConnect')
        self.fastConnect = self.file.Load_data('fastConnect')
        self.autoTarget = self.file.Load_data('autoTarget')
        self.showSend = self.file.Load_data('showSend')
        self.curveColor = '红色'
        self.curveName = self.file.Load_data('curveName')
        self.backColor = self.file.Load_data('backColor')
        self.limitLen = self.file.Load_data('limitLen')
        self.limit = self.file.Load_data('limit')
        self.target = None
        self.portname = None
        self.opening = 0
        self.searching = 0
        self.sendCount = 0
        self.receiveCount = 0
        
        #将数据载入控件
        window.byteSizeComboBox.setCurrentText(self.parameter[0])
        if self.parameter[1] == 'N':
            window.parityComboBox.setCurrentText('None')
        elif self.parameter[1] == 'E':
            window.parityComboBox.setCurrentText('Even')
        elif self.parameter[1] == 'M':
            window.parityComboBox.setCurrentText('Mark')
        elif self.parameter[1] == 'O':
            window.parityComboBox.setCurrentText('Odd')
        window.bpscomboBox.setCurrentText(str(self.bps))
        window.stopBitsComboBox.setCurrentText(self.parameter[2:])
        window.graphColorComboBox.setCurrentText(self.curveColor)
        window.backColorComboBox.setCurrentText(self.backColor)
        window.graphColorName.setText(self.curveName)
        window.showHexCheckBox.setChecked(self.showHex)
        window.showSendCheckBox.setChecked(self.showSend)
        window.cutFrameCheckBox.setChecked(self.Is_cut)
        window.sendHexCheckBox.setChecked(self.sendHex)
        window.autoConnectCheckBox.setChecked(self.autoConnect)
        window.limitCheckBox.setChecked(self.limit)
        if self.fastConnect == None:
            window.fastConnectRadioButton.setChecked(0)
        else:
            window.fastConnectRadioButton.setChecked(1)
        if self.lineChange == '\r\n':
            window.lineChangeComboBox.setCurrentIndex(0)
        elif self.lineChange == '\r':
            window.lineChangeComboBox.setCurrentIndex(1)
        elif self.lineChange == '\n':
            window.lineChangeComboBox.setCurrentIndex(2)
        else:
            window.lineChangeComboBox.setCurrentIndex(3)
        window.autoConnectLineEdit.setText(self.autoTarget)
        window.cutTimeSpinBox.setValue(int(self.sleep_time * 1000))
        window.sendTimeSpinBox.setValue(self.setTimeSend)
        window.limitLenSpinBox.setValue(self.limitLen)
        window.sendTimeCheckBox.setChecked(0)
        window.bpscomboBox.currentTextChanged.connect(Back.bpscomboBox_)
        window.byteSizeComboBox.currentTextChanged.connect(Back.byteSizeComboBox_)
        window.parityComboBox.currentTextChanged.connect(Back.parityComboBox_)
        window.stopBitsComboBox.currentTextChanged.connect(Back.stopBitsComboBox_)
        window.openSerialButton.clicked.connect(Back.openSerialButton_)
        window.showHexCheckBox.clicked.connect(Back.showHexCheckBox_)
        window.sendHexCheckBox.clicked.connect(Back.sendHexCheckBox_)
        window.cutFrameCheckBox.clicked.connect(Back.cutFrameCheckBox_)
        window.cutTimeSpinBox.valueChanged.connect(Back.cutTimeSpinBox_)
        window.saveMsgPushButton.clicked.connect(Back.saveMsgPushButton_)
        window.cleanMsgPushButton.clicked.connect(Back.cleanMsgPushButton_)
        window.cleanGraphMsgButton.clicked.connect(Back.cleanMessageButton_)
        window.sendButton.clicked.connect(Back.sendButton_)
        window.cleanMessageButton.clicked.connect(Back.cleanMessageButton_)
        window.autoConnectCheckBox.clicked.connect(Back.autoConnectCheckBox_)
        window.autoConnectLineEdit.textChanged.connect(Back.autoConnectLineEdit_)
        window.searchSerialButton.clicked.connect(Back.searchSerialButton_)
        window.serialListWidget.itemClicked.connect(Back.serialListWidget_)
        window.showSendCheckBox.clicked.connect(Back.showSendCheckBox_)
        window.lineChangeComboBox.currentIndexChanged.connect(Back.lineChangeComboBox_)
        window.fastConnectRadioButton.clicked.connect(Back.fastConnectRadioButton_)
        window.enterSendCheckBox.clicked.connect(Back.enterSendCheckBox_)
        window.sendTimeSpinBox.valueChanged.connect(Back.sendTimeSpinBox_)
        window.sendTimeCheckBox.clicked.connect(Back.sendTimeCheckBox_)
        global Text
        Text = currentHex(window.sendBox, Back)
        window.sendBox.textChanged.connect(Text.default)
        window.customCheckBox.clicked.connect(Back.customCheckBox_)
        window.graphSendButton.clicked.connect(Back.graphSendButton_)
        window.graphColorComboBox.currentTextChanged.connect(Back.graphColorComboBox_)
        window.backColorComboBox.currentTextChanged.connect(Back.backColorComboBox_)
        window.graphColorName.textChanged.connect(Back.graphColorName_)
        window.addGraphColor.clicked.connect(Back.addGraphColor_)
        window.clearDataButton.clicked.connect(Back.clearDataButton_)
        window.limitCheckBox.clicked.connect(Back.limitCheckBox_)
        window.limitLenSpinBox.valueChanged.connect(Back.limitLenSpinBox_)
        window.saveDataButton.clicked.connect(Back.saveDataButton_)
        
        
        
        
        
def toMessageBox(msg):
    window.messageBox.setText(msg)
    window.graphMsgBox.setText(msg)

#可连接 0 已连接1 正在连接2
def connectState(state):
    if state == 0:
        window.openSerialButton.setText(_translate("MainWindow", "打开串口"))
        window.connectStateRadioButton.setChecked(0)
        window.connectStateRadioButton.setCheckable(0)
        data.opening = 0
    elif state == 1:
        window.openSerialButton.setText(_translate("MainWindow", "关闭串口"))
        window.connectStateRadioButton.setCheckable(1)
        window.connectStateRadioButton.setChecked(1)
        data.opening = 1
    else:
        window.openSerialButton.setText(_translate("MainWindow", "正在连接"))
        window.connectStateRadioButton.setCheckable(1)
        window.connectStateRadioButton.setChecked(1)
        data.opening = 1

class QMainWindowClose(QMainWindow):
    def closeEvent(self, event):
        os._exit(0)

if __name__ == '__main__':
    global data, Back, MainWindow, window, _translate, ser
    global receiveT, graph
    app = QApplication(sys.argv)


    # 创建启动界面，支持png透明图片
    splash = QSplashScreen(QtGui.QPixmap(":/Mainico/Start2.png"))
    splash.show()

    Back = callBack()
    _translate = QtCore.QCoreApplication.translate
    MainWindow = QMainWindowClose()
    
    window = Ui_MainWindow()
    window.setupUi(MainWindow)
    data = dataInit(window)
    receiveT = receiveTimer()
    autoConnect = autoConnectThread()
    autoConnect.openStart()
    graph = MyGraphWindow(window.graph_Layout, BackColor=backColorSelect())
    receiveT.timer.start(1)
    toMessageBox("启动完成")
    MainWindow.show()
    splash.close()
    autoConnect.exec_()
    sys.exit(app.exec_())
