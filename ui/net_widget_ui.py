# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'net_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)
import icoPack_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(288, 573)
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
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_10 = QFrame(self.widget)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_16 = QSpacerItem(8, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_16, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.bpsLabel_4 = QLabel(self.frame_10)
        self.bpsLabel_4.setObjectName(u"bpsLabel_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bpsLabel_4.sizePolicy().hasHeightForWidth())
        self.bpsLabel_4.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.bpsLabel_4.setFont(font)

        self.gridLayout_4.addWidget(self.bpsLabel_4, 1, 0, 1, 1)

        self.bpsLabel_3 = QLabel(self.frame_10)
        self.bpsLabel_3.setObjectName(u"bpsLabel_3")
        sizePolicy.setHeightForWidth(self.bpsLabel_3.sizePolicy().hasHeightForWidth())
        self.bpsLabel_3.setSizePolicy(sizePolicy)
        self.bpsLabel_3.setFont(font)

        self.gridLayout_4.addWidget(self.bpsLabel_3, 0, 0, 1, 1)

        self.byteSizeLabel_2 = QLabel(self.frame_10)
        self.byteSizeLabel_2.setObjectName(u"byteSizeLabel_2")
        sizePolicy.setHeightForWidth(self.byteSizeLabel_2.sizePolicy().hasHeightForWidth())
        self.byteSizeLabel_2.setSizePolicy(sizePolicy)
        self.byteSizeLabel_2.setFont(font)

        self.gridLayout_4.addWidget(self.byteSizeLabel_2, 2, 0, 1, 1)

        self.connectButton = QPushButton(self.frame_10)
        self.connectButton.setObjectName(u"connectButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy1)
        self.connectButton.setMinimumSize(QSize(0, 27))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.connectButton.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/Mainico/ico/\u8fde\u63a5.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.connectButton.setIcon(icon)
        self.connectButton.setIconSize(QSize(30, 30))
        self.connectButton.setCheckable(False)
        self.connectButton.setFlat(False)

        self.gridLayout_4.addWidget(self.connectButton, 0, 4, 3, 1)

        self.modeComboBox = QComboBox(self.frame_10)
        self.modeComboBox.addItem("")
        self.modeComboBox.addItem("")
        self.modeComboBox.setObjectName(u"modeComboBox")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.modeComboBox.setFont(font2)

        self.gridLayout_4.addWidget(self.modeComboBox, 0, 2, 1, 1)

        self.IPEdit = QLineEdit(self.frame_10)
        self.IPEdit.setObjectName(u"IPEdit")
        self.IPEdit.setFont(font2)

        self.gridLayout_4.addWidget(self.IPEdit, 1, 2, 1, 1)

        self.PortEdit = QSpinBox(self.frame_10)
        self.PortEdit.setObjectName(u"PortEdit")
        self.PortEdit.setFont(font2)
        self.PortEdit.setMaximum(65535)
        self.PortEdit.setValue(6000)

        self.gridLayout_4.addWidget(self.PortEdit, 2, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_10)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.frame_9 = QFrame(self.widget)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy2)
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_29 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(2, 2, 2, 3)
        self.sendHexCheckBox = QCheckBox(self.frame_9)
        self.sendHexCheckBox.setObjectName(u"sendHexCheckBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sendHexCheckBox.sizePolicy().hasHeightForWidth())
        self.sendHexCheckBox.setSizePolicy(sizePolicy3)
        self.sendHexCheckBox.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.sendHexCheckBox.setFont(font3)
        icon1 = QIcon()
        icon1.addFile(u":/Mainico/ico/20200510-234010.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.sendHexCheckBox.setIcon(icon1)
        self.sendHexCheckBox.setIconSize(QSize(18, 18))

        self.horizontalLayout_29.addWidget(self.sendHexCheckBox)

        self.enterSendCheckBox = QCheckBox(self.frame_9)
        self.enterSendCheckBox.setObjectName(u"enterSendCheckBox")
        sizePolicy3.setHeightForWidth(self.enterSendCheckBox.sizePolicy().hasHeightForWidth())
        self.enterSendCheckBox.setSizePolicy(sizePolicy3)
        self.enterSendCheckBox.setMinimumSize(QSize(0, 0))
        self.enterSendCheckBox.setFont(font3)
        icon2 = QIcon()
        icon2.addFile(u":/Mainico/ico/20200510-234445.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.enterSendCheckBox.setIcon(icon2)
        self.enterSendCheckBox.setIconSize(QSize(18, 18))
        self.enterSendCheckBox.setChecked(True)

        self.horizontalLayout_29.addWidget(self.enterSendCheckBox)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(2, 2, 2, 3)
        self.connectRraw = QCheckBox(self.widget)
        self.connectRraw.setObjectName(u"connectRraw")
        self.connectRraw.setFont(font3)
        icon3 = QIcon()
        icon3.addFile(u":/Mainico/ico/20200511-103831.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.connectRraw.setIcon(icon3)
        self.connectRraw.setIconSize(QSize(18, 18))
        self.connectRraw.setChecked(False)

        self.horizontalLayout_13.addWidget(self.connectRraw)

        self.showSendMsgBox = QCheckBox(self.widget)
        self.showSendMsgBox.setObjectName(u"showSendMsgBox")
        sizePolicy3.setHeightForWidth(self.showSendMsgBox.sizePolicy().hasHeightForWidth())
        self.showSendMsgBox.setSizePolicy(sizePolicy3)
        self.showSendMsgBox.setMinimumSize(QSize(0, 0))
        self.showSendMsgBox.setFont(font3)
        icon4 = QIcon()
        icon4.addFile(u":/Mainico/ico/\u4e0a\u4e00\u5c42.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.showSendMsgBox.setIcon(icon4)
        self.showSendMsgBox.setIconSize(QSize(18, 18))

        self.horizontalLayout_13.addWidget(self.showSendMsgBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.frame_15 = QFrame(self.widget)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.showIPBox = QCheckBox(self.frame_15)
        self.showIPBox.setObjectName(u"showIPBox")
        self.showIPBox.setFont(font3)
        icon5 = QIcon()
        icon5.addFile(u":/Mainico/ico/\u8bbe\u5907.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.showIPBox.setIcon(icon5)
        self.showIPBox.setIconSize(QSize(18, 18))
        self.showIPBox.setChecked(True)

        self.horizontalLayout_40.addWidget(self.showIPBox)

        self.showPortBox = QCheckBox(self.frame_15)
        self.showPortBox.setObjectName(u"showPortBox")
        self.showPortBox.setFont(font3)
        icon6 = QIcon()
        icon6.addFile(u":/Mainico/ico/\u7aef\u53e3 (1).ico", QSize(), QIcon.Normal, QIcon.Off)
        self.showPortBox.setIcon(icon6)
        self.showPortBox.setIconSize(QSize(18, 18))
        self.showPortBox.setChecked(True)

        self.horizontalLayout_40.addWidget(self.showPortBox)


        self.verticalLayout_2.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.widget)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.frame_16)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.sendTimeRadioButton = QRadioButton(self.widget)
        self.sendTimeRadioButton.setObjectName(u"sendTimeRadioButton")
        sizePolicy3.setHeightForWidth(self.sendTimeRadioButton.sizePolicy().hasHeightForWidth())
        self.sendTimeRadioButton.setSizePolicy(sizePolicy3)
        self.sendTimeRadioButton.setFont(font3)
        icon7 = QIcon()
        icon7.addFile(u":/MainWin/ico/20200510-230202.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.sendTimeRadioButton.setIcon(icon7)
        self.sendTimeRadioButton.setIconSize(QSize(18, 18))

        self.horizontalLayout_32.addWidget(self.sendTimeRadioButton)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.sendTimeSpinBox = QSpinBox(self.widget)
        self.sendTimeSpinBox.setObjectName(u"sendTimeSpinBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sendTimeSpinBox.sizePolicy().hasHeightForWidth())
        self.sendTimeSpinBox.setSizePolicy(sizePolicy4)
        self.sendTimeSpinBox.setMinimumSize(QSize(0, 0))
        self.sendTimeSpinBox.setFont(font3)
        self.sendTimeSpinBox.setMinimum(1)
        self.sendTimeSpinBox.setMaximum(20000)

        self.horizontalLayout_33.addWidget(self.sendTimeSpinBox)

        self.sendTimeLabel_2 = QLabel(self.widget)
        self.sendTimeLabel_2.setObjectName(u"sendTimeLabel_2")
        sizePolicy3.setHeightForWidth(self.sendTimeLabel_2.sizePolicy().hasHeightForWidth())
        self.sendTimeLabel_2.setSizePolicy(sizePolicy3)
        self.sendTimeLabel_2.setFont(font3)

        self.horizontalLayout_33.addWidget(self.sendTimeLabel_2)


        self.horizontalLayout_32.addLayout(self.horizontalLayout_33)


        self.verticalLayout_2.addLayout(self.horizontalLayout_32)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        icon8 = QIcon()
        icon8.addFile(u":/Mainico/ico/20200510-221413.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon8)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.frame_11 = QFrame(self.widget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.listenButton = QPushButton(self.frame_11)
        self.listenButton.setObjectName(u"listenButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.listenButton.sizePolicy().hasHeightForWidth())
        self.listenButton.setSizePolicy(sizePolicy5)
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.listenButton.setFont(font4)
        icon9 = QIcon()
        icon9.addFile(u":/Mainico/ico/\u672a\u76d1\u542c.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.listenButton.setIcon(icon9)
        self.listenButton.setCheckable(True)
        self.listenButton.setChecked(False)

        self.horizontalLayout_10.addWidget(self.listenButton)

        self.serverIPBox = QComboBox(self.frame_11)
        self.serverIPBox.addItem("")
        self.serverIPBox.addItem("")
        self.serverIPBox.addItem("")
        self.serverIPBox.setObjectName(u"serverIPBox")
        self.serverIPBox.setFont(font2)
        self.serverIPBox.setEditable(False)
        self.serverIPBox.setFrame(True)

        self.horizontalLayout_10.addWidget(self.serverIPBox)

        self.serverPortEdit = QSpinBox(self.frame_11)
        self.serverPortEdit.setObjectName(u"serverPortEdit")
        sizePolicy5.setHeightForWidth(self.serverPortEdit.sizePolicy().hasHeightForWidth())
        self.serverPortEdit.setSizePolicy(sizePolicy5)
        self.serverPortEdit.setFont(font2)
        self.serverPortEdit.setMaximum(65535)
        self.serverPortEdit.setValue(6000)

        self.horizontalLayout_10.addWidget(self.serverPortEdit)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.connectListWidget = QListWidget(self.widget)
        self.connectListWidget.setObjectName(u"connectListWidget")
        self.connectListWidget.setFont(font4)

        self.verticalLayout_2.addWidget(self.connectListWidget)

        self.frame_13 = QFrame(self.widget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.selectLabel = QLabel(self.frame_13)
        self.selectLabel.setObjectName(u"selectLabel")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.selectLabel.sizePolicy().hasHeightForWidth())
        self.selectLabel.setSizePolicy(sizePolicy6)
        self.selectLabel.setMaximumSize(QSize(16777215, 16777215))
        self.selectLabel.setFont(font4)

        self.horizontalLayout_31.addWidget(self.selectLabel)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer)

        self.setThreadButton = QPushButton(self.frame_13)
        self.setThreadButton.setObjectName(u"setThreadButton")
        icon10 = QIcon()
        icon10.addFile(u":/Mainico/ico/\u7ebf\u7a0b\u7a0b\u6570.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.setThreadButton.setIcon(icon10)

        self.horizontalLayout_31.addWidget(self.setThreadButton)


        self.verticalLayout_2.addWidget(self.frame_13)


        self.verticalLayout.addWidget(self.widget)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)
        self.modeComboBox.currentIndexChanged.connect(Form.modeSet)
        self.IPEdit.textChanged.connect(Form.setIP)
        self.PortEdit.valueChanged.connect(Form.setServerPort)
        self.connectButton.clicked.connect(Form.startConnect)
        self.showIPBox.clicked.connect(Form.showIP)
        self.showPortBox.clicked.connect(Form.showPort)
        self.sendTimeRadioButton.clicked.connect(Form.timeSend)
        self.sendTimeSpinBox.valueChanged.connect(Form.timerTime)
        self.pushButton.clicked.connect(Form.clearAllConnection)
        self.listenButton.clicked.connect(Form.listenStart)
        self.serverPortEdit.valueChanged.connect(Form.setServerPort)
        self.connectListWidget.itemClicked.connect(Form.listClicked)
        self.setThreadButton.clicked.connect(Form.setThreadNum)
        self.serverIPBox.currentIndexChanged.connect(Form.setServerIP)
        self.connectRraw.clicked.connect(Form.setConnDraw)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.bpsLabel_4.setText(QCoreApplication.translate("Form", u"IP", None))
        self.bpsLabel_3.setText(QCoreApplication.translate("Form", u"\u6a21\u5f0f", None))
        self.byteSizeLabel_2.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3", None))
#if QT_CONFIG(tooltip)
        self.connectButton.setToolTip(QCoreApplication.translate("Form", u"\u9ed8\u8ba4\u8fde\u63a5CH340", None))
#endif // QT_CONFIG(tooltip)
        self.connectButton.setText("")
        self.modeComboBox.setItemText(0, QCoreApplication.translate("Form", u"TCP Socket", None))
        self.modeComboBox.setItemText(1, QCoreApplication.translate("Form", u"UDP Socket", None))

        self.IPEdit.setText(QCoreApplication.translate("Form", u"127.0.0.1", None))
#if QT_CONFIG(tooltip)
        self.sendHexCheckBox.setToolTip(QCoreApplication.translate("Form", u"\u53d1\u9001\u5341\u516d\u8fdb\u5236\u6570\u636e", None))
#endif // QT_CONFIG(tooltip)
        self.sendHexCheckBox.setText(QCoreApplication.translate("Form", u"\u53d1\u9001HEX", None))
#if QT_CONFIG(tooltip)
        self.enterSendCheckBox.setToolTip(QCoreApplication.translate("Form", u"\u4ec5\u5bf9\u5355\u6761\u53d1\u9001\u6709\u6548", None))
#endif // QT_CONFIG(tooltip)
        self.enterSendCheckBox.setText(QCoreApplication.translate("Form", u"\u56de\u8f66\u53d1\u9001", None))
        self.connectRraw.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5\u7ed8\u56fe", None))
#if QT_CONFIG(tooltip)
        self.showSendMsgBox.setToolTip(QCoreApplication.translate("Form", u"\u4ec5\u5bf9\u5355\u6761\u53d1\u9001\u6709\u6548", None))
#endif // QT_CONFIG(tooltip)
        self.showSendMsgBox.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u53d1\u9001", None))
        self.showIPBox.setText(QCoreApplication.translate("Form", u"\u663e\u793aIP", None))
        self.showPortBox.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u7aef\u53e3", None))
        self.sendTimeRadioButton.setText(QCoreApplication.translate("Form", u"\u5b9a\u65f6\u53d1\u9001", None))
#if QT_CONFIG(tooltip)
        self.sendTimeSpinBox.setToolTip(QCoreApplication.translate("Form", u"\u6700\u592720000ms", None))
#endif // QT_CONFIG(tooltip)
        self.sendTimeLabel_2.setText(QCoreApplication.translate("Form", u"ms", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u" \u6e05\u7a7a\u6240\u6709\u8fde\u63a5", None))
#if QT_CONFIG(tooltip)
        self.listenButton.setToolTip(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u7ebf\u7a0b\u6570", None))
#endif // QT_CONFIG(tooltip)
        self.listenButton.setText(QCoreApplication.translate("Form", u"\u76d1\u542c", None))
        self.serverIPBox.setItemText(0, QCoreApplication.translate("Form", u"\u6240\u6709\u5730\u5740", None))
        self.serverIPBox.setItemText(1, QCoreApplication.translate("Form", u"\u672c\u5730\u5730\u5740", None))
        self.serverIPBox.setItemText(2, QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49", None))

        self.selectLabel.setText(QCoreApplication.translate("Form", u"\u672a\u9009\u62e9", None))
#if QT_CONFIG(tooltip)
        self.setThreadButton.setToolTip(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u7ebf\u7a0b\u6570", None))
#endif // QT_CONFIG(tooltip)
        self.setThreadButton.setText("")
    # retranslateUi

