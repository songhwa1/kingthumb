import sys
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import numpy as np
from PyQt5 import uic

form_class = uic.loadUiType("graphui.ui")[0]


class GraphWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        w = pg.PlotWidget(background='w')
        self.setCentralWidget(w)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    graph = GraphWidget()
    graph.show()
    app.exec_()
