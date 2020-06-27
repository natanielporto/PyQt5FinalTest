 
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QAbstractItemView
from searchTop import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError

class SearchTopWindow(QDialog, Ui_Dialog):
    top = []

    def __init__(self):
      QDialog.__init__(self)
      self.ui = Ui_Dialog()
      self.ui.setupUi(self)

      self.ui.searchBtn.clicked.connect(self.searchTop)


    def error(self):
      msg = QMessageBox()
      msg.setWindowTitle('Erro:')
      msg.setText('Nenhum disco cadastrado.')
      msg.setIcon(QMessageBox.Critical)
      msg.exec_()
      return	
        
        
    def searchTop(self):
      

      if self.ui.radioSeven.isChecked():
        sql = 'SELECT nota, artista, disco FROM metal WHERE nota >= 7 ORDER BY nota ASC'
      elif self.ui.radioEight.isChecked():
        sql = 'SELECT nota, artista, disco FROM metal WHERE nota >= 8 ORDER BY nota ASC'
      elif self.ui.radioNine.isChecked():
        sql = 'SELECT nota, artista, disco FROM metal WHERE nota >= 9 ORDER BY nota ASC'
      elif self.ui.radioTen.isChecked():
        sql = 'SELECT nota, artista, disco FROM metal WHERE nota = 10'
      else:
        sql = 'SELECT nota, artista, disco FROM metal ORDER BY nota DESC'

      with db_connect() as db:
        try:
          cursor = db.cursor()
          cursor.execute(sql)
          self.top = cursor.fetchall()

          if self.top == []:
            self.error()

        except ProgrammingError as e:
          self.error()

      self.setTable()
      self.createRows(('nota', 'Artista', 'Disco'), (60, 130, 200))
      self.displayRows()

    def createRows(self, col, wdt):
      self.ui.resultTable.setColumnCount(len(col))
      self.ui.resultTable.setHorizontalHeaderLabels(col)
      for i, newWidth in enumerate(wdt):
        self.ui.resultTable.setColumnWidth(i, newWidth)


    def displayRows(self):
      self.ui.resultTable.setRowCount(len(self.top))

      for line, rank in enumerate(self.top):
        displayBest = QTableWidgetItem(str(rank[0]))
        self.ui.resultTable.setItem(line, 0, displayBest)
        
        artist = QTableWidgetItem(str(rank[1]))
        self.ui.resultTable.setItem(line, 1, artist)

        record = QTableWidgetItem(str(rank[2]))
        self.ui.resultTable.setItem(line, 2, record)


    def setTable(self):
      self.ui.resultTable.setSelectionBehavior(QAbstractItemView.SelectRows)
      self.ui.resultTable.setSelectionMode(QAbstractItemView.SingleSelection)
      
      self.ui.resultTable.verticalHeader().setVisible(False)
      
      self.ui.resultTable.setAlternatingRowColors(True)
      
      self.ui.resultTable.setEditTriggers(QAbstractItemView.NoEditTriggers)