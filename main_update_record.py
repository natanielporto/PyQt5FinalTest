from PyQt5.QtWidgets import QDialog, QMessageBox
from update_record import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError
from typing import List


class Update_record_window(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.update_btn.clicked.connect(self.update_record)
        self.ui.update_data_btn.clicked.connect(self.update_artist)

    def update_record(self):
        record = str(self.ui.update_input.text())
        sql = f"""SELECT disco, artista, duracao, faixas, gravadora, nota, goat FROM metal WHERE disco = '{record}'"""

        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(sql)
                update_query = cursor.fetchall()

                if len(update_query) == 0:
                    msg = QMessageBox()
                    msg.setWindowTitle("Erro:")
                    msg.setText("Nenhum disco com este nome para ser alterado.")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    return

                self.ui.artist_input.setText(str(update_query[0][1]))
                self.ui.record_input.setText(str(update_query[0][0]))
                self.ui.track_input.setText(str(update_query[0][3]))
                self.ui.duration_input.setText(str(update_query[0][2]))
                self.ui.score_input.setText(str(update_query[0][5]))
                self.ui.record_label_input.setText(str(update_query[0][4]))
                if update_query[0][6] == "1":
                    self.ui.goat_box.toggle()

            except ProgrammingError as e:
                msg = QMessageBox()
                msg.setWindowTitle("Erro:")
                msg.setText("Nenhum disco com este nome para ser alterado.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return

    def update_artist(self):
        record = str(self.ui.update_input.text())
        artista = self.ui.artist_input.text()
        disco = self.ui.record_input.text()
        faixas = self.ui.track_input.text()
        duracao = self.ui.duration_input.text()
        nota = self.ui.score_input.text()
        gravadora = self.ui.record_label_input.text()
        goat = self.ui.goat_box.isChecked()

        goat_result = False

        if goat:
            goat_result = True

        sql = f"""UPDATE metal SET disco = '{disco}', artista = '{artista}', duracao = '{duracao}', faixas = {faixas}, gravadora = '{gravadora}', nota = {nota}, goat = {goat} WHERE disco = '{record}'"""
        print(sql)

        if (
            not artista
            or not disco
            or not faixas
            or not duracao
            or not nota
            or not gravadora
        ):
            msg = QMessageBox()
            msg.setWindowTitle("Erro:")
            msg.setText(
                "Campos disco, artista, gravadora, duração, número de faixas e nota são de preenchimento obrigatório."
            )
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            return

        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(
                    sql,
                    (disco, artista, duracao, int(faixas), gravadora, int(nota), goat),
                )
                db.commit()
            except ProgrammingError as e:
                msg = QMessageBox()
                msg.setWindowTitle("Erro:")
                msg.setText(e.msg)
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Sucesso!")
                msg.setText("Disco alterado com sucesso.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return

        self.ui.artist_input.setText("")
        self.ui.record_input.setText("")
        self.ui.track_input.setText("")
        self.ui.duration_input.setText("")
        self.ui.score_input.setText("")
        self.ui.record_label_input.setText("")

        if self.ui.goat_box.isChecked():
            self.ui.goat_box.setChecked(False)
