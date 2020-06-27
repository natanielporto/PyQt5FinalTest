# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eraseAllRecords.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(551, 525)
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(30, 50, 461, 201))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.remove_all_btn = QtWidgets.QPushButton(Dialog)
        self.remove_all_btn.setGeometry(QtCore.QRect(70, 310, 381, 111))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.remove_all_btn.setFont(font)
        self.remove_all_btn.setObjectName("remove_all_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Remover Tudo"))
        self.title.setText(
            _translate(
                "Dialog",
                '<html><head/><body><p align="center">Atençao: ao clicar no botao abaixo</p><p align="center">voce vai excluir toda a base de dados</p><p align="center">do programa e recomeçar do zero.</p><p align="center">Tem certeza que quer fazer isso?</p></body></html>',
            )
        )
        self.remove_all_btn.setText(
            _translate("Dialog", "Eu concordo: remover toda a base de dados.")
        )
