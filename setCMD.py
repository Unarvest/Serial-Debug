

from Ui_cmdSetWindow import Ui_Form
from PyQt5.QtWidgets import QWidget, QLineEdit, QCompleter, QDialog, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import Qt, QEvent, pyqtSignal
from PyQt5.QtGui import QKeyEvent
import os, json


defaultCMDList = {
}

Linux_CMD_List = {
  "PATH": "",
  "cal": "\u663e\u793a\u65e5\u5386",
  "cat": "",
  "cd": "change directory",
  "chmod": "",
  "chown": "",
  "cp": "\u590d\u5236\u6587\u4ef6",
  "data": "\u663e\u793a\u65e5\u671f\u65f6\u95f4",
  "depth": "",
  "df": "\u663e\u793a\u78c1\u76d8\u7a7a\u95f4\u4f7f\u7528\u60c5\u51b5",
  "du": "\u67e5\u770b\u4f7f\u7528\u7a7a\u95f4",
  "find": "\u67e5\u627e\u6587\u4ef6",
  "free": "\u663e\u793a\u7cfb\u7edf\u5185\u5b58\u60c5\u51b5",
  "grep": "\u6587\u672c\u641c\u7d22",
  "head": "",
  "kill": "\u7ed3\u675f\u8fdb\u7a0b",
  "less": "",
  "list": "list",
  "ln": "\u94fe\u63a5",
  "locate": "\u641c\u7d22",
  "ls": "\u5217\u51fa\u6587\u4ef6\u5217\u8868",
  "mkdir": "\u521b\u5efa\u6587\u4ef6\u5939",
  "more": "",
  "mv": "\u79fb\u52a8\u6587\u4ef6",
  "ps": "\u67e5\u770b\u8fdb\u7a0b\u72b6\u6001",
  "pwd": "\u67e5\u770b\u5f53\u524d\u8def\u5f84",
  "rm": "\u5220\u9664",
  "rndir": "\u5220\u9664\u6587\u4ef6\u5939",
  "swap": "",
  "tail": "",
  "top": "\u67e5\u770b\u8fdb\u7a0b\u4f7f\u7528\u60c5\u51b5",
  "wc": "\u7edf\u8ba1\u5b57\u6570",
  "whereis": "\u641c\u7d22\u7a0b\u5e8f",
  "which": "\u67e5\u627e\u6587\u4ef6"
}

