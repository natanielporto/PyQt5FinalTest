from PyQt5.QtWidgets import QDialog, QMessageBox
from erase_all_records import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError


class Erase_all_records_window(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.remove_all_btn.clicked.connect(self.remove_all)

    def remove_all(self):
        sql = "TRUNCATE TABLE metal"

        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(sql)

                msg = QMessageBox()
                msg.setWindowTitle("Sucesso")
                msg.setText("Base de dados reiniciada.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return

            except ProgrammingError as e:
                msg = QMessageBox()
                msg.setWindowTitle("Erro:")
                msg.setText(e.msg)
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return
