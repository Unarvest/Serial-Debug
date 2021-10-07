# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cmdSetWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import cmdSetWindow_rc
import icoPack_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(444, 557)
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
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(13)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.default = QWidget()
        self.default.setObjectName(u"default")
        self.verticalLayout_2 = QVBoxLayout(self.default)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.frame_2 = QFrame(self.default)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.deletePage = QPushButton(self.frame_2)
        self.deletePage.setObjectName(u"deletePage")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(13)
        self.deletePage.setFont(font1)

        self.horizontalLayout_2.addWidget(self.deletePage)

        self.renamePage = QPushButton(self.frame_2)
        self.renamePage.setObjectName(u"renamePage")
        self.renamePage.setFont(font1)

        self.horizontalLayout_2.addWidget(self.renamePage)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.cmdListTabel = QTableWidget(self.default)
        if (self.cmdListTabel.columnCount() < 2):
            self.cmdListTabel.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.cmdListTabel.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.cmdListTabel.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.cmdListTabel.setObjectName(u"cmdListTabel")
        self.cmdListTabel.setFont(font1)
        self.cmdListTabel.setTabKeyNavigation(True)
        self.cmdListTabel.horizontalHeader().setStretchLastSection(True)
        self.cmdListTabel.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.cmdListTabel)

        self.frame = QFrame(self.default)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.addButton = QPushButton(self.frame)
        self.addButton.setObjectName(u"addButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(14)
        self.addButton.setFont(font2)
        self.addButton.setStyleSheet(u"image: url(:/Main/ico/\u6dfb\u52a0.ico);")
        icon = QIcon()
        icon.addFile(u":/Main/ico/\u6dfb\u52a0.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon)
        self.addButton.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.addButton)

        self.deleteButton = QPushButton(self.frame)
        self.deleteButton.setObjectName(u"deleteButton")
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/Main/ico/\u51cf.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.deleteButton)

        self.horizontalSpacer = QSpacerItem(118, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.enableCheckBox = QCheckBox(self.frame)
        self.enableCheckBox.setObjectName(u"enableCheckBox")
        self.enableCheckBox.setFont(font1)

        self.horizontalLayout.addWidget(self.enableCheckBox)

        self.savePushButton = QPushButton(self.frame)
        self.savePushButton.setObjectName(u"savePushButton")
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(12)
        self.savePushButton.setFont(font3)
        icon2 = QIcon()
        icon2.addFile(u":/Mainico/ico/20200510-221417.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.savePushButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.savePushButton)


        self.verticalLayout_2.addWidget(self.frame)

        self.tabWidget.addTab(self.default, "")
        self.new = QWidget()
        self.new.setObjectName(u"new")
        self.verticalLayout_4 = QVBoxLayout(self.new)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget.addTab(self.new, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7f16\u8f91\u6307\u4ee4\u96c6", None))
        self.deletePage.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u9875", None))
        self.renamePage.setText(QCoreApplication.translate("Form", u"\u91cd\u547d\u540d", None))
        ___qtablewidgetitem = self.cmdListTabel.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u6307\u4ee4\u5757", None));
        ___qtablewidgetitem1 = self.cmdListTabel.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u63cf\u8ff0", None));
        self.addButton.setText("")
        self.deleteButton.setText("")
        self.enableCheckBox.setText(QCoreApplication.translate("Form", u"\u542f\u7528", None))
        self.savePushButton.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.default), QCoreApplication.translate("Form", u"\u9ed8\u8ba4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.new), QCoreApplication.translate("Form", u"+", None))
    # retranslateUi

