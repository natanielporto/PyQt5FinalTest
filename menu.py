import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiSubWindow
from music_tracker import Ui_MainWindow
from main_add_remove_record import Add_remove_record_window
from main_update_record import Update_record_window
from main_erase_all_records import Erase_all_records_window
from main_search_record import Search_record_window
from main_search_artist import Search_artist_window
from main_search_record_label import Search_record_label_window
from main_search_top import Search_top_window
from main_search_goat import Search_goat_window
from main_show_statistics_text import Show_statistics_text_window
from main_show_statistics_graph import Show_statistics_graph_window


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionAdicionar_Remover_um_artista.triggered.connect(
            self.main_add_remove_record
        )
        self.ui.actionEditar_disco.triggered.connect(self.main_update_record)
        self.ui.actionApagar_todos_os_dados.triggered.connect(
            self.main_erase_all_records
        )
        self.ui.actionPor_disco.triggered.connect(self.main_search_record)
        self.ui.actionPor_artista.triggered.connect(self.main_search_artist)
        self.ui.actionPor_gravadora.triggered.connect(self.main_search_record_label)
        self.ui.actionPor_melhores.triggered.connect(self.main_search_top)
        self.ui.actionPor_GOATs.triggered.connect(self.main_search_goat)
        self.ui.actionPor_numeros.triggered.connect(self.main_show_statistics_text)
        self.ui.actionPor_graficos.triggered.connect(self.main_show_statistics_graph)

    def main_add_remove_record(self):
        sub = QMdiSubWindow()
        add_rm = Add_remove_record_window()
        sub.setWidget(add_rm)
        self.ui.mdiArea.addSubWindow(sub)
        sub.setFixedSize(545, 550)
        sub.show()

    def main_update_record(self):
        sub = QMdiSubWindow()
        updt = Update_record_window()
        sub.setWidget(updt)
        self.ui.mdiArea.addSubWindow(sub)
        sub.setFixedSize(545, 550)
        sub.show()

    def main_erase_all_records(self):
        sub = QMdiSubWindow()
        updt = Erase_all_records_window()
        sub.setWidget(updt)
        self.ui.mdiArea.addSubWindow(sub)
        sub.setFixedSize(545, 550)
        sub.show()

    def main_search_record(self):
        sub = QMdiSubWindow()
        updt = Search_record_window()
        sub.setWidget(updt)
        self.ui.mdiArea.addSubWindow(sub)
        sub.setFixedSize(545, 550)
        sub.show()

    def main_search_artist(self):
        sub = QMdiSubWindow()
        updt = Search_artist_window()
        sub.setWidget(updt)
        self.ui.mdiArea.addSubWindow(sub)
        sub.setFixedSize(545, 550)
        sub.show()

    def main_search_record_label(self):
        sub = QMdiSubWindow()
        updt = Search_record_label_window()
        sub.setWidget(updt)
        self.ui.mdiArea.addSubWindow(sub)
        sub.setFixedSize(545, 550)
        sub.show()

    def main_search_top(self):
        sub = QMdiSubWindow()
        updt = Search_top_window()
        sub.setWidget(updt)
        self.ui.mdiArea.addSubWindow(sub)
        sub.setFixedSize(545, 550)
        sub.show()

    def main_search_goat(self):
        sub = QMdiSubWindow()
        updt = Search_goat_window()
        sub.setWidget(updt)
        self.ui.mdiArea.addSubWindow(sub)
        sub.setFixedSize(545, 550)
        sub.show()

    def main_show_statistics_text(self):
        sub = QMdiSubWindow()
        updt = Show_statistics_text_window()
        sub.setWidget(updt)
        self.ui.mdiArea.addSubWindow(sub)
        sub.setFixedSize(545, 550)
        sub.show()

    def main_show_statistics_graph(self):
        sub = QMdiSubWindow()
        updt = Show_statistics_graph_window()
        sub.setWidget(updt)
        self.ui.mdiArea.addSubWindow(sub)
        sub.setFixedSize(545, 550)
        sub.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
