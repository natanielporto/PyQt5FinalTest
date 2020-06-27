from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QAbstractItemView
from search_top import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError
from typing import List


class Search_top_window(QDialog, Ui_Dialog):
    top: List[tuple] = []

    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.search_btn.clicked.connect(self.search_top)

    def error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Erro:")
        msg.setText("Nenhum disco cadastrado.")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        return

    def search_top(self):

        if self.ui.radio_seven.isChecked():
            sql = "SELECT nota, artista, disco FROM metal WHERE nota >= 7 ORDER BY nota ASC"
        elif self.ui.radio_eight.isChecked():
            sql = "SELECT nota, artista, disco FROM metal WHERE nota >= 8 ORDER BY nota ASC"
        elif self.ui.radio_nine.isChecked():
            sql = "SELECT nota, artista, disco FROM metal WHERE nota >= 9 ORDER BY nota ASC"
        elif self.ui.radio_ten.isChecked():
            sql = "SELECT nota, artista, disco FROM metal WHERE nota = 10"
        else:
            sql = "SELECT nota, artista, disco FROM metal ORDER BY nota DESC"

        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(sql)
                self.top = cursor.fetchall()

                if self.top == []:
                    self.error()

            except ProgrammingError as e:
                self.error()

        self.set_table()
        self.create_rows(("Nota", "Artista", "Disco"), (60, 130, 245))
        self.display_rows()

    def create_rows(self, col, wdt):
        self.ui.result_table.setColumnCount(len(col))
        self.ui.result_table.setHorizontalHeaderLabels(col)
        for i, new_width in enumerate(wdt):
            self.ui.result_table.setColumnWidth(i, new_width)

    def display_rows(self):
        self.ui.result_table.setRowCount(len(self.top))

        for line, rank in enumerate(self.top):
            display_best = QTableWidgetItem(str(rank[0]))
            self.ui.result_table.setItem(line, 0, display_best)

            artist = QTableWidgetItem(str(rank[1]))
            self.ui.result_table.setItem(line, 1, artist)

            record = QTableWidgetItem(str(rank[2]))
            self.ui.result_table.setItem(line, 2, record)

    def set_table(self):
        self.ui.result_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.result_table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.ui.result_table.verticalHeader().setVisible(False)

        self.ui.result_table.setAlternatingRowColors(True)

        self.ui.result_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
