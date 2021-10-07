

import cmdSetWindow_rc
import icoPack_rc
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from src.File_loader import getAccess
import os, json


defaultCMDList = {
  "FinSH": {
	"CMD": {
		"command": "\u547d\u4ee4",
		"dummy": "finsh\u7684\u865a\u62df\u53d8\u91cf",
		"error": "\u9519\u8bef",
		"hello": "\u6253\u5370hello world",
		"left": "",
		"list": "list all symbol in system",
		"list_device": "\u5217\u51fa\u7cfb\u7edf\u4e2d\u7684\u8bbe\u5907",
		"list_event": "\u5217\u51fa\u7cfb\u7edf\u4e2d\u7684event",
		"list_magqueue": "\u5217\u51fa\u7cfb\u7edf\u4e2d\u7684\u6d88\u606f\u961f\u5217",
		"list_mailbox": "\u5217\u51fa\u7cfb\u7edf\u4e2d\u7684mailbox",
		"list_mem": "\u5217\u51fa\u5185\u5b58\u4f7f\u7528\u4fe1\u606f",
		"list_mempool": "\u5217\u51fa\u7cfb\u7edf\u4e2d\u7684memory pool",
		"list_mutex": "\u5217\u51fa\u7cfb\u7edf\u4e2d\u7684mutex",
		"list_sem": "\u5217\u51fa\u7cfb\u7edf\u4e2d\u7684semaphone",
		"list_thread": "\u5217\u51fa\u7ebf\u7a0b",
		"list_timer": "\u5217\u51fa\u7cfb\u7edf\u4e2d\u7684\u5b9a\u65f6\u5668",
		"max": "\u6700\u5927",
		"min": "\u6700\u5c0f",
		"pri": "\u4f18\u5148\u7ea7",
		"sp": "\u7ebf\u7a0b\u5f53\u524d\u7684\u6808\u4f4d\u7f6e",
		"status": "\u72b6\u6001",
		"thread": "\u7ebf\u7a0b\u7684\u540d\u79f0",
		"tick": "",
		"used": "",
		"version": "\u663e\u793aRT-Thread\u7248\u672c\u4fe1\u606f"
	  },
	"Enable": False
  },
  "HC_05": {
	"CMD": {
		"AT": "\u6d4b\u8bd5\u6307\u4ee4",
		"AT+": "",
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
	  },
	"Enable": True
  },
  "Linux": {
	"CMD": {
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
	  },
	"Enable": True
  },
  "\u9ed8\u8ba4": {
	"CMD": {
	  "": "",
	  "\"\"": "",
	  "''": "",
	  "()": "",
	  "+1": "",
	  ", ": "",
	  "-1": "",
	  "3.3V": "",
	  "5V": "",
	  "<>": "",
	  "ADDR": "",
	  "AT": "",
	  "AT+": "",
	  "CMD": "",
	  "GND": "",
	  "Hello world": "",
	  "ID": "",
	  "IO": "",
	  "Max": "",
	  "Min": "",
	  "NAME": "",
	  "NULL": "",
	  "PACK": "",
	  "PI": "",
	  "VCC": "",
	  "[]": "",
	  "accept": "",
	  "alt": "",
	  "back": "",
	  "begin": "",
	  "break": "",
	  "bug": "",
	  "cancel": "",
	  "catch": "",
	  "client": "",
	  "close": "",
	  "connect": "",
	  "control": "",
	  "data": "",
	  "date": "",
	  "delete": "",
	  "do": "",
	  "down": "",
	  "download": "",
	  "else": "",
	  "en": "",
	  "end": "",
	  "enter": "",
	  "exit": "",
	  "false": "",
	  "find": "",
	  "for": "",
	  "go": "",
	  "hello": "",
	  "high": "",
	  "home": "",
	  "id": "",
	  "if": "",
	  "in": "",
	  "input": "",
	  "insert": "",
	  "io": "",
	  "it": "",
	  "kill": "",
	  "left": "",
	  "load": "",
	  "low": "",
	  "max": "",
	  "min": "",
	  "mode": "",
	  "name": "",
	  "no": "",
	  "null": "",
	  "num": "",
	  "open": "",
	  "out": "",
	  "output": "",
	  "pack": "",
	  "packet": "",
	  "page": "",
	  "port": "",
	  "quit": "",
	  "re": "",
	  "read": "",
	  "reset": "",
	  "right": "",
	  "run": "",
	  "server": "",
	  "servo": "",
	  "setup": "",
	  "shift": "",
	  "shut": "",
	  "shutdown": "",
	  "so": "",
	  "start": "",
	  "stop": "",
	  "sys": "",
	  "tab": "",
	  "test": "",
	  "to": "",
	  "true": "",
	  "try": "",
	  "un": "",
	  "up": "",
	  "use": "",
	  "value": "",
	  "var": "",
	  "vcc": "",
	  "view": "",
	  "write": "",
	  "yes": "",
	  "{}": ""
	},
	"Enable": True
  }
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
	keyUpSignal = Signal()
	keyDownSignal = Signal()
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
	def _setupCompleter(self, model = []):
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
		window.ui.cmdSendLine.deleteLater()
		self.cmdSendLine = AutoCompleteEdit(model=self._loadList())
		window.ui.cmdSendLine = self.cmdSendLine
		window.ui.horizontalLayout_26.addWidget(window.ui.cmdSendLine)
		self.cmdSendLine.returnPressed.connect(self.sendCMD)
		# self.cmdSendLine.textEdited.connect(self.inputCallBack)
		self.cmdSendLine.keyUpSignal.connect(self.keyUpCallBack)
		self.cmdSendLine.keyDownSignal.connect(self.keyDownCallBack)
		font = QFont()
		font.setFamilies([u"Cascadia Code"])
		font.setPointSize(12)
		font.setBold(False)
		font.setItalic(False)
		font.setUnderline(False)
		font.setStrikeOut(False)
		self.cmdSendLine.setFont(font)
		

	def _setModel(self):
		self.cmdSendLine._setupCompleter(model=self._loadList())

	def _loadList(self):
		CMDList = []
		dataDict = {}
		try:
			with open(cmdListFileName, 'r') as f:
				dataDict = json.load(f)
			for item in dataDict.keys():
				if dataDict[item]['Enable']:
					CMDList += dataDict[item]['CMD'].keys()
		except Exception as e:
			print(cmdListFileName + "文件不存在", e)
			getAccess()
			with open(cmdListFileName, 'w') as f:
				json.dump(defaultCMDList, f, sort_keys=True,indent=2, separators=(',', ': '))
			dataDict = defaultCMDList
			for item in dataDict.keys():
				if dataDict[item]['Enable']:
					CMDList += dataDict[item]['CMD'].keys()
		finally:
			return CMDList
		
		

	def sendCMD(self):
		Msg = self.window.ui.cmdSendLine.text()
		if self.SendFunc != None:
			if self.SendFunc(Msg) != True:
				return
		else:
			print('无发送函数')
			return
		self.window.ui.cmdSendLabel.setText(Msg)
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


class setCmdWindow(QWidget):
	closeSignal = Signal()
	def __init__(self):
		super().__init__()
		self.tabList = {}
		self.defaultList = ['默认', 'HC_05', 'FinSH', 'Linux']

		_translate = QCoreApplication.translate

		self.setWindowTitle(_translate("Form", "编辑指令集"))
		self.setObjectName("Form")
		self.resize(444, 557)
		self.verticalLayout = QVBoxLayout(self)
		self.verticalLayout.setObjectName("verticalLayout")
		self.tabWidget = QTabWidget(self)
		font = QFont()
		font.setFamilies("Microsoft YaHei UI")
		font.setPointSize(13)
		self.tabWidget.setFont(font)
		self.tabWidget.setObjectName("tabWidget")
		self.verticalLayout.addWidget(self.tabWidget)
		self._loadData()
		self.new = QWidget()
		self.new.setObjectName("new")
		self.tabWidget.addTab(self.new, "+")
		self.tabWidget.setCurrentIndex(0)

		self.tabWidget.currentChanged.connect(self._insertNewTab)
		self.tabWidget.setContextMenuPolicy(Qt.CustomContextMenu)

	class _newTab(QWidget):
		def __init__(self, name=""):
			super().__init__()
			if name != "":
				self.setObjectName(name)
			else:
				name = '默认'
			self.name = name
			self._setupItem()
			self.addList = {}
			self.deleteList = {}
			self.itemList = {}
			self.IsChange = False
			self.ItemFlag = 0
			self.enable = True
			self._loadList()
			self.addButton.clicked.connect(self._addItem)
			self.deleteButton.clicked.connect(self._deleteItem)
			self.savePushButton.clicked.connect(self._saveList)
			self.cmdListTabel.cellChanged.connect(self._edit)
			self.cmdListTabel.cellPressed.connect(self._press)
			self.enableCheckBox.clicked.connect(self._setEnable)
			self.enableCheckBox.setChecked(self.enable)

		def _setupItem(self):
			_translate = QCoreApplication.translate
			self.verticalLayout_2 = QVBoxLayout(self)
			self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
			self.verticalLayout_2.setObjectName("verticalLayout_2")
			self.cmdListTabel = QTableWidget(self)
			font = QFont()
			font.setFamily("Microsoft YaHei UI")
			font.setPointSize(12)
			self.cmdListTabel.setFont(font)
			self.cmdListTabel.setTabKeyNavigation(True)
			self.cmdListTabel.setObjectName("cmdListTabel")
			self.cmdListTabel.setColumnCount(2)
			self.cmdListTabel.setRowCount(0)
			item = QTableWidgetItem()
			self.cmdListTabel.setHorizontalHeaderItem(0, item)
			item = QTableWidgetItem()
			self.cmdListTabel.setHorizontalHeaderItem(1, item)
			self.cmdListTabel.horizontalHeader().setStretchLastSection(True)
			self.cmdListTabel.verticalHeader().setVisible(False)
			item = self.cmdListTabel.horizontalHeaderItem(0)
			item.setText(_translate("Form", "指令块"))
			item = self.cmdListTabel.horizontalHeaderItem(1)
			item.setText(_translate("Form", "描述"))
			self.frame = QFrame(self)
			self.frame.setFrameShape(QFrame.StyledPanel)
			self.frame.setFrameShadow(QFrame.Raised)
			self.frame.setObjectName("frame")
			self.horizontalLayout = QHBoxLayout(self.frame)
			self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
			self.horizontalLayout.setObjectName("horizontalLayout")
			self.addButton = QPushButton(self.frame)
			sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
			self.addButton.setSizePolicy(sizePolicy)
			font = QFont()
			font.setFamily("Microsoft YaHei UI")
			font.setPointSize(14)
			self.addButton.setFont(font)
			self.addButton.setStyleSheet("image: url(:/Main/ico/添加.ico);")
			self.addButton.setText("")
			icon = QIcon()
			icon.addPixmap(QPixmap(":/Main/ico/添加.ico"), QIcon.Normal, QIcon.Off)
			self.addButton.setIcon(icon)
			self.addButton.setIconSize(QSize(22, 22))
			self.addButton.setObjectName("addButton")
			self.horizontalLayout.addWidget(self.addButton)
			self.deleteButton = QPushButton(self.frame)
			sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
			sizePolicy.setHorizontalStretch(0)
			sizePolicy.setVerticalStretch(0)
			sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
			self.deleteButton.setSizePolicy(sizePolicy)
			font = QFont()
			font.setFamily("Microsoft YaHei UI")
			font.setPointSize(14)
			self.deleteButton.setFont(font)
			self.deleteButton.setText("")
			icon1 = QIcon()
			icon1.addPixmap(QPixmap(":/Main/ico/减.ico"), QIcon.Normal, QIcon.Off)
			self.deleteButton.setIcon(icon1)
			self.deleteButton.setIconSize(QSize(22, 22))
			self.deleteButton.setObjectName("deleteButton")
			self.horizontalLayout.addWidget(self.deleteButton)
			spacerItem = QSpacerItem(118, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)
			self.horizontalLayout.addItem(spacerItem)

			self.enableCheckBox = QCheckBox(self.frame)
			self.enableCheckBox.setObjectName("enableCheckBox")
			self.horizontalLayout.addWidget(self.enableCheckBox)
			self.enableCheckBox.setText('启用')

			self.savePushButton = QPushButton(self.frame)
			font = QFont()
			font.setFamily("Microsoft YaHei UI")
			font.setPointSize(12)
			self.savePushButton.setFont(font)
			icon2 = QIcon()
			icon2.addPixmap(QPixmap(":/Mainico/ico/20200510-221417.ico"), QIcon.Normal, QIcon.Off)
			self.savePushButton.setIcon(icon2)
			self.savePushButton.setObjectName("savePushButton")
			self.horizontalLayout.addWidget(self.savePushButton)
			self.savePushButton.setText('保存')
		
		def _setupBottom(self):
			self.verticalLayout_2.addWidget(self.cmdListTabel)
			self.verticalLayout_2.addWidget(self.frame)

		def _setupTopButton(self):
			self.frame_2 = QFrame(self)
			self.frame_2.setFrameShape(QFrame.StyledPanel)
			self.frame_2.setFrameShadow(QFrame.Raised)
			self.frame_2.setObjectName("frame_2")
			self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
			self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
			self.horizontalLayout_2.setObjectName("horizontalLayout_2")
			spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
			self.horizontalLayout_2.addItem(spacerItem)
			self.deletePage = QPushButton(self.frame_2)
			self.deletePage.setObjectName("deletePage")
			self.horizontalLayout_2.addWidget(self.deletePage)
			self.renamePage = QPushButton(self.frame_2)
			self.renamePage.setObjectName("renamePage")
			self.deletePage.setText("删除页")
			self.renamePage.setText("重命名")
			self.horizontalLayout_2.addWidget(self.renamePage)
			self.verticalLayout_2.addWidget(self.frame_2)

		def _setEnable(self, value):
			self.enable = value
			self.IsChange = True

		def _loadList(self):
			CMDDict = {}
			dataDict = {}
			try:
				with open(cmdListFileName, 'r') as f:
					dataDict = json.load(f)
					
			except:
				getAccess()
				with open(cmdListFileName, 'w') as f:
					json.dump(defaultCMDList, f, sort_keys=True,indent=2, separators=(',', ': '))
				dataDict = defaultCMDList

			finally:
				if self.name in dataDict.keys():
					CMDDict = dataDict[self.name]
					self.itemList = CMDDict['CMD']
					self.enable = CMDDict['Enable']

				for item in self.itemList.keys():
					itemText = QTableWidgetItem(str(item))
					itemDescribe = QTableWidgetItem(str(self.itemList[item]))
					self.cmdListTabel.insertRow(self.ItemFlag)
					self.cmdListTabel.setItem(self.ItemFlag, 0, itemText)
					self.cmdListTabel.setItem(self.ItemFlag, 1, itemDescribe)
					self.ItemFlag += 1
					
		def _saveList(self):
			self.itemList.clear()
			for row in range(self.cmdListTabel.rowCount()):
				itemText = self.cmdListTabel.item(row, 0)
				itemDescribe = self.cmdListTabel.item(row, 1)
				if itemText == None:
					itemText = ""
				else:
					itemText = itemText.text()
				if itemDescribe == None:
					itemDescribe = ""
				else:
					itemDescribe = itemDescribe.text()
				self.itemList[itemText] = itemDescribe
			with open(cmdListFileName, 'r') as f:
				dataDict = json.load(f)
			if self.name in dataDict.keys():
				CMDDict = dataDict[self.name]
			else:
				CMDDict = {}
			CMDDict["CMD"] = self.itemList
			CMDDict["Enable"] = self.enable
			dataDict[self.name] = CMDDict
			with open(cmdListFileName, 'w') as f:
				json.dump(dataDict, f, sort_keys=True,indent=2, separators=(',', ': '))
			self.IsChange = False
			self.savePushButton.setText('保存成功')

		def _addItem(self):
			self.cmdListTabel.insertRow(self.ItemFlag)
			# if self.ItemFlag in self.deleteList.keys():
			# 	self.deleteList.pop(self.ItemFlag)
			# else:
			# 	self.addList[self.ItemFlag] = ""
			# 	print('add', self.ItemFlag)
			self.ItemFlag += 1
		
		def _deleteItem(self):
			ItemFlag_ = self.ItemFlag - 1
			self.IsChange = True
			self.savePushButton.setText('保存')
			if ItemFlag_ >= 0:
				self.cmdListTabel.removeRow(ItemFlag_)
				# if (ItemFlag_) in self.addList.keys():
				# 	self.addList.pop(ItemFlag_)
				# else:
				# 	self.deleteList[ItemFlag_] = ""
				# print('delete', ItemFlag_)
				self.ItemFlag -= 1
			elif self.cmdListTabel.rowCount() > 0:
				self.cmdListTabel.removeRow(0)
		
		def _edit(self, row, column):
			self.IsChange = True
			self.savePushButton.setText('保存')
		
		def _press(self, row, column):
			self.ItemFlag = row + 1
	
	def _addDefaultTab(self, name):
		newTab = self._newTab(name=name)
		if name in self.defaultList:
			newTab._setupBottom()
		else:
			newTab._setupTopButton()
			newTab._setupBottom()
			newTab.deletePage.clicked.connect(lambda: self._removeTab(self.tabWidget.currentIndex()))
			newTab.renamePage.clicked.connect(lambda: self._renameTab(self.tabWidget.currentIndex()))
		self.tabList[name] = newTab
		self.tabWidget.addTab(newTab, name)

	def _loadData(self):
		try:
			with open(cmdListFileName, 'r') as f:
				dataDict = json.load(f)
			for name in self.defaultList:
				self._addDefaultTab(name)
				dataDict.pop(name)
		except:
			with open(cmdListFileName, 'w') as f:
				json.dump(defaultCMDList, f, sort_keys=True, indent=2, separators=(',', ': '))
				dataDict = defaultCMDList
			for name in self.defaultList:
				self._addDefaultTab(name)
				dataDict.pop(name)
		finally:
			for name in dataDict.keys():
				self._addDefaultTab(name)
			

		# for name in self.defaultList:
		# 	self._addDefaultTab(name)	

	def _removeTab(self, tabNum):
		currentTabText = self.tabWidget.tabText(tabNum)
		if currentTabText in self.defaultList:
			QMessageBox.warning(self, '警告', currentTabText + '页不可删除')
		else:
			if QMessageBox.question(self, '警告', '是否删除{}?'.format(currentTabText),
			 QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
				self.tabList[self.defaultList[0]].IsChange = True
				self.tabWidget.setCurrentIndex(tabNum - 1)
				self.tabList.pop(currentTabText)
				with open(cmdListFileName, 'r') as f:
					dataDict = json.load(f)
				if currentTabText in dataDict.keys():
					dataDict.pop(currentTabText)
				with open(cmdListFileName, 'w') as f:
					json.dump(dataDict, f, sort_keys=True, indent=2, separators=(',', ': '))
				self.tabWidget.removeTab(tabNum)

	def _renameTab(self, tabNum):
		currentTabText = self.tabWidget.tabText(tabNum)
		if currentTabText in self.defaultList:
			QMessageBox.warning(self, '警告', currentTabText + '页不可重命名')
			return 
		name, ok = QInputDialog.getText(self, "命名标签", "内容与页标签互相绑定", QLineEdit.Normal, "页{}".format(tabNum))
		if ok:
			if name in self.tabList.keys():
				QMessageBox.warning(self, '警告', '存在同名页')
			else:
				self.tabList[currentTabText].IsChange = True
				self.tabList[name] = self.tabList.pop(currentTabText)
				self.tabWidget.setTabText(tabNum, name)

	def _addNewTab(self, indexOfNewTab):
		name, ok = QInputDialog.getText(self, "命名标签", "内容与页标签互相绑定", QLineEdit.Normal, "页{}".format(indexOfNewTab - len(defaultCMDList) + 1))
		if ok:
			if name in self.tabList.keys():
				QMessageBox.warning(self, '警告', '存在同名页')
			else:
				newTab = self._newTab(name)
				newTab._setupTopButton()
				newTab._setupBottom()
				newTab.deletePage.clicked.connect(lambda: self._removeTab(self.tabWidget.currentIndex()))
				newTab.renamePage.clicked.connect(lambda: self._renameTab(self.tabWidget.currentIndex()))
				self.tabList[name] = newTab
				self.tabWidget.insertTab(indexOfNewTab, newTab, name)
			indexOfNewTab += 1
		self.tabWidget.setCurrentIndex(indexOfNewTab-1)

	def _insertNewTab(self, num):
		indexOfNewTab =  self.tabWidget.indexOf(self.new)
		if num == indexOfNewTab:	
			self._addNewTab(num)
	
	def _saveAll(self):
		for tab in self.tabList:
			if self.tabList[tab].IsChange:
				self.tabList[tab]._saveList()

	def closeEvent(self, event):
		for tab in self.tabList:
			if self.tabList[tab].IsChange:
				if QMessageBox.question(self, "警告",
					"你想要在关闭之前保存对这个表格所做的改变吗？",
					QMessageBox.Yes,
					QMessageBox.No
				) == QMessageBox.Yes:
					self._saveAll()
					break
		self.closeSignal.emit()

# if __name__ == "__main__":
# 	import sys
# 	from PySide6.QtWidgets import QApplication
# 	app = QApplication(sys.argv)
# 	cmd = setCmdWindow()
# 	cmd.show()
# 	sys.exit(app.exec_())







