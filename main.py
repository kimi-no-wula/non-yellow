import sys
from random import randint, choice

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_yellow_ellipse = QtWidgets.QPushButton(self.centralwidget)
        self.btn_yellow_ellipse.setGeometry(QtCore.QRect(580, 700, 111, 41))
        self.btn_yellow_ellipse.setObjectName("btn_yellow_ellipse")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_yellow_ellipse.setText(_translate("MainWindow", "Рисовать"))


class YellowEllipse(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(700, 800)
        self.setWindowTitle('main')
        self.do_paint = False
        self.btn_yellow_ellipse.clicked.connect(self.touched)

    def touched(self):
        self.paint()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            # Создаем объект QPainter для рисования
            self.qp = QPainter()
            # Начинаем процесс рисования
            self.qp.begin(self)
            self.draw_smth()
            # Завершаем рисование
            self.qp.end()
            self.do_paint = False

    def draw_smth(self):
        self.qp.setBrush(QColor(0, 0, 255))
        z, x, y = randint(5, 200), randint(5, 680), randint(5, 580)

        color = QColor(choice(QColor.colorNames()))

        self.qp.setBrush(QColor(color))
        self.qp.drawEllipse(x, y, z, z)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowEllipse()
    ex.show()
    sys.exit(app.exec())
