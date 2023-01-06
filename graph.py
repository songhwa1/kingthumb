import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import numpy as np
from PyQt5 import uic
import pymysql
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

form_class = uic.loadUiType("ui.ui")[0]
# matplot 그래프 한글
plt.rc('font', family='Malgun Gothic')


class TabWidget(QWidget, form_class):
    def __init__(self):
        super().__init__()
        # 원형 차트 캔버스 생성
        self.setupUi(self)
        self.fig1 = plt.Figure()
        self.fig2 = plt.Figure()
        self.fig3 = plt.Figure()
        self.canvas1 = FigureCanvas(self.fig1)
        self.canvas2 = FigureCanvas(self.fig2)
        self.canvas3 = FigureCanvas(self.fig3)
        self.crime_chart.addWidget(self.canvas1)
        self.office_chart.addWidget(self.canvas2)
        self.people_chart.addWidget(self.canvas3)
        # 데이터 베이스 연결
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='data')
        self.curs = self.conn.cursor()
        # 그래프 기능
        self.police_graph_pushButton.clicked.connect(self.draw_office)
        self.crime_graph_pushButton.clicked.connect(self.draw_crime)
        # 원형 차트 기능
        self.c_chart_button.clicked.connect(self.draw_c_chart)
        self.o_chart_button.clicked.connect(self.draw_o_chart)
        self.p_chart_button.clicked.connect(self.draw_p_chart)

    def draw_office(self):

        # 그래프 x축 설정
        office_x = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종",
                    "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]
        x_dict = dict(enumerate(office_x))
        ticks = [list(zip(x_dict.keys(), x_dict.values()))]
        
        # 경찰서 수 그래프 y값 설정
        for i in range(len(office_x)):
            self.curs.execute("SELECT count(ji) FROM data.office where ji like '%s%%'" % office_x[i])
            office_row = self.curs.fetchall()
            if i == 0:
                seoul_office = office_row[0][0]
            elif i == 1:
                busan_office = office_row[0][0]
            elif i == 2:
                daegu_office = office_row[0][0]
            elif i == 3:
                incheon_office = office_row[0][0]
            elif i == 4:
                gwangju_office = office_row[0][0]
            elif i == 5:
                daejeon_office = office_row[0][0]
            elif i == 6:
                ulsan_office = office_row[0][0]
            elif i == 7:
                sejong_office = office_row[0][0]
            elif i == 8:
                gyeonggi_office = office_row[0][0]
            elif i == 9:
                gangwon_office = office_row[0][0]
            elif i == 10:
                chungbuk_office = office_row[0][0]
            elif i == 11:
                chungnam_office = office_row[0][0]
            elif i == 12:
                jeonbuk_office = office_row[0][0]
            elif i == 13:
                jeonnam_office = office_row[0][0]
            elif i == 14:
                gyeongbuk_office = office_row[0][0]
            elif i == 15:
                gyeongnam_office = office_row[0][0]
            elif i == 16:
                jaeju_office = office_row[0][0]

        # 경찰서 수 y값 설정
        office_y = [seoul_office, busan_office, daegu_office, incheon_office, gwangju_office, daejeon_office,
                    ulsan_office, sejong_office, gyeonggi_office, gangwon_office, chungbuk_office, chungnam_office,
                    jeonbuk_office, jeonnam_office, gyeongbuk_office, gyeongnam_office, jaeju_office]

        # # 다중 막대그래프
        # x = np.arange(17) + 0.15
        # bar = pg.BarGraphItem(x=x, height=office_y, width=0.3, pen=None, brush='b')
        # self.graph1.addItem(bar)
        # self.graph1.setLabel('bottom', '범죄 수')

        # 그래프 x축 설정
        self.office_graph.setLabel('bottom', '[경찰서 수]')
        office_bottom = self.office_graph.getAxis('bottom')
        office_bottom.setTicks(ticks)

        # 그래프 y축 설정
        o_yticks = [[(0, '0 개'), (25, '25 개'), (50, '50 개'), (75, '75 개'), (100, '100 개'), (150, '150 개'),
                     (200, '200 개'), (250, '250 개'), (300, '300 개'), (350, '250 개'), (400, '400 개')]]
        office_left = self.office_graph.getAxis('left')
        office_left.setTicks(o_yticks)

        # 경찰서 수 그래프 그리기
        # self.graph2.plot(list(range(len(crime_x))), office_y)
        x = np.arange(17)
        bar = pg.BarGraphItem(x=x, height=office_y, width=0.3, pen=None, brush='b', name='경찰서 수')
        self.office_graph.addLegend(offset=(-30, 30))
        self.office_graph.addItem(bar)

        people_x = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종",
                    "경기", "강원", "충청북", "충청남", "전라북", "전라남", "경상북", "경상남", "제주"]

        for i in range(len(people_x)):
            self.curs.execute("SELECT sum(sum) from data.peopletest where city like '%s%%'" % people_x[i])
            people_row = self.curs.fetchall()
            if i == 0:
                seoul_people = people_row[0][0]
            elif i == 1:
                busan_people = people_row[0][0]
            elif i == 2:
                daegu_people = people_row[0][0]
            elif i == 3:
                incheon_people = people_row[0][0]
            elif i == 4:
                gwangju_people = people_row[0][0]
            elif i == 5:
                daejeon_people = people_row[0][0]
            elif i == 6:
                ulsan_people = people_row[0][0]
            elif i == 7:
                sejong_people = people_row[0][0]
            elif i == 8:
                gyeonggi_people = people_row[0][0]
            elif i == 9:
                gangwon_people = people_row[0][0]
            elif i == 10:
                chungbuk_people = people_row[0][0]
            elif i == 11:
                chungnam_people = people_row[0][0]
            elif i == 12:
                jeonbuk_people = people_row[0][0]
            elif i == 13:
                jeonnam_people = people_row[0][0]
            elif i == 14:
                gyeongbuk_people = people_row[0][0]
            elif i == 15:
                gyeongnam_people = people_row[0][0]
            elif i == 16:
                jaeju_people = people_row[0][0]

        people_y = [seoul_people, busan_people, daegu_people, incheon_people, gwangju_people, daejeon_people,
                    ulsan_people, sejong_people, gyeonggi_people, gangwon_people, chungbuk_people, chungnam_people,
                    jeonbuk_people, jeonnam_people, gyeongbuk_people, gyeongnam_people, jaeju_people]

        # 그래프 x축 설정
        self.people_graph.setLabel('bottom', '[지역 별 인구 수]')
        people_bottom = self.people_graph.getAxis('bottom')
        people_bottom.setTicks(ticks)

        # 그래프 y축 설정
        p_yticks = [[(0, '0 명'), (1000000, '100만 명'), (2000000, '200만 명'), (3000000, '300만 명'),
                     (4000000, '400만 명'), (6000000, '600만 명'), (8000000, '800만 명'), (10000000, '1000만 명'),
                     (12000000, '1200만 명'), (14000000, '1400만 명')]]
        people_left = self.people_graph.getAxis('left')
        people_left.setTicks(p_yticks)

        # 인구 수 그래프 그리기
        x = np.arange(17)
        bar = pg.BarGraphItem(x=x, height=people_y, width=0.3, pen=None, brush='b', name='인구 수')
        self.people_graph.addLegend(offset=(-30, 30))
        self.people_graph.addItem(bar)

    def draw_crime(self):

        # 그래프 x축 설정
        crime_x = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종",
                   "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]
        x_dict = dict(enumerate(crime_x))
        ticks = [list(zip(x_dict.keys(), x_dict.values()))]
        crime_bottom = self.crime_graph.getAxis('bottom')
        crime_bottom.setTicks(ticks)

        # 그래프 y축 설정
        c_yticks = [[(0, '0 건'), (10000, '1만 건'), (20000, '2만 건'), (30000, '3만 건'),
                     (40000, '4만 건'), (60000, '6만 건'), (80000, '8만 건'), (100000, '10만 건')]]
        crime_left = self.crime_graph.getAxis('left')
        crime_left.setTicks(c_yticks)

        seoul_crime, busan_crime, daegu_crime, incheon_crime, gwangju_crime = 0, 0, 0, 0, 0
        daejeon_crime, ulsan_crime, sejong_crime, gyeonggi_crime = 0, 0, 0, 0
        gangwon_crime, chungbuk_crime, chungnam_crime, jeonbuk_crime = 0, 0, 0, 0
        jeonnam_crime, gyeongbuk_crime, gyeongnam_crime, jaeju_crime = 0, 0, 0, 0

        # 범죄 수 그래프 y값 설정
        for i in range(len(crime_x)):
            self.curs.execute("SELECT * FROM data.crime where office like '%s%%'" % crime_x[i])
            crime_rows = self.curs.fetchall()
            if i == 0:
                for row in crime_rows:
                    seoul_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 1:
                for row in crime_rows:
                    busan_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 2:
                for row in crime_rows:
                    daegu_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 3:
                for row in crime_rows:
                    incheon_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 4:
                for row in crime_rows:
                    gwangju_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 5:
                for row in crime_rows:
                    daejeon_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 6:
                for row in crime_rows:
                    ulsan_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 7:
                for row in crime_rows:
                    sejong_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 8:
                for row in crime_rows:
                    gyeonggi_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 9:
                for row in crime_rows:
                    gangwon_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 10:
                for row in crime_rows:
                    chungbuk_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 11:
                for row in crime_rows:
                    chungnam_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 12:
                for row in crime_rows:
                    jeonbuk_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 13:
                for row in crime_rows:
                    jeonnam_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 14:
                for row in crime_rows:
                    gyeongbuk_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 15:
                for row in crime_rows:
                    gyeongnam_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 16:
                for row in crime_rows:
                    jaeju_crime += row[2] + row[3] + row[4] + row[5]

        crime_y = [seoul_crime, busan_crime, daegu_crime, incheon_crime, gwangju_crime, daejeon_crime,
                   ulsan_crime, sejong_crime, gyeonggi_crime, gangwon_crime, chungbuk_crime, chungnam_crime,
                   jeonbuk_crime, jeonnam_crime, gyeongbuk_crime, gyeongnam_crime, jaeju_crime]

        # 범죄 수 그래프
        x = np.arange(17)
        bar = pg.BarGraphItem(x=x, height=crime_y, width=0.3, pen=None, brush='b', name='범죄 수')
        self.crime_graph.addLegend(offset=(-30, 30))
        self.crime_graph.addItem(bar)
        self.crime_graph.setLabel('bottom', '[범죄 수]')

    def draw_c_chart(self):

        crime_x = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종",
                   "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]

        seoul_crime, busan_crime, daegu_crime, incheon_crime, gwangju_crime = 0, 0, 0, 0, 0
        daejeon_crime, ulsan_crime, sejong_crime, gyeonggi_crime = 0, 0, 0, 0
        gangwon_crime, chungbuk_crime, chungnam_crime, jeonbuk_crime = 0, 0, 0, 0
        jeonnam_crime, gyeongbuk_crime, gyeongnam_crime, jaeju_crime = 0, 0, 0, 0

        # 범죄 수 그래프 y값 설정
        for i in range(len(crime_x)):
            self.curs.execute("SELECT * FROM data.crime where office like '%s%%'" % crime_x[i])
            crime_rows = self.curs.fetchall()
            if i == 0:
                for row in crime_rows:
                    seoul_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 1:
                for row in crime_rows:
                    busan_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 2:
                for row in crime_rows:
                    daegu_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 3:
                for row in crime_rows:
                    incheon_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 4:
                for row in crime_rows:
                    gwangju_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 5:
                for row in crime_rows:
                    daejeon_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 6:
                for row in crime_rows:
                    ulsan_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 7:
                for row in crime_rows:
                    sejong_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 8:
                for row in crime_rows:
                    gyeonggi_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 9:
                for row in crime_rows:
                    gangwon_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 10:
                for row in crime_rows:
                    chungbuk_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 11:
                for row in crime_rows:
                    chungnam_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 12:
                for row in crime_rows:
                    jeonbuk_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 13:
                for row in crime_rows:
                    jeonnam_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 14:
                for row in crime_rows:
                    gyeongbuk_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 15:
                for row in crime_rows:
                    gyeongnam_crime += row[2] + row[3] + row[4] + row[5]
            elif i == 16:
                for row in crime_rows:
                    jaeju_crime += row[2] + row[3] + row[4] + row[5]

        crime_y = [seoul_crime, busan_crime, daegu_crime, incheon_crime, gwangju_crime, daejeon_crime,
                   ulsan_crime, sejong_crime, gyeonggi_crime, gangwon_crime, chungbuk_crime, chungnam_crime,
                   jeonbuk_crime, jeonnam_crime, gyeongbuk_crime, gyeongnam_crime, jaeju_crime]

        # 범죄 수 원형 차트
        crime_sum = 0
        for crime in crime_y:
            crime_sum += crime

        crime_ratio = [seoul_crime / crime_sum, busan_crime / crime_sum, daegu_crime / crime_sum,
                       incheon_crime / crime_sum, gwangju_crime / crime_sum, daejeon_crime / crime_sum,
                       ulsan_crime / crime_sum, sejong_crime / crime_sum, gyeonggi_crime / crime_sum,
                       gangwon_crime / crime_sum, chungbuk_crime / crime_sum, chungnam_crime / crime_sum,
                       jeonbuk_crime / crime_sum, jeonnam_crime / crime_sum,
                       gyeongbuk_crime / crime_sum, gyeongnam_crime / crime_sum, jaeju_crime / crime_sum]

        self.fig1.clf()
        chart = self.fig1.add_subplot(111)
        chart.pie(crime_ratio, labels=crime_x, startangle=45, pctdistance=0.8, autopct='%.1f%%')
        self.canvas1.draw()

    def draw_o_chart(self):
        office_x = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종",
                    "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]

        for i in range(len(office_x)):
            self.curs.execute("SELECT count(ji) FROM data.office where ji like '%s%%'" % office_x[i])
            office_row = self.curs.fetchall()
            if i == 0:
                seoul_office = office_row[0][0]
            elif i == 1:
                busan_office = office_row[0][0]
            elif i == 2:
                daegu_office = office_row[0][0]
            elif i == 3:
                incheon_office = office_row[0][0]
            elif i == 4:
                gwangju_office = office_row[0][0]
            elif i == 5:
                daejeon_office = office_row[0][0]
            elif i == 6:
                ulsan_office = office_row[0][0]
            elif i == 7:
                sejong_office = office_row[0][0]
            elif i == 8:
                gyeonggi_office = office_row[0][0]
            elif i == 9:
                gangwon_office = office_row[0][0]
            elif i == 10:
                chungbuk_office = office_row[0][0]
            elif i == 11:
                chungnam_office = office_row[0][0]
            elif i == 12:
                jeonbuk_office = office_row[0][0]
            elif i == 13:
                jeonnam_office = office_row[0][0]
            elif i == 14:
                gyeongbuk_office = office_row[0][0]
            elif i == 15:
                gyeongnam_office = office_row[0][0]
            elif i == 16:
                jaeju_office = office_row[0][0]

        # 경찰서 수 y값 설정
        office_y = [seoul_office, busan_office, daegu_office, incheon_office, gwangju_office, daejeon_office,
                    ulsan_office, sejong_office, gyeonggi_office, gangwon_office, chungbuk_office, chungnam_office,
                    jeonbuk_office, jeonnam_office, gyeongbuk_office, gyeongnam_office, jaeju_office]

        office_sum = 0
        for office in office_y:
            office_sum += office

        office_ratio = [seoul_office/office_sum, busan_office/office_sum, daegu_office/office_sum,
                        incheon_office/office_sum, gwangju_office/office_sum, daejeon_office/office_sum,
                        ulsan_office/office_sum, sejong_office/office_sum, gyeonggi_office/office_sum,
                        gangwon_office/office_sum, chungbuk_office/office_sum, chungnam_office/office_sum,
                        jeonbuk_office/office_sum, jeonnam_office/office_sum, gyeongbuk_office/office_sum,
                        gyeongnam_office/office_sum, jaeju_office/office_sum]

        self.fig2.clf()
        chart = self.fig2.add_subplot(111)
        chart.pie(office_ratio, labels=office_x, startangle=45, pctdistance=0.8, autopct='%.1f%%')
        self.canvas2.draw()

    def draw_p_chart(self):
        people_x = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종",
                    "경기", "강원", "충청북", "충청남", "전라북", "전라남", "경상북", "경상남", "제주"]

        office_x = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종",
                    "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]

        for i in range(len(people_x)):
            self.curs.execute("SELECT sum(sum) from data.peopletest where city like '%s%%'" % people_x[i])
            people_row = self.curs.fetchall()
            if i == 0:
                seoul_people = people_row[0][0]
            elif i == 1:
                busan_people = people_row[0][0]
            elif i == 2:
                daegu_people = people_row[0][0]
            elif i == 3:
                incheon_people = people_row[0][0]
            elif i == 4:
                gwangju_people = people_row[0][0]
            elif i == 5:
                daejeon_people = people_row[0][0]
            elif i == 6:
                ulsan_people = people_row[0][0]
            elif i == 7:
                sejong_people = people_row[0][0]
            elif i == 8:
                gyeonggi_people = people_row[0][0]
            elif i == 9:
                gangwon_people = people_row[0][0]
            elif i == 10:
                chungbuk_people = people_row[0][0]
            elif i == 11:
                chungnam_people = people_row[0][0]
            elif i == 12:
                jeonbuk_people = people_row[0][0]
            elif i == 13:
                jeonnam_people = people_row[0][0]
            elif i == 14:
                gyeongbuk_people = people_row[0][0]
            elif i == 15:
                gyeongnam_people = people_row[0][0]
            elif i == 16:
                jaeju_people = people_row[0][0]

        people_y = [seoul_people, busan_people, daegu_people, incheon_people, gwangju_people, daejeon_people,
                    ulsan_people, sejong_people, gyeonggi_people, gangwon_people, chungbuk_people, chungnam_people,
                    jeonbuk_people, jeonnam_people, gyeongbuk_people, gyeongnam_people, jaeju_people]

        people_sum = 0
        for people in people_y:
            people_sum += people

        people_ratio = [seoul_people/people_sum, busan_people/people_sum, daegu_people/people_sum,
                        incheon_people/people_sum, gwangju_people/people_sum, daejeon_people/people_sum,
                        ulsan_people/people_sum, sejong_people/people_sum, gyeonggi_people/people_sum,
                        gangwon_people/people_sum, chungbuk_people/people_sum, chungnam_people/people_sum,
                        jeonbuk_people/people_sum, jeonnam_people/people_sum, gyeongbuk_people/people_sum,
                        gyeongnam_people/people_sum, jaeju_people/people_sum]

        self.fig3.clf()
        chart = self.fig3.add_subplot(111)
        chart.pie(people_ratio, labels=office_x, startangle=45, pctdistance=0.8, autopct='%.1f%%')
        self.canvas3.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    graph = TabWidget()
    graph.show()
    app.exec_()