HC05_CMD_List = {
  "": "",
  "AT": "\u6d4b\u8bd5\u6307\u4ee4",
  "AT+ADCN?": "\u83b7\u53d6\u84dd\u7259\u914d\u5bf9\u5217\u8868\u4e2d\u8ba4\u8bc1\u8bbe\u5907\u6570",
  "AT+ADDR?": "\u83b7\u53d6\u6a21\u5757\u5730\u5740",
  "AT+BIND": "\u8bbe\u7f6e/\u67e5\u8be2-\u7ed1\u5b9a\u84dd\u7259\u5730\u5740",
  "AT+CLASS": "\u8bbe\u7f6e/\u67e5\u8be2-\u8bbe\u5907\u7c7b",
  "AT+CMODE": "\u8bbe\u7f6e/\u67e5\u8be2-\u8fde\u63a5\u6a21\u5f0f",
  "AT+DISC": "\u65ad\u5f00\u8fde\u63a5",
  "AT+ENSNIFF=": "\u8fdb\u5165\u8282\u80fd\u6a21\u5f0f",
  "AT+EXSNIFF=": "\u9000\u51fa\u8282\u80fd\u6a21\u5f0f",
  "AT+FSAD": "\u4ece\u84dd\u7259\u914d\u5bf9\u5217\u8868\u4e2d\u67e5\u627e\u6307\u5b9a\u8ba4\u8bc1\u8bbe\u5907",
  "AT+IAC": "\u8bbe\u7f6e/\u67e5\u8be2-\u67e5\u8be2\u8bbf\u95ee\u7801",
  "AT+INIT": "\u521d\u59cb\u5316 SPP \u89c4\u8303\u5e93",
  "AT+INQ": "\u67e5\u8be2\u84dd\u7259\u8bbe\u5907",
  "AT+INQC": "\u53d6\u6d88\u67e5\u8be2\u84dd\u7259\u8bbe\u5907",
  "AT+INQM": "\u8bbe\u7f6e/\u67e5\u8be2-\u67e5\u8be2\u8bbf\u95ee\u6a21\u5f0f",
  "AT+IPSCAN": "\u8bbe\u7f6e/\u67e5\u8be2-\u5bfb\u547c\u626b\u63cf\u3001\u67e5\u8be2\u626b\u63cf\u53c2\u6570",
  "AT+LINK=": "\u8fde\u63a5\u8bbe\u5907",
  "AT+MPIO": "\u8bbe\u7f6e PIO \u591a\u7aef\u53e3\u8f93\u51fa",
  "AT+MRAD?": "\u83b7\u53d6\u6700\u8fd1\u4f7f\u7528\u8fc7\u7684\u84dd\u7259\u8ba4\u8bc1\u8bbe\u5907\u5730\u5740",
  "AT+NAME": "\u8bbe\u7f6e/\u67e5\u8be2\u8bbe\u5907\u540d\u79f0",
  "AT+ORGL": "\u6062\u590d\u9ed8\u8ba4\u72b6\u6001",
  "AT+PAIR=": "\u8bbe\u5907\u914d\u5bf9",
  "AT+PIO": "\u8bbe\u7f6e PIO \u5355\u7aef\u53e3\u8f93\u51fa",
  "AT+POLAR": "\u8bbe\u7f6e/\u67e5\u8be2- LED ",
  "AT+PSWD": "\u8bbe\u7f6e/\u67e5\u8be2-\u914d\u5bf9\u7801",
  "AT+RESET": "\u6a21\u5757\u590d\u4f4d",
  "AT+RMAAD": "\u4ece\u84dd\u7259\u914d\u5bf9\u5217\u8868\u4e2d\u5220\u9664\u6240\u6709\u8ba4\u8bc1\u8bbe\u5907",
  "AT+RMSAD=": "\u4ece\u84dd\u7259\u914d\u5bf9\u5217\u8868\u4e2d\u5220\u9664\u6307\u5b9a\u8ba4\u8bc1\u8bbe\u5907",
  "AT+RNAME?": "\u83b7\u53d6\u8fdc\u7a0b\u84dd\u7259\u8bbe\u5907\u540d\u79f0",
  "AT+ROLE": "\u8bbe\u7f6e/\u67e5\u8be2-\u6a21\u5757\u89d2\u8272",
  "AT+SENM": "\u8bbe\u7f6e/\u67e5\u8be2-\u5b89\u5168\u3001\u52a0\u5bc6\u6a21\u5f0f",
  "AT+SNIFF": "\u8bbe\u7f6e/\u67e5\u8be2-SNIFF \u8282\u80fd\u53c2\u6570",
  "AT+STATE?": "\u83b7\u53d6\u84dd\u7259\u6a21\u5757\u5de5\u4f5c\u72b6\u6001",
  "AT+UART": "\u8bbe\u7f6e/\u67e5\u8be2-\u4e32\u53e3\u53c2\u6570",
  "AT+VERSION?": "\u83b7\u53d6\u8f6f\u4ef6\u7248\u672c\u53f7"
}

cmdListFileName = 'CMDList.json'

