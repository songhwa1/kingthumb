import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg
# from pyqtgraph import PlotWidget, plot
import numpy as np
from PyQt5 import uic
# import os
import pymysql
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

form_class = uic.loadUiType("d3f0837feab22ffb.ui")[0]
# matplot 그래프 한글
# plt.rc('font', family='Malgun Gothic')


class GraphWidget(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.office_graph)
        self.pushButton_4.clicked.connect(self.crime_graph)

        # #matplot 그래프 캔버스 설정
        # self.fig = plt.Figure()
        # self.canvas = FigureCanvas(self.fig)
        # self.graph1.addWidget(self.canvas)

    def office_graph(self):
        # 데이터 베이스 연결
        conn = pymysql.connect(host='127.0.0.1', user='root', password='agumon200_', db='data')
        curs = conn.cursor()

        # # 원형 차트
        # crime_sum = 0
        # for crime in crime_y:
        #     crime_sum += crime
        #
        # crime_ratio = [seoul_crime/crime_sum, busan_crime/crime_sum, daegu_crime/crime_sum,
        #                incheon_crime/crime_sum, gwangju_crime/crime_sum, daejeon_crime/crime_sum,
        #                ulsan_crime/crime_sum, sejong_crime/crime_sum, gyeonggi_crime/crime_sum,
        #                gangwon_crime/crime_sum, chungbuk_crime/crime_sum, chungnam_crime/crime_sum,
        #                jeonbuk_crime/crime_sum, jeonnam_crime/crime_sum,
        #                gyeongbuk_crime/crime_sum, gyeongnam_crime/crime_sum, jaeju_crime/crime_sum]

        # self.fig = plt.Figure()
        # self.canvas = FigureCanvas(self.fig)
        # self.crime_chart.addWidget(self.canvas)
        # chart = self.fig.add_subplot(111)
        # chart.pie(crime_ratio, labels=crime_x, autopct='%.1f%%')
        # self.canvas.draw()

        # 그래프 x축 설정
        office_x = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종",
                    "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]
        x_dict = dict(enumerate(office_x))
        ticks = [list(zip(x_dict.keys(), x_dict.values()))]
        crime_bottom = self.graph1.getAxis('bottom')
        crime_bottom.setTicks(ticks)
        
        # 경찰서 수 그래프 y값 설정
        curs.execute("SELECT count(ji) FROM data.office where ji = '서울청'")
        office_row = curs.fetchall()
        seoul_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji = '부산청'")
        office_row = curs.fetchall()
        busan_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji = '대구청'")
        office_row = curs.fetchall()
        daegu_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji = '인천청'")
        office_row = curs.fetchall()
        incheon_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji = '광주청'")
        office_row = curs.fetchall()
        gwangju_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji = '대전청'")
        office_row = curs.fetchall()
        daejeon_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji = '울산청'")
        office_row = curs.fetchall()
        ulsan_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji = '세종청'")
        office_row = curs.fetchall()
        sejong_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '경기%'")
        office_row = curs.fetchall()
        gyeonggi_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '강원청'")
        office_row = curs.fetchall()
        gangwon_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '충북청'")
        office_row = curs.fetchall()
        chungbuk_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '충남청'")
        office_row = curs.fetchall()
        chungnam_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '전북청'")
        office_row = curs.fetchall()
        jeonbuk_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '전남청'")
        office_row = curs.fetchall()
        jeonnam_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '경북청'")
        office_row = curs.fetchall()
        gyeongbuk_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '경남청'")
        office_row = curs.fetchall()
        gyeongnam_office = office_row[0]

        curs.execute("SELECT count(ji) FROM data.office where ji like '제주청'")
        office_row = curs.fetchall()
        jaeju_office = office_row[0]

        # 경찰서 수 y값 설정
        office_y = [seoul_office, busan_office, daegu_office, incheon_office, gwangju_office, daejeon_office,
                    ulsan_office, sejong_office, gyeonggi_office, gangwon_office, chungbuk_office, chungnam_office,
                    jeonbuk_office, jeonnam_office, gyeongbuk_office, gyeongnam_office, jaeju_office]

        # # 다중 막대그래프
        # x = np.arange(17) + 0.15
        # bar = pg.BarGraphItem(x=x, height=office_y, width=0.3, pen=None, brush='b')
        # self.graph1.addItem(bar)
        # self.graph1.setLabel('bottom', '범죄 수')

        # 경찰서 수 그래프 그리기
        # self.graph2.plot(list(range(len(crime_x))), office_y)
        x = np.arange(17)
        bar = pg.BarGraphItem(x=x, height=office_y, width=0.3, pen=None, brush='b')
        self.graph2.addItem(bar)
        self.graph2.setLabel('bottom', '경찰서 수')
        office_bottom = self.graph2.getAxis('bottom')
        office_bottom.setTicks(ticks)

        # 인구 수 그래프 y값 설정
        curs.execute("SELECT sum(sum) FROM data.people where city = '서울%'")
        people_row = curs.fetchall()
        seoul_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '부산%'")
        people_row = curs.fetchall()
        busan_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '대구%'")
        people_row = curs.fetchall()
        daegu_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '인천%'")
        people_row = curs.fetchall()
        incheon_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '광주%'")
        people_row = curs.fetchall()
        gwangju_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '대전%'")
        people_row = curs.fetchall()
        daejeon_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '울산%'")
        people_row = curs.fetchall()
        ulsan_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '세종%'")
        people_row = curs.fetchall()
        sejong_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '경기%'")
        people_row = curs.fetchall()
        gyeonggi_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '강원%'")
        people_row = curs.fetchall()
        gangwon_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '충청북도'")
        people_row = curs.fetchall()
        chungbuk_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '충청남도'")
        people_row = curs.fetchall()
        chungnam_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '전라북도'")
        people_row = curs.fetchall()
        jeonbuk_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '전라남도'")
        people_row = curs.fetchall()
        jeonnam_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '경상북도'")
        people_row = curs.fetchall()
        gyeongbuk_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '경상남도'")
        people_row = curs.fetchall()
        gyeongnam_people = people_row[0]

        curs.execute("SELECT sum(sum) FROM data.people where city = '제주%'")
        people_row = curs.fetchall()
        jaeju_people = people_row[0]

        people_y = [seoul_people, busan_people, daegu_people, incheon_people, gwangju_people, daejeon_people,
                    ulsan_people, sejong_people, gyeonggi_people, gangwon_people, chungbuk_people, chungnam_people,
                    jeonbuk_people, jeonnam_people, gyeongbuk_people, gyeongnam_people, jaeju_people]

        # 인구 수 그래프 그리기
        x = np.arange(17)
        bar = pg.BarGraphItem(x=x, height=people_y, width=0.3, pen=None, brush='b')
        self.graph3.addItem(bar)
        self.graph3.setLabel('bottom', '지역 별 인구 수')
        people_bottom = self.graph3.getAxis('bottom')
        people_bottom.setTicks(ticks)

    def crime_graph(self):
        # 데이터 베이스 연결
        conn = pymysql.connect(host='127.0.0.1', user='root', password='agumon200_', db='data')
        curs = conn.cursor()

        # 그래프 x축 설정
        crime_x = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종",
                   "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]
        x_dict = dict(enumerate(crime_x))
        ticks = [list(zip(x_dict.keys(), x_dict.values()))]
        crime_bottom = self.graph1.getAxis('bottom')
        crime_bottom.setTicks(ticks)

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
        gwangju_crime = 0
        for row in crime_rows:
            gwangju_crime += row[2] + row[3] + row[4] + row[5]

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

        crime_y = [seoul_crime, busan_crime, daegu_crime, incheon_crime, gwangju_crime, daejeon_crime,
                   ulsan_crime, sejong_crime, gyeonggi_crime, gangwon_crime, chungbuk_crime, chungnam_crime,
                   jeonbuk_crime, jeonnam_crime, gyeongbuk_crime, gyeongnam_crime, jaeju_crime]

        # 범죄 수 그래프
        x = np.arange(17)
        bar = pg.BarGraphItem(x=x, height=crime_y, width=0.3, pen=None, brush='b')
        self.graph1.addItem(bar)
        self.graph1.setLabel('bottom', '범죄 수')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    graph = GraphWidget()
    graph.show()
    app.exec_()
