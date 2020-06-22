from PyQt5.QtWidgets import QDialog, QMessageBox
from updateRecord import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError

class UpdateRecordWindow(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.updateBtn.clicked.connect(self.updateRecord)
        # self.ui.updateDataBtn.clicked.connect(self.updateDataRecord)

    def updateRecord(self):
        record = self.ui.updateInput.text()
        sql = 'SELECT * FROM metal WHERE record LIKE "${record}"'

        sql = 'SELECT artist, record, tracks, duration, rate, label, goat FROM metal WHERE record LIKE "${record}"'
        # sql = 'SELECT INTO metal(artist, record, tracks, duration, rate, label, goat) VALUES (%s, %s, %s, %s, %s, %s, %s);'

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