# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchRecordLabel.ui'
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
        self.search_btn.setGeometry(QtCore.QRect(50, 120, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.remove_record = QtWidgets.QLabel(Dialog)
        self.remove_record.setGeometry(QtCore.QRect(50, 90, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.remove_record.setFont(font)
        self.remove_record.setObjectName("remove_record")
        self.search_input = QtWidgets.QLineEdit(Dialog)
        self.search_input.setGeometry(QtCore.QRect(110, 90, 381, 21))
        self.search_input.setObjectName("search_input")
        self.main_title = QtWidgets.QLabel(Dialog)
        self.main_title.setGeometry(QtCore.QRect(70, 10, 411, 71))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.main_title.setFont(font)
        self.main_title.setObjectName("main_title")
        self.info_show = QtWidgets.QLabel(Dialog)
        self.info_show.setGeometry(QtCore.QRect(40, 150, 461, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.info_show.setFont(font)
        self.info_show.setObjectName("info_show")
        self.result_table = QtWidgets.QTableWidget(Dialog)
        self.result_table.setGeometry(QtCore.QRect(45, 210, 451, 291))
        self.result_table.setObjectName("result_table")
        self.result_table.setColumnCount(0)
        self.result_table.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Procurar Gravadora"))
        self.search_btn.setText(_translate("Dialog", "Procurar"))
        self.remove_record.setText(_translate("Dialog", "Nome:"))
        self.main_title.setText(
            _translate(
                "Dialog",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Noto Sans'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:18pt;">Qual gravadora deseja encontrar?</span></p>\n'
                '<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">(Deixe em branco para ver a lista completa)</span></p></body></html>',
            )
        )
        self.info_show.setText(
            _translate(
                "Dialog",
                '<html><head/><body><p align="center">Resultado da pesquisa:</p></body></html>',
            )
        )
