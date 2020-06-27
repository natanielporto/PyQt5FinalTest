import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiSubWindow
from musicTracker import Ui_MainWindow
from mainTabAddRemoveRecord import AddRemoveRecordWindow
from mainTabUpdateRecord import UpdateRecordWindow
from mainEraseAllRecords import EraseAllRecordsWindow
from mainSearchRecord import SearchRecordWindow
from mainSearchArtist import SearchArtistWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionAdicionar_Remover_um_artista.triggered.connect(self.mainTabAddRemoveRecord)
        self.ui.actionEditar_disco.triggered.connect(self.mainTabUpdateRecord)
        self.ui.actionApagar_todos_os_dados.triggered.connect(self.mainTabEraseAllRecords)
        self.ui.actionPor_disco.triggered.connect(self.mainSearchRecord)
        self.ui.actionPor_artista.triggered.connect(self.mainSearchArtist)
        
    def mainTabAddRemoveRecord(self):
        sub = QMdiSubWindow()
        addRm = AddRemoveRecordWindow()
        sub.setWidget(addRm)
        self.ui.mdiArea.addSubWindow(sub)
        sub.setFixedSize(545, 550)
        sub.show()

    def mainTabUpdateRecord(self):
        sub = QMdiSubWindow()
        updt = UpdateRecordWindow()
        sub.setWidget(updt)
        self.ui.mdiArea.addSubWindow(sub)
        sub.setFixedSize(545, 550)
        sub.show()

    def mainTabEraseAllRecords(self):
        sub = QMdiSubWindow()
        updt = EraseAllRecordsWindow()
        sub.setWidget(updt)
        self.ui.mdiArea.addSubWindow(sub)
        sub.setFixedSize(545, 550)
        sub.show()

    def mainSearchRecord(self):
        sub = QMdiSubWindow()
        updt = SearchRecordWindow()
        sub.setWidget(updt)
        self.ui.mdiArea.addSubWindow(sub)
        sub.setFixedSize(545, 550)
        sub.show()

    def mainSearchArtist(self):
        sub = QMdiSubWindow()
        updt = SearchArtistWindow()
        sub.setWidget(updt)
        self.ui.mdiArea.addSubWindow(sub)
        sub.setFixedSize(545, 550)
        sub.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

