from PyQt5.QtWidgets import QDialog, QMessageBox
from addRemoveRecords import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError

class AddRemoveWindow(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.addBtn.clicked.connect(self.addArtist)
        self.ui.removeBtn.clicked.connect(self.removeArtist)

    def addArtist(self):
        sql = 'INSERT INTO metal(disco, artista, duracao, faixas, gravadora, nota, goat) VALUES (%s, %s, %s, %s, %s, %s, %s);'

        artista = self.ui.artistInput.text()
        disco = self.ui.recordInput.text()
        faixas = self.ui.trackInput.text()
        duracao = self.ui.durationInput.text()
        nota = self.ui.scoreInput.text()
        gravadora = self.ui.recordLabelInput.text()
        goat = self.ui.goatBox.isChecked()

        goatResult = False

        if goat:
            goatResult = True

        if not artista or not disco or not faixas or not duracao or not nota or not gravadora:
            msg = QMessageBox()
            msg.setWindowTitle('Erro:')
            msg.setText(
                'Campos disco, artista, gravadora, duração, número de faixas e nota são de preenchimento obrigatório.')
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            return

        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(sql, (disco, artista, duracao, int(faixas), gravadora, int(nota), goat))
                db.commit()
            except ProgrammingError as e:
                msg = QMessageBox()
                msg.setWindowTitle('Erro:')
                msg.setText(e.msg)
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return
            else:
                msg = QMessageBox()
                msg.setWindowTitle('Sucesso!')
                msg.setText('Disco adicionado com sucesso.')
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return

        self.ui.artistInput.setText('')
        self.ui.recordInput.setText('')
        self.ui.trackInput.setText('')
        self.ui.durationInput.setText('')
        self.ui.scoreInput.setText('')
        self.ui.recordLabelInput.setText('')
        
        if self.ui.goatBox.isChecked():
            self.ui.goatBox.setChecked()


    def removeArtist(self):
        remove = self.ui.removeInput.text()
        sqlShow = (f'SELECT * FROM metal WHERE disco="{remove}"')
        sqlDelete = (f'DELETE FROM metal WHERE disco="{remove}"')


        if not remove:    
            msg = QMessageBox()
            msg.setWindowTitle('Erro:')
            msg.setText(
                'Preencha o campo para remover um disco.')
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            return


        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(sqlShow)
                if cursor.fetchall() is []:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Nenhum disco encontrado com este nome.')
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
                    return
                else:
                    cursor.execute(sqlDelete)
                    db.commit()
            except ProgrammingError as e:
                msg = QMessageBox()
                msg.setWindowTitle('Erro:')
                # msg.setText('Disco não encontrado. Tente novamente.')
                msg.setText(e)
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return
            else:
                msg = QMessageBox()
                msg.setWindowTitle('Sucesso!')
                msg.setText('Disco removido com sucesso.')
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return
