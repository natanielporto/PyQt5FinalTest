from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QAbstractItemView
from search_record_label import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError
from typing import List


class Search_record_label_window(QDialog, Ui_Dialog):
    labels: List[tuple] = []

    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.search_btn.clicked.connect(self.search_record_label)

    def error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Erro:")
        msg.setText("Nenhuma gravadora cadastrada com este nome.")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        return

    def search_record_label(self):
        search = self.ui.search_input.text()

        if search == "":
            sql = "SELECT gravadora, artista, disco FROM metal"
        else:
            sql = f'SELECT gravadora, artista, disco FROM metal WHERE gravadora="{search}"'

        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(sql)
                self.labels = cursor.fetchall()

                if self.labels == []:
                    self.error()

            except ProgrammingError as e:
                self.error()

        self.set_table()
        self.create_rows(("Gravadora", "Artista", "Disco"), (130, 130, 200))
        self.display_rows()

    def create_rows(self, col, wdt):
        self.ui.result_table.setColumnCount(len(col))
        self.ui.result_table.setHorizontalHeaderLabels(col)
        for i, new_width in enumerate(wdt):
            self.ui.result_table.setColumnWidth(i, new_width)

    def display_rows(self):
        self.ui.result_table.setRowCount(len(self.labels))

        for line, label in enumerate(self.labels):
            display_label = QTableWidgetItem(str(label[0]))
            self.ui.result_table.setItem(line, 0, display_label)

            artist = QTableWidgetItem(str(label[1]))
            self.ui.result_table.setItem(line, 1, artist)

            record = QTableWidgetItem(str(label[2]))
            self.ui.result_table.setItem(line, 2, record)

    def set_table(self):
        self.ui.result_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.result_table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.ui.result_table.verticalHeader().setVisible(False)

        self.ui.result_table.setAlternatingRowColors(True)

        self.ui.result_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
