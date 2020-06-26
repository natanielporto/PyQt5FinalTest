from PyQt5.QtWidgets import QDialog, QMessageBox
from searchRecord import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError

class SearchRecordWindow(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.searchBtn.clicked.connect(self.searchRecord)

    def searchRecord(self):
        search = self.ui.searchInput.text()

        sql = (f'SELECT * FROM metal WHERE disco = {search}')

        print(sql)
        print(search)

        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(sql)
                
            except ProgrammingError as e:
                msg = QMessageBox()
                msg.setWindowTitle('Erro:')
                msg.setText('Nenhum cadastro foi encontrado com este nome.')
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return
