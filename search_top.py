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
        self.search_btn = QtWidgets.QPushButton(Dialog)
        self.search_btn.setGeometry(QtCore.QRect(50, 140, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.main_title = QtWidgets.QLabel(Dialog)
        self.main_title.setGeometry(QtCore.QRect(70, 10, 411, 71))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.main_title.setFont(font)
        self.main_title.setObjectName("main_title")
        self.result_table = QtWidgets.QTableWidget(Dialog)
        self.result_table.setGeometry(QtCore.QRect(45, 200, 451, 301))
        self.result_table.setObjectName("result_table")
        self.result_table.setColumnCount(0)
        self.result_table.setRowCount(0)
        self.radio_all = QtWidgets.QRadioButton(Dialog)
        self.radio_all.setGeometry(QtCore.QRect(60, 100, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_all.setFont(font)
        self.radio_all.setObjectName("radio_all")
        self.radio_seven = QtWidgets.QRadioButton(Dialog)
        self.radio_seven.setGeometry(QtCore.QRect(170, 100, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_seven.setFont(font)
        self.radio_seven.setObjectName("radio_seven")
        self.radio_eight = QtWidgets.QRadioButton(Dialog)
        self.radio_eight.setGeometry(QtCore.QRect(270, 100, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_eight.setFont(font)
        self.radio_eight.setObjectName("radio_eight")
        self.radio_ten = QtWidgets.QRadioButton(Dialog)
        self.radio_ten.setGeometry(QtCore.QRect(450, 100, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_ten.setFont(font)
        self.radio_ten.setObjectName("radio_ten")
        self.radio_nine = QtWidgets.QRadioButton(Dialog)
        self.radio_nine.setGeometry(QtCore.QRect(360, 100, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radio_nine.setFont(font)
        self.radio_nine.setObjectName("radio_nine")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Procurar Melhores"))
        self.search_btn.setText(_translate("Dialog", "Procurar"))
        self.main_title.setText(
            _translate(
                "Dialog",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Noto Sans'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt;">Qual a nota de corte?</span></p>\n'
                '<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">(Deixe em branco para ver a lista completa)</span></p></body></html>',
            )
        )
        self.radio_all.setText(_translate("Dialog", "todos"))
        self.radio_seven.setText(_translate("Dialog", "7+"))
        self.radio_eight.setText(_translate("Dialog", "8+"))
        self.radio_ten.setText(_translate("Dialog", "10"))
        self.radio_nine.setText(_translate("Dialog", "9+"))
