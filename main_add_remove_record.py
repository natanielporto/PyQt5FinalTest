from PyQt5.QtWidgets import QDialog, QMessageBox
from add_remove_record import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError


class Add_remove_record_window(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.add_btn.clicked.connect(self.add_artist)
        self.ui.remove_btn.clicked.connect(self.remove_artist)

    def add_artist(self):
        sql = "INSERT INTO metal(disco, artista, duracao, faixas, gravadora, nota, goat) VALUES (%s, %s, %s, %s, %s, %s, %s);"

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
                msg.setText("Disco adicionado com sucesso.")
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
            self.ui.goat_box.setChecked()

    def remove_artist(self):
        remove = self.ui.remove_input.text()
        sql_show = f'SELECT * FROM metal WHERE disco="{remove}"'
        sql_delete = f'DELETE FROM metal WHERE disco="{remove}"'

        if not remove:
            msg = QMessageBox()
            msg.setWindowTitle("Erro:")
            msg.setText("Preencha o campo para remover um disco.")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            return

        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(sql_show)
                if cursor.fetchall() is []:
                    msg = QMessageBox()
                    msg.setWindowTitle("Erro:")
                    msg.setText("Nenhum disco encontrado com este nome.")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    return
                else:
                    cursor.execute(sql_delete)
                    db.commit()
            except ProgrammingError as e:
                msg = QMessageBox()
                msg.setWindowTitle("Erro:")
                msg.setText(e)
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Sucesso!")
                msg.setText("Disco removido com sucesso.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return
