import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiSubWindow
from musicTracker import Ui_MainWindow
from mainTabAddRemove import AddRemoveWindow
from mainTabUpdateRecord import UpdateRecordWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionAdicionar_Remover_um_artista.triggered.connect(self.mainTabAddRemove)
        self.ui.actionEditar_disco.triggered.connect(self.mainTabUpdateRecord)

    def mainTabAddRemove(self):
        sub = QMdiSubWindow()
        addRm = AddRemoveWindow()
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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

