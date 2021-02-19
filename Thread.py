from PyQt5 import QtCore, QtGui

class receiveTimer():
	def __init__(self):
		self.timer = QtCore.QTimer()                #初始化一个定时器
		self.timer.timeout.connect(self.operate)    #计时结束调用operate()方法
	def operate(self):
		global ser, window, data
		if ser.Is_receive:
			if data.showSend == 1:
				if data.showHex:
					window.receiveBox.setPlainText(ser.HexShow())
					window.graphReceiveBox.setPlainText(ser.HexShow())
				else:
					Msg = ser.receive_data
					if data.file.Load_data('limitMsgLen'):
						msgLen = len(Msg)
						limitLen = data.file.Load_data('MsgLen')
						if msgLen > limitLen:
							ser.receive_data = ser.receive_data[-limitLen:]
							Msg = ser.receive_data
					window.receiveBox.setPlainText(Msg)
					window.graphReceiveBox.setPlainText(Msg)

				#移动光标到末尾
				cursor = window.receiveBox.textCursor()
				cursor.movePosition(QtGui.QTextCursor.End)
				window.receiveBox.setTextCursor(cursor)
				cursor = window.graphReceiveBox.textCursor()
				cursor.movePosition(QtGui.QTextCursor.End)
				window.graphReceiveBox.setTextCursor(cursor)

			if data.showCurve == 1:
				graph.formatData(data = ser.data, time = 1)
			data.receiveCount += ser.receiveCount
			window.receiveCountLabel.setText(str(data.receiveCount))
			ser.receiveCount = 0
			ser.Is_receive = 0
			if ser.Is_open == False:
				try:
					if ser.Is_open:
						ser.Close_port()
						data.file.Save_data('Cache', ser.receive_data)
				except Exception:
					pass
				if data.opening == 0:
					connectState(0)