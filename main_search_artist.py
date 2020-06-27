from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QAbstractItemView
from search_artist import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError
from typing import List


class Search_artist_window(QDialog, Ui_Dialog):
    records: List[tuple] = []

    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.search_btn.clicked.connect(self.search_artist)

    some_dict = ["me", "myself", "you", "notI", 4040402402, "sure"]

    def error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Erro:")
        msg.setText("Nenhum artista cadastrado com este nome.")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        return

    def search_artist(self):
        search = self.ui.search_input.text()

        if search == "":
            sql = "SELECT artista, disco FROM metal"
        else:
            sql = f'SELECT artista, disco FROM metal WHERE artista="{search}"'

        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(sql)
                self.records = cursor.fetchall()

                if self.records == []:
                    self.error()

            except ProgrammingError as e:
                self.error()

        self.set_table()
        self.create_rows(("Artista", "Disco"), (150, 294))
        self.display_rows()

    def create_rows(self, col, wdt):
        self.ui.result_table.setColumnCount(len(col))
        self.ui.result_table.setHorizontalHeaderLabels(col)
        for i, new_width in enumerate(wdt):
            self.ui.result_table.setColumnWidth(i, new_width)

    def display_rows(self):
        self.ui.result_table.setRowCount(len(self.records))

        for line, record in enumerate(self.records):
            artist = QTableWidgetItem(str(record[0]))
            self.ui.result_table.setItem(line, 0, artist)

            display_record = QTableWidgetItem(str(record[1]))
            self.ui.result_table.setItem(line, 1, display_record)

    def set_table(self):
        self.ui.result_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.result_table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.ui.result_table.verticalHeader().setVisible(False)

        self.ui.result_table.setAlternatingRowColors(True)

        self.ui.result_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
