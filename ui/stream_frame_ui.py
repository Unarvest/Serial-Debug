# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stream_frame.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import icoPack_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(303, 160)
        font = QFont()
        font.setPointSize(13)
        Form.setFont(font)
        Form.setStyleSheet(u"QPalette{background:#FFFFFF;}*{outline:0px;color:#57595B;}\n"
"\n"
"QWidget[form=\"true\"],QLabel[frameShape=\"1\"]{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QWidget[form=\"bottom\"]{\n"
"background:#E4E4E4;\n"
"}\n"
"\n"
"QWidget[form=\"bottom\"] .QFrame{\n"
"border:1px solid #57595B;\n"
"}\n"
"\n"
"QWidget[form=\"bottom\"] QLabel,QWidget[form=\"title\"] QLabel{\n"
"border-radius:0px;\n"
"color:#57595B;\n"
"background:none;\n"
"border-style:none;\n"
"}\n"
"\n"
"QWidget[form=\"title\"],QWidget[nav=\"left\"],QWidget[nav=\"top\"] QAbstractButton{\n"
"border-style:none;\n"
"border-radius:0px;\n"
"padding:5px;\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QWidget[nav=\"top\"] QAbstractButton:hover,QWidget[nav=\"top\"] QAbstractButton:pressed,QWidget[nav=\"top\"] QAbstractButton:checked{\n"
"border-style:solid;\n"
"border-width:0px 0px 2px 0px;\n"
"padding:4px 4px 2px 4px;\n"
"border-color:#00BB9E;\n"
"backg"
                        "round:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QWidget[nav=\"left\"] QAbstractButton{\n"
"border-radius:0px;\n"
"color:#57595B;\n"
"background:none;\n"
"border-style:none;\n"
"}\n"
"\n"
"QWidget[nav=\"left\"] QAbstractButton:hover{\n"
"color:#FFFFFF;\n"
"background-color:#00BB9E;\n"
"}\n"
"\n"
"QWidget[nav=\"left\"] QAbstractButton:checked,QWidget[nav=\"left\"] QAbstractButton:pressed{\n"
"color:#57595B;\n"
"border-style:solid;\n"
"border-width:0px 0px 0px 2px;\n"
"padding:4px 4px 4px 2px;\n"
"border-color:#00BB9E;\n"
"background-color:#FFFFFF;\n"
"}\n"
"\n"
"QWidget[video=\"true\"] QLabel{\n"
"color:#57595B;\n"
"border:1px solid #B6B6B6;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QWidget[video=\"true\"] QLabel:focus{\n"
"border:1px solid #00BB9E;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QLineEdit,QTextEdit,QPlainTextEdit,QSpi"
                        "nBox,QDoubleSpinBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:3px;\n"
"padding:2px;\n"
"background:none;\n"
"selection-background-color:#00BB9E;\n"
"selection-color:#FFFFFF;\n"
"}\n"
"\n"
"QLineEdit:focus,QTextEdit:focus,QPlainTextEdit:focus,QSpinBox:focus,QDoubleSpinBox:focus,QComboBox:focus,QDateEdit:focus,QTimeEdit:focus,QDateTimeEdit:focus,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QSpinBox:hover,QDoubleSpinBox:hover,QComboBox:hover,QDateEdit:hover,QTimeEdit:hover,QDateTimeEdit:hover{\n"
"border:1px solid #B6B6B6;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"]{\n"
"lineedit-password-character:9679;\n"
"}\n"
"\n"
"/* .QFrame{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:3px;\n"
"} */\n"
"\n"
".QGroupBox{\n"
"border:1px solid #B6B6B6;\n"
"border-radius:5px;\n"
"margin-top:3ex;\n"
"}\n"
"\n"
".QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"position:relative;\n"
"left:10px;\n"
"}\n"
"\n"
".QPushButton,.QToolButton{\n"
"border-style:none;\n"
"border"
                        ":1px solid #B6B6B6;\n"
"color:#57595B;\n"
"padding:5px;\n"
"min-height:15px;\n"
"border-radius:5px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
".QPushButton:hover,.QToolButton:hover{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
".QPushButton:pressed,.QToolButton:pressed{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
".QToolButton::menu-indicator{\n"
"image:None;\n"
"}\n"
"\n"
"QToolButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{\n"
"border-radius:3px;\n"
"color:#57595B;\n"
"padding:3px;\n"
"margin:0px;\n"
"background:none;\n"
"border-style:none;\n"
"}\n"
"\n"
"QToolButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{\n"
"color:#FFFFFF;\n"
"margin:1px 1px 2px 1px;\n"
"background-color:rgba(51,127,209,230);\n"
"}\n"
"\n"
"QPushButton#btnMenu_Close:hover{\n"
""
                        "color:#FFFFFF;\n"
"margin:1px 1px 2px 1px;\n"
"background-color:rgba(238,0,0,128);\n"
"}\n"
"\n"
"QRadioButton::indicator{\n"
"width:15px;\n"
"height:15px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{\n"
"image:url(:/flat/flatwhite/radiobutton_unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked:disabled{\n"
"image:url(:/flat/flatwhite/radiobutton_unchecked_disable.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{\n"
"image:url(:/flat/flatwhite/radiobutton_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::checked:disabled{\n"
"image:url(:/flat/flatwhite/radiobutton_checked_disable.png);\n"
"}\n"
"\n"
"QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{\n"
"padding:0px -3px 0px 0px;\n"
"}\n"
"\n"
"QCheckBox::indicator,QGroupBox::indicator,QTreeWidget::indicator,QListWidget::indicator{\n"
"width:13px;\n"
"height:13px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked,QGroupBox::indicator:unchecked,QTreeWidget::indicator:unchecked,QListWidget::indicator:unchecked{\n"
"image"
                        ":url(:/flat/flatwhite/checkbox_unchecked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled,QGroupBox::indicator:unchecked:disabled,QTreeWidget::indicator:unchecked:disabled,QListWidget::indicator:disabled{\n"
"image:url(:/flat/flatwhite/checkbox_unchecked_disable.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked,QGroupBox::indicator:checked,QTreeWidget::indicator:checked,QListWidget::indicator:checked{\n"
"image:url(:/flat/flatwhite/checkbox_checked.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled,QGroupBox::indicator:checked:disabled,QTreeWidget::indicator:checked:disabled,QListWidget::indicator:checked:disabled{\n"
"image:url(:/flat/flatwhite/checkbox_checked_disable.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate,QGroupBox::indicator:indeterminate,QTreeWidget::indicator:indeterminate,QListWidget::indicator:indeterminate{\n"
"image:url(:/flat/flatwhite/checkbox_parcial.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:indeterminate:disabled,QGroupBox::indicator:indeterminate:disabled,QTr"
                        "eeWidget::indicator:indeterminate:disabled,QListWidget::indicator:indeterminate:disabled{\n"
"image:url(:/flat/flatwhite/checkbox_parcial_disable.png);\n"
"}\n"
"\n"
"QTimeEdit::up-button,QDateEdit::up-button,QDateTimeEdit::up-button,QDoubleSpinBox::up-button,QSpinBox::up-button{\n"
"image:url(:/flat/flatwhite/add_top.png);\n"
"width:10px;\n"
"height:10px;\n"
"padding:2px 5px 0px 0px;\n"
"}\n"
"\n"
"QTimeEdit::down-button,QDateEdit::down-button,QDateTimeEdit::down-button,QDoubleSpinBox::down-button,QSpinBox::down-button{\n"
"image:url(:/flat/flatwhite/add_bottom.png);\n"
"width:10px;\n"
"height:10px;\n"
"padding:0px 5px 2px 0px;\n"
"}\n"
"\n"
"QTimeEdit::up-button:pressed,QDateEdit::up-button:pressed,QDateTimeEdit::up-button:pressed,QDoubleSpinBox::up-button:pressed,QSpinBox::up-button:pressed{\n"
"top:-2px;\n"
"}\n"
"  \n"
"QTimeEdit::down-button:pressed,QDateEdit::down-button:pressed,QDateTimeEdit::down-button:pressed,QDoubleSpinBox::down-button:pressed,QSpinBox::down-button:pressed,QSpinBox::down-button:pre"
                        "ssed{\n"
"bottom:-2px;\n"
"}\n"
"\n"
"QComboBox::down-arrow,QDateEdit[calendarPopup=\"true\"]::down-arrow,QTimeEdit[calendarPopup=\"true\"]::down-arrow,QDateTimeEdit[calendarPopup=\"true\"]::down-arrow{\n"
"image:url(:/flat/flatwhite/add_bottom.png);\n"
"width:10px;\n"
"height:10px;\n"
"right:2px;\n"
"}\n"
"\n"
"QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{\n"
"subcontrol-origin:padding;\n"
"subcontrol-position:top right;\n"
"width:15px;\n"
"border-left-width:0px;\n"
"border-left-style:solid;\n"
"border-top-right-radius:3px;\n"
"border-bottom-right-radius:3px;\n"
"border-left-color:#B6B6B6;\n"
"}\n"
"\n"
"QComboBox::drop-down:on{\n"
"top:1px;\n"
"}\n"
"\n"
"QMenuBar::item{\n"
"color:#57595B;\n"
"background-color:#E4E4E4;\n"
"margin:0px;\n"
"padding:3px 10px;\n"
"}\n"
"\n"
"QMenu,QMenuBar,QMenu:disabled,QMenuBar:disabled{\n"
"color:#57595B;\n"
"background-color:#E4E4E4;\n"
"border:1px solid #B6B6B6;\n"
"margin:0px;\n"
"}\n"
"\n"
"QMenu::item{\n"
"padding:3px 20px;\n"
""
                        "}\n"
"\n"
"QMenu::indicator{\n"
"width:13px;\n"
"height:13px;\n"
"}\n"
"\n"
"QMenu::item:selected,QMenuBar::item:selected{\n"
"color:#57595B;\n"
"border:0px solid #B6B6B6;\n"
"background:#F6F6F6;\n"
"}\n"
"\n"
"QMenu::separator{\n"
"height:1px;\n"
"background:#B6B6B6;\n"
"}\n"
"\n"
"QProgressBar{\n"
"min-height:10px;\n"
"background:#E4E4E4;\n"
"border-radius:5px;\n"
"text-align:center;\n"
"border:1px solid #E4E4E4;\n"
"}\n"
"\n"
"QProgressBar:chunk{\n"
"border-radius:5px;\n"
"background-color:#B6B6B6;\n"
"}\n"
"\n"
"QSlider::groove:horizontal{\n"
"background:#E4E4E4;\n"
"height:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"background:#E4E4E4;\n"
"height:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal{\n"
"background:#B6B6B6;\n"
"height:8px;\n"
"border-radius:4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"width:13px;\n"
"margin-top:-3px;\n"
"margin-bottom:-3px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx"
                        ":0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #B6B6B6);\n"
"}\n"
"\n"
"QSlider::groove:vertical{\n"
"width:8px;\n"
"border-radius:4px;\n"
"background:#E4E4E4;\n"
"}\n"
"\n"
"QSlider::add-page:vertical{\n"
"width:8px;\n"
"border-radius:4px;\n"
"background:#E4E4E4;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical{\n"
"width:8px;\n"
"border-radius:4px;\n"
"background:#B6B6B6;\n"
"}\n"
"\n"
"QSlider::handle:vertical{\n"
"height:14px;\n"
"margin-left:-3px;\n"
"margin-right:-3px;\n"
"border-radius:6px;\n"
"background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #B6B6B6);\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"background:#E4E4E4;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-height:12px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"background:#B6B6B6;\n"
"min-width:50px;\n"
"border-radius:6px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"background:#00BB9E;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed{\n"
"background:#00BB9E;\n"
"}\n"
"\n"
"QScrollBar::add-"
                        "page:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"background:#E4E4E4;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-width:12px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background:#B6B6B6;\n"
"min-height:50px;\n"
"border-radius:6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background:#00BB9E;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed{\n"
"background:#00BB9E;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollArea{\n"
"border:0px;\n"
"}\n"
"\n"
"QTreeView,QListView,QTableView,QTabWidget::pane{\n"
"border:1px solid #"
                        "B6B6B6;\n"
"selection-background-color:#F6F6F6;\n"
"background-color: rgb(255, 255, 255);\n"
"selection-color:#57595B;\n"
"alternate-background-color:#F6F6F6;\n"
"gridline-color:#B6B6B6;\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-children{\n"
"margin:4px;\n"
"border-image:url(:/flat/flatwhite/branch_open.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children{\n"
"margin:4px;\n"
"border-image:url(:/flat/flatwhite/branch_close.png);\n"
"}\n"
"\n"
"QTreeView,QListView,QTableView,QSplitter::handle,QTreeView::branch{\n"
"background:#FFFFFF;\n"
"}\n"
"\n"
"QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QTableView::item:hover,QListView::item:hover,QTreeView::item:hover,QHeaderView{\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QTableView::item,QListView::item,QTreeView::item{\n"
""
                        "padding:1px;\n"
"margin:0px;\n"
"}\n"
"\n"
"QHeaderView::section,QTableCornerButton:section{\n"
"padding:3px;\n"
"margin:0px;\n"
"color:#57595B;\n"
"border:1px solid #B6B6B6;\n"
"border-left-width:0px;\n"
"border-right-width:1px;\n"
"border-top-width:0px;\n"
"border-bottom-width:1px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"border:1px solid #B6B6B6;\n"
"color:#57595B;\n"
"margin:0px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QTabBar::tab:selected,QTabBar::tab:hover{\n"
"border-style:solid;\n"
"border-color:#00BB9E;\n"
"background:#FFFFFF;\n"
"}\n"
"\n"
"QTabBar::tab:top,QTabBar::tab:bottom{\n"
"padding:3px 8px 3px 8px;\n"
"}\n"
"\n"
"QTabBar::tab:left,QTabBar::tab:right{\n"
"padding:8px 3px 8px 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected,QTabBar::tab:top:hover{\n"
"border-width:2px 0px 0px 0px;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected,QTabBar::tab:right:ho"
                        "ver{\n"
"border-width:0px 0px 0px 2px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected,QTabBar::tab:bottom:hover{\n"
"border-width:0px 0px 2px 0px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected,QTabBar::tab:left:hover{\n"
"border-width:0px 2px 0px 0px;\n"
"}\n"
"\n"
"QTabBar::tab:first:top:selected,QTabBar::tab:first:top:hover,QTabBar::tab:first:bottom:selected,QTabBar::tab:first:bottom:hover{\n"
"border-left-width:1px;\n"
"border-left-color:#B6B6B6;\n"
"}\n"
"\n"
"QTabBar::tab:first:left:selected,QTabBar::tab:first:left:hover,QTabBar::tab:first:right:selected,QTabBar::tab:first:right:hover{\n"
"border-top-width:1px;\n"
"border-top-color:#B6B6B6;\n"
"}\n"
"\n"
"QTabBar::tab:last:top:selected,QTabBar::tab:last:top:hover,QTabBar::tab:last:bottom:selected,QTabBar::tab:last:bottom:hover{\n"
"border-right-width:1px;\n"
"border-right-color:#B6B6B6;\n"
"}\n"
"\n"
"QTabBar::tab:last:left:selected,QTabBar::tab:last:left:hover,QTabBar::tab:last:right:selected,QTabBar::tab:last:right:hover{\n"
"border-bottom-width:1px;\n"
"borde"
                        "r-bottom-color:#B6B6B6;\n"
"}\n"
"\n"
"QStatusBar::item{\n"
"border:0px solid #E4E4E4;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QToolBox::tab,QGroupBox#gboxDevicePanel,QGroupBox#gboxDeviceTitle,QFrame#gboxDevicePanel,QFrame#gboxDeviceTitle{\n"
"padding:3px;\n"
"border-radius:5px;\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QToolTip{\n"
"border:0px solid #57595B;\n"
"padding:1px;\n"
"color:#57595B;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QToolBox::tab:selected{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F6F6F6,stop:1 #F6F6F6);\n"
"}\n"
"\n"
"QPrintPreviewDialog QToolButton{\n"
"border:0px solid #57595B;\n"
"border-radius:0px;\n"
"margin:0px;\n"
"padding:3px;\n"
"background:none;\n"
"}\n"
"\n"
"QColorDialog QPushButton,QFileDialog QPushButton{\n"
"min-width:80px;\n"
"}\n"
"\n"
"QToolButton#qt_calendar_prevmonth{\n"
"icon-size:0px;\n"
"min"
                        "-width:20px;\n"
"image:url(:/flat/flatwhite/calendar_prevmonth.png);\n"
"}\n"
"\n"
"QToolButton#qt_calendar_nextmonth{\n"
"icon-size:0px;\n"
"min-width:20px;\n"
"image:url(:/flat/flatwhite/calendar_nextmonth.png);\n"
"}\n"
"\n"
"QToolButton#qt_calendar_prevmonth,QToolButton#qt_calendar_nextmonth,QToolButton#qt_calendar_monthbutton,QToolButton#qt_calendar_yearbutton{\n"
"border:0px solid #57595B;\n"
"border-radius:3px;\n"
"margin:3px 3px 3px 3px;\n"
"padding:3px;\n"
"background:none;\n"
"}\n"
"\n"
"QToolButton#qt_calendar_prevmonth:hover,QToolButton#qt_calendar_nextmonth:hover,QToolButton#qt_calendar_monthbutton:hover,QToolButton#qt_calendar_yearbutton:hover,QToolButton#qt_calendar_prevmonth:pressed,QToolButton#qt_calendar_nextmonth:pressed,QToolButton#qt_calendar_monthbutton:pressed,QToolButton#qt_calendar_yearbutton:pressed{\n"
"border:1px solid #B6B6B6;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox#qt_calendar_yearedit{\n"
"margin:2px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::menu-indicator{\n"
"image:None;\n"
""
                        "}\n"
"\n"
"QCalendarWidget QTableView{\n"
"border-width:0px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar{\n"
"border:1px solid #B6B6B6;\n"
"border-width:1px 1px 0px 1px;\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #E4E4E4,stop:1 #E4E4E4);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item{\n"
"min-height:20px;\n"
"min-width:10px;\n"
"}\n"
"\n"
"QTableView[model=\"true\"]::item{\n"
"padding:0px;\n"
"margin:0px;\n"
"}\n"
"\n"
"QTableView QLineEdit,QTableView QComboBox,QTableView QSpinBox,QTableView QDoubleSpinBox,QTableView QDateEdit,QTableView QTimeEdit,QTableView QDateTimeEdit{\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QTableView QLineEdit:focus,QTableView QComboBox:focus,QTableView QSpinBox:focus,QTableView QDoubleSpinBox:focus,QTableView QDateEdit:focus,QTableView QTimeEdit:focus,QTableView QDateTimeEdit:focus{\n"
"border-width:0px;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QDoubleSpinBox,QComboBox,QDateEdit"
                        ",QTimeEdit,QDateTimeEdit{\n"
"background:#FFFFFF;\n"
"}\n"
"\n"
"QTabWidget::pane:top{top:-1px;}\n"
"QTabWidget::pane:bottom{bottom:-1px;}\n"
"QTabWidget::pane:left{right:-1px;}\n"
"QTabWidget::pane:right{left:-1px;}\n"
"\n"
"*:disabled{\n"
"background:#FFFFFF;\n"
"border-color:#E4E4E4;\n"
"color:#B6B6B6;\n"
"}\n"
"\n"
"/*TextColor:#57595B*/\n"
"/*PanelColor:#FFFFFF*/\n"
"/*BorderColor:#B6B6B6*/\n"
"/*NormalColorStart:#E4E4E4*/\n"
"/*NormalColorEnd:#E4E4E4*/\n"
"/*DarkColorStart:#F6F6F6*/\n"
"/*DarkColorEnd:#F6F6F6*/\n"
"/*HighColor:#00BB9E*/")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        font2 = QFont()
        font2.setPointSize(12)
        self.checkBox.setFont(font2)

        self.gridLayout.addWidget(self.checkBox, 0, 2, 1, 1)

        self.checkBox_2 = QCheckBox(Form)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font2)

        self.gridLayout.addWidget(self.checkBox_2, 1, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(13, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.checkBox_3 = QCheckBox(Form)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font2)

        self.gridLayout.addWidget(self.checkBox_3, 1, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(13, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font1)

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMaximumSize(QSize(80, 16777215))
        self.lineEdit.setFont(font2)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.checkBox_4 = QCheckBox(self.frame)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font)
        self.checkBox_4.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBox_4)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u786c\u4ef6\u6d41", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"XON/XOFF", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"RTS/CTS", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8f6f\u4ef6\u6d41", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"DSR/DTR", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5206\u5e27\u6807\u5fd7", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"\\n", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"\u5206\u5e27\u6362\u884c", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"  \u786e\u5b9a  ", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"  \u53d6\u6d88  ", None))
    # retranslateUi

