# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ice.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 465)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.LblWidth = QtWidgets.QLabel(self.centralwidget)
        self.LblWidth.setObjectName("LblWidth")
        self.gridLayout.addWidget(self.LblWidth, 0, 0, 1, 1)
        self.CBWidth = QtWidgets.QComboBox(self.centralwidget)
        self.CBWidth.setObjectName("CBWidth")
        self.CBWidth.addItem("")
        self.CBWidth.addItem("")
        self.CBWidth.addItem("")
        self.gridLayout.addWidget(self.CBWidth, 0, 1, 1, 1)
        self.LblPercent = QtWidgets.QLabel(self.centralwidget)
        self.LblPercent.setObjectName("LblPercent")
        self.gridLayout.addWidget(self.LblPercent, 0, 4, 1, 1)
        self.CBHeight = QtWidgets.QComboBox(self.centralwidget)
        self.CBHeight.setObjectName("CBHeight")
        self.CBHeight.addItem("")
        self.CBHeight.addItem("")
        self.CBHeight.addItem("")
        self.gridLayout.addWidget(self.CBHeight, 0, 3, 1, 1)
        self.SpinPercent = QtWidgets.QSpinBox(self.centralwidget)
        self.SpinPercent.setObjectName("SpinPercent")
        self.gridLayout.addWidget(self.SpinPercent, 0, 5, 1, 1)
        self.LblHeight = QtWidgets.QLabel(self.centralwidget)
        self.LblHeight.setObjectName("LblHeight")
        self.gridLayout.addWidget(self.LblHeight, 0, 2, 1, 1)
        self.BtnCreate = QtWidgets.QPushButton(self.centralwidget)
        self.BtnCreate.setObjectName("BtnCreate")
        self.gridLayout.addWidget(self.BtnCreate, 0, 6, 1, 1)
        self.GBField = QtWidgets.QGroupBox(self.centralwidget)
        self.GBField.setObjectName("GBField")
        self.label = QtWidgets.QLabel(self.GBField)
        self.label.setGeometry(QtCore.QRect(10, 23, 703, 344))
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.GBField, 2, 0, 1, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ледовое поле"))
        self.LblWidth.setText(_translate("MainWindow", "Ширина поля"))
        self.CBWidth.setItemText(0, _translate("MainWindow", "3"))
        self.CBWidth.setItemText(1, _translate("MainWindow", "4"))
        self.CBWidth.setItemText(2, _translate("MainWindow", "5"))
        self.LblPercent.setText(_translate("MainWindow", "Процент известных льдин"))
        self.CBHeight.setItemText(0, _translate("MainWindow", "3"))
        self.CBHeight.setItemText(1, _translate("MainWindow", "4"))
        self.CBHeight.setItemText(2, _translate("MainWindow", "5"))
        self.LblHeight.setText(_translate("MainWindow", "Высота поля"))
        self.BtnCreate.setText(_translate("MainWindow", "Создать поле"))
        self.GBField.setTitle(_translate("MainWindow", "Ледовое поле"))

