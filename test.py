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
        self.police_lineEdit.returnPressed.connect(self.searchPolice)
        self.crime_pushButton.clicked.connect(self.searchCrime)
        self.crime_tableWidget.cellClicked.connect(self.addlabel)
        self.crime_lineEdit.returnPressed.connect(self.searchCrime)
        self.add_button.clicked.connect(self.addcrime)


        # MySQL로 가공한 파일 csv파일로 만들기
        # f= open("경찰서1.csv",'w',encoding = "utf-8",newline='')
        # wr = csv.writer(f)
        # for i in police:
        #     wr.writerow(i)
        # f.close()

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
        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='safety')
        a = conn.cursor()
        a.execute(f"SELECT * FROM safety.경찰서1 where 지방청 like '%{word}%'")
        police = a.fetchall()

        # 테이블위젯에 보여주기
        Row = 0
        self.police_tableWidget.setRowCount(len(police))
        for s in police:
            self.police_tableWidget.setItem(Row, 0, QTableWidgetItem(s[1]))
            self.police_tableWidget.setItem(Row, 1, QTableWidgetItem(s[2]))
            self.police_tableWidget.setItem(Row, 2, QTableWidgetItem(s[3]))
            self.police_tableWidget.setItem(Row, 3, QTableWidgetItem(s[4]))
            self.police_tableWidget.setItem(Row, 4, QTableWidgetItem(s[5]))
            self.police_tableWidget.setItem(Row, 5, QTableWidgetItem(s[6]))

            Row += 1
        conn.close()

    def searchCrime(self):      # 범죄 검색하는 함수
        word = self.crime_lineEdit.text()       # 검색어

        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='safety')
        a = conn.cursor()
        a.execute(f"SELECT * FROM safety.범죄건수 where 경찰서 like'%{word}%'")
        crime = a.fetchall()

        Row = 0
        self.crime_tableWidget.setRowCount(len(crime))
        for s in crime:
            self.crime_tableWidget.setItem(Row, 0, QTableWidgetItem(str(s[0])))
            self.crime_tableWidget.setItem(Row, 1, QTableWidgetItem(s[1]))
            self.crime_tableWidget.setItem(Row, 2, QTableWidgetItem(str(s[2])))
            self.crime_tableWidget.setItem(Row, 3, QTableWidgetItem(str(s[3])))
            self.crime_tableWidget.setItem(Row, 4, QTableWidgetItem(str(s[4])))
            self.crime_tableWidget.setItem(Row, 5, QTableWidgetItem(str(s[5])))

            Row += 1
        conn.close()

    # crime_tableWidget에서 수정/삭제로 넘어가는 함수
    def cellclicked(self, row, column):
        select = self.crime_tableWidget.item(row, column).text()    # 클릭한 cell값 추출
        reply = QMessageBox.question(self, "알림", "추가, 삭제 탭으로 이동 하시겠습니까?",
        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.tabWidget.setCurrentIndex(2)
        else:
            pass
        return select

    # crime_tableWidget에서 수정/삭제로 넘어갈 때 경찰서 이름 lineedit에 추가
    def addlabel(self, row, column):
        select_police = self.cellclicked(row, column)
        self.police_check_lineEdit.setText(select_police)

    def addcrime(self):
        crime_category = self.crime_category_lineEdit.text()
        crime_number = self.crime_number_lineEdit.text()

        # MySQL에서 import 해오기
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='safety')
        a = conn.cursor()
        a.execute(f"SELECT * FROM safety.범죄건수 where 경찰서 like'%{word}%'")
        crime = a.fetchall()







if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = Search()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(881)
    widget.setFixedWidth(1771)
    widget.show()
    app.exec_()