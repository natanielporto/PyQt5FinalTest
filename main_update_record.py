from PyQt5.QtWidgets import QDialog, QMessageBox
from update_record import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError
from typing import List

update_query: List[tuple] = []


class Update_record_window(QDialog, Ui_Dialog):
    
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.update_btn.clicked.connect(self.update_record)

    def update_record(self):
        record = str(self.ui.update_input.text())
        sql = (f'SELECT * FROM metal WHERE disco = "{record}"')

        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(sql)
                self.update_query = cursor.fetchall()
                self.ui.artist_input.setText(str(self.update_query[2]))
                self.ui.record_input.setText(str(self.update_query[1]))
                self.ui.track_input.setText(str(self.update_query[4]))
                self.ui.duration_input.setText(str(self.update_query[3]))
                self.ui.score_input.setText(str(self.update_query[6]))
                self.ui.record_label_input.setText(str(self.update_query[5]))
                if self.update_query[7] == 1:
                    self.ui.goat_box.isChecked(True)


                if len(self.update_query) == 0:
                    msg = QMessageBox()
                    msg.setWindowTitle("Erro:")
                    msg.setText("Nenhum disco com este nome para ser alterado.")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    return

            except ProgrammingError as e:
                msg = QMessageBox()
                msg.setWindowTitle("Erro:")
                msg.setText("Nenhum disco com este nome para ser alterado.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return
        

    # with db_connect() as db:
    #     try:
    #         cursor = db.cursor()
    #         cursor.execute(sql)
    #         self.ui.artistInput.setText(sql.artist)
    #         self.ui.recordInput.setText(sql.record)
    #         self.ui.recordLabelInput.setText(sql.label)
    #         self.ui.durationInput.setText(sql.duration)
    #         self.ui.trackInput.setText(sql.track)
    #         self.ui.scoreInput.setText(sql.score)
