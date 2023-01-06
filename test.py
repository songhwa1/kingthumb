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
        self.delete_button.clicked.connect(self.deletecrime)


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
        a.execute(f"SELECT * FROM safety.crime_num where police like'%{word}%' and del=0")
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
        sql = "INSERT INTO safety.crime_num(year,police,murder,burglar,theft,violence, del) VALUES (%d, '%s', %d, %d, %d, %d, 0);" % (int(year1), police_check1, int(murder1), int(burglar1), int(theft1), int(violence1))
        a.execute(sql)
        conn.commit()
        a.execute("SELECT * FROM safety.crime_num where year = 2023")
        crime = a.fetchall()
        print(crime)
        Row = 0
        self.change_tableWidget.setRowCount(len(crime))
        if crime:
            for i in crime:
                self.change_tableWidget.setItem(Row, 0, QTableWidgetItem(str(int(i[0]))))
                self.change_tableWidget.setItem(Row, 1, QTableWidgetItem(i[1]))
                self.change_tableWidget.setItem(Row, 2, QTableWidgetItem(str(int(i[2]))))
                self.change_tableWidget.setItem(Row, 3, QTableWidgetItem(str(int(i[3]))))
                self.change_tableWidget.setItem(Row, 4, QTableWidgetItem(str(int(i[4]))))
                self.change_tableWidget.setItem(Row, 5, QTableWidgetItem(str(int(i[5]))))
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
        #  year,police,murder,burglar,theft,violence, del
        sql = "update safety.crime_num set del = 1 where year = %d and police = '%s' and murder = %d and burglar = %d and theft = %d and violence = %d;" %(int(year1), police_check1, int(murder1), int(burglar1), int(theft1), int(violence1))
        a.execute(sql)
        conn.commit()

    # def addlabel(self, row, column):
    #     select = self.crime_tableWidget.item(row, column).text()
    #     self.police_check_lineEdit.setText(select)
    #     reply = QMessageBox.question(self, "알림", "추가, 삭제 탭으로 이동 하시겠습니까?",
    #                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    #     if reply == QMessageBox.Yes:
    #         self.tabWidget.setCurrentIndex(2)
    #         mydb1 = pymysql.connect(host='127.0.0.1',
    #                                 port=3306,
    #                                 user='root',
    #                                 password='0000',
    #                                 db='safety')
    #         a = mydb1.cursor()
    #         a.execute("SELECT * FROM safety.범죄건수 WHERE 경찰서 = "'" + self.police_check_lineEdit.text() + "'")
    #         result = a.fetchall()
    #         print("*",result)
    #
    #         # a.execute("alter table safety.범죄건수 add 사이버범죄 varchar(100) not null")
    #
    #         sql = f"""(INSERT INTO safety.범죄건수 (발생년도, 경찰서, 살인, 강도, 절도, 폭력, 사이버범죄)
    #                 VALUES ('{result[0][0]}','{result[0][1]}','{result[0][2]}','{result[0][3]}','{result[0][4]}','{result[0][5]}','{self.crime_number_lineEdit.text()}')"""
    #         a.execute(sql)
    #         a.execute("SELECT * FROM safety.범죄건수 WHERE 사이버범죄")
    #         result1 = a.fetchall()
    #         print(result1)
    #
    #         Row = 0
    #         self.change_tableWidget.setRowCount(len(result1))
    #         if result1:
    #             for i in result1:
    #                 self.change_tableWidget.setItem(Row, 0, QTableWidgetItem(str(int(i[0]))))
    #                 self.change_tableWidget.setItem(Row, 1, QTableWidgetItem(i[1]))
    #                 self.change_tableWidget.setItem(Row, 2, QTableWidgetItem(str(int(i[2]))))
    #                 self.change_tableWidget.setItem(Row, 3, QTableWidgetItem(str(int(i[3]))))
    #                 self.change_tableWidget.setItem(Row, 4, QTableWidgetItem(str(int(i[4]))))
    #                 self.change_tableWidget.setItem(Row, 5, QTableWidgetItem(str(int(i[5]))))
    #                 Row += 1
    #         mydb1.close()
    #     else:
    #         pass


    # SELECT * FROM safety.범죄건수;
    # alter table safety.범죄건수 add 사이버범죄 varchar(100) not null;
    # INSERT INTO safety.범죄건수 (발생년도, 경찰서, 살인, 강도, 절도, 폭력, 사이버범죄)
    #     VALUES (2022,'광인개경찰서',1,1,1,1,1);
    #  SELECT * FROM safety.범죄건수 WHERE 발생년도 = 2022;




if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = Search()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(881)
    widget.setFixedWidth(1771)
    widget.show()
    app.exec_()