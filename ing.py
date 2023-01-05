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
        self.police_tableWidget.doubleClicked.connect(self.police_cellclicked)
        self.police_lineEdit.returnPressed.connect(self.searchPolice)
        self.crime_pushButton.clicked.connect(self.searchCrime)
        self.crime_tableWidget.doubleClicked.connect(self.cellclicked)
        self.crime_lineEdit.returnPressed.connect(self.searchCrime)
        self.modify_pushButton.clicked.connect(self.modify)
        self.add_delete_pushButton.clicked.connect(self.add_delete)
        self.gomain_button.clicked.connect(self.main)
        self.gotomain_button.clicked.connect(self.main)
        self.district_office_combobox.currentIndexChanged.connect(self.fill_combobox_selected)
        self.police_combobox.currentIndexChanged.connect(self.fill_combobox_selected2)
        self.detail_combobox.currentIndexChanged.connect(self.fill_lineEdit_combobox)
        self.modify_button.clicked.connect(self.modify_data)



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

    def showlist(self):  # 경찰서 조회하는 함수, 연결된 시그널 없음..

        self.police_division = ['구분']
        self.police_number = ['전화번호']
        self.police_address = ['주소']
        mydb1 = MySQLdb.connect(host='127.0.0.1',
                                # port=3306,
                                user='root',
                                password='0000',
                                db='policearea')
        a = mydb1.cursor()
        a.execute("SELECT * FROM `policearea`.`policearea`")
        result = a.fetchall()
        if result:
            for i in result:
                self.police_division.append(str(i[3]))
                self.police_number.append(str(i[4]))
                self.police_address.append(str(i[5]))
        mydb1.close()
        print(self.police_division)
        print(self.police_number)
        print(self.police_address)

        Row = 0
        self.police_tableWidget.setRowCount(len(self.police_info))
        for s in self.police_info:
            self.police_tableWidget.setItem(Row, 0, QTableWidgetItem(s[0]))
            self.police_tableWidget.setItem(Row, 1, QTableWidgetItem(s[2]))
            self.police_tableWidget.setItem(Row, 2, QTableWidgetItem(s[3]))
            self.police_tableWidget.setItem(Row, 3, QTableWidgetItem(s[4]))
            self.police_tableWidget.setItem(Row, 4, QTableWidgetItem(s[5]))
            self.police_tableWidget.setItem(Row, 5, QTableWidgetItem(s[6]))
            Row += 1
    def searchPolice(self):
        word = self.police_lineEdit.text()
        mydb1 = MySQLdb.connect(host='127.0.0.1',
                                # port=3306,
                                user='root',
                                password='0000',
                                db='policearea')
        a = mydb1.cursor()
        a.execute(f"SELECT * FROM `policearea`.`policearea` where 지방청 like '%{word}%'")
        police = a.fetchall()

        Row = 0
        self.police_tableWidget.setRowCount(len(police))

        for s in police:
            self.police_tableWidget.setItem(Row, 0, QTableWidgetItem(s[0]))
            self.police_tableWidget.setItem(Row, 1, QTableWidgetItem(s[1]))
            self.police_tableWidget.setItem(Row, 2, QTableWidgetItem(s[2]))
            self.police_tableWidget.setItem(Row, 3, QTableWidgetItem(s[3]))
            self.police_tableWidget.setItem(Row, 4, QTableWidgetItem(s[4]))
            self.police_tableWidget.setItem(Row, 5, QTableWidgetItem(s[5]))
            Row += 1
        mydb1.close()
    def searchCrime(self):
        word = self.crime_lineEdit.text()
        mydb2 = MySQLdb.connect(host='127.0.0.1',
                               # port=3306,
                               user='root',
                               password='0000',
                               db='crime')
        b = mydb2.cursor()
        b.execute("SELECT * from `crime`.`crime`")
        crime = b.fetchall()

        Row = 0
        self.crime_tableWidget.setRowCount(len(crime))

        for j in crime:
            self.crime_tableWidget.setItem(Row, 0, QTableWidgetItem(str(int(j[0]))))
            self.crime_tableWidget.setItem(Row, 1, QTableWidgetItem(j[1]))
            self.crime_tableWidget.setItem(Row, 2, QTableWidgetItem(str(int(j[2]))))
            self.crime_tableWidget.setItem(Row, 3, QTableWidgetItem(str(int(j[3]))))
            self.crime_tableWidget.setItem(Row, 4, QTableWidgetItem(str(int(j[4]))))
            self.crime_tableWidget.setItem(Row, 5, QTableWidgetItem(str(int(j[5]))))
            Row += 1
        mydb2.close()

    def cellclicked(self, event):
        reply = QMessageBox.question(self, "알림", "추가, 삭제 탭으로 이동 하시겠습니까?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.tabWidget.setCurrentIndex(2)
        else:
            pass

    def police_cellclicked(self, event):
        reply = QMessageBox.question(self, "알림", "수정 탭으로 이동하시겠습니까?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.tabWidget.setCurrentIndex(1)
            mydb1 = MySQLdb.connect(host='127.0.0.1',
                                    # port=3306,
                                    user='root',
                                    password='0000',
                                    db='policearea')
            a = mydb1.cursor()
            a.execute("SELECT DISTINCT 지방청 from `policearea`.`policearea`")
            result = a.fetchall()
            if result:
                for i in result:
                    self.district_office_combobox.addItem(str(i[0]))
            mydb1.close()
        else:
            pass
    def modify(self):
        self.tabWidget.setCurrentIndex(1)
        mydb1 = MySQLdb.connect(host='127.0.0.1',
                                # port=3306,
                                user='root',
                                password='0000',
                                db='policearea')
        a = mydb1.cursor()
        a.execute("SELECT DISTINCT 지방청 from `policearea`.`policearea`")
        result = a.fetchall()
        if result:
            for i in result:
                self.district_office_combobox.addItem(str(i[0]))
        mydb1.close()
    def fill_combobox_selected(self):
        mydb1 = MySQLdb.connect(host='127.0.0.1',
                                # port=3306,
                                user='root',
                                password='0000',
                                db='policearea')
        a = mydb1.cursor()
        a.execute("SELECT DISTINCT 경찰서 from `policearea`.`policearea` WHERE 지방청 = '"+self.district_office_combobox.currentText()+"'")
        result = a.fetchall()
        print('hi')
        self.police_combobox.clear()
        # self.detail_combobox.clear()
        if result:
            for j in result:
                self.police_combobox.addItem(str(j[0]))
        mydb1.close()
    def fill_combobox_selected2(self):
        mydb1 = MySQLdb.connect(host='127.0.0.1',
                                # port=3306,
                                user='root',
                                password='0000',
                                db='policearea')
        a = mydb1.cursor()
        b = mydb1.cursor()
        a.execute("SELECT DISTINCT 관서명 from `policearea`.`policearea` WHERE 경찰서 = '"+self.police_combobox.currentText()+"'")
        b.execute("SELECT * from `policearea`.`policearea` WHERE 경찰서 = '" + self.police_combobox.currentText() + "'")
        result = a.fetchall()
        result2 = b.fetchall()
        Row = 0
        self.modify_tableWidget.setRowCount(len(result2))
        if result2:
            for i in result2:
                self.modify_tableWidget.setItem(Row, 0, QTableWidgetItem(i[0]))
                self.modify_tableWidget.setItem(Row, 1, QTableWidgetItem(i[1]))
                self.modify_tableWidget.setItem(Row, 2, QTableWidgetItem(i[2]))
                self.modify_tableWidget.setItem(Row, 3, QTableWidgetItem(i[3]))
                self.modify_tableWidget.setItem(Row, 4, QTableWidgetItem(i[4]))
                self.modify_tableWidget.setItem(Row, 5, QTableWidgetItem(i[5]))
                Row += 1
        self.detail_combobox.clear()
        # self.detail_combobox.clear()
        if result:
            for j in result:
                self.detail_combobox.addItem(str(j[0]))
        mydb1.close()

    def fill_lineEdit_combobox(self):
        mydb1 = MySQLdb.connect(host='127.0.0.1',
                                # port=3306,
                                user='root',
                                password='0000',
                                db='policearea')
        a = mydb1.cursor()
        a.execute(
            "SELECT * from `policearea`.`policearea` WHERE 관서명 = '" + self.detail_combobox.currentText() + "'")
        result = a.fetchall()
        if result:
            for i in result:
                self.police_division_lineEdit.setText(str(i[3]))
                self.police_call_number_lineEdit.setText(str(i[4]))
                self.police_address_lineEdit.setText(str(i[5]))


        mydb1.close()

    def modify_data(self):
        mydb1 = MySQLdb.connect(host='127.0.0.1',
                                # port=3306,
                                user='root',
                                password='0000',
                                db='policearea')
        a = mydb1.cursor()
        a.execute("UPDATE `policearea`.`policearea` SET 구분 = '"+self.police_division_lineEdit.text() +"', 전화번호 = '"+self.police_call_number_lineEdit.text() +"', 주소 = '"+self.police_address_lineEdit.text() +"' WHERE 구분 = '"+self.detail_combobox.currentText()+"'")
        mydb1.commit()
        mydb1.close()
        self.modify_tableWidget.item(0, 3).setText(self.police_division_lineEdit.text())
        self.modify_tableWidget.item(0, 4).setText(self.police_call_number_lineEdit.text())
        self.modify_tableWidget.item(0, 5).setText(self.police_address_lineEdit.text())
        self.showlist()



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