'''
@description: 自动补全QLineEdit
@param model: 补全列表
@param separator: 分割标识符
@param addSpaceAfterCompleting: 添加尾随文本
@param tailText: 尾随文本
'''
class AutoCompleteEdit(QLineEdit):
	keyUpSignal = pyqtSignal()
	keyDownSignal = pyqtSignal()
	def __init__(self, model = [], separator=' ', addSpaceAfterCompleting=False, tailText = ' '):
		super(AutoCompleteEdit, self).__init__()
		self._tailText = tailText
		self._separator = separator
		self._addSpaceAfterCompleting = addSpaceAfterCompleting
		self.setFocusPolicy(Qt.ClickFocus)
		self._setupCompleter(model)
		self._keysToIgnore = [Qt.Key_Enter,
							  Qt.Key_Return,
							  Qt.Key_Escape,
							  Qt.Key_Tab]
		self.installEventFilter(self)

	'''
	@description: tab选择的补全框
	@param signal: 补全回调
	@param model: 补全列表
	'''
	class Mycompleter(QCompleter):
		def __init__(self, signal, model):
			super().__init__(model)
			self.signal = signal

		def eventFilter(self, objwatched, event):
			if event.type() == QEvent.KeyPress:
				if event.key() == Qt.Key_Tab:
					if self.signal._completer.popup().isVisible():
						self.signal._insertCompletion(self.signal._completer.currentCompletion())
						self.signal._completer.popup().hide()
					return True
			return super().eventFilter(objwatched, event)
	'''
	@description: 设置补全
	@param model: 补全列表
	'''
	def _setupCompleter(self, model):
		self._completer = self.Mycompleter(self, model)
		self._completer.setWidget(self)
		self._completer.installEventFilter(self._completer)
		self._completer.activated.connect(self._insertCompletion)
	'''
	@description: 插入补全字符
	@param completion: 补全文本
	'''
	def _insertCompletion(self, completion):
		extra = len(completion) - len(self._completer.completionPrefix())
		if extra > 0:
			extra_text = completion[-extra:]
			if self._addSpaceAfterCompleting:
				extra_text += self._tailText
			self.setText(self.text() + extra_text)

	'''
	@description: 待补全文本
	'''
	def textUnderCursor(self):
		text = self.text()
		textUnderCursor = ''
		i = self.cursorPosition() - 1
		while i >= 0 and text[i] != self._separator:
			textUnderCursor = text[i] + textUnderCursor
			i -= 1
		return textUnderCursor

	def keyPressEvent(self, event):
		if self._completer.popup().isVisible():
			if event.key() in self._keysToIgnore:
				# self._insertCompletion()
				event.ignore()
				return
		if event.key() == Qt.Key_Return:
			return super(AutoCompleteEdit, self).keyPressEvent(event)
		super(AutoCompleteEdit, self).keyPressEvent(event)
		completionPrefix = self.textUnderCursor()
		if completionPrefix != self._completer.completionPrefix():
			self._updateCompleterPopupItems(completionPrefix)
		if len(event.text()) > 0 and len(completionPrefix) > 0:
			self._completer.complete()
		if len(completionPrefix) == 0:
			self._completer.popup().hide()

	'''
	@description: 补全弹窗内容设置
	@param completionPrefix: 补全文本匹配子串
	'''
	def _updateCompleterPopupItems(self, completionPrefix):
		self._completer.setCompletionPrefix(completionPrefix)
		self._completer.popup().setCurrentIndex(
			self._completer.completionModel().index(0, 0))

	def eventFilter(self, objwatched, event):
		if event.type() == QEvent.KeyPress:
			if event.key() == Qt.Key_Tab:
				# if self.text()[-1] != ' ':
				#	 self.setText(self.text() + ' ')
				return True
			elif event.key() == Qt.Key_Up:
				self.keyUpSignal.emit()
			elif event.key() == Qt.Key_Down:
				self.keyDownSignal.emit()
		return super().eventFilter(objwatched, event)


class CMDSendLine():
	def __init__(self, window, SendFunc = None, maxListLen = 20):
		self.sendList = []		  #已发送消息列表
		self.sendListFlag = -1	  #标志位
		self.sendListLen = 0		#列表长度
		self.window = window
		self.SendFunc = SendFunc
		self.maxListLen = maxListLen
		window.cmdSendLine.deleteLater()
		self.cmdSendLine = AutoCompleteEdit(model=self._loadList())
		window.cmdSendLine = self.cmdSendLine
		window.horizontalLayout_26.addWidget(window.cmdSendLine)
		self.cmdSendLine.returnPressed.connect(self.sendCMD)
		# self.cmdSendLine.textEdited.connect(self.inputCallBack)
		self.cmdSendLine.keyUpSignal.connect(self.keyUpCallBack)
		self.cmdSendLine.keyDownSignal.connect(self.keyDownCallBack)

	def _loadList(self):
		if os.path.exists(cmdListFileName):
			with open(cmdListFileName, 'r') as f:
				return json.load(f).keys()
		else:
			with open(cmdListFileName, 'w') as f:
				json.dump(defaultCMDList, f, sort_keys=True,indent=2, separators=(',', ': '))
		return defaultCMDList.keys()
		

	def sendCMD(self):
		Msg = self.window.cmdSendLine.text()
		if self.SendFunc != None:
			if self.SendFunc(Msg) != True:
				return
		else:
			print('无发送函数')
			return
		self.window.cmdSendLabel.setText(Msg)
		if self.sendListLen > 0:
			if Msg == self.sendList[-1]:
				self.sendListFlag = self.sendListLen - 1
				return
		self.sendList.append(Msg)
		if self.sendListLen < self.maxListLen:
			self.sendListLen = len(self.sendList)
		else:
			self.sendList = self.sendList[1:]
		self.sendListFlag = self.sendListLen - 1
		# print(self.sendList)

	def inputCallBack(self, text = ''):
		print(text)

	def keyUpCallBack(self):
		self.sendListFlag -= 1
		if self.sendListFlag >= 0:
			self.cmdSendLine.setText(self.sendList[self.sendListFlag])
		else:
			self.sendListFlag = 0

	def keyDownCallBack(self):
		self.sendListFlag += 1
		if self.sendListFlag < self.sendListLen:
			self.cmdSendLine.setText(self.sendList[self.sendListFlag])
		else:
			self.sendListFlag = self.sendListLen - 1

	def setModel(self, model):
		self.cmdSendLine._setupCompleter(model)


