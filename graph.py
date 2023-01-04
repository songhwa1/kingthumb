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
        self.graphstack.setCurrentIndex(0)
        self.crimebutton.clicked.connect(self.move_crime)
        self.crimebutton_2.clicked.connect(self.move_crime)
        self.officebutton.clicked.connect(self.move_office)
        self.officebutton_2.clicked.connect(self.move_office)
        self.peoplebutton.clicked.connect(self.move_people)
        self.peoplebutton_2.clicked.connect(self.move_people)

        conn = pymysql.connect(host='127.0.0.1', user='root', password='agumon200_', db='data')
        curs = conn.cursor()

        curs.execute("SELECT * FROM data.crime where office like '서울%'")
        rows = curs.fetchall()
        seoul_crime = 0
        for row in rows:
            print(row)
            seoul_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '부산%'")
        rows = curs.fetchall()
        busan_crime = 0
        for row in rows:
            print(row)
            busan_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '대구%'")
        rows = curs.fetchall()
        daegu_crime = 0
        for row in rows:
            print(row)
            daegu_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '인천%'")
        rows = curs.fetchall()
        incheon_crime = 0
        for row in rows:
            print(row)
            incheon_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '광주%'")
        rows = curs.fetchall()
        gwanju_crime = 0
        for row in rows:
            print(row)
            gwanju_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '대전%'")
        rows = curs.fetchall()
        daejeon_crime = 0
        for row in rows:
            print(row)
            daejeon_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '울산%'")
        rows = curs.fetchall()
        ulsan_crime = 0
        for row in rows:
            print(row)
            ulsan_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '세종%'")
        rows = curs.fetchall()
        sejong_crime = 0
        for row in rows:
            print(row)
            sejong_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '경기%'")
        rows = curs.fetchall()
        gyeonggi_crime = 0
        for row in rows:
            print(row)
            gyeonggi_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '강원%'")
        rows = curs.fetchall()
        gangwon_crime = 0
        for row in rows:
            print(row)
            gangwon_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '충북%'")
        rows = curs.fetchall()
        chungbuk_crime = 0
        for row in rows:
            print(row)
            chungbuk_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '충남%'")
        rows = curs.fetchall()
        chungnam_crime = 0
        for row in rows:
            print(row)
            chungnam_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '전북%'")
        rows = curs.fetchall()
        jeonbuk_crime = 0
        for row in rows:
            print(row)
            jeonbuk_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '전남%'")
        rows = curs.fetchall()
        jeonnam_crime = 0
        for row in rows:
            print(row)
            jeonnam_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '경북%'")
        rows = curs.fetchall()
        gyeongbuk_crime = 0
        for row in rows:
            print(row)
            gyeongbuk_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '경남%'")
        rows = curs.fetchall()
        gyeongnam_crime = 0
        for row in rows:
            print(row)
            gyeongnam_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '제주%'")
        rows = curs.fetchall()
        jaeju_crime = 0
        for row in rows:
            print(row)
            jaeju_crime += row[2] + row[3] + row[4] + row[5]

        x_plot = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종",
                  "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]
        y_plot = [seoul_crime, busan_crime, daegu_crime, incheon_crime, gwanju_crime, daejeon_crime,
                  ulsan_crime, sejong_crime, gyeonggi_crime, gangwon_crime,  chungbuk_crime, chungnam_crime,
                  jeonbuk_crime, jeonnam_crime, gyeongbuk_crime, gyeongnam_crime, jaeju_crime]

        x_dict = dict(enumerate(x_plot))

        ticks = [list(zip(x_dict.keys(), x_dict.values()))]

        self.graph1.plot(list(range(len(x_plot))), y_plot)

        x_bottom = self.graph1.getAxis('bottom')
        x_bottom.setTicks(ticks)

    def move_crime(self):
        self.graphstack.setCurrentIndex(0)

    def move_office(self):
        self.graphstack.setCurrentIndex(1)

    def move_people(self):
        self.graphstack.setCurrentIndex(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    graph = GraphWidget()
    graph.show()
    app.exec_()
