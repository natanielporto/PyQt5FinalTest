from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QAbstractItemView
from show_statistics_text import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError
from typing import List


class Show_statistics_text_window(QDialog, Ui_Dialog):
    db_data: List[tuple] = []

    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.sql_query("SELECT disco FROM metal")
        self.ui.total_records_show.setText(str(len(db_data)))
        print(db_data)

    def sql_query(self, new_query: str):
        sql = f"{new_query}"
        print(sql)

        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(sql)
                db_data = cursor.fetchall()

            except ProgrammingError as e:
                msg = QMessageBox()
                msg.setWindowTitle("Erro:")
                msg.setText("Base de dados vazia: nenhum dado para ser apresentado.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return
