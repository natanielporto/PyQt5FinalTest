# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicTracker.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(10, 0, 991, 811))
        self.mdiArea.setObjectName("mdiArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 22))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuPesquisar = QtWidgets.QMenu(self.menubar)
        self.menuPesquisar.setObjectName("menuPesquisar")
        self.menuEstatistica = QtWidgets.QMenu(self.menubar)
        self.menuEstatistica.setObjectName("menuEstatistica")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPor_disco = QtWidgets.QAction(MainWindow)
        self.actionPor_disco.setObjectName("actionPor_disco")
        self.actionPor_artista = QtWidgets.QAction(MainWindow)
        self.actionPor_artista.setObjectName("actionPor_artista")
        self.actionPor_gravadora = QtWidgets.QAction(MainWindow)
        self.actionPor_gravadora.setObjectName("actionPor_gravadora")
        self.actionPor_melhores = QtWidgets.QAction(MainWindow)
        self.actionPor_melhores.setObjectName("actionPor_melhores")
        self.actionPor_GOATs = QtWidgets.QAction(MainWindow)
        self.actionPor_GOATs.setObjectName("actionPor_GOATs")
        self.actionHoras_de_musica = QtWidgets.QAction(MainWindow)
        self.actionHoras_de_musica.setObjectName("actionHoras_de_musica")
        self.actionQuantidade_de_discos = QtWidgets.QAction(MainWindow)
        self.actionQuantidade_de_discos.setObjectName("actionQuantidade_de_discos")
        self.actionQuantidade_de_musicas = QtWidgets.QAction(MainWindow)
        self.actionQuantidade_de_musicas.setObjectName("actionQuantidade_de_musicas")
        self.actionQuantidade_de_gravadoras = QtWidgets.QAction(MainWindow)
        self.actionQuantidade_de_gravadoras.setObjectName(
            "actionQuantidade_de_gravadoras"
        )
        self.actionDiferentes_tipos_de_musicas = QtWidgets.QAction(MainWindow)
        self.actionDiferentes_tipos_de_musicas.setObjectName(
            "actionDiferentes_tipos_de_musicas"
        )
        self.actionAdicionar_disco = QtWidgets.QAction(MainWindow)
        self.actionAdicionar_disco.setObjectName("actionAdicionar_disco")
        self.actionRemover_disco = QtWidgets.QAction(MainWindow)
        self.actionRemover_disco.setObjectName("actionRemover_disco")
        self.actionEditar_disco = QtWidgets.QAction(MainWindow)
        self.actionEditar_disco.setObjectName("actionEditar_disco")
        self.actionApagar_todos_os_dados = QtWidgets.QAction(MainWindow)
        self.actionApagar_todos_os_dados.setObjectName("actionApagar_todos_os_dados")
        self.actionAdicionar_Remover_um_artista = QtWidgets.QAction(MainWindow)
        self.actionAdicionar_Remover_um_artista.setObjectName(
            "actionAdicionar_Remover_um_artista"
        )
        self.actionFechar = QtWidgets.QAction(MainWindow)
        self.actionFechar.setObjectName("actionFechar")
        self.actionPor_graficos = QtWidgets.QAction(MainWindow)
        self.actionPor_graficos.setObjectName("actionPor_graficos")
        self.actionPor_numeros = QtWidgets.QAction(MainWindow)
        self.actionPor_numeros.setObjectName("actionPor_numeros")
        self.menuMain.addAction(self.actionAdicionar_Remover_um_artista)
        self.menuMain.addAction(self.actionEditar_disco)
        self.menuMain.addAction(self.actionApagar_todos_os_dados)
        self.menuMain.addAction(self.actionFechar)
        self.menuPesquisar.addAction(self.actionPor_disco)
        self.menuPesquisar.addAction(self.actionPor_artista)
        self.menuPesquisar.addAction(self.actionPor_gravadora)
        self.menuPesquisar.addAction(self.actionPor_melhores)
        self.menuPesquisar.addAction(self.actionPor_GOATs)
        self.menuEstatistica.addAction(self.actionPor_graficos)
        self.menuEstatistica.addAction(self.actionPor_numeros)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuPesquisar.menuAction())
        self.menubar.addAction(self.menuEstatistica.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Tracker"))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.menuPesquisar.setTitle(_translate("MainWindow", "Pesquisar"))
        self.menuEstatistica.setTitle(_translate("MainWindow", "Estatistica"))
        self.actionPor_disco.setText(_translate("MainWindow", "Por disco"))
        self.actionPor_artista.setText(_translate("MainWindow", "Por artista"))
        self.actionPor_gravadora.setText(_translate("MainWindow", "Por gravadora"))
        self.actionPor_melhores.setText(_translate("MainWindow", "Por melhores"))
        self.actionPor_GOATs.setText(_translate("MainWindow", "Por GOATs"))
        self.actionHoras_de_musica.setText(_translate("MainWindow", "Horas de musica"))
        self.actionQuantidade_de_discos.setText(
            _translate("MainWindow", "Quantidade de discos")
        )
        self.actionQuantidade_de_musicas.setText(
            _translate("MainWindow", "Quantidade de musicas")
        )
        self.actionQuantidade_de_gravadoras.setText(
            _translate("MainWindow", "Quantidade de gravadoras")
        )
        self.actionDiferentes_tipos_de_musicas.setText(
            _translate("MainWindow", "Estatisticas em graficos")
        )
        self.actionAdicionar_disco.setText(_translate("MainWindow", "Adicionar disco"))
        self.actionRemover_disco.setText(_translate("MainWindow", "Remover um disco"))
        self.actionEditar_disco.setText(_translate("MainWindow", "Editar disco"))
        self.actionApagar_todos_os_dados.setText(
            _translate("MainWindow", "Apagar todos os dados")
        )
        self.actionAdicionar_Remover_um_artista.setText(
            _translate("MainWindow", "Adicionar/Remover disco")
        )
        self.actionFechar.setText(_translate("MainWindow", "Fechar"))
        self.actionPor_graficos.setText(_translate("MainWindow", "Por graficos"))
        self.actionPor_numeros.setText(_translate("MainWindow", "Por numeros"))