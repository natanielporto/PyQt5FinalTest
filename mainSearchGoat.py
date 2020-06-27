 
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QAbstractItemView
from searchGoat import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError

class SearchGoatWindow(QDialog, Ui_Dialog):
		goats = []

		def __init__(self):
			QDialog.__init__(self)
			self.ui = Ui_Dialog()
			self.ui.setupUi(self)

			self.ui.searchBtn.clicked.connect(self.searchGoat)


		def error(self):
			msg = QMessageBox()
			msg.setWindowTitle('Erro:')
			msg.setText('Nenhum GOAT no cadastro.')
			msg.setIcon(QMessageBox.Critical)
			msg.exec_()
			return	
				
				
		def searchGoat(self):
			sql = 'SELECT artista, disco FROM metal WHERE goat=true'

			with db_connect() as db:
				try:
					cursor = db.cursor()
					cursor.execute(sql)
					self.goats = cursor.fetchall()

					if self.goats == []:
						self.error()

				except ProgrammingError as e:
					self.error()

			self.setTable()
			self.createRows(('Artista', 'Disco'), (149, 300))
			self.displayRows()

		def createRows(self, col, wdt):
			self.ui.resultTable.setColumnCount(len(col))
			self.ui.resultTable.setHorizontalHeaderLabels(col)
			for i, newWidth in enumerate(wdt):
				self.ui.resultTable.setColumnWidth(i, newWidth)


		def displayRows(self):
			self.ui.resultTable.setRowCount(len(self.goats))

			for line, label in enumerate(self.goats):
				artist = QTableWidgetItem(str(label[0]))
				self.ui.resultTable.setItem(line, 0, artist)

				record = QTableWidgetItem(str(label[1]))
				self.ui.resultTable.setItem(line, 1, record)


		def setTable(self):
			self.ui.resultTable.setSelectionBehavior(QAbstractItemView.SelectRows)
			self.ui.resultTable.setSelectionMode(QAbstractItemView.SingleSelection)
			
			self.ui.resultTable.verticalHeader().setVisible(False)
			
			self.ui.resultTable.setAlternatingRowColors(True)
			
			self.ui.resultTable.setEditTriggers(QAbstractItemView.NoEditTriggers)