import pymysql
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import Qt
from PyQt5.QtCore import pyqtSlot
import csv
from PyQt5.QtCore import QDate, Qt


form_widget = uic.loadUiType('population.ui')[0]
class Search(QWidget, form_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.search_pushButton.clicked.connect(self.search)
        conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               password='0000',
                               db='safety')
        a = conn.cursor()
        a.execute("SELECT * from `safety`.`경찰서`")
        police = a.fetchall()
        police_list1 = list(police)
        self.police_info = []
        for i in police_list1:
            self.police_info.append(list(i))

        # tableWidget 열 넓이 조절
        self.tableWidget.setColumnWidth(0, 121)
        self.tableWidget.setColumnWidth(1, 121)
        self.tableWidget.setColumnWidth(2, 121)
        self.tableWidget.setColumnWidth(3, 121)
        self.tableWidget.setColumnWidth(4, 327)


    def showlist(self):
        Row = 0
        self.tableWidget.setRowCount(len(self.police_info))
        for s in self.police_info:
            self.tableWidget.setItem(Row, 0, QTableWidgetItem(s[0]))
            self.tableWidget.setItem(Row, 1, QTableWidgetItem(s[1]))
            self.tableWidget.setItem(Row, 2, QTableWidgetItem(s[2]))
            self.tableWidget.setItem(Row, 3, QTableWidgetItem(s[3]))
            self.tableWidget.setItem(Row, 4, QTableWidgetItem(s[4]))
            Row += 1

    def search(self):
        word = self.search_lineEdit.text()
        search_list = []
        for i in range(len(self.police_info)):
            if word in self.police_info[i][0]:
                search_list.append(self.police_info[i])

        Row = 0
        self.tableWidget.setRowCount(len(search_list))
        for s in search_list:
            self.tableWidget.setItem(Row, 0, QTableWidgetItem(s[0]))
            self.tableWidget.setItem(Row, 1, QTableWidgetItem(s[1]))
            self.tableWidget.setItem(Row, 2, QTableWidgetItem(s[2]))
            self.tableWidget.setItem(Row, 3, QTableWidgetItem(s[3]))
            self.tableWidget.setItem(Row, 4, QTableWidgetItem(s[4]))
            Row += 1


if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = Search()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(768)
    widget.setFixedWidth(1024)
    widget.show()
    app.exec_()