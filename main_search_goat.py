from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QAbstractItemView
from search_goat import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError
from typing import List


class Search_goat_window(QDialog, Ui_Dialog):
    goats: List[tuple] = []

    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.search_btn.clicked.connect(self.search_goat)

    def error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Erro:")
        msg.setText("Nenhum GOAT no cadastro.")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        return

    def search_goat(self):
        sql = "SELECT artista, disco FROM metal WHERE goat=true"

        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(sql)
                self.goats = cursor.fetchall()

                if self.goats == []:
                    self.error()

            except ProgrammingError as e:
                self.error()

        self.set_table()
        self.create_rows(("Artista", "Disco"), (149, 300))
        self.display_rows()

    def create_rows(self, col, wdt):
        self.ui.result_table.setColumnCount(len(col))
        self.ui.result_table.setHorizontalHeaderLabels(col)
        for i, new_width in enumerate(wdt):
            self.ui.result_table.setColumnWidth(i, new_width)

    def display_rows(self):
        self.ui.result_table.setRowCount(len(self.goats))

        for line, label in enumerate(self.goats):
            artist = QTableWidgetItem(str(label[0]))
            self.ui.result_table.setItem(line, 0, artist)

            record = QTableWidgetItem(str(label[1]))
            self.ui.result_table.setItem(line, 1, record)

    def set_table(self):
        self.ui.result_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.result_table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.ui.result_table.verticalHeader().setVisible(False)

        self.ui.result_table.setAlternatingRowColors(True)

        self.ui.result_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
