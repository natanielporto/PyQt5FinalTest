from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QAbstractItemView
from searchArtist import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError

class SearchArtistWindow(QDialog, Ui_Dialog):
		records = []

		def __init__(self):
			QDialog.__init__(self)
			self.ui = Ui_Dialog()
			self.ui.setupUi(self)

			self.ui.searchBtn.clicked.connect(self.searchArtist)


		def error(self):
			msg = QMessageBox()
			msg.setWindowTitle('Erro:')
			msg.setText('Nenhum artista cadastrado com este nome.')
			msg.setIcon(QMessageBox.Critical)
			msg.exec_()
			return	
				
				
		def searchArtist(self):
			search = self.ui.searchInput.text()

			if search == '':
				sql = 'SELECT artista, disco FROM metal'
			else: 
				sql = (f'SELECT artista, disco FROM metal WHERE artista="{search}"')

			with db_connect() as db:
				try:
					cursor = db.cursor()
					cursor.execute(sql)
					self.records = cursor.fetchall()

					if self.records == []:
						self.error()

				except ProgrammingError as e:
					self.error()

			self.setTable()
			self.createRows(('Artista', 'Disco'), (150, 294))
			self.displayRows()

		def createRows(self, col, wdt):
			self.ui.resultTable.setColumnCount(len(col))
			self.ui.resultTable.setHorizontalHeaderLabels(col)
			for i, newWidth in enumerate(wdt):
				self.ui.resultTable.setColumnWidth(i, newWidth)


		def displayRows(self):
			self.ui.resultTable.setRowCount(len(self.records))
			rows = 0
			for linha, record in enumerate(self.records):
				artist = QTableWidgetItem(str(record[0]))
				self.ui.resultTable.setItem(linha, 0, artist)

				displayRecord = QTableWidgetItem(record[1])
				self.ui.resultTable.setItem(linha, 1, displayRecord)


		def setTable(self):
			self.ui.resultTable.setSelectionBehavior(QAbstractItemView.SelectRows)
			self.ui.resultTable.setSelectionMode(QAbstractItemView.SingleSelection)
			
			self.ui.resultTable.verticalHeader().setVisible(False)
			
			self.ui.resultTable.setAlternatingRowColors(True)
			
			self.ui.resultTable.setEditTriggers(QAbstractItemView.NoEditTriggers)