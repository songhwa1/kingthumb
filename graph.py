import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import numpy as np
from PyQt5 import uic
import pymysql
import MySQLdb
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QDate, Qt

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
        self.statistics_pushButton.clicked.connect(self.statistics_data)
        # 원형 차트 기능
        self.c_chart_button.clicked.connect(self.draw_c_chart)
        self.o_chart_button.clicked.connect(self.draw_o_chart)
        self.p_chart_button.clicked.connect(self.draw_p_chart)
        # 송화, 의용
        self.police_pushButton.clicked.connect(self.searchPolice)
        self.police_tableWidget.doubleClicked.connect(self.police_cellclicked)
        self.police_lineEdit.returnPressed.connect(self.searchPolice)
        self.crime_pushButton.clicked.connect(self.searchCrime)
        self.crime_tableWidget.cellClicked.connect(self.addlabel)
        self.crime_lineEdit.returnPressed.connect(self.searchCrime)
        self.modify_pushButton.clicked.connect(self.modify)
        self.add_delete_pushButton.clicked.connect(self.add_delete)
        self.gomain_button.clicked.connect(self.main)
        self.gotomain_button.clicked.connect(self.main)
        self.district_office_combobox.currentIndexChanged.connect(self.fill_police_combobox)
        self.police_combobox.currentIndexChanged.connect(self.fill_detail_combobox)
        self.detail_combobox.currentIndexChanged.connect(self.fill_lineEdit_combobox)
        self.modify_button.clicked.connect(self.modify_data)
        self.add_button.clicked.connect(self.addcrime)
        self.delete_button.clicked.connect(self.deletecrime)

        # tableWidget 열 넓이 조절
        self.police_tableWidget.setColumnWidth(0, 121)
        self.police_tableWidget.setColumnWidth(1, 121)
        self.police_tableWidget.setColumnWidth(2, 121)
        self.police_tableWidget.setColumnWidth(3, 121)
        self.police_tableWidget.setColumnWidth(4, 121)
        self.police_tableWidget.setColumnWidth(5, 327)

        self.crime_tableWidget.setColumnWidth(0, 121)
        self.crime_tableWidget.setColumnWidth(1, 327)
        self.crime_tableWidget.setColumnWidth(2, 121)
        self.crime_tableWidget.setColumnWidth(3, 121)
        self.crime_tableWidget.setColumnWidth(4, 121)
        self.crime_tableWidget.setColumnWidth(5, 121)

        self.modify_tableWidget.setColumnWidth(0, 121)
        self.modify_tableWidget.setColumnWidth(1, 121)
        self.modify_tableWidget.setColumnWidth(2, 121)
        self.modify_tableWidget.setColumnWidth(3, 121)
        self.modify_tableWidget.setColumnWidth(4, 121)
        self.modify_tableWidget.setColumnWidth(5, 327)

        self.change_tableWidget.setColumnWidth(0, 121)
        self.change_tableWidget.setColumnWidth(1, 300)
        self.change_tableWidget.setColumnWidth(2, 121)
        self.change_tableWidget.setColumnWidth(3, 121)
        self.change_tableWidget.setColumnWidth(4, 121)
        self.change_tableWidget.setColumnWidth(5, 121)

    def statistics_data(self):
        self.tabWidget.setCurrentIndex(3)

    def searchPolice(self):
        word = self.police_lineEdit.text()
        mydb1 = MySQLdb.connect(host='127.0.0.1',
                                # port=3306,
                                user='root',
                                password='0000',
                                db='data')
        a = mydb1.cursor()
        a.execute(f"SELECT * FROM data.office where 지방청 like '%{word}%'")
        police = a.fetchall()

        Row = 0
        self.police_tableWidget.setRowCount(len(police))

        for s in police:
            self.police_tableWidget.setItem(Row, 0, QTableWidgetItem(s[1]))
            self.police_tableWidget.setItem(Row, 1, QTableWidgetItem(s[2]))
            self.police_tableWidget.setItem(Row, 2, QTableWidgetItem(s[3]))
            self.police_tableWidget.setItem(Row, 3, QTableWidgetItem(s[5]))
            self.police_tableWidget.setItem(Row, 4, QTableWidgetItem(s[6]))
            self.police_tableWidget.setItem(Row, 5, QTableWidgetItem(s[7]))
            Row += 1
        mydb1.close()

    def searchCrime(self):
        word = self.crime_lineEdit.text()
        self.curs.execute(f"SELECT * FROM data.crime where office like '%{word}%' and del=0")
        crime = self.curs.fetchall()

        Row = 0
        self.crime_tableWidget.setRowCount(len(crime))

        for j in crime:
            self.crime_tableWidget.setItem(Row, 0, QTableWidgetItem(str(j[0])))
            self.crime_tableWidget.setItem(Row, 1, QTableWidgetItem(j[1]))
            self.crime_tableWidget.setItem(Row, 2, QTableWidgetItem(str(j[2])))
            self.crime_tableWidget.setItem(Row, 3, QTableWidgetItem(str(j[3])))
            self.crime_tableWidget.setItem(Row, 4, QTableWidgetItem(str(j[4])))
            self.crime_tableWidget.setItem(Row, 5, QTableWidgetItem(str(j[5])))
            Row += 1

    def addlabel(self, row, column):
        select = self.crime_tableWidget.item(row, column).text()
        self.police_check_lineEdit.setText(select)
        reply = QMessageBox.question(self, "알림", "추가, 삭제 탭으로 이동 하시겠습니까?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.tabWidget.setCurrentIndex(2)
            self.curs.execute("SELECT * FROM data.crime WHERE office = '" + self.police_check_lineEdit.text() + "'")
            result = self.curs.fetchall()
            Row = 0
            self.change_tableWidget.setRowCount(len(result))
            if result:
                for i in result:
                    self.change_tableWidget.setItem(Row, 0, QTableWidgetItem(str(i[0])))
                    self.change_tableWidget.setItem(Row, 1, QTableWidgetItem(i[1]))
                    self.change_tableWidget.setItem(Row, 2, QTableWidgetItem(str(i[2])))
                    self.change_tableWidget.setItem(Row, 3, QTableWidgetItem(str(i[3])))
                    self.change_tableWidget.setItem(Row, 4, QTableWidgetItem(str(i[4])))
                    self.change_tableWidget.setItem(Row, 5, QTableWidgetItem(str(i[5])))
                    Row += 1
        else:
            pass

    def addcrime(self):
        year1 = self.year_lineEdit.text()
        police_check1 = self.police_check_lineEdit.text()
        murder1 = self.murder_lineEdit.text()
        burglar1 = self.burglar_lineEdit.text()
        theft1 = self.theft_lineEdit.text()
        violence1 = self.violence_lineEdit.text()

        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='safety')
        a = conn.cursor()
        sql = "INSERT INTO data.crime(year,office,murder,gang,steal,attack,del) VALUES (%d, '%s', %d, %d, %d, %d, 0);" % (int(year1), police_check1, int(murder1), int(burglar1), int(theft1), int(violence1))
        a.execute(sql)
        conn.commit()
        a.execute("SELECT * FROM data.crime where year = 2023")
        crime = a.fetchall()
        Row = 0
        self.change_tableWidget.setRowCount(len(crime))
        if crime:
            for i in crime:
                self.change_tableWidget.setItem(Row, 0, QTableWidgetItem(str(i[0])))
                self.change_tableWidget.setItem(Row, 1, QTableWidgetItem(i[1]))
                self.change_tableWidget.setItem(Row, 2, QTableWidgetItem(str(i[2])))
                self.change_tableWidget.setItem(Row, 3, QTableWidgetItem(str(i[3])))
                self.change_tableWidget.setItem(Row, 4, QTableWidgetItem(str(i[4])))
                self.change_tableWidget.setItem(Row, 5, QTableWidgetItem(str(i[5])))
                Row += 1

    def deletecrime(self):
        year1 = self.year_lineEdit.text()
        police_check1 = self.police_check_lineEdit.text()
        murder1 = self.murder_lineEdit.text()
        burglar1 = self.burglar_lineEdit.text()
        theft1 = self.theft_lineEdit.text()
        violence1 = self.violence_lineEdit.text()

        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='safety')
        a = conn.cursor()
        sql = "update data.crime set del = 1 where year = %d and office = '%s' and murder = %d and gang = %d and steal = %d and attack = %d;" %(int(year1), police_check1, int(murder1), int(burglar1), int(theft1), int(violence1))
        a.execute(sql)
        conn.commit()
        a.execute("SELECT * FROM data.crime where year = 2023 and del = 0")
        crime = a.fetchall()
        print("*",crime)
        Row = 0
        self.change_tableWidget.setRowCount(len(crime))
        if crime:
            for i in crime:
                self.change_tableWidget.setItem(Row, 0, QTableWidgetItem(str(i[0])))
                self.change_tableWidget.setItem(Row, 1, QTableWidgetItem(i[1]))
                self.change_tableWidget.setItem(Row, 2, QTableWidgetItem(str(i[2])))
                self.change_tableWidget.setItem(Row, 3, QTableWidgetItem(str(i[3])))
                self.change_tableWidget.setItem(Row, 4, QTableWidgetItem(str(i[4])))
                self.change_tableWidget.setItem(Row, 5, QTableWidgetItem(str(i[5])))
                Row += 1



    def police_cellclicked(self, event):
        reply = QMessageBox.question(self, "알림", "수정 탭으로 이동하시겠습니까?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.tabWidget.setCurrentIndex(1)
            self.curs.execute("SELECT DISTINCT 지방청 from data.office")
            result = self.curs.fetchall()
            if result:
                for i in result:
                    self.district_office_combobox.addItem(str(i[0]))
        else:
            pass

    def modify(self):
        self.tabWidget.setCurrentIndex(1)
        self.curs.execute("SELECT DISTINCT 지방청 from data.office")
        result = self.curs.fetchall()
        if result:
            for i in result:
                self.district_office_combobox.addItem(str(i[0]))

    def fill_police_combobox(self):
        self.curs.execute("SELECT DISTINCT 경찰서 from data.office WHERE 지방청 = '"+self.district_office_combobox.currentText()+"'")
        result = self.curs.fetchall()
        self.police_combobox.clear()
        if result:
            for j in result:
                self.police_combobox.addItem(str(j[0]))

    def fill_detail_combobox(self):
        self.curs.execute("SELECT DISTINCT 관서명 from data.office WHERE 경찰서 = '"+self.police_combobox.currentText()+"'")
        result = self.curs.fetchall()
        self.curs.execute("SELECT * from data.office WHERE 경찰서 = '" + self.police_combobox.currentText() + "'")
        result2 = self.curs.fetchall()
        Row = 0
        self.modify_tableWidget.setRowCount(len(result2))
        if result2:
            for i in result2:
                self.modify_tableWidget.setItem(Row, 0, QTableWidgetItem(i[1]))
                self.modify_tableWidget.setItem(Row, 1, QTableWidgetItem(i[2]))
                self.modify_tableWidget.setItem(Row, 2, QTableWidgetItem(i[3]))
                self.modify_tableWidget.setItem(Row, 3, QTableWidgetItem(i[5]))
                self.modify_tableWidget.setItem(Row, 4, QTableWidgetItem(i[6]))
                self.modify_tableWidget.setItem(Row, 5, QTableWidgetItem(i[7]))
                Row += 1
        self.detail_combobox.clear()
        if result:
            for j in result:
                self.detail_combobox.addItem(str(j[0]))

    def fill_lineEdit_combobox(self):
        self.curs.execute(
            "SELECT * from data.office WHERE 관서명 = '" + self.detail_combobox.currentText() + "'")
        result = self.curs.fetchall()
        if result:
            for i in result:
                self.police_division_lineEdit.setText(str(i[5]))
                self.police_call_number_lineEdit.setText(str(i[6]))
                self.police_address_lineEdit.setText(str(i[7]))

    def modify_data(self):
        mydb1 = MySQLdb.connect(host='127.0.0.1',
                                # port=3306,
                                user='root',
                                password='0000',
                                db='data')
        a = mydb1.cursor()
        a.execute("UPDATE data.office SET 구분 = '" + self.police_division_lineEdit.text() + "', 전화번호 = '" + self.police_call_number_lineEdit.text() + "', 주소 = '" + self.police_address_lineEdit.text() + "' WHERE 관서명 = '"+ self.detail_combobox.currentText() +"'")
        mydb1.commit()
        a.close()
        mydb1.close()
        self.modify_tableWidget.item(0, 3).setText(self.police_division_lineEdit.text())
        self.modify_tableWidget.item(0, 4).setText(self.police_call_number_lineEdit.text())
        self.modify_tableWidget.item(0, 5).setText(self.police_address_lineEdit.text())
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("수정사항이 반영되었습니다.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()


    def add_delete(self):
        self.tabWidget.setCurrentIndex(2)

    def main(self):
        self.tabWidget.setCurrentIndex(0)

    def draw_office(self):

        # 그래프 x축 설정
        office_x = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종",
                    "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]
        x_dict = dict(enumerate(office_x))
        ticks = [list(zip(x_dict.keys(), x_dict.values()))]
        
        # 경찰서 수 그래프 y값 설정
        for i in range(len(office_x)):
            self.curs.execute("SELECT count(지방청) FROM data.office where 지방청 like '%s%%'" % office_x[i])
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
            self.curs.execute("SELECT count(지방청) FROM data.office where 지방청 like '%s%%'" % office_x[i])
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
