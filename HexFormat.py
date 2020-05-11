'''
@Author: your name
@Date: 2020-05-03 14:09:17
@LastEditTime: 2020-05-11 16:00:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Calculation\HexFormat.py
'''


from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox


'''
@description: 将十六进制字符串格式化
@param string{str}: 十六进制字符串
@return: 格式化后的字符串
'''
def formatHex(string = ''):
    string = string.replace(' ', '')
    if len(string) % 2:
        string = string + '0'
        print("字符串有误")
    return bytes.fromhex(string)

'''
@description: 十六进制输入格式化
@param sendBox:  十六进制输入窗口窗口
'''
class currentHex():
    '''
    @description: 初始化
    @param charLen:  十六进制字符长度, 用于内部判断
    @param canChange:  避免内部改变递归, 用于内部判断
    @param lastMessageLen:  上一次总字符长度, 用于内部判断
    '''
    def __init__(self, sendBox, Back):
        self.sendBox = sendBox
        self.Back = Back
        self.charLen = 0
        self.canChange = 1
        self.lastMessageLen = 0
        self.enterSend = 0

    '''
    @description: 格式化十六进制字符串, 插入空格 
    '''
    def insertBlock(self):
        if self.canChange:
            message = self.sendBox.toPlainText()
            if len(message) > self.lastMessageLen:
                if self.enterSend:
                    if message[-1] == '\n':
                        print(1)
                        message = message[:-1]
                        self.sendBox.setPlainText(message)
                        cursor = self.sendBox.textCursor()
                        cursor.movePosition(QtGui.QTextCursor.End)
                        self.sendBox.setTextCursor(cursor)
                        self.Back.sendButton_()
                        message += '\n'
                c = ord(message[-1])
                if ((c>=48) & (c<=57)) | ((c>=65) & (c<=70)) | ((c>=97) & (c<=102)):
                    self.charLen += 1
                    if self.charLen > 1:
                        self.charLen = 0
                        message += ' '
                        self.lastMessageLen += 1
                else:
                    message = message[:-1]
                    print("输入错误字符")
            else :
                if self.charLen == 0:
                    self.charLen = 2
                elif self.charLen > 1:
                    self.charLen -= 1
            self.canChange = 0
            self.lastMessageLen = len(message)
            self.sendBox.setPlainText(message)
        else :
            self.canChange = 1
            cursor = self.sendBox.textCursor()
            cursor.movePosition(QtGui.QTextCursor.End)
            self.sendBox.setTextCursor(cursor)
    def default(self):
        if self.enterSend:
            message = self.sendBox.toPlainText()
            if len(message) > 0:
                if message[-1] == '\n':
                    self.Back.sendButton_()
                    cursor = self.sendBox.textCursor()
                    cursor.movePosition(QtGui.QTextCursor.End)
                    self.sendBox.setTextCursor(cursor)