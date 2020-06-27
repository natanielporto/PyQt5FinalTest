# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showStatisticsText.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(542, 525)
        self.total_records = QtWidgets.QLabel(Dialog)
        self.total_records.setGeometry(QtCore.QRect(80, 60, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.total_records.setFont(font)
        self.total_records.setObjectName("total_records")
        self.total_records_show = QtWidgets.QLineEdit(Dialog)
        self.total_records_show.setGeometry(QtCore.QRect(390, 70, 71, 21))
        self.total_records_show.setObjectName("total_records_show")
        self.main_title = QtWidgets.QLabel(Dialog)
        self.main_title.setGeometry(QtCore.QRect(100, 10, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.main_title.setFont(font)
        self.main_title.setObjectName("main_title")
        self.total_artists_show = QtWidgets.QLineEdit(Dialog)
        self.total_artists_show.setGeometry(QtCore.QRect(390, 110, 71, 21))
        self.total_artists_show.setObjectName("total_artists_show")
        self.total_artists = QtWidgets.QLabel(Dialog)
        self.total_artists.setGeometry(QtCore.QRect(80, 100, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.total_artists.setFont(font)
        self.total_artists.setObjectName("total_artists")
        self.total_record_labels_show = QtWidgets.QLineEdit(Dialog)
        self.total_record_labels_show.setGeometry(QtCore.QRect(390, 150, 71, 21))
        self.total_record_labels_show.setObjectName("total_record_labels_show")
        self.total_record_labels = QtWidgets.QLabel(Dialog)
        self.total_record_labels.setGeometry(QtCore.QRect(80, 140, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.total_record_labels.setFont(font)
        self.total_record_labels.setObjectName("total_record_labels")
        self.total_tracks_sum_show = QtWidgets.QLineEdit(Dialog)
        self.total_tracks_sum_show.setGeometry(QtCore.QRect(390, 190, 71, 21))
        self.total_tracks_sum_show.setObjectName("total_tracks_sum_show")
        self.total_tracks_sum = QtWidgets.QLabel(Dialog)
        self.total_tracks_sum.setGeometry(QtCore.QRect(80, 180, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.total_tracks_sum.setFont(font)
        self.total_tracks_sum.setObjectName("total_tracks_sum")
        self.average_tracks = QtWidgets.QLabel(Dialog)
        self.average_tracks.setGeometry(QtCore.QRect(80, 220, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.average_tracks.setFont(font)
        self.average_tracks.setObjectName("average_tracks")
        self.average_tracks_show = QtWidgets.QLineEdit(Dialog)
        self.average_tracks_show.setGeometry(QtCore.QRect(390, 230, 71, 21))
        self.average_tracks_show.setObjectName("average_tracks_show")
        self.worst_score_record_show = QtWidgets.QLineEdit(Dialog)
        self.worst_score_record_show.setGeometry(QtCore.QRect(390, 310, 71, 21))
        self.worst_score_record_show.setObjectName("worst_score_record_show")
        self.worst_score_record = QtWidgets.QLabel(Dialog)
        self.worst_score_record.setGeometry(QtCore.QRect(80, 300, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.worst_score_record.setFont(font)
        self.worst_score_record.setObjectName("worst_score_record")
        self.best_record_score_show = QtWidgets.QLineEdit(Dialog)
        self.best_record_score_show.setGeometry(QtCore.QRect(390, 270, 71, 21))
        self.best_record_score_show.setObjectName("best_record_score_show")
        self.best_record_score = QtWidgets.QLabel(Dialog)
        self.best_record_score.setGeometry(QtCore.QRect(80, 260, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.best_record_score.setFont(font)
        self.best_record_score.setObjectName("best_record_score")
        self.average_record_score = QtWidgets.QLabel(Dialog)
        self.average_record_score.setGeometry(QtCore.QRect(80, 340, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.average_record_score.setFont(font)
        self.average_record_score.setObjectName("average_record_score")
        self.average_record_score_show = QtWidgets.QLineEdit(Dialog)
        self.average_record_score_show.setGeometry(QtCore.QRect(390, 350, 71, 21))
        self.average_record_score_show.setObjectName("average_record_score_show")
        self.longest_record_show = QtWidgets.QLineEdit(Dialog)
        self.longest_record_show.setGeometry(QtCore.QRect(390, 390, 71, 21))
        self.longest_record_show.setObjectName("longest_record_show")
        self.longest_record = QtWidgets.QLabel(Dialog)
        self.longest_record.setGeometry(QtCore.QRect(80, 380, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.longest_record.setFont(font)
        self.longest_record.setObjectName("longest_record")
        self.total_goats_show = QtWidgets.QLineEdit(Dialog)
        self.total_goats_show.setGeometry(QtCore.QRect(390, 470, 71, 21))
        self.total_goats_show.setObjectName("total_goats_show")
        self.total_goats = QtWidgets.QLabel(Dialog)
        self.total_goats.setGeometry(QtCore.QRect(80, 460, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.total_goats.setFont(font)
        self.total_goats.setObjectName("total_goats")
        self.shortest_record_show = QtWidgets.QLineEdit(Dialog)
        self.shortest_record_show.setGeometry(QtCore.QRect(390, 430, 71, 21))
        self.shortest_record_show.setObjectName("shortest_record_show")
        self.shortestRecord = QtWidgets.QLabel(Dialog)
        self.shortestRecord.setGeometry(QtCore.QRect(80, 420, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.shortestRecord.setFont(font)
        self.shortestRecord.setObjectName("shortestRecord")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Procurar Disco"))
        self.total_records.setText(
            _translate(
                "Dialog", "<html><head/><body><p>Total de discos:</p></body></html>"
            )
        )
        self.main_title.setText(
            _translate(
                "Dialog",
                '<html><head/><body><p align="center">Estatisticas do programa:</p></body></html>',
            )
        )
        self.total_artists.setText(
            _translate(
                "Dialog", "<html><head/><body><p>Total de artistas:</p></body></html>"
            )
        )
        self.total_record_labels.setText(
            _translate(
                "Dialog", "<html><head/><body><p>Total de gravadoras:</p></body></html>"
            )
        )
        self.total_tracks_sum.setText(
            _translate(
                "Dialog",
                "<html><head/><body><p>Total de faixas somadas:</p></body></html>",
            )
        )
        self.average_tracks.setText(
            _translate(
                "Dialog",
                "<html><head/><body><p>Media de musicas por disco:</p></body></html>",
            )
        )
        self.worst_score_record.setText(
            _translate(
                "Dialog",
                "<html><head/><body><p>Pior nota de um disco:</p></body></html>",
            )
        )
        self.best_record_score.setText(
            _translate(
                "Dialog",
                "<html><head/><body><p>Melhor nota de um disco:</p></body></html>",
            )
        )
        self.average_record_score.setText(
            _translate(
                "Dialog",
                "<html><head/><body><p>Media de todas as notas:</p></body></html>",
            )
        )
        self.longest_record.setText(
            _translate(
                "Dialog",
                "<html><head/><body><p>Disco com a maior duraçao:</p></body></html>",
            )
        )
        self.total_goats.setText(
            _translate(
                "Dialog", "<html><head/><body><p>Quantidade de GOATs:</p></body></html>"
            )
        )
        self.shortestRecord.setText(
            _translate(
                "Dialog",
                "<html><head/><body><p>Disco com a menor duraçao:</p></body></html>",
            )
        )
