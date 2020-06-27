 
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QAbstractItemView
from searchRecordLabel import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError

class SearchRecordLabelWindow(QDialog, Ui_Dialog):
		labels = []

		def __init__(self):
			QDialog.__init__(self)
			self.ui = Ui_Dialog()
			self.ui.setupUi(self)

			self.ui.searchBtn.clicked.connect(self.searchRecordLabel)


		def error(self):
			msg = QMessageBox()
			msg.setWindowTitle('Erro:')
			msg.setText('Nenhuma gravadora cadastrada com este nome.')
			msg.setIcon(QMessageBox.Critical)
			msg.exec_()
			return	
				
				
		def searchRecordLabel(self):
			search = self.ui.searchInput.text()

			if search == '':
				sql = 'SELECT gravadora, artista, disco FROM metal'
			else: 
				sql = (f'SELECT gravadora, artista, disco FROM metal WHERE gravadora="{search}"')

			with db_connect() as db:
				try:
					cursor = db.cursor()
					cursor.execute(sql)
					self.labels = cursor.fetchall()

					if self.labels == []:
						self.error()

				except ProgrammingError as e:
					self.error()

			self.setTable()
			self.createRows(('Gravadora', 'Artista', 'Disco'), (130, 130, 200))
			self.displayRows()

		def createRows(self, col, wdt):
			self.ui.resultTable.setColumnCount(len(col))
			self.ui.resultTable.setHorizontalHeaderLabels(col)
			for i, newWidth in enumerate(wdt):
				self.ui.resultTable.setColumnWidth(i, newWidth)


		def displayRows(self):
			self.ui.resultTable.setRowCount(len(self.labels))

			for line, label in enumerate(self.labels):
				displayLabel = QTableWidgetItem(str(label[0]))
				self.ui.resultTable.setItem(line, 0, displayLabel)
        
				artist = QTableWidgetItem(str(label[1]))
				self.ui.resultTable.setItem(line, 1, artist)

				record = QTableWidgetItem(str(label[2]))
				self.ui.resultTable.setItem(line, 2, record)


		def setTable(self):
			self.ui.resultTable.setSelectionBehavior(QAbstractItemView.SelectRows)
			self.ui.resultTable.setSelectionMode(QAbstractItemView.SingleSelection)
			
			self.ui.resultTable.verticalHeader().setVisible(False)
			
			self.ui.resultTable.setAlternatingRowColors(True)
			
			self.ui.resultTable.setEditTriggers(QAbstractItemView.NoEditTriggers)