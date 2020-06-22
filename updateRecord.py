# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateRecord.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(551, 525)
        self.updateBtn = QtWidgets.QPushButton(Dialog)
        self.updateBtn.setGeometry(QtCore.QRect(60, 100, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.updateBtn.setFont(font)
        self.updateBtn.setObjectName("updateBtn")
        self.removeRecord = QtWidgets.QLabel(Dialog)
        self.removeRecord.setGeometry(QtCore.QRect(60, 60, 54, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.removeRecord.setFont(font)
        self.removeRecord.setObjectName("removeRecord")
        self.updateInput = QtWidgets.QLineEdit(Dialog)
        self.updateInput.setGeometry(QtCore.QRect(120, 60, 381, 21))
        self.updateInput.setObjectName("updateInput")
        self.removeTitle = QtWidgets.QLabel(Dialog)
        self.removeTitle.setGeometry(QtCore.QRect(110, 10, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.removeTitle.setFont(font)
        self.removeTitle.setObjectName("removeTitle")
        self.recordLabel = QtWidgets.QLabel(Dialog)
        self.recordLabel.setGeometry(QtCore.QRect(60, 340, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recordLabel.setFont(font)
        self.recordLabel.setObjectName("recordLabel")
        self.goatBox = QtWidgets.QCheckBox(Dialog)
        self.goatBox.setGeometry(QtCore.QRect(60, 420, 451, 21))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.goatBox.setFont(font)
        self.goatBox.setObjectName("goatBox")
        self.artistInput = QtWidgets.QLineEdit(Dialog)
        self.artistInput.setGeometry(QtCore.QRect(130, 300, 371, 21))
        self.artistInput.setObjectName("artistInput")
        self.scoreInput = QtWidgets.QLineEdit(Dialog)
        self.scoreInput.setGeometry(QtCore.QRect(440, 380, 61, 21))
        self.scoreInput.setObjectName("scoreInput")
        self.durationInput = QtWidgets.QLineEdit(Dialog)
        self.durationInput.setGeometry(QtCore.QRect(140, 380, 61, 21))
        self.durationInput.setObjectName("durationInput")
        self.artist = QtWidgets.QLabel(Dialog)
        self.artist.setGeometry(QtCore.QRect(60, 300, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.artist.setFont(font)
        self.artist.setObjectName("artist")
        self.trackInput = QtWidgets.QLineEdit(Dialog)
        self.trackInput.setGeometry(QtCore.QRect(320, 380, 61, 21))
        self.trackInput.setObjectName("trackInput")
        self.recordInput = QtWidgets.QLineEdit(Dialog)
        self.recordInput.setGeometry(QtCore.QRect(120, 260, 381, 21))
        self.recordInput.setObjectName("recordInput")
        self.tracks = QtWidgets.QLabel(Dialog)
        self.tracks.setGeometry(QtCore.QRect(210, 380, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tracks.setFont(font)
        self.tracks.setObjectName("tracks")
        self.duration = QtWidgets.QLabel(Dialog)
        self.duration.setGeometry(QtCore.QRect(60, 380, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.duration.setFont(font)
        self.duration.setObjectName("duration")
        self.addTitle = QtWidgets.QLabel(Dialog)
        self.addTitle.setGeometry(QtCore.QRect(50, 160, 461, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.addTitle.setFont(font)
        self.addTitle.setObjectName("addTitle")
        self.updateDataBtn = QtWidgets.QPushButton(Dialog)
        self.updateDataBtn.setGeometry(QtCore.QRect(60, 450, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.updateDataBtn.setFont(font)
        self.updateDataBtn.setObjectName("updateDataBtn")
        self.addRecord = QtWidgets.QLabel(Dialog)
        self.addRecord.setGeometry(QtCore.QRect(60, 260, 54, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addRecord.setFont(font)
        self.addRecord.setObjectName("addRecord")
        self.grade = QtWidgets.QLabel(Dialog)
        self.grade.setGeometry(QtCore.QRect(390, 380, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.grade.setFont(font)
        self.grade.setObjectName("grade")
        self.recordLabelInput = QtWidgets.QLineEdit(Dialog)
        self.recordLabelInput.setGeometry(QtCore.QRect(160, 340, 341, 21))
        self.recordLabelInput.setObjectName("recordLabelInput")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Editar Disco"))
        self.updateBtn.setText(_translate("Dialog", "Alterar"))
        self.removeRecord.setText(_translate("Dialog", "Disco:"))
        self.removeTitle.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Qual disco deseja alterar?</span></p></body></html>"))
        self.recordLabel.setText(_translate("Dialog", "Gravadora:"))
        self.goatBox.setText(_translate("Dialog", "Melhor Disco / Banda / Artista de todos os tempos."))
        self.artist.setText(_translate("Dialog", "Artista:"))
        self.tracks.setText(_translate("Dialog", "Nº de faixas:"))
        self.duration.setText(_translate("Dialog", "Duracao:"))
        self.addTitle.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Preencha todos os campos </span></p><p align=\"center\"><span style=\" font-size:18pt;\">abaixo para alterar o disco.</span></p></body></html>"))
        self.updateDataBtn.setText(_translate("Dialog", "Substituir dados"))
        self.addRecord.setText(_translate("Dialog", "Disco:"))
        self.grade.setText(_translate("Dialog", "Nota:"))
