import pymysql
import MySQLdb
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import Qt
from PyQt5.QtCore import pyqtSlot
import csv
from PyQt5.QtCore import QDate, Qt


form_widget = uic.loadUiType('ui.ui')[0]

class Search(QWidget, form_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.police_pushButton.clicked.connect(self.searchPolice)
        self.crime_pushButton.clicked.connect(self.searchCrime)
        self.modify_pushButton.clicked.connect(self.modify)
        self.add_delete_pushButton.clicked.connect(self.add_delete)
        self.gomain_button.clicked.connect(self.main)
        self.gotomain_button.clicked.connect(self.main)
        # self.modifybutton.clicked.connect(self.Add_New_Crime)

        mydb1 = MySQLdb.connect(host='127.0.0.1',
                               # port=3306,
                               user='root',
                               password='0000',
                               db='policearea')

        mydb2 = MySQLdb.connect(host='127.0.0.1',
                               # port=3306,
                               user='root',
                               password='0000',
                               db='crime')
        a = mydb1.cursor()
        a.execute("SELECT * from `policearea`.`policearea`")
        police = a.fetchall()
        police_list1 = list(police)
        self.police_info = []
        for i in police_list1:
            self.police_info.append(list(i))

        # tableWidget 열 넓이 조절
        self.police_tableWidget.setColumnWidth(0, 121)
        self.police_tableWidget.setColumnWidth(1, 121)
        self.police_tableWidget.setColumnWidth(2, 121)
        self.police_tableWidget.setColumnWidth(3, 121)
        self.police_tableWidget.setColumnWidth(4, 121)
        self.police_tableWidget.setColumnWidth(5, 327)

        b = mydb2.cursor()
        b.execute("SELECT * from `crime`.`crime`")
        crime = b.fetchall()
        crime_list1 = list(crime)
        self.crime_info = []
        for i in crime_list1:
            self.crime_info.append(list(i))
        self.crime_tableWidget.setColumnWidth(0, 121)
        self.crime_tableWidget.setColumnWidth(1, 327)
        self.crime_tableWidget.setColumnWidth(2, 121)
        self.crime_tableWidget.setColumnWidth(3, 121)
        self.crime_tableWidget.setColumnWidth(4, 121)
        self.crime_tableWidget.setColumnWidth(5, 121)
        # connections ={
        #     'conn1' : pymysql.connect(host='127.0.0.1',
        #                        port=3306,
        #                        user='root',
        #                        password='0000',
        #                        db='policearea'),
        #     'conn2': pymysql.connect(host='127.0.0.1',
        #                              port=3306,
        #                              user='root',
        #                              password='0000',
        #                              db='crime')
        # }
        # a = connections['conn1'].cursor()
        # a.execute("SELECT * from `policearea`.`policearea`")
        # police = a.fetchall()
        # police_list1 = list(police)
        # self.police_info = []
        # for i in police_list1:
        #     self.police_info.append(list(i))
        #
        # # tableWidget 열 넓이 조절
        # self.police_tableWidget.setColumnWidth(0, 121)
        # self.police_tableWidget.setColumnWidth(1, 121)
        # self.police_tableWidget.setColumnWidth(2, 121)
        # self.police_tableWidget.setColumnWidth(3, 121)
        # self.police_tableWidget.setColumnWidth(4, 121)
        # self.police_tableWidget.setColumnWidth(5, 327)
        # # conn2 = pymysql.connect(host='127.0.0.1',
        # #                        port=3306,
        # #                        user='root',
        # #                        password='0000',
        # #                        db='crime')
        # b = connections['conn2'].cursor()
        # b.execute("SELCET * from `crime`.`crime`")
        # crime = b.fetchall()
        # crime_list1 = list(crime)
        # self.crime_info = []
        # for i in crime_list1:
        #     self.crime_info.append(list(i))
        # self.crime_tableWidget.setColumnWidth(0, 121)
        # self.crime_tableWidget.setColumnWidth(1, 327)
        # self.crime_tableWidget.setColumnWidth(2, 121)
        # self.crime_tableWidget.setColumnWidth(3, 121)
        # self.crime_tableWidget.setColumnWidth(4, 121)
        # self.crime_tableWidget.setColumnWidth(5, 121)
        #
        # conn1 = pymysql.connect(host='127.0.0.1',
        #                        port=3306,
        #                        user='root',
        #                        password='0000',
        #                        db='policearea')
        # a = conn1.cursor()
        # a.execute("SELECT * from `policearea`.`policearea`")
        # police = a.fetchall()
        # police_list1 = list(police)
        # self.police_info = []
        # for i in police_list1:
        #     self.police_info.append(list(i))
        #
        # # tableWidget 열 넓이 조절
        # self.police_tableWidget.setColumnWidth(0, 121)
        # self.police_tableWidget.setColumnWidth(1, 121)
        # self.police_tableWidget.setColumnWidth(2, 121)
        # self.police_tableWidget.setColumnWidth(3, 121)
        # self.police_tableWidget.setColumnWidth(4, 121)
        # self.police_tableWidget.setColumnWidth(5, 327)

    def showlist(self):
        Row = 0
        self.police_tableWidget.setRowCount(len(self.police_info))
        for s in self.police_info:
            self.police_tableWidget.setItem(Row, 0, QTableWidgetItem(s[0]))
            self.police_tableWidget.setItem(Row, 1, QTableWidgetItem(s[1]))
            self.police_tableWidget.setItem(Row, 2, QTableWidgetItem(s[2]))
            self.police_tableWidget.setItem(Row, 3, QTableWidgetItem(s[3]))
            self.police_tableWidget.setItem(Row, 4, QTableWidgetItem(s[4]))
            self.police_tableWidget.setItem(Row, 5, QTableWidgetItem(s[5]))
            Row += 1

    def searchPolice(self):
        word = self.police_lineEdit.text()
        search_list = []
        for i in range(len(self.police_info)):
            if word in self.police_info[i][0]:
                search_list.append(self.police_info[i])
        Row = 0
        self.police_tableWidget.setRowCount(len(search_list))

        for s in search_list:
            self.police_tableWidget.setItem(Row, 0, QTableWidgetItem(s[0]))
            self.police_tableWidget.setItem(Row, 1, QTableWidgetItem(s[1]))
            self.police_tableWidget.setItem(Row, 2, QTableWidgetItem(s[2]))
            self.police_tableWidget.setItem(Row, 3, QTableWidgetItem(s[3]))
            self.police_tableWidget.setItem(Row, 4, QTableWidgetItem(s[4]))
            self.police_tableWidget.setItem(Row, 5, QTableWidgetItem(s[5]))
            Row += 1

    def searchCrime(self):
        word = self.crime_lineEdit.text()
        search_list = []
        for i in range(len(self.crime_info)):
            if word in self.crime_info[i][1]:
                search_list.append(self.crime_info[i])
        Row = 0
        self.crime_tableWidget.setRowCount(len(search_list))

        for j in search_list:
            self.crime_tableWidget.setItem(Row, 0, QTableWidgetItem(str(int(j[0]))))
            self.crime_tableWidget.setItem(Row, 1, QTableWidgetItem(j[1]))
            self.crime_tableWidget.setItem(Row, 2, QTableWidgetItem(str(int(j[2]))))
            self.crime_tableWidget.setItem(Row, 3, QTableWidgetItem(str(int(j[3]))))
            self.crime_tableWidget.setItem(Row, 4, QTableWidgetItem(str(int(j[4]))))
            self.crime_tableWidget.setItem(Row, 5, QTableWidgetItem(str(int(j[5]))))
            Row += 1


    def modify(self):
        self.tabWidget.setCurrentIndex(1)

    def add_delete(self):
        self.tabWidget.setCurrentIndex(2)

    def main(self):
        self.tabWidget.setCurrentIndex(0)

    # #해당 지방청의 경찰서 혹은 파출소의 새로운 범죄 항목 추가
    # def Add_New_Crime(self):
    #     self.db = pymysql.connect(host='127.0.0.1',
    #                                port=3306,
    #                                user='root',
    #                                password='0000',
    #                                db='criminal'
    #                                )
    #
    #     self.cur = self.db.cursor()
    #
    #
    #     # police_office_title = self.lineEdit.text()
    #     crime_occurrence_year = self.lineEdit1.text()
    #     crime_category = self.lineEdit2.text()
    #     crime_number = self.lineEdit3.text()
    #
    # def Edit_Number_Criminal(self):
    #     pass
    #
    # def Delete_Category_Criminal(self):
    #     pass

if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = Search()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(881)
    widget.setFixedWidth(1771)
    widget.show()
    app.exec_()