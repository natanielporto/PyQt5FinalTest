from PyQt5.QtWidgets import QDialog, QMessageBox
from show_statistics_text import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError
from typing import List
import math

db_data: List[tuple] = []


class Show_statistics_text_window(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.sql_query("SELECT disco FROM metal")
        self.ui.total_records_show.setText(str(len(self.db_data)))

        self.sql_query("SELECT artista FROM metal GROUP BY artista")
        self.ui.total_artists_show.setText(str(len(self.db_data)))

        self.sql_query("SELECT gravadora FROM metal GROUP BY gravadora")
        self.ui.total_record_labels_show.setText(str(len(self.db_data)))

        self.sql_query("SELECT faixas FROM metal")
        list_tracks = list(map(lambda x: x[0], self.db_data))
        sum = 0
        for track in list_tracks:
            sum += track
        self.ui.total_tracks_sum_show.setText(str(sum))

        avg = sum / len(list_tracks)
        self.ui.average_tracks_show.setText(str(math.ceil(avg)))

        self.sql_query("SELECT MAX(nota) FROM metal")
        self.ui.best_record_score_show.setText(str(self.db_data[0][0]))

        self.sql_query("SELECT MIN(nota) FROM metal")
        self.ui.worst_score_record_show.setText(str(self.db_data[0][0]))

        self.sql_query("SELECT AVG(nota) FROM metal")
        self.ui.average_record_score_show.setText(str(self.db_data[0][0]))

        self.sql_query("SELECT MAX(duracao) FROM metal")
        self.ui.longest_record_show.setText(str(self.db_data[0][0]))

        self.sql_query("SELECT MIN(duracao) FROM metal")
        self.ui.shortest_record_show.setText(str(self.db_data[0][0]))

        self.sql_query("SELECT goat FROM metal where goat=1")
        self.ui.total_goats_show.setText(str(len(self.db_data)))

    def sql_query(self, str):
        sql = str
        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(sql)
                self.db_data = cursor.fetchall()

            except ProgrammingError as e:
                msg = QMessageBox()
                msg.setWindowTitle("Erro:")
                msg.setText("Base de dados vazia: nenhum dado para ser apresentado.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return
