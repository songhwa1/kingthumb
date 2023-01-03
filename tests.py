import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
import numpy as np
from PyQt5 import uic
import os
import pymysql

form_class = uic.loadUiType("graphui.ui")[0]


class GraphWidget(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        conn = pymysql.connect(host='127.0.0.1', user='root', password='agumon200_', db='data')
        curs = conn.cursor()

        curs.execute("SELECT * FROM data.crime")

        rows1 = curs.fetchall()

        crime_sum = 0
        for row in rows1:
            print(row)
            crime_sum += row[2] + row[3] + row[4] + row[5]

        x_plot = ["범죄수 합", "지역 2", "지역 3", "지역 4", "지역 5"]
        y_plot = [crime_sum, 245, 543, 327, 356]

        x_dict = dict(enumerate(x_plot))

        ticks = [list(zip(x_dict.keys(), x_dict.values()))]

        self.graph1.plot(list(range(len(x_plot))), y_plot)

        x_bottom = self.graph1.getAxis('bottom')
        x_bottom.setTicks(ticks)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    graph = GraphWidget()
    graph.show()
    app.exec_()
