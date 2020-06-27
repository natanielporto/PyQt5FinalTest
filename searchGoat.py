# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchGoat.ui'
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
        self.searchBtn.setGeometry(QtCore.QRect(50, 60, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.searchBtn.setFont(font)
        self.searchBtn.setObjectName("searchBtn")
        self.mainTitle = QtWidgets.QLabel(Dialog)
        self.mainTitle.setGeometry(QtCore.QRect(90, 0, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.mainTitle.setFont(font)
        self.mainTitle.setObjectName("mainTitle")
        self.resultTable = QtWidgets.QTableWidget(Dialog)
        self.resultTable.setGeometry(QtCore.QRect(45, 120, 451, 381))
        self.resultTable.setObjectName("resultTable")
        self.resultTable.setColumnCount(0)
        self.resultTable.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Procurar GOATs"))
        self.searchBtn.setText(_translate("Dialog", "Quem sao?"))
        self.mainTitle.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">G.O.A.T.: Greatest Of All Time</p></body></html>"))
