from PyQt5.QtWidgets import QDialog, QMessageBox
from eraseAllRecords import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError

class EraseAllRecordsWindow(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.removeAllBtn.clicked.connect(self.removeAll)

    def removeAll(self):
        sql = 'TRUNCATE TABLE metal'

        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(sql)

                msg = QMessageBox()
                msg.setWindowTitle('Sucesso')
                msg.setText('Base de dados reiniciada.')
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return
                
            except ProgrammingError as e:
                msg = QMessageBox()
                msg.setWindowTitle('Erro:')
                msg.setText(e.msg)
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return


                