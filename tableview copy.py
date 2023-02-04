# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableview.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import webbrowser

import pyperclip
from ast import keyword
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import pickle
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from functools import partial
import requests
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from os import environ       
import requests
import time
import  hmac
import  hashlib
import  base64
import json
import doubleagent


def suppress_qt_warnings():   
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"   


class Ui_root_widget(object):
    def __init__(self):
        f = open("식품.pkl", "rb")
        temp = pickle.load(f)
        f.close()
        self.category_data = temp   
        self.BASE_URL = 'https://api.naver.com'
        self.API_KEY = "0100000000621aae65a5a7d651ffcb463d89f74a27d08e61f26fa4514be999d771a0cdfb99"
        self.SECRET_KEY ="AQAAAABiGq5lpafWUf/LRj2J90onCrj+bzbfcT48VD4z9PX9JA=="
        self.CUSTOMER_ID = "1538797"
        self.scoutedata_lst = [] 
        self.copydata_lst_lst=[]
    def setupUi(self, root_widget):
        root_widget.setObjectName("root_widget")
        root_widget.resize(1840, 900)
        root_widget.setStyleSheet("border:rgb(0, 0, 0);")
        self.root_layout = QtWidgets.QVBoxLayout(root_widget)
        self.root_layout.setContentsMargins(0, 0, 0, 0)
        self.root_layout.setSpacing(0)
        self.root_layout.setObjectName("root_layout")
        self.stack_widget = QtWidgets.QStackedWidget(root_widget)
        self.stack_widget.setStyleSheet("background-color: rgb(30, 28, 28);")
        self.stack_widget.setObjectName("stack_widget")
        self.page1_main_widget = QtWidgets.QWidget()
        self.page1_main_widget.setObjectName("page1_main_widget")
        self.page1_main_layout = QtWidgets.QVBoxLayout(self.page1_main_widget)
        self.page1_main_layout.setContentsMargins(0, 0, 0, 0)
        self.page1_main_layout.setSpacing(0)
        self.page1_main_layout.setObjectName("page1_main_layout")
        self.page1_input_widget = QtWidgets.QWidget(self.page1_main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page1_input_widget.sizePolicy().hasHeightForWidth())
        self.page1_input_widget.setSizePolicy(sizePolicy)
        self.page1_input_widget.setObjectName("page1_input_widget")
        self.page1_input_layout = QtWidgets.QHBoxLayout(self.page1_input_widget)
        self.page1_input_layout.setContentsMargins(0, 0, 0, 0)
        self.page1_input_layout.setSpacing(0)
        self.page1_input_layout.setObjectName("page1_input_layout")
        self.page1_input = QtWidgets.QLineEdit(self.page1_input_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page1_input.sizePolicy().hasHeightForWidth())
        self.page1_input.setSizePolicy(sizePolicy)
        self.page1_input.setMinimumSize(QtCore.QSize(0, 100))
        self.page1_input.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.page1_input.setFont(font)
        self.page1_input.setStyleSheet("background-color: rgb(30, 28, 28);\n"
"border-style: solid;\n"
"border-color:rgb(29, 27, 27);\n"
"border-width: 1px;\n"
"color: white;")
        # self.page1_input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.page1_input.setObjectName("page1_input")
        self.page1_input_layout.addWidget(self.page1_input)
        self.page1_btn = QtWidgets.QPushButton(self.page1_input_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page1_btn.sizePolicy().hasHeightForWidth())
        self.page1_btn.setSizePolicy(sizePolicy)
        self.page1_btn.setMinimumSize(QtCore.QSize(60, 100))
        self.page1_btn.setMaximumSize(QtCore.QSize(60, 100))
        self.page1_btn.setStyleSheet("\n"
"QPushButton::hover {\n"
"color : white;\n"
"background-color: rgb(33,90,181);\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"border-style: solid;\n"
"border-color:rgb(30, 28, 28);\n"
"border-width: 2px;\n"
"border-radius:15px;\n"
"background-color: rgb(0,0,0);\n"
"    image: url(:/newPrefix/sorce.png);\n"
"}\n"
"")
        self.page1_btn.setText("")
        self.page1_btn.setObjectName("page1_btn")
        self.page1_input_layout.addWidget(self.page1_btn)
        self.page1_main_layout.addWidget(self.page1_input_widget)
        self.page1_scrollarea = QtWidgets.QScrollArea(self.page1_main_widget)
        self.page1_scrollarea.setStyleSheet("QScrollArea{\n"
"border-style: solid;\n"
"border-color:rgb(27, 29, 35);\n"
"border-width: 0px;\n"
"border-radius:15px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"    QScrollBar::sub-line:vertical {\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::handle:vertical {    \n"
"background-color: rgb(33,90,181);\n"
"\n"
"min-height: 30px;\n"
"\n"
"\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.page1_scrollarea.setWidgetResizable(True)
        self.page1_scrollarea.setObjectName("page1_scrollarea")
        self.page1_scrollarea_widget = QtWidgets.QWidget()
        self.page1_scrollarea_widget.setGeometry(QtCore.QRect(0, 0, 87, 16))
        self.page1_scrollarea_widget.setStyleSheet("background-color: rgb(0,0,0);\n"
"\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"\n"
"")
        self.page1_scrollarea_widget.setObjectName("page1_scrollarea_widget")
        self.page1_scrollarea_layout = QtWidgets.QFormLayout(self.page1_scrollarea_widget)
        self.page1_scrollarea_layout.setObjectName("page1_scrollarea_layout")
        self.page1_scrollarea.setWidget(self.page1_scrollarea_widget)
        self.page1_main_layout.addWidget(self.page1_scrollarea)
        self.stack_widget.addWidget(self.page1_main_widget)
        self.page2_main_widget = QtWidgets.QWidget()
        self.page2_main_widget.setObjectName("page2_main_widget")
        self.page2_main_layout = QtWidgets.QVBoxLayout(self.page2_main_widget)
        self.page2_main_layout.setObjectName("page2_main_layout")
        self.page2_first_widget = QtWidgets.QWidget(self.page2_main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page2_first_widget.sizePolicy().hasHeightForWidth())
        self.page2_first_widget.setSizePolicy(sizePolicy)
        self.page2_first_widget.setMinimumSize(QtCore.QSize(50, 0))
        self.page2_first_widget.setObjectName("page2_first_widget")
        self.page2_first_layout = QtWidgets.QHBoxLayout(self.page2_first_widget)
        self.page2_first_layout.setContentsMargins(0, 6, 0, 0)
        self.page2_first_layout.setObjectName("page2_first_layout")
        self.page2_linedt = QtWidgets.QLineEdit(self.page2_first_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page2_linedt.sizePolicy().hasHeightForWidth())
        self.page2_linedt.setSizePolicy(sizePolicy)
        self.page2_linedt.setMinimumSize(QtCore.QSize(530, 20))
        self.page2_linedt.setMaximumSize(QtCore.QSize(530, 16777215))
        self.page2_linedt.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-color:rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"color: white;")
        self.page2_linedt.setObjectName("page2_linedt")
        self.page2_first_layout.addWidget(self.page2_linedt)
        self.page2_search_btn = QtWidgets.QPushButton(self.page2_first_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page2_search_btn.sizePolicy().hasHeightForWidth())
        self.page2_search_btn.setSizePolicy(sizePolicy)
        self.page2_search_btn.setMinimumSize(QtCore.QSize(210, 50))
        self.page2_search_btn.setMaximumSize(QtCore.QSize(210, 50))
        self.page2_search_btn.clicked.connect(self.naver)
        self.page2_search_btn.setStyleSheet("\n"
"QPushButton::hover {\n"
"color : white;\n"
"background-color: rgb(33,90,181);\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"border-style: solid;\n"
"border-color:rgb(30, 28, 28);\n"
"color:white;\n"
"border-radius: 5px;\n"
"background-color: rgb(0,0,0);\n"
"font-weight:bold;\n"
"}\n"
"")
        self.page2_search_btn.setObjectName("page2_search_btn")
        self.page2_first_layout.addWidget(self.page2_search_btn)
        self.page2_link_btn = QtWidgets.QPushButton(self.page2_first_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page2_link_btn.sizePolicy().hasHeightForWidth())
        self.page2_link_btn.clicked.connect(self.linkevent)
        self.page2_link_btn.setSizePolicy(sizePolicy)
        self.page2_link_btn.setMinimumSize(QtCore.QSize(560, 20))

        self.page2_link_btn.setStyleSheet("\n"
"QPushButton::hover {\n"
"color : white;\n"
"background-color: rgb(33,90,181);\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"border-style: solid;\n"
"border-color:rgb(30, 28, 28);\n"
"color:white;\n"
"border-radius: 5px;\n"
"background-color: rgb(0,0,0);\n"
"font-weight:bold;\n"
"}")
        self.page2_link_btn.setObjectName("page2_link_btn")

        self.page2_first_layout.addWidget(self.page2_link_btn)
        self.page2_copy_btn = QtWidgets.QPushButton(self.page2_first_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page2_copy_btn.sizePolicy().hasHeightForWidth())
        self.page2_copy_btn.setSizePolicy(sizePolicy)
        self.page2_copy_btn.setMinimumSize(QtCore.QSize(50, 20))
        self.page2_copy_btn.setStyleSheet("\n"
"QPushButton::hover {\n"
"color : white;\n"
"background-color: rgb(33,90,181);\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"border-style: solid;\n"
"border-color:rgb(30, 28, 28);\n"
"color:white;\n"
"border-radius: 5px;\n"
"background-color: rgb(0,0,0);\n"
"font-weight:bold;\n"
"}")
        self.page2_copy_btn.setObjectName("page2_copy_btn")
        self.page2_copy_btn.clicked.connect(self.copyevent)
        self.page2_first_layout.addWidget(self.page2_copy_btn)
        self.page2_clear_btn = QtWidgets.QPushButton(self.page2_first_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page2_clear_btn.sizePolicy().hasHeightForWidth())
        self.page2_clear_btn.setSizePolicy(sizePolicy)
        self.page2_clear_btn.setMinimumSize(QtCore.QSize(50, 20))
        self.page2_clear_btn.clicked.connect(self.clearevent)
        self.page2_clear_btn.setStyleSheet("\n"
"QPushButton::hover {\n"
"color : white;\n"
"background-color: rgb(33,90,181);\n"
"        \n"
"}\n"
"\n"
"QPushButton {\n"
"border-style: solid;\n"
"border-color:rgb(30, 28, 28);\n"
"color:white;\n"
"border-radius: 5px;\n"
"background-color: rgb(0,0,0);\n"
"font-weight:bold;\n"
"}")
        self.page2_clear_btn.setObjectName("page2_clear_btn")
        self.page2_first_layout.addWidget(self.page2_clear_btn)
        self.page2_main_layout.addWidget(self.page2_first_widget)
        self.page2_middle_widget = QtWidgets.QWidget(self.page2_main_widget)
        self.page2_middle_widget.setStyleSheet("border:rgb(0, 0, 0);\n"
"color:white;\n"
"font-size:15px;\n"
"")
        self.page2_middle_widget.setObjectName("page2_middle_widget")
        self.page2_middle_layout = QtWidgets.QHBoxLayout(self.page2_middle_widget)
        self.page2_middle_layout.setContentsMargins(0, 0, 0, 0)
        self.page2_middle_layout.setObjectName("page2_middle_layout")
        self.page2_scout_tablewidget = QtWidgets.QTableWidget(self.page2_middle_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page2_scout_tablewidget.sizePolicy().hasHeightForWidth())
        self.page2_scout_tablewidget.setSizePolicy(sizePolicy)
        self.page2_scout_tablewidget.setMinimumSize(QtCore.QSize(350, 0))
        self.page2_scout_tablewidget.setMaximumSize(QtCore.QSize(300000, 16777215))
        self.page2_scout_tablewidget.setStyleSheet("QWidget {\n"
"    background-color: rgb(0,0,0);\n"
"    font-size: 10pt;\n"
"border-style: solid;\n"
"border-color:rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"    QScrollBar::add-line:vertical {\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"    QScrollBar::sub-line:vertical {\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::handle:vertical {    \n"
"background-color: rgb(33,90,181);\n"
"\n"
"min-height: 30px;\n"
"\n"
"\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"/* 테이블 뷰 속성 */\n"
"QHeaderView::section {\n"
"    background-color: rgb(30, 28, 28);\n"
"    padding: 1px;\n"
"    font-size: 14pt;\n"
"    border-style: none;\n"
"    border: 1px solid #fffff8;\n"
"\n"
"}\n"
"QTableView QTableCornerButton::section {\n"
"    background-color: rgb(30, 28, 28);\n"
"}\n"
"\n"
"\n"
"")
        self.page2_scout_tablewidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.page2_scout_tablewidget.setAlternatingRowColors(False)
        self.page2_scout_tablewidget.setRowCount(0)
        self.page2_scout_tablewidget.setObjectName("page2_scout_tablewidget")
        self.page2_scout_tablewidget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.page2_scout_tablewidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.page2_scout_tablewidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.page2_scout_tablewidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.page2_scout_tablewidget.setHorizontalHeaderItem(3, item)
        self.page2_scout_tablewidget.horizontalHeader().setCascadingSectionResizes(False)
        self.page2_scout_tablewidget.verticalHeader().setCascadingSectionResizes(False)
        self.page2_middle_layout.addWidget(self.page2_scout_tablewidget)
        self.page2_naver_tablewidget = QtWidgets.QTableWidget(self.page2_middle_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page2_naver_tablewidget.sizePolicy().hasHeightForWidth())
        self.page2_naver_tablewidget.setSizePolicy(sizePolicy)
        self.page2_naver_tablewidget.setMinimumSize(QtCore.QSize(400, 0))
        self.page2_naver_tablewidget.setMaximumSize(QtCore.QSize(17000, 16777215))
        self.page2_naver_tablewidget.setStyleSheet("QWidget {\n"
"    background-color: rgb(0,0,0);\n"
"    font-size: 10pt;\n"
"border-style: solid;\n"
"border-color:rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"    QScrollBar::add-line:vertical {\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"    QScrollBar::sub-line:vertical {\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::handle:vertical {    \n"
"background-color: rgb(33,90,181);\n"
"\n"
"min-height: 30px;\n"
"\n"
"\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"/* 테이블 뷰 속성 */\n"
"QHeaderView::section {\n"
"    background-color: rgb(30, 28, 28);\n"
"    padding: 1px;\n"
"    font-size: 14pt;\n"
"    border-style: none;\n"
"    border: 1px solid #fffff8;\n"
"\n"
"}\n"
"QTableView QTableCornerButton::section {\n"
"    background-color: rgb(30, 28, 28);\n"
"}\n"
"\n"
"\n"
"")
        self.page2_naver_tablewidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.page2_naver_tablewidget.setObjectName("page2_naver_tablewidget")
        self.page2_naver_tablewidget.setColumnCount(4)
        self.page2_naver_tablewidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.page2_naver_tablewidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.page2_naver_tablewidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.page2_naver_tablewidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.page2_naver_tablewidget.setHorizontalHeaderItem(3, item)
        self.page2_naver_tablewidget.horizontalHeader().setCascadingSectionResizes(True)
        self.page2_naver_tablewidget.verticalHeader().setCascadingSectionResizes(False)
        self.page2_middle_layout.addWidget(self.page2_naver_tablewidget)
        self.page2_result_plaintext = QtWidgets.QPlainTextEdit(self.page2_middle_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page2_result_plaintext.sizePolicy().hasHeightForWidth())
        self.page2_result_plaintext.setSizePolicy(sizePolicy)
        self.page2_result_plaintext.setMinimumSize(QtCore.QSize(800, 0))
        self.page2_result_plaintext.setMaximumSize(QtCore.QSize(800, 16777215))
        self.page2_result_plaintext.setStyleSheet("    QScrollBar::add-line:vertical {\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"    QScrollBar::sub-line:vertical {\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::handle:vertical {    \n"
"background-color: rgb(33,90,181);\n"
"\n"
"min-height: 30px;\n"
"\n"
"\n"
"}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"QPlainTextEdit{\n"
"\n"
"border:rgb(0, 0, 0);\n"
"color:white;\n"
"font-size:20px;\n"
"\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.page2_result_plaintext.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.page2_result_plaintext.setPlainText("")
        self.page2_result_plaintext.setObjectName("page2_result_plaintext")
        self.page2_middle_layout.addWidget(self.page2_result_plaintext)
        self.page2_main_layout.addWidget(self.page2_middle_widget)
        self.page2_back_btn = QtWidgets.QPushButton(self.page2_main_widget)
        self.page2_back_btn.clicked.connect(self.switchevent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page2_back_btn.sizePolicy().hasHeightForWidth())
        self.page2_back_btn.setSizePolicy(sizePolicy)
        self.page2_back_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.page2_back_btn.setStyleSheet("background-color: rgb(33,90,181);\n"
"color:white;\n"
"font-weight:bold;\n"
"")
        self.page2_back_btn.setObjectName("page2_back_btn")
        self.page2_main_layout.addWidget(self.page2_back_btn)
        self.stack_widget.addWidget(self.page2_main_widget)
        self.root_layout.addWidget(self.stack_widget)

        self.retranslateUi(root_widget)
        self.stack_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(root_widget)
        self.page1_btn.clicked.connect(self.click_event1) 
        self.page2_scout_tablewidget.doubleClicked.connect(self.to_page2scout_plaintext)
        self.page2_naver_tablewidget.doubleClicked.connect(self.page2_naverclickevent)
        self.page2_naver_tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.page2_scout_tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
    def clearevent(self):
        self.page2_result_plaintext.clear()
    def copyevent(self):
        t = self.page2_result_plaintext.toPlainText()
        pyperclip.copy(t)
        self.page2_result_plaintext.copy()
    def linkevent(self):
        t = self.page2_linedt.text()
        webbrowser.open("https://search.shopping.naver.com/search/all?where=all&frm=NVSCTAB&query="+t)
    def click_event1(self,cate):

        count = self.page1_scrollarea_layout.count()
        keyword = self.page1_input.text()
        keyword = keyword.upper()
        for li in range(0,count):
            child = self.page1_scrollarea_layout.takeAt(0)
            try:


                child.widget().deleteLater()   

            except:
                pass
        name_lst = self.category_data[0]
        num_lst = self.category_data[1]

        searchnum_lst = []

        count = 0
        for name,num in zip(name_lst,num_lst):


            name = name.split('>')[-1]

            if keyword in name:
                searchnum_lst.append(count)
            count +=1


        for i,searchnum in enumerate(searchnum_lst):

            self.pushButton = QtWidgets.QPushButton(name_lst[searchnum],self.page1_scrollarea_widget)
            self.pushButton.setObjectName("pushButton")
            self.pushButton.setMaximumSize(QtCore.QSize(300, 200))
            self.pushButton.setMinimumSize(QtCore.QSize(800, 70))
            self.pushButton.clicked.connect( partial(self.click_event2, num_lst[searchnum]))
            self.pushButton.setStyleSheet("\n"
                                            "QPushButton::hover {\n"
                                            "color : white;\n"
                                            "background-color: rgb(33,90,181);\n"
                                            "        \n"
                                            "}\n"
                                            "\n"
                                            "QPushButton {\n"
                                            "border-style: solid;\n"
                                            "border-color:rgb(30, 28, 28);\n"
                                            "border-width: 2px;\n"
                                            "color : white;\n"
                                            "font : bold;\n"
                                            "font-size : 40px;\n"
                                            "\n"
                                            "background-color: rgb(0,0,0);\n"
            
                                            "}\n"
                                            "")
            self.page1_scrollarea_layout.addRow(self.pushButton)

    def click_event2(self,searchnum):
        count = self.page1_scrollarea_layout.count()
        for li in range(0,count):
            child = self.page1_scrollarea_layout.takeAt(0)
            try:

                if child.widget():
                   child.widget().deleteLater()   

            except:
                pass



        name_array = []
        pc_bid_array = []
        mobile_bid_array = []
        prdCnt_array = []
        total_array = []
        average_array = []



        duration_dict = {
            "duration": '30d',
            "genders": "f,m",
            "ages": "10,20,30,40"
        }

        json_trans = json.dumps(duration_dict)
        r = requests.post('https://api.itemscout.io/api/category/'+str(searchnum)+'/data',
                        data=duration_dict)

        key_id = json.loads(r.text)


        array = key_id['data']['data']
        i = 1
        json_key = []
        for li in array:
            json_key.append(li)
        # key_id = json.dumps(array)
        # print(key_id[0])
        key_lst_lst = []
        for al in json_key:
            li = array[al]
            try:


                name = li['keyword']
                bid = li['bid']
                pc_bid = bid['pc_bid']
                mobile_bid = bid['mobile_bid']
                prdCnt = li['prdCnt']
                monthly = li['monthly']
                total = monthly['total']
                average = prdCnt/total
                name_array.append(name)
                pc_bid_array.append(pc_bid)
                mobile_bid_array.append(mobile_bid)
                total_array.append(total)
                average = round(average, 2)
                average_array.append(average)
                prdCnt_array.append(prdCnt)
            # name_array,total_array,prdCnt_array,average_array
                key_lst = [name,total,prdCnt,average]
                key_lst_lst.append(key_lst)
            except:
                continue
        self.page2_scout_tablewidget.setColumnWidth(0, 350)
        self.page2_scout_tablewidget.setColumnWidth(1, 100)
        self.page2_scout_tablewidget.setColumnWidth(2, 100)
        self.page2_scout_tablewidget.setColumnWidth(3, 100)
        self.page2_naver_tablewidget.setColumnWidth(0, 350)
        self.page2_naver_tablewidget.setColumnWidth(1, 100)
        self.page2_naver_tablewidget.setColumnWidth(2, 100)      
        self.page2_naver_tablewidget.setColumnWidth(3, 100)
        key_lst_lst=sorted(key_lst_lst, key=lambda key_lst: int(key_lst[1]),reverse=True)
        self.page2_scout_tablewidget.setRowCount(len(key_lst_lst))
        self.page2_naver_tablewidget.setRowCount(50)
        count = 0
        self.scoutedata_lst = []
        for key_lst in key_lst_lst:

            self.page2_scout_tablewidget.setItem(count,0, QTableWidgetItem(key_lst[0]))
            self.page2_scout_tablewidget.setItem(count,1, QTableWidgetItem(str(key_lst[1])))
            self.page2_scout_tablewidget.setItem(count,2, QTableWidgetItem(str(key_lst[2])))
            self.page2_scout_tablewidget.setItem(count,3, QTableWidgetItem(str((key_lst[3]))))
            self.scoutedata_lst.append(key_lst[0])
            count += 1
        self.stack_widget.setCurrentIndex(1)
        self.copydata_lst_lst=[]
    def to_page2scout_plaintext(self):
        item = self.page2_scout_tablewidget.currentItem().text()
        item=item.split('\n')[0]

        self.page2_result_plaintext.appendPlainText(item)
    def page2_naverclickevent(self):
        row = self.page2_naver_tablewidget.currentIndex().row()
        column = self.page2_naver_tablewidget.currentIndex().column()
        try:
            t = self.page2_naver_tablewidget.item(row, column+2).text()
            t = self.page2_naver_tablewidget.item(row, column).text()
            self.page2_result_plaintext.appendPlainText(t)
            pass
        except:


            item = self.page2_naver_tablewidget.currentItem().text()
            headers = {
                "accept": "text/plain, */*; q=0.01",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "pragma": "no-cache",
                "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\", \"Google Chrome\";v=\"102\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-requested-with": "XMLHttpRequest"
            }
            body =  { 'keyword':item}
            r = requests.post('https://api.itemscout.io/api/keyword',data=body)
            q = r.text
            q= q.split(':')[-1][:-1]

            r = requests.get('https://api.itemscout.io/api/v2/keyword/stats/'+q+'').text
            totalProductCount = r.split('"totalProductCount":')[1].split(',')[0]

            totalSearchCount= r.split('"totalSearchCount":')[1].split(',')[0]
            self.page2_naver_tablewidget.setItem(row,2, QTableWidgetItem(str(totalProductCount)))
            self.page2_naver_tablewidget.setItem(row,3, QTableWidgetItem(str(round(int(totalProductCount)/int(totalSearchCount),2))))

    def to_page2naver_plaintext(self):
        item = self.page2_naver_tablewidget.currentItem().text()
        item=item.split('\n')[0]

        self.page2_result_plaintext.appendPlainText(item)
    def switchevent(self):

        self.stack_widget.setCurrentIndex(0)
        self.page2_naver_tablewidget.clearContents()
        self.page2_scout_tablewidget.clearContents()
        self.page2_linedt.clear()
        self.page2_result_plaintext.clear()	

    def generate(self,timestamp, method, uri, secret_key):
        message = "{}.{}.{}".format(timestamp, method, uri)
        #hash = hmac.new(bytes(secret_key, "utf-8"), bytes(message, "utf-8"), hashlib.sha256)
        hash = hmac.new(secret_key.encode("utf-8"), message.encode("utf-8"), hashlib.sha256)
        hash.hexdigest()
        return base64.b64encode(hash.digest())


    def get_header(self,method, uri, api_key, secret_key, customer_id):
        timestamp = str(int(time.time() * 1000))
        signature = self.generate(timestamp, method, uri, self.SECRET_KEY)
        return {'Content-Type': 'application/json; charset=UTF-8', 'X-Timestamp': timestamp, 'X-API-KEY': self.API_KEY, 'X-Customer': str(self.CUSTOMER_ID), 'X-Signature': signature}
    def naver(self):
        keyword = self.page2_linedt.text()
        keyword=keyword.upper()
        dic_return_kwd = {}
        naver_ad_url = '/keywordstool'
        #_kwds_string = '원피스' #1개일경우
        #_kwds_string = ['나이키', '원피스', '운동화'] #키워드 여러개일경우
        method = 'GET'
        prm = {'hintKeywords' : keyword , 'showDetail':1}
        #    ManageCustomerLink Usage Sample
        r = requests.get(self.BASE_URL + naver_ad_url, params=prm, headers=self.get_header(method, naver_ad_url, self.API_KEY, self.SECRET_KEY, self.CUSTOMER_ID))

        key_id = json.loads(r.text)


        array = key_id['keywordList']
        naver_lst_lst = []
        for li in array:
            try:
                relkeyword = li["relKeyword"]

                viewcount = int(li["monthlyPcQcCnt"])+int(li["monthlyMobileQcCnt"])

                if viewcount < 300:
                    continue
                key_lst =[relkeyword,str(viewcount)]
                naver_lst_lst.append(key_lst)
            except:
  
                continue
        prenaver_lst_lst=sorted(naver_lst_lst, key=lambda key_lst: int(key_lst[1]),reverse=True)

        count =0
        naver_lst_lst = []
        for li_lst in prenaver_lst_lst:
            t = doubleagent.sublist(self.scoutedata_lst,li_lst[0])
            if len(self.scoutedata_lst) == len(t):
                naver_lst_lst.append(li_lst)
        self.page2_naver_tablewidget.setRowCount(len(naver_lst_lst))
        for naver_lst in naver_lst_lst:

            self.page2_naver_tablewidget.setItem(count,0, QTableWidgetItem(naver_lst[0]))
            self.page2_naver_tablewidget.setItem(count,1, QTableWidgetItem(str(naver_lst[1])))

            count += 1
    def retranslateUi(self, root_widget):
        _translate = QtCore.QCoreApplication.translate
        root_widget.setWindowTitle(_translate("root_widget", "Form"))
        self.page2_search_btn.setText(_translate("root_widget", "SEARCH"))
        self.page2_link_btn.setText(_translate("root_widget", "LINK"))
        self.page2_copy_btn.setText(_translate("root_widget", "COPY"))
        self.page2_clear_btn.setText(_translate("root_widget", "CLEAR"))
        item = self.page2_scout_tablewidget.horizontalHeaderItem(0)
        item.setText(_translate("root_widget", "키워드"))
        item = self.page2_scout_tablewidget.horizontalHeaderItem(1)
        item.setText(_translate("root_widget", "검색량"))
        item = self.page2_scout_tablewidget.horizontalHeaderItem(2)
        item.setText(_translate("root_widget", "상품량"))
        item = self.page2_scout_tablewidget.horizontalHeaderItem(3)
        item.setText(_translate("root_widget", "경쟁량"))
        item = self.page2_naver_tablewidget.horizontalHeaderItem(0)
        item.setText(_translate("root_widget", "키워드"))
        item = self.page2_naver_tablewidget.horizontalHeaderItem(1)
        item.setText(_translate("root_widget", "검색량"))
        item = self.page2_naver_tablewidget.horizontalHeaderItem(2)
        item.setText(_translate("root_widget", "삼품량"))
        item = self.page2_naver_tablewidget.horizontalHeaderItem(3)
        item.setText(_translate("root_widget", "경쟁량"))
        self.page2_back_btn.setText(_translate("root_widget", "BACK"))
        self.page1_btn.setShortcut("Return")    
        self.page2_search_btn.setShortcut("Return")    
        root_widget.setWindowIcon(QIcon('web.png'))

import df_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    root_widget = QtWidgets.QWidget()
    ui = Ui_root_widget()
    ui.setupUi(root_widget)
    suppress_qt_warnings()
    root_widget.show()
    sys.exit(app.exec_())
