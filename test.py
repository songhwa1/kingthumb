import pymysql
import sys
import pyqtgraph
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import Qt
import csv

form_widget = uic.loadUiType('ui.ui')[0]
class Search(QWidget, form_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 시그널과 함수 연결
        self.police_pushButton.clicked.connect(self.searchPolice)
        self.crime_pushButton.clicked.connect(self.searchCrime)

        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='safety')
        a = conn.cursor()
        a.execute("SELECT * from `safety`.`경찰서1`")
        police = a.fetchall()

        # MySQL로 가공한 파일 csv파일로 만들기
        # f= open("경찰서1.csv",'w',encoding = "utf-8",newline='')
        # wr = csv.writer(f)
        # for i in police:
        #     wr.writerow(i)
        # f.close()

        # import해온 데이터 리스트화
        police_list1 = list(police)
        self.police_info = []
        for i in police_list1:
            self.police_info.append(list(i))

        # tableWidget 열 넓이 조절
        self.police_tableWidget.setColumnWidth(0, 121)
        self.police_tableWidget.setColumnWidth(1, 121)
        self.police_tableWidget.setColumnWidth(2, 121)
        self.police_tableWidget.setColumnWidth(3, 121)
        self.police_tableWidget.setColumnWidth(5, 327)

    def showlist(self):     # 경찰서 조회하는 함수, 연결된 시그널 없음..
        Row = 0
        self.police_tableWidget.setRowCount(len(self.police_info))
        for s in self.police_info:
            self.police_tableWidget.setItem(Row, 0, QTableWidgetItem(s[1]))
            self.police_tableWidget.setItem(Row, 1, QTableWidgetItem(s[2]))
            self.police_tableWidget.setItem(Row, 2, QTableWidgetItem(s[3]))
            self.police_tableWidget.setItem(Row, 3, QTableWidgetItem(s[4]))
            self.police_tableWidget.setItem(Row, 4, QTableWidgetItem(s[5]))
            self.police_tableWidget.setItem(Row, 5, QTableWidgetItem(s[6]))
            Row += 1

    def searchPolice(self):       # 경찰서 검색하는 함수
        word = self.police_lineEdit.text()      # 검색어
        search_list = []    # 빈 리스트 생성
        for i in range(len(self.police_info)):
            if word in self.police_info[i][1]:
                search_list.append(self.police_info[i])     # 빈 리스트에 검색어가 포함된 항목 추가

        # 테이블위젯에 보여주기
        Row = 0
        self.police_tableWidget.setRowCount(len(search_list))
        for s in search_list:
            self.police_tableWidget.setItem(Row, 0, QTableWidgetItem(s[1]))
            self.police_tableWidget.setItem(Row, 1, QTableWidgetItem(s[2]))
            self.police_tableWidget.setItem(Row, 2, QTableWidgetItem(s[3]))
            self.police_tableWidget.setItem(Row, 3, QTableWidgetItem(s[4]))
            self.police_tableWidget.setItem(Row, 4, QTableWidgetItem(s[5]))
            self.police_tableWidget.setItem(Row, 5, QTableWidgetItem(s[6]))

            Row += 1

    def searchCrime(self):      # 범죄 검색하는 함수
        word = self.crime_lineEdit.text()       # 검색어
        crime_info =[]      # 빈 리스트 생성
        with open('범죄.csv', 'r', encoding='cp949', newline='') as f:
            rdr = csv.reader(f)
            for line in rdr:
                crime_info.append(line)
        search_crime = []       # 빈 리스트 생성, 검색어가 포함된 항목 추가
        for i in range(len(crime_info)):
            if word in crime_info[i][1]:
                search_crime.append(crime_info[i])

        Row = 0
        self.crime_tableWidget.setRowCount(len(search_crime))
        for s in search_crime:
            self.crime_tableWidget.setItem(Row, 0, QTableWidgetItem(s[0]))
            self.crime_tableWidget.setItem(Row, 1, QTableWidgetItem(s[1]))
            self.crime_tableWidget.setItem(Row, 2, QTableWidgetItem(s[2]))
            self.crime_tableWidget.setItem(Row, 3, QTableWidgetItem(s[3]))
            self.crime_tableWidget.setItem(Row, 4, QTableWidgetItem(s[4]))
            self.crime_tableWidget.setItem(Row, 5, QTableWidgetItem(s[5]))

            Row += 1


if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = Search()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(881)
    widget.setFixedWidth(1771)
    widget.show()
    app.exec_()