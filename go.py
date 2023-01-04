from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox, QVBoxLayout
import sys
from PyQt5 import QtGui
import MySQLdb as mdb
class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Database Connection"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        self.btn = QPushButton("DB Connection")


        self.btn.clicked.connect(self.DBConnect)

        vbox.addWidget(self.btn)

        self.setLayout(vbox)

        self.show()

    def DBConnect(self):
        try:
            db = mdb.connect('localhost', 'root', '', 'pyqt5')
            QMessageBox.about(self, '연결', "성공적으로 데이터 베이스와 연결 되었습니다.")

        except mdb.Error as e:
            QMessageBox.about(self, '연결', "데이터 베이스 연결이 실패했습니다.")
            sys.exit()



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())