class setCmdWindow(QWidget):
	closeSignal = pyqtSignal(list)
	def __init__(self):
		super().__init__()
		self.windowItem = Ui_Form()
		self.windowItem.setupUi(self)
		self.addList = {}
		self.deleteList = {}
		self.itemList = {}
		self.IsChange = False
		self.ItemFlag = 0
		self._loadList()
		self.windowItem.addButton.clicked.connect(self._addItem)
		self.windowItem.deleteButton.clicked.connect(self._deleteItem)
		self.windowItem.savePushButton.clicked.connect(self._saveList)
		self.windowItem.cmdListTabel.cellChanged.connect(self._edit)
		self.windowItem.cmdListTabel.cellPressed.connect(self._press)



	def _loadList(self):
		if os.path.exists(cmdListFileName):
			with open(cmdListFileName, 'r') as f:
				self.itemList = json.load(f)
		else:
			with open(cmdListFileName, 'w') as f:
				json.dump(defaultCMDList, f, sort_keys=True,indent=2, separators=(',', ': '))
			self.itemList = defaultCMDList
		for item in self.itemList.keys():
			itemText = QTableWidgetItem(str(item))
			itemDescribe = QTableWidgetItem(str(self.itemList[item]))
			print(self.ItemFlag, item)
			self.windowItem.cmdListTabel.insertRow(self.ItemFlag)
			self.windowItem.cmdListTabel.setItem(self.ItemFlag, 0, itemText)
			self.windowItem.cmdListTabel.setItem(self.ItemFlag, 1, itemDescribe)
			self.ItemFlag += 1
# 			self.window.dataTable.setItem(row, column, item)

	def _saveList(self):
		self.itemList.clear()
		for row in range(self.windowItem.cmdListTabel.rowCount()):
			itemText = self.windowItem.cmdListTabel.item(row, 0)
			itemDescribe = self.windowItem.cmdListTabel.item(row, 1)
			if itemText == None:
				itemText = ""
			else:
				itemText = itemText.text()
			if itemDescribe == None:
				itemDescribe = ""
			else:
				itemDescribe = itemDescribe.text()
			self.itemList[itemText] = itemDescribe
		with open(cmdListFileName, 'w') as f:
			json.dump(self.itemList, f, sort_keys=True,indent=2, separators=(',', ': '))
		self.IsChange = False

	def _addItem(self):
		self.windowItem.cmdListTabel.insertRow(self.ItemFlag)
		# if self.ItemFlag in self.deleteList.keys():
		# 	self.deleteList.pop(self.ItemFlag)
		# else:
		# 	self.addList[self.ItemFlag] = ""
		# 	print('add', self.ItemFlag)
		self.ItemFlag += 1
	
	def _deleteItem(self):
		ItemFlag_ = self.ItemFlag - 1
		self.IsChange = True
		if ItemFlag_ >= 0:
			self.windowItem.cmdListTabel.removeRow(ItemFlag_)
			# if (ItemFlag_) in self.addList.keys():
			# 	self.addList.pop(ItemFlag_)
			# else:
			# 	self.deleteList[ItemFlag_] = ""
			# print('delete', ItemFlag_)
			self.ItemFlag -= 1
		elif self.windowItem.cmdListTabel.rowCount() > 0:
			self.windowItem.cmdListTabel.removeRow(0)
	
	def _edit(self, row, column):
		self.IsChange = True
	
	def _press(self, row, column):
		self.ItemFlag = row + 1
	
	def closeEvent(self, event):
		if self.IsChange:
			if QMessageBox.question(self, "警告",
				"你想要在关闭之前保存对这个表格所做的改变吗？",
				QMessageBox.Yes,
				QMessageBox.No
			) == QMessageBox.Yes:
				self._saveList()
		self.closeSignal.emit(list(self.itemList.keys()))
		
			



if __name__ == "__main__":
	import sys
	from PyQt5 import QtWidgets
	app = QtWidgets.QApplication(sys.argv)
	cmd = setCmdWindow()
	cmd.show()
	sys.exit(app.exec_())

# def test():
# 	






