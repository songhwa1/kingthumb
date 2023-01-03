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

        curs.execute("SELECT * FROM data.crime where office like '서울%'")
        rows = curs.fetchall()
        seoul_sum = 0
        for row in rows:
            print(row)
            seoul_sum += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '부산%'")
        rows = curs.fetchall()
        busan_sum = 0
        for row in rows:
            print(row)
            busan_sum += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '대구%'")
        rows = curs.fetchall()
        daegu_sum = 0
        for row in rows:
            print(row)
            daegu_sum += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '인천%'")
        rows = curs.fetchall()
        incheon_sum = 0
        for row in rows:
            print(row)
            incheon_sum += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '광주%'")
        rows = curs.fetchall()
        gwangju_sum = 0
        for row in rows:
            print(row)
            gwangju_sum += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '대전%'")
        rows = curs.fetchall()
        daejeon_sum = 0
        for row in rows:
            print(row)
            daejeon_sum += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '울산%'")
        rows = curs.fetchall()
        ulsan_sum = 0
        for row in rows:
            print(row)
            ulsan_sum += row[2] + row[3] + row[4] + row[5]

        x_plot = ["서울", "부산", "대구", "인천", "광주", "대전", "울산"]
        y_plot = [seoul_sum, busan_sum, daegu_sum, incheon_sum, gwangju_sum, daejeon_sum, ulsan_sum]

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
