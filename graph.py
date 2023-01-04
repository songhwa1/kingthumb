import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
import numpy as np
from PyQt5 import uic
import os
import pymysql
import matplotlib.pyplot as plt

form_class = uic.loadUiType("d3f0837feab22ffb.ui")[0]


class GraphWidget(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.graphstack.setCurrentIndex(0)
        # self.crimebutton.clicked.connect(self.move_crime)
        # self.crimebutton_2.clicked.connect(self.move_crime)
        # self.officebutton.clicked.connect(self.move_office)
        # self.officebutton_2.clicked.connect(self.move_office)
        # self.peoplebutton.clicked.connect(self.move_people)
        # self.peoplebutton_2.clicked.connect(self.move_people)

        # 데이터 베이스 연결
        conn = pymysql.connect(host='127.0.0.1', user='root', password='agumon200_', db='data')
        curs = conn.cursor()

        # 범죄 수 그래프 y값 설정
        curs.execute("SELECT * FROM data.crime where office like '서울%'")
        crime_rows = curs.fetchall()
        seoul_crime = 0
        for row in crime_rows:
            seoul_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '부산%'")
        crime_rows = curs.fetchall()
        busan_crime = 0
        for row in crime_rows:
            busan_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '대구%'")
        crime_rows = curs.fetchall()
        daegu_crime = 0
        for row in crime_rows:
            daegu_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '인천%'")
        crime_rows = curs.fetchall()
        incheon_crime = 0
        for row in crime_rows:
            incheon_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '광주%'")
        crime_rows = curs.fetchall()
        gwanju_crime = 0
        for row in crime_rows:
            gwanju_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '대전%'")
        crime_rows = curs.fetchall()
        daejeon_crime = 0
        for row in crime_rows:
            daejeon_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '울산%'")
        crime_rows = curs.fetchall()
        ulsan_crime = 0
        for row in crime_rows:
            ulsan_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '세종%'")
        crime_rows = curs.fetchall()
        sejong_crime = 0
        for row in crime_rows:
            sejong_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '경기%'")
        crime_rows = curs.fetchall()
        gyeonggi_crime = 0
        for row in crime_rows:
            gyeonggi_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '강원%'")
        crime_rows = curs.fetchall()
        gangwon_crime = 0
        for row in crime_rows:
            gangwon_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '충북%'")
        crime_rows = curs.fetchall()
        chungbuk_crime = 0
        for row in crime_rows:
            chungbuk_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '충남%'")
        crime_rows = curs.fetchall()
        chungnam_crime = 0
        for row in crime_rows:
            chungnam_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '전북%'")
        crime_rows = curs.fetchall()
        jeonbuk_crime = 0
        for row in crime_rows:
            jeonbuk_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '전남%'")
        crime_rows = curs.fetchall()
        jeonnam_crime = 0
        for row in crime_rows:
            jeonnam_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '경북%'")
        crime_rows = curs.fetchall()
        gyeongbuk_crime = 0
        for row in crime_rows:
            gyeongbuk_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '경남%'")
        crime_rows = curs.fetchall()
        gyeongnam_crime = 0
        for row in crime_rows:
            gyeongnam_crime += row[2] + row[3] + row[4] + row[5]

        curs.execute("SELECT * FROM data.crime where office like '제주%'")
        crime_rows = curs.fetchall()
        jaeju_crime = 0
        for row in crime_rows:
            jaeju_crime += row[2] + row[3] + row[4] + row[5]

        crime_x = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종",
                   "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]
        crime_y = [seoul_crime, busan_crime, daegu_crime, incheon_crime, gwanju_crime, daejeon_crime,
                   ulsan_crime, sejong_crime, gyeonggi_crime, gangwon_crime,  chungbuk_crime, chungnam_crime,
                   jeonbuk_crime, jeonnam_crime, gyeongbuk_crime, gyeongnam_crime, jaeju_crime]

        # x축 설정
        x_dict = dict(enumerate(crime_x))
        ticks = [list(zip(x_dict.keys(), x_dict.values()))]

        # 범죄 수 그래프 그리기
        self.graph1.plot(list(range(len(crime_x))), crime_y)
        crime_bottom = self.graph1.getAxis('bottom')
        crime_bottom.setTicks(ticks)
        
        # 경찰서 수 y값 설정
        curs.execute("SELECT count(ji) FROM data.office where ji = '서울청'")
        office_row = curs.fetchall()
        for row in office_row:
            seoul_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji = '부산청'")
        office_row = curs.fetchall()
        for row in office_row:
            busan_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji = '대구청'")
        office_row = curs.fetchall()
        for row in office_row:
            daegu_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji = '인천청'")
        office_row = curs.fetchall()
        for row in office_row:
            incheon_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji = '광주청'")
        office_row = curs.fetchall()
        for row in office_row:
            gwanju_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji = '대전청'")
        office_row = curs.fetchall()
        for row in office_row:
            daejeon_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji = '울산청'")
        office_row = curs.fetchall()
        for row in office_row:
            ulsan_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji = '세종청'")
        office_row = curs.fetchall()
        for row in office_row:
            sejong_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '경기%'")
        office_row = curs.fetchall()
        for row in office_row:
            gyeonggi_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '강원청'")
        office_row = curs.fetchall()
        for row in office_row:
            gangwon_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '충북청'")
        office_row = curs.fetchall()
        for row in office_row:
            chungbuk_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '충남청'")
        office_row = curs.fetchall()
        for row in office_row:
            chungnam_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '전북청'")
        office_row = curs.fetchall()
        for row in office_row:
            jeonbuk_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '전남청'")
        office_row = curs.fetchall()
        for row in office_row:
            jeonnam_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '경북청'")
        office_row = curs.fetchall()
        for row in office_row:
            gyeongbuk_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '경남청'")
        office_row = curs.fetchall()
        for row in office_row:
            gyeongnam_office = row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '제주청'")
        office_row = curs.fetchall()
        for row in office_row:
            jaeju_office = row[0]

        # 경찰서 수 y값 설정
        office_y = [seoul_office, busan_office, daegu_office, incheon_office, gwanju_office, daejeon_office,
                    ulsan_office, sejong_office, gyeonggi_office, gangwon_office, chungbuk_office, chungnam_office,
                    jeonbuk_office, jeonnam_office, gyeongbuk_office, gyeongnam_office, jaeju_office]

        # 경찰서 수 그래프 그리기
        self.graph2.plot(list(range(len(crime_x))), office_y)
        office_bottom = self.graph2.getAxis('bottom')
        office_bottom.setTicks(ticks)

        # curs.execute("SELECT * FROM ")

    # def move_crime(self):
    #     self.graphstack.setCurrentIndex(0)
    #
    # def move_office(self):
    #     self.graphstack.setCurrentIndex(1)
    #
    # def move_people(self):
    #     self.graphstack.setCurrentIndex(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    graph = GraphWidget()
    graph.show()
    app.exec_()
