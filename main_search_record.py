from PyQt5.QtWidgets import QDialog, QMessageBox
from search_record import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError


class Search_record_window(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.search_btn.clicked.connect(self.search_record)

    def search_record(self):
        record = str(self.ui.search_input.text())
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

                self.ui.artist_show.setText(str(update_query[0][1]))
                self.ui.record_show.setText(str(update_query[0][0]))
                self.ui.track_show.setText(str(update_query[0][3]))
                self.ui.duration_show.setText(str(update_query[0][2]))
                self.ui.score_show.setText(str(update_query[0][5]))
                self.ui.record_label_show.setText(str(update_query[0][4]))
                if update_query[0][6] == "1":
                    self.ui.goat_box.toggle()

            except ProgrammingError as e:
                msg = QMessageBox()
                msg.setWindowTitle("Erro:")
                msg.setText("Nenhum disco com foi encontrado.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return