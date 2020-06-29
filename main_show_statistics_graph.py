from PyQt5.QtWidgets import QDialog
from show_statistics_graph import Ui_Dialog
from banco import db_connect
from mysql.connector.errors import ProgrammingError
from typing import List
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
from pandas import *

from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *


class Show_statistics_graph_window(QDialog, Ui_Dialog):
    graph: List[tuple] = []

    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.load_graph()

        self.ui.by_artist.clicked.connect(self.graph_by_artist)
        self.ui.by_label.clicked.connect(self.graph_by_label)
        self.ui.by_goat.clicked.connect(self.graph_by_goat)

    def load_graph(self):
        sql = "SELECT disco, artista, duracao, faixas, gravadora, nota, goat FROM metal"

        with db_connect() as db:
            try:
                cursor = db.cursor()
                cursor.execute(sql)
                self.graph = cursor.fetchall()
            except ProgrammingError as e:
                msg = QMessageBox()
                msg.setWindowTitle("Erro:")
                msg.setText("Dados insuficientes para exibir o gráfico.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                return

    def graph_by_artist(self):
        arq = open("graph_by_artist.html", "w", encoding="utf-8")
        arq.write(
            self.display_top_graph()
            + self.display_graph_3d()
            + self.display_bottom_graph_3d()
        )
        arq.close()

        self.ui.graph.load(
            QUrl(
                r"file:///media/nataniel/HD_grande_3/Tudo%20de%20programa%C3%A7%C3%A3o/Senac/Algor%C3%ADtmos%20e%20Programa%C3%A7%C3%A3o%20II/PyQtTrabalhoFinal/graph_by_artist.html"
            )
        )

    def graph_by_label(self):
        arq = open("graph_by_label.html", "w", encoding="utf-8")
        arq.write(
            self.display_top_graph()
            + self.display_graph_slice()
            + self.display_bottom_graph_slice()
        )
        arq.close()

        self.ui.graph.load(
            QUrl(
                r"file:///media/nataniel/HD_grande_3/Tudo%20de%20programa%C3%A7%C3%A3o/Senac/Algor%C3%ADtmos%20e%20Programa%C3%A7%C3%A3o%20II/PyQtTrabalhoFinal/graph_by_label.html"
            )
        )

    def graph_by_goat(self):
        arq = open("graph_by_goat.html", "w", encoding="utf-8")
        arq.write(
            self.display_top_graph()
            + self.display_graph_donut()
            + self.display_bottom_graph_donut()
        )
        arq.close()

        self.ui.graph.load(
            QUrl(
                r"file:///media/nataniel/HD_grande_3/Tudo%20de%20programa%C3%A7%C3%A3o/Senac/Algor%C3%ADtmos%20e%20Programa%C3%A7%C3%A3o%20II/PyQtTrabalhoFinal/graph_by_goat.html"
            )
        )

    def display_top_graph(self):
        return """<html>
    <head>
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">
            google.charts.load("current", {packages:["corechart"]});
            google.charts.setOnLoadCallback(drawChart);"""

    def display_graph_3d(self):
        list1 = list(map(lambda x: x[1], self.graph))
        list2 = pandas.DataFrame(list1, columns=["Artista"])
        list3 = list2.groupby("Artista").Artista.count()

        all_data = ""
        for artista in zip(list3.index, list3):
            all_data += f"['{artista[0]}', {artista[1]}],"

        data = """
        function drawChart() {
        var data = google.visualization.arrayToDataTable([
            ['Artistas', 'Nº de discos'],
        """
        return data + all_data + "]);"

    def display_graph_slice(self):
        list1 = list(map(lambda x: x[4], self.graph))
        list2 = pandas.DataFrame(list1, columns=["Gravadora"])
        list3 = list2.groupby("Gravadora").Gravadora.count()

        all_data = ""
        for gravadora in zip(list3.index, list3):
            all_data += f"['{gravadora[0]}', {gravadora[1]}],"

        data = """
        function drawChart() {
        var data = google.visualization.arrayToDataTable([
            ['Gravadora', 'Nº de artistas'],
        """
        return data + all_data + "]);"

    def display_graph_donut(self):
        list1 = list(map(lambda x: x[6], self.graph))
        list2 = pandas.DataFrame(list1, columns=["GOAT"])
        list3 = list2.groupby("GOAT").GOAT.count()

        all_data = ""
        for goat in zip(list3.index, list3):
            all_data += f"['{goat[0]}', {goat[1]}],"

        data = """
        function drawChart() {
        var data = google.visualization.arrayToDataTable([
            ['GOAT', 'Nº de discos'],
        """
        return data + all_data + "]);"

    def display_bottom_graph_3d(self):
        return """
            var options = {
              title: 'Gráfico de número de discos por banda.',
              is3D: true,
            };

            var chart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
            chart.draw(data, options);
        }
        </script>
        </head>
    <body>
        <div id="piechart_3d" style="width: 452px; height: 335px;"></div>
    </body>
    </html>"""

    def display_bottom_graph_donut(self):
        return """
            var options = {
              title: 'Gráfico com os melhores discos que você já ouviu até hoje.',
              pieHole: 0.2,

            };

            var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
            chart.draw(data, options);
        }
        </script>
        </head>
    <body>
        <div id="donutchart" style="width: 452px; height: 335px;"></div>
    </body>
    </html>"""

    def display_bottom_graph_slice(self):
        return """
            var options = {
              title: 'Gráfico de número de artistas por gravadora.',
              legend: 'none',
              pieSliceText: 'label',
              slices: {  2: {offset: 0.3},
                         4: {offset: 0.1},
                         6: {offset: 0.2},
              },
            };

            var chart = new google.visualization.PieChart(document.getElementById('piechart'));
            chart.draw(data, options);
        }
        </script>
        </head>
    <body>
        <div id="piechart" style="width: 452px; height: 335px;"></div>
    </body>
    </html>"""
