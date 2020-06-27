# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchTop.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(542, 525)
        self.searchBtn = QtWidgets.QPushButton(Dialog)
        self.searchBtn.setGeometry(QtCore.QRect(50, 140, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.searchBtn.setFont(font)
        self.searchBtn.setObjectName("searchBtn")
        self.mainTitle = QtWidgets.QLabel(Dialog)
        self.mainTitle.setGeometry(QtCore.QRect(70, 10, 411, 71))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.mainTitle.setFont(font)
        self.mainTitle.setObjectName("mainTitle")
        self.resultTable = QtWidgets.QTableWidget(Dialog)
        self.resultTable.setGeometry(QtCore.QRect(45, 200, 451, 301))
        self.resultTable.setObjectName("resultTable")
        self.resultTable.setColumnCount(0)
        self.resultTable.setRowCount(0)
        self.radioAll = QtWidgets.QRadioButton(Dialog)
        self.radioAll.setGeometry(QtCore.QRect(60, 100, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioAll.setFont(font)
        self.radioAll.setObjectName("radioAll")
        self.radioSeven = QtWidgets.QRadioButton(Dialog)
        self.radioSeven.setGeometry(QtCore.QRect(170, 100, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioSeven.setFont(font)
        self.radioSeven.setObjectName("radioSeven")
        self.radioEight = QtWidgets.QRadioButton(Dialog)
        self.radioEight.setGeometry(QtCore.QRect(270, 100, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioEight.setFont(font)
        self.radioEight.setObjectName("radioEight")
        self.radioTen = QtWidgets.QRadioButton(Dialog)
        self.radioTen.setGeometry(QtCore.QRect(450, 100, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioTen.setFont(font)
        self.radioTen.setObjectName("radioTen")
        self.radioNine = QtWidgets.QRadioButton(Dialog)
        self.radioNine.setGeometry(QtCore.QRect(360, 100, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioNine.setFont(font)
        self.radioNine.setObjectName("radioNine")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Procurar Melhores"))
        self.searchBtn.setText(_translate("Dialog", "Procurar"))
        self.mainTitle.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Qual a nota de corte?</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">(Deixe em branco para ver a lista completa)</span></p></body></html>"))
        self.radioAll.setText(_translate("Dialog", "todos"))
        self.radioSeven.setText(_translate("Dialog", "7+"))
        self.radioEight.setText(_translate("Dialog", "8+"))
        self.radioTen.setText(_translate("Dialog", "10"))
        self.radioNine.setText(_translate("Dialog", "9+"))
