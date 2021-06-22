from re import T
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QTableWidget, QTableWidgetItem,
                             QAbstractItemView, QHeaderView, QMenu, QActionGroup, QAction, QMessageBox)
from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from sympy.core.evalf import pure_complex
from sympy.core.symbol import symbols

# importamos nuestros metodos
from metodosYformularios import *
import metodosYformularios.metodos_Unidad_2y3 as metodos
import metodosYformularios.metodos_unidad_4 as metodos_uni4
import metodosYformularios.metodosUnidad1 as metodos_uni1
import metodosYformularios.metodos_Unidad5 as metodos_uni5

from metodosYformularios.mensajesUi import Ui_Mensajes


import matplotlib.pyplot as plt
import numpy as np
import math as mt
import sys
from sympy.plotting import plot
import cmath

GLOBAL_STATE = 0


counter = 0
etiquetaHermite = "y'"
filasHermite = 2

tabla_unidad4_si_no = 0

tamanioInicialTabla = 183
posicionX = 1
posicionY = 1
cuantasFilasYColumnas = 3

class Mensajes_error(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Mensajes()
        self.ui.setupUi(self)

        self.ui.btnAceptar.clicked.connect(self.close)
        self.ui.btnClose.clicked.connect(self.close)

        def close(self):
            self.close()

        def moveWinsdow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
            
        self.ui.frame_2.mouseMoveEvent = moveWinsdow
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
                
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setStyleSheet("Background-color: rgb(242, 242, 242);")

        # Frame donde se encuentran los botones de cerrar, minimizar y maximizar
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1000, 31))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)  # poner Noframe
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        #self.frame.mouseMoveEvent = moveWindow

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(5, 8, 400, 16))
        self.label_10.setObjectName("label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(134, 155, 208);")

        # btn minimizar
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(900, 10, 16, 16))
        self.pushButton_8.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton_8.setMaximumSize(QtCore.QSize(17, 17))
        self.pushButton_8.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(
            "QPushButton {\n""border: none;\n""border-radius: 8px;\n""background-color: rgb(246, 221, 164);\n""}\n""QPushButton:hover {    \n""background-color: rgb(255, 255, 0);\n""}")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_6")

        # btn maximizar
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(930, 10, 16, 16))
        self.pushButton_9.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton_9.setMaximumSize(QtCore.QSize(17, 17))
        self.pushButton_9.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(
            "QPushButton {\n""border: none;\n""background-color: rgb(167, 227, 171);\n""border-radius: 8px;\n""}\n""QPushButton:hover { \n""background-color: rgb(55, 255, 0);\n""}")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_2")

        # btn cerrar
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(960, 10, 16, 16))
        self.pushButton_7.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton_7.setMaximumSize(QtCore.QSize(17, 17))
        self.pushButton_7.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(
            "QPushButton {\n""border: none;\n""background-color: rgb(246, 180, 180);\n""border-radius: 8px;\n""}\n""QPushButton:hover {        \n""background-color: rgba(255, 0, 0, 150);\n""}")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(134, 155, 208);")
        self.label_3.setGeometry(QtCore.QRect(400, 45, 211, 16))
        self.label_3.setObjectName("label_3")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 83, 21, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(134, 155, 208);")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 123, 20, 20))
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(134, 155, 208);")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 83, 21, 16))
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(134, 155, 208);")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(660, 45, 191, 20))
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(134, 155, 208);")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 45, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(134, 155, 208);")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(620, 45, 270, 16))
        self.label_9.setObjectName("label_8")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(134, 155, 208);")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 65, 60, 23))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("QComboBox{\n""background-color: rgb(242, 242, 242);\n""border-radius: 5px;\n""border: 2px solid rgb(232, 137, 137);\n""padding: 5px;\n""padding-left: 10px;\n""color: rgb(216, 55, 55)\n""}\n""QComboBox:hover{\n""border: 2px solid rgb(216, 55, 55);\n""border_left-color: rgb(215,55,55);\n""}\n""QComboBox::drop-down {\n""subcontrol-origin: padding;\n""subcontrol-position: top right;\n""width: 25px; \n""border-left-width: 3px;\n""border-left-color: rgb(232, 137, 137);\n""border-left-style: solid;\n""border-top-right-radius: 3px;\n""border-bottom-right-radius: 3px;    \n""background-image: url(recursos/row_baja.png);\n""background-position: center;\n""background-repeat: no-reperat;\n"" }\n""QComboBox QAbstractItemView {\n""color: rgb(216, 55, 55);    \n""background-color: rgb(242, 242, 242);\n""padding: 5px;\n""selection-background-color: rgb(232, 137 , 137);\n""}\n""")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.activated[str].connect(self.cambiar_metodos_cmb2)

        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(460, 80, 70, 26))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.setStyleSheet("QComboBox{\n""background-color: rgb(242, 242, 242);\n""border-radius: 5px;\n""border: 2px solid rgb(232, 137, 137);\n""padding: 5px;\n""padding-left: 10px;\n""color: rgb(216, 55, 55)\n""}\n""QComboBox:hover{\n""border: 2px solid rgb(216, 55, 55);\n""border_left-color: rgb(215,55,55);\n""}\n""QComboBox::drop-down {\n""subcontrol-origin: padding;\n""subcontrol-position: top right;\n""width: 25px; \n""border-left-width: 3px;\n""border-left-color: rgb(232, 137, 137);\n""border-left-style: solid;\n""border-top-right-radius: 3px;\n""border-bottom-right-radius: 3px;    \n""background-image: url(recursos/row_baja.png);\n""background-position: center;\n""background-repeat: no-reperat;\n"" }\n""QComboBox QAbstractItemView {\n""color: rgb(216, 55, 55);    \n""background-color: rgb(242, 242, 242);\n""padding: 5px;\n""selection-background-color: rgb(232, 137 , 137);\n""}\n""")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.activated[str].connect(self.usar_tabla_unidad4_o_no)

        # self.comboBox_2.setGeometry(QtCore.QRect(200, 80, 200, 26))

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 75, 51, 24))
        self.lineEdit_2.setStyleSheet(
            "background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(430, 115, 51, 24))
        self.lineEdit_3.setStyleSheet(
            "background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(530, 75, 51, 24))
        self.lineEdit_4.setStyleSheet(
            "background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(660, 70, 51, 24))
        self.lineEdit_5.setStyleSheet(
            "background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(900, 150, 51, 24))
        self.lineEdit_6.setStyleSheet(
            "background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)

        self.lineOrden = QtWidgets.QLineEdit(self.centralwidget)
        self.lineOrden.setGeometry(QtCore.QRect(745, 70, 51, 24))
        self.lineOrden.setStyleSheet(
            "background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.lineOrden.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineOrden.setObjectName("lineOrden")
        self.lineOrden.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblOrden = QtWidgets.QLabel(self.centralwidget)
        self.lblOrden.setGeometry(QtCore.QRect(745, 45, 191, 20))
        self.lblOrden.setObjectName("lblOrden")
        self.lblOrden.setFont(font)
        self.lblOrden.setStyleSheet("color: rgb(134, 155, 208);")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 330, 931, 220))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setStyleSheet("QTableWidget{\n"" border: 1px solid;\n"" color: rgb(134, 155, 208);\n"" border-color: rgb(134, 155, 208);\n"" border-radius: 15px;\n"" \n""}\n""\n""QTableWidget:hover{\n"" border: 1px solid;\n"" border-radius: 15px;\n"" border-color: rgb(134, 155, 208);\n""}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

        # Caja de texto de respuesta unidad 4
        self.cajaTexto = QtWidgets.QTextEdit(self.centralwidget)
        self.cajaTexto.setGeometry(QtCore.QRect(30, 330, 931, 200))
        self.cajaTexto.setStyleSheet("background-color: rgb(242, 242, 242);\n"
                                     "color: rgb(124, 152, 255);\n"
                                     "border: 1px solid;\n"
                                     "border-color: rgb(116, 125, 255);\n"
                                     "border-radius: 10px;")
        self.cajaTexto.setObjectName("cajaTexto")
        self.cajaTexto.setReadOnly(True)

        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(170, 120, 823, 81))
        self.tableWidget_2.setStyleSheet("QTableWidget{\n"" border: 1px solid;\n"" color: rgb(134, 155, 208);\n"" border-color: rgb(134, 155, 208);\n"" border-radius: 10px;\n"" \n""}\n""\n""QTableWidget:hover{\n"" border: 1px solid;\n"" border-radius: 10px;\n"" border-color: rgb(134, 155, 208);\n""}")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 255, 100, 50))
        self.pushButton.setStyleSheet(
            "QPushButton {\n""border: 2px solid;\n""border-radius: 20px;\n""font: 12pt \"MS Shell Dlg 2\";\n""border-color: rgb(150, 173, 234);\n""color: \'#96ADEA\'\n""}\n""\n""QPushButton:hover {\n""background-color: rgb(150, 173, 234);\n""color: \'#ffffff\';\n""}\n""")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 255, 100, 50))
        self.pushButton_2.setStyleSheet(
            "QPushButton {\n""border: 2px solid;\n""color: \'#E88989\';\n""border-color: rgb(232, 137, 137);\n""border-radius: 20px;\n""font: 12pt \"MS Shell Dlg 2\";\n""\n""}\n""QPushButton:hover {\n""background-color: rgb(232, 137, 137);\n""color: \'#ffffff\'\n""\n""\n""}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(425, 575, 100, 50))
        self.pushButton_3.setStyleSheet("QPushButton {\n"" border: 2px solid;\n"" border-radius: 20px;\n"" font: 12pt \"MS Shell Dlg 2\";\n"" border-color: rgb(150, 173, 234);\n""    color: \'#96ADEA\'\n""}\n""\n""QPushButton:hover {\n""    background-color: rgb(150, 173, 234);\n""    color: \'#ffffff\';\n""}\n""/*\n""QPushButton:pressed {\n"" background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"" stop: 0 #dadbde, stop: 1 #96adea);\n""\n""}*/")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 110, 80, 16))
        self.label_12.setStyleSheet("color: \'#96ADEA\'\n""")
        self.label_12.setObjectName("label_12")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 127, 65, 40))
        self.pushButton_5.setStyleSheet(
            "QPushButton {\n""border: 2px solid;\n""border-radius: 15px;\n""font: 7pt \"MS Shell Dlg 2\";\n""border-color: rgb(150, 173, 234);\n""color: \'#96ADEA\'\n""}\n""\n""QPushButton:hover {\n""background-color: rgb(150, 173, 234);\n""color: \'#ffffff\';\n""}\n""")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(85, 127, 65, 40))
        self.pushButton_6.setStyleSheet(
            "QPushButton {\n""border: 2px solid;\n""color: \'#E88989\';\n""border-color: rgb(232, 137, 137);\n""border-radius: 15px;\n""font: 7pt \"MS Shell Dlg 2\";\n""}\n""QPushButton:hover {\n""background-color: rgb(232, 137, 137);\n""color: \'#ffffff\'\n""\n""\n""}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 174, 80, 16))
        self.label_13.setStyleSheet("color: \'#96ADEA\'\n""")
        self.label_13.setObjectName("label_12")

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 192, 65, 40))
        self.pushButton_10.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(
            "QPushButton {\n""border: 2px solid;\n""border-radius: 15px;\n""font: 8pt \"MS Shell Dlg 2\";\n""border-color: rgb(150, 173, 234);\n""color: \'#96ADEA\'\n""}\n""\n""QPushButton:hover {\n""background-color: rgb(150, 173, 234);\n""color: \'#ffffff\';\n""}\n""")
        self.pushButton_10.setObjectName("pushButton_10")

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(85, 192, 65, 40))
        self.pushButton_11.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(
            "QPushButton {\n""border: 2px solid;\n""color: \'#E88989\';\n""border-color: rgb(232, 137, 137);\n""border-radius: 15px;\n""font: 8pt \"MS Shell Dlg 2\";\n""}\n""QPushButton:hover {\n""background-color: rgb(232, 137, 137);\n""color: \'#ffffff\'\n""\n""\n""}")
        self.pushButton_11.setObjectName("pushButton_11")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 118, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(134, 155, 208);")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 145, 131, 24))
        self.lineEdit.setStyleSheet(
            "background-color: rgb(242, 242, 242);\n""image: url(recursos/barra2.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(font)

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 80, 170, 35))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setStyleSheet("QComboBox{\n""background-color: rgb(242, 242, 242);\n""border-radius: 5px;\n""border: 2px solid rgb(232, 137, 137);\n""padding: 5px;\n""padding-left: 10px;\n""color: rgb(216, 55, 55)\n""}\n""QComboBox:hover{\n""border: 2px solid rgb(216, 55, 55);\n""border_left-color: rgb(215,55,55);\n""}\n""QComboBox::drop-down {\n""subcontrol-origin: padding;\n""subcontrol-position: top right;\n""width: 25px; \n""border-left-width: 3px;\n""border-left-color: rgb(232, 137, 137);\n""border-left-style: solid;\n""border-top-right-radius: 3px;\n""border-bottom-right-radius: 3px;    \n""background-image: url(recursos/row_baja.png);\n""background-position: center;\n""background-repeat: no-reperat;\n"" }\n""QComboBox QAbstractItemView {\n""color: rgb(216, 55, 55);    \n""background-color: rgb(242, 242, 242);\n""padding: 5px;\n""selection-background-color: rgb(232, 137 , 137);\n""}\n""")
        self.comboBox_2.activated[str].connect(self.metodos_de_cada_unidad)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 45, 140, 16))
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(134, 155, 208);")

        # label para interpolacion de hermite
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(870, 70, 100, 16))
        self.label_11.setObjectName("label_11")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(134, 155, 208);")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(900, 130, 200, 16))
        self.label_14.setObjectName("label_14")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(134, 155, 208);")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_ver_tabla = QtWidgets.QLabel(self.centralwidget)
        self.label_ver_tabla.setGeometry(QtCore.QRect(460, 45, 150, 16))
        self.label_ver_tabla.setObjectName("label_ver_tabla")
        self.label_ver_tabla.setFont(font)
        self.label_ver_tabla.setStyleSheet("color: rgb(134, 155, 208);")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        # posicion x , posicion y , largo, ancho
        self.radioButton.setGeometry(QtCore.QRect(620, 78, 82, 23))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setStyleSheet(
            "QRadioButton::indicator {\n""border: 2px solid #96adea;\n""width: 15px;\n""height: 15px;\n""border-radius: 9px;\n""background: rgb(242,242,242);\n""}\n""QRadioButton::indicator:hover {\n""border: 2px solid #7284b1;\n""}\n""QRadioButton::indicator:checked {\n""background: 2px solid #96adea;\n""border: 2px solid #7284b1;    \n""}\n""")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(700, 78, 82, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setStyleSheet(
            "QRadioButton::indicator {\n""border: 2px solid #96adea;\n""width: 15px;\n""height: 15px;\n""border-radius: 9px;\n""background: rgb(242,242,242);\n""}\n""QRadioButton::indicator:hover {\n""border: 2px solid #7284b1;\n""}\n""QRadioButton::indicator:checked {\n""background: 2px solid #96adea;\n""border: 2px solid #7284b1;    \n""}\n""")

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(780, 78, 82, 23))
        self.radioButton_3.setObjectName("radioButton")
        self.radioButton_3.setStyleSheet(
            "QRadioButton::indicator {\n""border: 2px solid #96adea;\n""width: 15px;\n""height: 15px;\n""border-radius: 9px;\n""background: rgb(242,242,242);\n""}\n""QRadioButton::indicator:hover {\n""border: 2px solid #7284b1;\n""}\n""QRadioButton::indicator:checked {\n""background: 2px solid #96adea;\n""border: 2px solid #7284b1;    \n""}\n""")

        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(860, 78, 82, 23))
        self.radioButton_4.setObjectName("radioButton")
        self.radioButton_4.setStyleSheet(
            "QRadioButton::indicator {\n""border: 2px solid #96adea;\n""width: 15px;\n""height: 15px;\n""border-radius: 9px;\n""background: rgb(242,242,242);\n""}\n""QRadioButton::indicator:hover {\n""border: 2px solid #7284b1;\n""}\n""QRadioButton::indicator:checked {\n""background: 2px solid #96adea;\n""border: 2px solid #7284b1;    \n""}\n""")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Componentes unidad 4
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)

        self.funcion_uni4 = QtWidgets.QLineEdit(self.centralwidget)
        self.funcion_uni4.setGeometry(QtCore.QRect(200, 180, 131, 24))
        self.funcion_uni4.setStyleSheet(
            "background-color: rgb(242, 242, 242);\n""image: url(recursos/barra2.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.funcion_uni4.setObjectName("funcion_uni4")
        self.funcion_uni4.setFont(font)

        self.nivel_uni4 = QtWidgets.QLineEdit(self.centralwidget)
        self.nivel_uni4.setGeometry(QtCore.QRect(760, 180, 51, 24))
        self.nivel_uni4.setStyleSheet(
            "background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.nivel_uni4.setObjectName("nivel_uni4")
        self.nivel_uni4.setFont(font)

        self.puntoInicial_uni4 = QtWidgets.QLineEdit(self.centralwidget)
        self.puntoInicial_uni4.setGeometry(QtCore.QRect(440, 180, 51, 24))
        self.puntoInicial_uni4.setStyleSheet(
            "background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.puntoInicial_uni4.setObjectName("puntoInicial_uni4")
        self.puntoInicial_uni4.setFont(font)

        self.h_uni4 = QtWidgets.QLineEdit(self.centralwidget)
        self.h_uni4.setGeometry(QtCore.QRect(600, 180, 51, 24))
        self.h_uni4.setStyleSheet(
            "background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.h_uni4.setObjectName("h_uni4")
        self.h_uni4.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_funcion_uni4 = QtWidgets.QLabel(self.centralwidget)
        self.label_funcion_uni4.setGeometry(QtCore.QRect(200, 140, 150, 16))
        self.label_funcion_uni4.setObjectName("label_funcion_uni4")
        self.label_funcion_uni4.setFont(font)
        self.label_funcion_uni4.setStyleSheet("color: rgb(134, 155, 208);")

        self.label_puntoInicial_uni4 = QtWidgets.QLabel(self.centralwidget)
        self.label_puntoInicial_uni4.setGeometry(
            QtCore.QRect(440, 140, 150, 16))
        self.label_puntoInicial_uni4.setObjectName("label_puntoInicial_uni4")
        self.label_puntoInicial_uni4.setFont(font)
        self.label_puntoInicial_uni4.setStyleSheet(
            "color: rgb(134, 155, 208);")

        self.label_h_uni4 = QtWidgets.QLabel(self.centralwidget)
        self.label_h_uni4.setGeometry(QtCore.QRect(600, 140, 150, 16))
        self.label_h_uni4.setObjectName("label_h_uni4")
        self.label_h_uni4.setFont(font)
        self.label_h_uni4.setStyleSheet("color: rgb(134, 155, 208);")

        self.label_nivel_uni4 = QtWidgets.QLabel(self.centralwidget)
        self.label_nivel_uni4.setGeometry(QtCore.QRect(760, 140, 150, 16))
        self.label_nivel_uni4.setObjectName("label_nivel_uni4")
        self.label_nivel_uni4.setFont(font)
        self.label_nivel_uni4.setStyleSheet("color: rgb(134, 155, 208);")

        # Componentes de integrales dobles y triples
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.funcion_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.funcion_txt.setGeometry(QtCore.QRect(260, 155, 141, 31))
        self.funcion_txt.setFont(font)
        self.funcion_txt.setStyleSheet(
            "background-color: rgb(242, 242, 242);\n""image: url(recursos/barra2.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.funcion_txt.setObjectName("funcion_txt")

        self.lbl_integral1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_integral1.setGeometry(QtCore.QRect(230, 140, 25, 50))
        self.lbl_integral1.setStyleSheet(
            "background-image: url(recursos/integral.png);")
        self.lbl_integral1.setText("")
        self.lbl_integral1.setObjectName("lbl_integral1")

        self.b0 = QtWidgets.QLineEdit(self.centralwidget)
        self.b0.setGeometry(QtCore.QRect(260, 110, 21, 20))
        self.b0.setFont(font)
        self.b0.setStyleSheet(
            "border: 1px solid;\n""border-color: rgb(240, 240, 240);\n""border-bottom-color: rgb(232, 137, 137);\n""color: rgb(232, 137, 137);\n""\n""")
        self.b0.setText("")
        self.b0.setObjectName("b0")

        self.a0 = QtWidgets.QLineEdit(self.centralwidget)
        self.a0.setGeometry(QtCore.QRect(215, 200, 21, 20))
        self.a0.setFont(font)
        self.a0.setStyleSheet(
            "border: 1px solid;\n""border-color: rgb(240, 240, 240);\n""border-bottom-color: rgb(232, 137, 137);\n""color: rgb(232, 137, 137);\n""\n""")
        self.a0.setText("")
        self.a0.setObjectName("a0")

        self.lbl_integral2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_integral2.setGeometry(QtCore.QRect(190, 140, 25, 50))
        self.lbl_integral2.setStyleSheet(
            "background-image: url(recursos/integral.png);")
        self.lbl_integral2.setText("")
        self.lbl_integral2.setObjectName("lbl_integral2")

        self.b1 = QtWidgets.QLineEdit(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(215, 110, 21, 20))
        self.b1.setFont(font)
        self.b1.setStyleSheet(
            "border: 1px solid;\n""border-color: rgb(240, 240, 240);\n""border-bottom-color: rgb(232, 137, 137);\n""color: rgb(232, 137, 137);\n""\n""")
        self.b1.setText("")
        self.b1.setObjectName("b1")

        self.a1 = QtWidgets.QLineEdit(self.centralwidget)
        self.a1.setGeometry(QtCore.QRect(175, 200, 21, 20))
        self.a1.setFont(font)
        self.a1.setStyleSheet(
            "border: 1px solid;\n""border-color: rgb(240, 240, 240);\n""border-bottom-color: rgb(232, 137, 137);\n""color: rgb(232, 137, 137);\n""\n""")
        self.a1.setText("")
        self.a1.setObjectName("a1")

        self.lbl_integral3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_integral3.setGeometry(QtCore.QRect(150, 140, 25, 50))
        self.lbl_integral3.setStyleSheet(
            "background-image: url(recursos/integral.png);")
        self.lbl_integral3.setText("")
        self.lbl_integral3.setObjectName("lbl_integral3")

        self.b2 = QtWidgets.QLineEdit(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(170, 110, 21, 20))
        self.b2.setFont(font)
        self.b2.setStyleSheet(
            "border: 1px solid;\n""border-color: rgb(240, 240, 240);\n""border-bottom-color: rgb(232, 137, 137);\n""color: rgb(232, 137, 137);\n""\n""")
        self.b2.setText("")
        self.b2.setObjectName("b2")

        self.a2 = QtWidgets.QLineEdit(self.centralwidget)
        self.a2.setGeometry(QtCore.QRect(140, 200, 21, 20))
        self.a2.setFont(font)
        self.a2.setStyleSheet(
            "border: 1px solid;\n""border-color: rgb(240, 240, 240);\n""border-bottom-color: rgb(232, 137, 137);\n""color: rgb(232, 137, 137);\n""\n""")
        self.a2.setText("")
        self.a2.setObjectName("a2")

        self.diff1 = QtWidgets.QComboBox(self.centralwidget)
        self.diff1.setGeometry(QtCore.QRect(420, 155, 41, 25))
        self.diff1.setStyleSheet("QComboBox{\n""    background-color: rgb(242, 242, 242);\n""    border-radius: 5px;\n""    border: 2px solid rgb(232, 137, 137);\n""    padding: 5px;\n""    padding-left: 5px;\n""    color: rgb(216, 55, 55)\n""}\n""QComboBox:hover{\n""    border: 2px solid rgb(216, 55, 55);\n""    border_left-color: rgb(215,55,55);\n""}\n""QComboBox::drop-down {\n""    subcontrol-origin: padding;\n""    subcontrol-position: top right;\n""    width: 10px; \n""    border-top-right-radius: 1px;\n""    border-bottom-right-radius: 1px;    \n""    background-image: url(:/imagenes/row_baja.png);\n""    background-position: center;\n""    background-repeat: no-reperat;\n"" }\n""QComboBox QAbstractItemView {\n""    color: rgb(216, 55, 55);    \n""    background-color: rgb(242, 242, 242);\n""    padding: 5px;\n""    selection-background-color: rgb(232, 137 , 137);\n""}\n""")
        self.diff1.setObjectName("diff1")
        self.diff1.activated[str].connect(self.control_diferenciacion_segundo_cmb)
        
        self.diff2 = QtWidgets.QComboBox(self.centralwidget)
        self.diff2.setGeometry(QtCore.QRect(470, 155, 41, 25))
        self.diff2.setStyleSheet("QComboBox{\n""    background-color: rgb(242, 242, 242);\n""    border-radius: 5px;\n""    border: 2px solid rgb(232, 137, 137);\n""    padding: 5px;\n""    padding-left: 5px;\n""    color: rgb(216, 55, 55)\n""}\n""QComboBox:hover{\n""    border: 2px solid rgb(216, 55, 55);\n""    border_left-color: rgb(215,55,55);\n""}\n""QComboBox::drop-down {\n""    subcontrol-origin: padding;\n""    subcontrol-position: top right;\n""    width: 10px; \n""    border-top-right-radius: 1px;\n""    border-bottom-right-radius: 1px;    \n""    background-image: url(:/imagenes/row_baja.png);\n""    background-position: center;\n""    background-repeat: no-reperat;\n"" }\n""QComboBox QAbstractItemView {\n""    color: rgb(216, 55, 55);    \n""    background-color: rgb(242, 242, 242);\n""    padding: 5px;\n""    selection-background-color: rgb(232, 137 , 137);\n""}\n""")
        self.diff2.setObjectName("diff2")
        self.diff2.activated[str].connect(self.control_diferenciacion_tercer_cmb)
        
        self.diff3 = QtWidgets.QComboBox(self.centralwidget)
        self.diff3.setGeometry(QtCore.QRect(520, 155, 41, 25))
        self.diff3.setStyleSheet("QComboBox{\n""    background-color: rgb(242, 242, 242);\n""    border-radius: 5px;\n""    border: 2px solid rgb(232, 137, 137);\n""    padding: 5px;\n""    padding-left: 5px;\n""    color: rgb(216, 55, 55)\n""}\n""QComboBox:hover{\n""    border: 2px solid rgb(216, 55, 55);\n""    border_left-color: rgb(215,55,55);\n""}\n""QComboBox::drop-down {\n""    subcontrol-origin: padding;\n""    subcontrol-position: top right;\n""    width: 10px; \n""    border-top-right-radius: 1px;\n""    border-bottom-right-radius: 1px;    \n""    background-image: url(:/imagenes/row_baja.png);\n""    background-position: center;\n""    background-repeat: no-reperat;\n"" }\n""QComboBox QAbstractItemView {\n""    color: rgb(216, 55, 55);    \n""    background-color: rgb(242, 242, 242);\n""    padding: 5px;\n""    selection-background-color: rgb(232, 137 , 137);\n""}\n""")
        self.diff3.setObjectName("diff3")

        self.cmb_doble_triple = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_doble_triple.setGeometry(QtCore.QRect(460, 80, 61, 25))
        self.cmb_doble_triple.setStyleSheet("QComboBox{\n"" background-color: rgb(242, 242, 242);\n"" border-radius: 5px;\n"" border: 2px solid rgb(232, 137, 137);\n"" padding: 5px;\n"" padding-left: 5px;\n"" color: rgb(216, 55, 55)\n""}\n""QComboBox:hover{\n"" border: 2px solid rgb(216, 55, 55);\n"" border_left-color: rgb(215,55,55);\n""}\n""QComboBox::drop-down {\n"" subcontrol-origin: padding;\n"" subcontrol-position: top right;\n"" width: 10px; \n"" border-top-right-radius: 1px;\n"" border-bottom-right-radius: 1px; \n"" background-image: url(:/imagenes/row_baja.png);\n"" background-position: center;\n"" background-repeat: no-reperat;\n"" }\n""QComboBox QAbstractItemView {\n"" color: rgb(216, 55, 55); \n"" background-color: rgb(242, 242, 242);\n"" padding: 5px;\n"" selection-background-color: rgb(232, 137 , 137);\n""}\n""")
        self.cmb_doble_triple.setObjectName("cmb_doble_triple")
        self.cmb_doble_triple.addItem("")
        self.cmb_doble_triple.addItem("")
        self.cmb_doble_triple.activated[str].connect(self.control_integral_doble_triple)

        self.lbl_cmb = QtWidgets.QLabel(self.centralwidget)
        self.lbl_cmb.setGeometry(QtCore.QRect(460, 45, 221, 16))
        self.lbl_cmb.setFont(font)
        self.lbl_cmb.setStyleSheet("color: rgb(134, 155, 208);")
        self.lbl_cmb.setObjectName("lbl_cmb")

        self.lbl_n = QtWidgets.QLabel(self.centralwidget)
        self.lbl_n.setGeometry(QtCore.QRect(600, 140, 30, 16))
        self.lbl_n.setStyleSheet("color: rgb(134, 155, 208);")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_n.setText("N")
        self.lbl_n.setFont(font)
        self.lbl_n.setObjectName("lbl_n")

        self.n_dobles = QtWidgets.QLineEdit(self.centralwidget)
        self.n_dobles.setGeometry(QtCore.QRect(600, 166, 30, 20))
        self.n_dobles.setFont(font)
        self.n_dobles.setStyleSheet(
            "border: 1px solid;\n""border-color: rgb(240, 240, 240);\n""border-bottom-color: rgb(232, 137, 137);\n""color: rgb(232, 137, 137);\n""\n""")
        self.n_dobles.setText("")
        self.n_dobles.setObjectName("n_dobles")


        #Widget para las integrales normales 
        self.lbl_integral_normal = QtWidgets.QLabel(self.centralwidget)
        self.lbl_integral_normal.setGeometry(QtCore.QRect(160, 165, 25, 50))
        self.lbl_integral_normal.setStyleSheet(
            "background-image: url(recursos/integral.png);")
        self.lbl_integral_normal.setText("")
        self.lbl_integral_normal.setObjectName("lbl_integral_normal")

        self.b0_normal = QtWidgets.QLineEdit(self.centralwidget)
        self.b0_normal.setGeometry(QtCore.QRect(190, 145, 21, 20))
        self.b0_normal.setFont(font)
        self.b0_normal.setStyleSheet(
            "border: 1px solid;\n""border-color: rgb(240, 240, 240);\n""border-bottom-color: rgb(232, 137, 137);\n""color: rgb(232, 137, 137);\n""\n""")
        self.b0_normal.setText("")
        self.b0_normal.setObjectName("b0_normal")

        self.a0_normal = QtWidgets.QLineEdit(self.centralwidget)
        self.a0_normal.setGeometry(QtCore.QRect(150, 222, 21, 20))
        self.a0_normal.setFont(font)
        self.a0_normal.setStyleSheet(
            "border: 1px solid;\n""border-color: rgb(240, 240, 240);\n""border-bottom-color: rgb(232, 137, 137);\n""color: rgb(232, 137, 137);\n""\n""")
        self.a0_normal.setText("")
        self.a0_normal.setObjectName("a0_normal")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        self.label_3.setText(_translate(
            "MainWindow", "Puntos en los que vamos a evaluar"))

        self.pushButton_8.setToolTip(
            QCoreApplication.translate("MainWindow", u"Minimizar", None))
        self.pushButton_8.setText("")

        self.pushButton_7.setToolTip(
            QCoreApplication.translate("MainWindow", u"Cerrar", None))
        self.pushButton_7.setText("")

        self.pushButton_9.setToolTip(
            QCoreApplication.translate("MainWindow", u"Maximizar", None))
        self.pushButton_9.setText("")

        self.label_4.setText(_translate("MainWindow", "#1"))
        self.label_5.setText(_translate("MainWindow", "#2"))
        self.label_6.setText(_translate("MainWindow", "#3"))
        self.label_7.setText(_translate(
            "MainWindow", "Numero de cifras significativas"))
        self.label_8.setText(_translate("MainWindow", "¿Que unidad?"))
        self.label_14.setText(_translate("MainWindow", "Evaluar en: "))
        self.label_9.setText(_translate(
            "MainWindow", "Seleccione el grado de la función spline"))
        self.label_10.setText("Analisis Numèrico")
        self.label_funcion_uni4.setText("Ingresa la función")
        self.label_puntoInicial_uni4.setText("Punto Inicial")
        self.label_h_uni4.setText("Valor de h")
        self.lblOrden.setText(_translate("MaunWindows", "Nivel"))
        self.label_nivel_uni4.setText("Nivel")
        self.label_12.setText(_translate("MainWindow", "COLUMNAS:"))
        self.pushButton.setText(_translate("MainWindow", "CALCULAR"))
        self.pushButton_2.setText(_translate("MainWindow", "LIMPIAR"))
        self.pushButton_3.setText(_translate("MainWindow", "GRAFICAR"))
        self.pushButton_5.setText(_translate(
            "MainWindow", "AGREGAR \n""COLUMNA"))
        self.pushButton_6.setText(_translate(
            "MainWindow", "ELIMINAR \n""COLUMNA"))
        self.pushButton_10.setText(_translate(
            "MainWindow", "AGREGAR \n""FILA"))
        self.pushButton_11.setText(_translate(
            "MainWindow", "ELIMINAR \n""FILA"))


        self.label_13.setText(_translate("MainWindows", "FILAS"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5"))

        self.comboBox_3.setItemText(0, _translate("MainWindow", "Si"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "No"))

        self.label_2.setText(_translate("MainWindow", "Ingresa la función"))
        self.label.setText(_translate("MainWindow", "Seleccione el metodo"))

        self.label_ver_tabla.setText(_translate(
            "MainWindow", "¿Trabajar con función?"))

        self.pushButton.clicked.connect(self.calcular)
        self.pushButton_2.clicked.connect(self.limpiar_Campos)
        self.pushButton_3.clicked.connect(self.graficar)
        self.pushButton_5.clicked.connect(
            self.control_agregar_columna_tabla_Unidad3)
        self.pushButton_6.clicked.connect(
            self.control_eliminar_columna_tabla_Unidad3)
        self.pushButton_10.clicked.connect(
            self.control_agregar_fila_tabla_Unidad3)
        self.pushButton_11.clicked.connect(
            self.control_eliminar_fila_tabla_Unidad3)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTextElideMode(Qt.ElideRight)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_2.setVisible(False)
        self.radioButton.setText(_translate("MainWindow", "Grado #0"))
        self.radioButton_2.setText(_translate("MainWindow", "Grado #1"))
        self.radioButton_3.setText(_translate("MainWindow", "Grado #2"))
        self.radioButton_4.setText(_translate("MainWindow", "Grado #3"))
        self.cmb_doble_triple.setItemText(
            0, _translate("MainWindow", "Dobles"))
        self.cmb_doble_triple.setItemText(
            1, _translate("MainWindow", "Triples"))
        self.lbl_cmb.setText(_translate(
            "MainWindow", "Seleccione el orden de la integral"))

        self.comboBox.setCurrentIndex(-1)

        # Validacion para solo aceptar numeros y signos en los txt
        self.lineEdit_2.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_3.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_4.setValidator(QtGui.QDoubleValidator())
        self.lineEdit_5.setValidator(QtGui.QDoubleValidator())

        # <------ vamos a ocultar todo al inicio ------------>

        # <---- dejamos solo los componentes que usaremos al inicio -->
        self.label_8.setVisible(True)
        self.comboBox.setVisible(True)

        # <-------- Ocultamos lo demas ------------->

        self.comboBox_2.setVisible(False)
        self.lineEdit_4.setVisible(False)
        self.lineEdit_3.setVisible(False)
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.label_6.setVisible(False)
        self.label_7.setVisible(False)
        self.label_12.setVisible(False)
        self.label_13.setVisible(False)
        self.lineEdit.setVisible(False)
        self.lineEdit_2.setVisible(False)
        self.lineEdit_3.setVisible(False)
        self.lineEdit_4.setVisible(False)
        self.lineEdit_5.setVisible(False)
        self.lineEdit_6.setVisible(False)
        self.pushButton_5.setVisible(False)
        self.pushButton_6.setVisible(False)
        self.pushButton_10.setVisible(False)
        self.pushButton_11.setVisible(False)
        self.label_ver_tabla.setVisible(False)
        self.label_14.setVisible(False)
        self.radioButton.setVisible(False)
        self.radioButton_2.setVisible(False)
        self.radioButton_3.setVisible(False)
        self.radioButton_4.setVisible(False)
        self.label_9.setVisible(False)
        self.comboBox_3.setVisible(False)
        self.funcion_uni4.setVisible(False)
        self.puntoInicial_uni4.setVisible(False)
        self.h_uni4.setVisible(False)
        self.label_funcion_uni4.setVisible(False)
        self.label_puntoInicial_uni4.setVisible(False)
        self.label_h_uni4.setVisible(False)
        self.nivel_uni4.setVisible(False)
        self.label_nivel_uni4.setVisible(False)
        self.cajaTexto.setVisible(False)
        self.tableWidget.setVisible(False)

        self.funcion_txt.setVisible(False)
        self.lbl_integral1.setVisible(False)
        self.lbl_integral2.setVisible(False)
        self.lbl_integral3.setVisible(False)
        self.a0.setVisible(False)
        self.a1.setVisible(False)
        self.a2.setVisible(False)
        self.b0.setVisible(False)
        self.b1.setVisible(False)
        self.b2.setVisible(False)
        self.diff1.setVisible(False)
        self.diff2.setVisible(False)
        self.diff3.setVisible(False)
        self.lbl_cmb.setVisible(False)
        self.cmb_doble_triple.setVisible(False)
        self.n_dobles.setVisible(False)
        self.lbl_n.setVisible(False)
        self.lbl_integral_normal.setVisible(False)
        self.a0_normal.setVisible(False)
        self.b0_normal.setVisible(False)

        self.lineOrden.setVisible(False)
        self.lblOrden.setVisible(False)

    # En este metodo vamos a capturar la posicion del primer combobox y luego dependiendo
    # de cual este seleccionado asi se llenara el otro combobox

    def cambiar_metodos_cmb2(self):
        cual = self.comboBox.currentIndex()
        self.tableWidget_2.setVisible(False)
        self.pushButton_5.setVisible(False)
        self.pushButton_6.setVisible(False)
        self.radioButton.setVisible(False)
        self.radioButton_2.setVisible(False)
        self.radioButton_3.setVisible(False)
        self.radioButton_4.setVisible(False)
        self.label_9.setVisible(False)
        self.label_14.setVisible(False)
        self.lineEdit_6.setVisible(False)
        self.label_ver_tabla.setVisible(False)
        self.comboBox_3.setVisible(False)
        self.label_12.setVisible(False)
        self.pushButton_10.setVisible(False)
        self.pushButton_11.setVisible(False)
        self.label_13.setVisible(False)
        self.funcion_uni4.setVisible(False)
        self.puntoInicial_uni4.setVisible(False)
        self.h_uni4.setVisible(False)
        self.label_funcion_uni4.setVisible(False)
        self.label_puntoInicial_uni4.setVisible(False)
        self.label_h_uni4.setVisible(False)
        self.tableWidget.setVisible(True)
        self.cajaTexto.setVisible(False)
        self.funcion_txt.setVisible(False)
        self.lbl_integral1.setVisible(False)
        self.lbl_integral2.setVisible(False)
        self.lbl_integral3.setVisible(False)
        self.a0.setVisible(False)
        self.a1.setVisible(False)
        self.a2.setVisible(False)
        self.b0.setVisible(False)
        self.b1.setVisible(False)
        self.b2.setVisible(False)
        self.diff1.setVisible(False)
        self.diff2.setVisible(False)
        self.diff3.setVisible(False)
        self.lbl_cmb.setVisible(False)
        self.cmb_doble_triple.setVisible(False)
        self.tableWidget.setVisible(False)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(9)
        self.tableWidget.clear()
        self.lineOrden.setVisible(False)
        self.lblOrden.setVisible(False)

        if cual == 0:  # Metodos de la primera unidad
            self.comboBox_2.setGeometry(QtCore.QRect(200, 80, 172, 24))
            self.label_10.setText('Series de Taylor')

            # Siempre limpiamos el combobox para evitar duplicados o cosas raras
            self.comboBox_2.clear()

            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")

            self.comboBox_2.setItemText(0, "Seleccione un metodo")
            self.comboBox_2.setItemText(1,  "ln(e+x)")
            self.comboBox_2.setItemText(2,  "e^(x^2)")
            self.comboBox_2.setItemText(3,  "sen(x)")
            self.comboBox_2.setItemText(4,  "cos(x)")
            self.comboBox_2.setItemText(5,  "e^x")
            self.comboBox_2.setItemText(6,  "sh(x)")
            self.comboBox_2.setItemText(7,  "ch(x)")
            self.comboBox_2.setItemText(8,  "arcsen(x)")
            self.comboBox_2.setItemText(9,  "ln(1+x)")
            self.comboBox_2.setItemText(10,  "1/(1+x^2)")
            self.comboBox_2.setItemText(11,  "arctg(x)")
            self.comboBox_2.setCurrentIndex(0)

            self.comboBox_2.setVisible(False)
            self.lineEdit_4.setVisible(False)
            self.lineEdit_3.setVisible(False)
            self.label.setVisible(False)
            self.label_2.setVisible(False)
            self.label_5.setVisible(False)
            self.label_6.setVisible(False)
            self.label_3.setVisible(False)
            self.label_4.setVisible(False)
            self.label_5.setVisible(False)
            self.label_6.setVisible(False)
            self.label_7.setVisible(False)
            self.lineEdit.setVisible(False)
            self.lineEdit_2.setVisible(False)
            self.lineEdit_3.setVisible(False)
            self.lineEdit_4.setVisible(False)
            self.lineEdit_5.setVisible(False)

          # <----------- Mostramos el combobox donde estan los metodos ---------->
            self.comboBox_2.setVisible(True)
            self.label.setVisible(True)

        elif cual == 1:  # Metodos de la segunda unidad
            self.comboBox_2.setGeometry(QtCore.QRect(200, 80, 172, 24))
            self.label_10.setText('Ecuaciones de una variable')

            # Siempre limpiamos el combobox para evitar duplicados o cosas raras
            self.comboBox_2.clear()
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")

            self.comboBox_2.setItemText(0,  "Seleccione un metodo")
            self.comboBox_2.setItemText(1,  "Biseccion")
            self.comboBox_2.setItemText(2,  "Falsa Posicion")
            self.comboBox_2.setItemText(3,  "Punto Fijo")
            self.comboBox_2.setItemText(4,  "Newton Raphson")
            self.comboBox_2.setItemText(5,  "Newton Raphson Mejorado")
            self.comboBox_2.setItemText(6,  "Secante")
            self.comboBox_2.setItemText(7,  "Ceros de polinomios")
            self.comboBox_2.setItemText(8,  "Horner")
            self.comboBox_2.setItemText(9, "Muller")
            self.comboBox_2.setItemText(10, "Bairstown")

            self.comboBox_2.setCurrentIndex(0)
            self.comboBox_2.setVisible(False)
            self.lineEdit_4.setVisible(False)
            self.lineEdit_3.setVisible(False)
            self.label.setVisible(False)
            self.label_2.setVisible(False)
            self.label_5.setVisible(False)
            self.label_6.setVisible(False)
            self.label_3.setVisible(False)
            self.label_4.setVisible(False)
            self.label_5.setVisible(False)
            self.label_6.setVisible(False)
            self.label_7.setVisible(False)
            self.lineEdit.setVisible(False)
            self.lineEdit_2.setVisible(False)
            self.lineEdit_3.setVisible(False)
            self.lineEdit_4.setVisible(False)
            self.lineEdit_5.setVisible(False)

          # <----------- Mostramos el combobox donde estan los metodos ---------->
            self.comboBox_2.setVisible(True)
            self.label.setVisible(True)

        elif cual == 2:  # Metodos de la unidad 3
            self.comboBox_2.setGeometry(QtCore.QRect(360, 45, 172, 24))
            self.label_10.setText('Interpolación y aproximacion lineal')

            self.comboBox_2.clear()
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")

            self.comboBox_2.setItemText(0,  "Seleccione un metodo")
            self.comboBox_2.setItemText(1,  "Interpolación Lineal")
            self.comboBox_2.setItemText(2,  "Interpolación cuadratica")
            self.comboBox_2.setItemText(3,  "Interpolación de lagrange")
            self.comboBox_2.setItemText(4,  "Interpolación de Newton")
            self.comboBox_2.setItemText(5,  "Interpolación de Hermite")
            self.comboBox_2.setItemText(6,  "Función Spline")

            # Mostramos el comboBox
            self.comboBox_2.setVisible(True)
            self.label.setVisible(True)

            # Ocultamos todo
            self.label_2.setVisible(False)
            self.label_3.setVisible(False)
            self.label_4.setVisible(False)
            self.label_5.setVisible(False)
            self.label_6.setVisible(False)
            self.label_7.setVisible(False)
            self.lineEdit.setVisible(False)
            self.lineEdit_2.setVisible(False)
            self.lineEdit_3.setVisible(False)
            self.lineEdit_4.setVisible(False)
            self.lineEdit_5.setVisible(False)

        elif cual == 3:  # metodos de la unidad 4
            self.comboBox_2.setGeometry(QtCore.QRect(200, 80, 230, 26))
            self.label_10.setText('Diferenciación e integración numérica')

            # Siempre limpiamos el combobox para evitar duplicados o cosas raras
            self.comboBox_2.clear()

            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")

            self.comboBox_2.setItemText(0, "Seleccione un metodo")
            self.comboBox_2.setItemText(1,  "Diferenciacion Numerica:")
            self.comboBox_2.setItemText(2,  "- Hacia adelante")
            self.comboBox_2.setItemText(3,  "- Hacia atras")
            self.comboBox_2.setItemText(4,  "- Centrada")
            self.comboBox_2.setItemText(5,  "- Tres puntos")
            self.comboBox_2.setItemText(6,  "- Cinco puntos")
            self.comboBox_2.setItemText(
                7,  "Diferenciacion Numerica (orden superior)")
            self.comboBox_2.setItemText(8,  "- Adelante")
            self.comboBox_2.setItemText(9,  "- Atras")
            self.comboBox_2.setItemText(10, "- Centrales")
            self.comboBox_2.setItemText(11, "Metodo Richardson")
            self.comboBox_2.setItemText(12, "Integracion Numerica")
            self.comboBox_2.setItemText(13, "- Trapecio simple")
            self.comboBox_2.setItemText(14, "- Trapecio compuesto")
            self.comboBox_2.setItemText(15, "- Integrales dobles y triples")
            self.comboBox_2.setItemText(16, "- Simpson un tercio simple")
            self.comboBox_2.setItemText(17, "- Simpson un tercio compuesta")
            self.comboBox_2.setItemText(18, "- Simpson tres octavos simple")
            self.comboBox_2.setItemText(19, "- Simpson tres octavos compuesta")
            self.comboBox_2.setItemText(20, "- Metodo Rosemberg")
            self.comboBox_2.setItemText(21, "- Metodo cuadratura Gaussiana")
            self.comboBox_2.setItemText(22, "- Simpson un tercio adaptativo")
            self.comboBox_2.setItemText(23, "- Metodo de boole")
            self.comboBox_2.setCurrentIndex(0)

            self.comboBox_2.setVisible(False)
            self.lineEdit_4.setVisible(False)
            self.lineEdit_3.setVisible(False)
            self.label.setVisible(False)
            self.label_2.setVisible(False)
            self.label_5.setVisible(False)
            self.label_6.setVisible(False)
            self.label_3.setVisible(False)
            self.label_4.setVisible(False)
            self.label_5.setVisible(False)
            self.label_6.setVisible(False)
            self.label_7.setVisible(False)
            self.lineEdit.setVisible(False)
            self.lineEdit_2.setVisible(False)
            self.lineEdit_3.setVisible(False)
            self.lineEdit_4.setVisible(False)
            self.lineEdit_5.setVisible(False)

          # <----------- Mostramos el combobox donde estan los metodos ---------->
            self.comboBox_2.setVisible(True)
            self.label.setVisible(True)

        elif cual == 4:  # metodos de la unidad 5

            self.comboBox_2.setGeometry(QtCore.QRect(200, 80, 172, 24))
            self.label_10.setText('Ecuaciones diferenciales ordinarias')
            self.comboBox_2.clear()

            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")
            self.comboBox_2.addItem("")

            self.comboBox_2.setItemText(0,  "Seleccione un metodo")
            self.comboBox_2.setItemText(1,  "Euler adelante")
            self.comboBox_2.setItemText(2,  "Euler atras")
            self.comboBox_2.setItemText(3,  "Euler centrado")
            self.comboBox_2.setItemText(4,  "Euler mejorado")
            self.comboBox_2.setItemText(5,  "Met. Taylor")
            self.comboBox_2.setItemText(6,  "Met. Runge Kutta")
            self.comboBox_2.setItemText(7,  "Met. Adam Bashforth")

            self.comboBox_2.setVisible(True)
            self.label.setVisible(True)

    def usar_tabla_unidad4_o_no(self):

        global tabla_unidad4_si_no
        si_o_no = self.comboBox_3.currentIndex()
        metodo = self.comboBox_2.currentIndex()

        if si_o_no == 0:

            tabla_unidad4_si_no = 0

            self.tableWidget_2.setVisible(False)
            self.pushButton_5.setVisible(False)
            self.pushButton_6.setVisible(False)
            self.lineEdit_6.setVisible(False)
            self.label_14.setVisible(False)

            if metodo == 2:
                self.funcion_uni4.setVisible(True)
                self.puntoInicial_uni4.setVisible(True)
                self.h_uni4.setVisible(True)
                self.label_funcion_uni4.setVisible(True)
                self.label_puntoInicial_uni4.setVisible(True)
                self.label_h_uni4.setVisible(True)

            elif metodo == 3:
                self.funcion_uni4.setVisible(True)
                self.puntoInicial_uni4.setVisible(True)
                self.h_uni4.setVisible(True)
                self.label_funcion_uni4.setVisible(True)
                self.label_puntoInicial_uni4.setVisible(True)
                self.label_h_uni4.setVisible(True)

            elif metodo == 4:
                self.funcion_uni4.setVisible(True)
                self.puntoInicial_uni4.setVisible(True)
                self.h_uni4.setVisible(True)
                self.label_funcion_uni4.setVisible(True)
                self.label_puntoInicial_uni4.setVisible(True)
                self.label_h_uni4.setVisible(True)

            elif metodo == 5:
                self.funcion_uni4.setVisible(True)
                self.puntoInicial_uni4.setVisible(True)
                self.h_uni4.setVisible(True)
                self.label_funcion_uni4.setVisible(True)
                self.label_puntoInicial_uni4.setVisible(True)
                self.label_h_uni4.setVisible(True)

            elif metodo == 6:
                self.funcion_uni4.setVisible(True)
                self.puntoInicial_uni4.setVisible(True)
                self.h_uni4.setVisible(True)
                self.label_funcion_uni4.setVisible(True)
                self.label_puntoInicial_uni4.setVisible(True)
                self.label_h_uni4.setVisible(True)

            if metodo == 8:
                self.funcion_uni4.setVisible(True)
                self.puntoInicial_uni4.setVisible(True)
                self.h_uni4.setVisible(True)
                self.label_funcion_uni4.setVisible(True)
                self.label_puntoInicial_uni4.setVisible(True)
                self.label_h_uni4.setVisible(True)

            elif metodo == 9:
                self.funcion_uni4.setVisible(True)
                self.puntoInicial_uni4.setVisible(True)
                self.h_uni4.setVisible(True)
                self.label_funcion_uni4.setVisible(True)
                self.label_puntoInicial_uni4.setVisible(True)
                self.label_h_uni4.setVisible(True)

            elif metodo == 10:
                self.funcion_uni4.setVisible(True)
                self.puntoInicial_uni4.setVisible(True)
                self.h_uni4.setVisible(True)
                self.label_funcion_uni4.setVisible(True)
                self.label_puntoInicial_uni4.setVisible(True)
                self.label_h_uni4.setVisible(True)

            elif metodo == 13:
                self.lbl_integral_normal.setVisible(True)
                self.a0_normal.setVisible(True)
                self.b0_normal.setVisible(True)
                self.funcion_uni4.setVisible(True)

            elif metodo == 14:
                self.label_puntoInicial_uni4.setText('n: ')
                self.label_puntoInicial_uni4.setVisible(True)
                self.puntoInicial_uni4.setVisible(True)
                self.funcion_uni4.setVisible(True)
                self.lbl_integral_normal.setVisible(True)
                self.a0_normal.setVisible(True)
                self.b0_normal.setVisible(True)

            elif metodo == 16:
                self.funcion_uni4.setVisible(True)
                self.lbl_integral_normal.setVisible(True)
                self.a0_normal.setVisible(True)
                self.b0_normal.setVisible(True)


            elif metodo == 17:
                self.label_puntoInicial_uni4.setText('n: ')
                self.label_puntoInicial_uni4.setVisible(True)
                self.puntoInicial_uni4.setVisible(True)
                self.funcion_uni4.setVisible(True)
                self.lbl_integral_normal.setVisible(True)
                self.a0_normal.setVisible(True)
                self.b0_normal.setVisible(True)

        elif si_o_no == 1:
            global cuantasFilasYColumnas
            cuantasFilasYColumnas = 2  # Columnas iniciales

            self.creacion_tabla_por_defecto_unidad3(3, 0)
            self.funcion_uni4.setVisible(False)
            self.puntoInicial_uni4.setVisible(False)
            self.h_uni4.setVisible(False)
            self.label_funcion_uni4.setVisible(False)
            self.label_puntoInicial_uni4.setVisible(False)
            self.label_h_uni4.setVisible(False)
            tabla_unidad4_si_no = 1
            self.lineEdit_6.setVisible(True)
            self.label_14.setText('X0 :')
            self.label_14.setVisible(True)
            self.lbl_integral_normal.setVisible(False)
            self.a0_normal.setVisible(False)
            self.b0_normal.setVisible(False)

    # Controlar los comboBox para las derivadas de orden 2 y 3
    def control_integral_doble_triple(self):
        doble_o_triple = self.cmb_doble_triple.currentIndex()
        self.diff3.clear()
        self.diff2.clear()

        if doble_o_triple == 0:
            self.funcion_txt.setVisible(True)
            self.lbl_integral1.setVisible(True)
            self.lbl_integral2.setVisible(True)
            self.lbl_integral3.setVisible(False)
            self.a0.setVisible(True)
            self.a1.setVisible(True)
            self.a2.setVisible(False)
            self.b0.setVisible(True)
            self.b1.setVisible(True)
            self.b2.setVisible(False)
            self.diff1.setVisible(True)
            self.diff2.setVisible(True)
            self.diff3.setVisible(False)

            self.diff1.clear()
            self.diff1.addItem("")
            self.diff1.addItem("")

            self.diff1.setItemText(0, "dx")
            self.diff1.setItemText(1, "dy")

        elif doble_o_triple == 1:
            self.funcion_txt.setVisible(True)
            self.lbl_integral1.setVisible(True)
            self.lbl_integral2.setVisible(True)
            self.lbl_integral3.setVisible(True)
            self.a0.setVisible(True)
            self.a1.setVisible(True)
            self.a2.setVisible(True)
            self.b0.setVisible(True)
            self.b1.setVisible(True)
            self.b2.setVisible(True)
            self.diff1.setVisible(True)
            self.diff2.setVisible(True)
            self.diff3.setVisible(True)

            self.diff1.clear()
            self.diff1.addItem("")
            self.diff1.addItem("")
            self.diff1.addItem("")

            self.diff1.setItemText(0, "dx")
            self.diff1.setItemText(1, "dy")
            self.diff1.setItemText(2, "dz")

    def control_diferenciacion_segundo_cmb(self):
        cmb1 = self.diff1.currentIndex()
        cmb_doble_o_triple = self.cmb_doble_triple.currentIndex()
        self.diff2.clear()
        self.diff3.clear()

        if cmb_doble_o_triple == 0:   #Integral doble

            if cmb1 == 0:
                self.diff2.addItem("")
                self.diff2.setItemText(0, "dy")
            elif cmb1 == 1:
                self.diff2.addItem("")
                self.diff2.setItemText(0, "dx")

        elif cmb_doble_o_triple == 1: #Integral triple
            if cmb1 == 0:
                self.diff2.addItem("")
                self.diff2.addItem("")
                self.diff2.setItemText(0, "dy")
                self.diff2.setItemText(1, "dz")
            elif cmb1 == 1:
                self.diff2.addItem("")
                self.diff2.addItem("")
                self.diff2.setItemText(0, "dx")
                self.diff2.setItemText(1, "dz")
            elif cmb1 == 2:
                self.diff2.addItem("")
                self.diff2.addItem("")
                self.diff2.setItemText(0, "dx")
                self.diff2.setItemText(1, "dy")

    def control_diferenciacion_tercer_cmb(self):
        cmb2 = self.diff2.currentText()
        cmb1 = self.diff1.currentText()
        self.diff3.clear()

        cmb_doble_o_triple = self.cmb_doble_triple.currentIndex()

        if cmb_doble_o_triple == 1:   #Integral triple

            if cmb1 == 'dx' and cmb2 == 'dy': 
                self.diff3.addItem("") 
                self.diff3.setItemText(0, "dz")

            elif cmb1 == 'dx' and cmb2 == 'dz': 
                self.diff3.addItem("")
                self.diff3.setItemText(0, "dy")

            if cmb1 == 'dz' and cmb2 == 'dx': 
                self.diff3.addItem("")
                self.diff3.setItemText(0, "dy")

            elif cmb1 == 'dz' and cmb2 == 'dy': 
                self.diff3.addItem("")
                self.diff3.setItemText(0, "dx")

            elif cmb1 == 'dy' and cmb2 == 'dx':
                self.diff3.addItem("")
                self.diff3.setItemText(0, "dz")

            elif cmb1 == 'dy' and cmb2 == 'dz':
                self.diff3.addItem("")
                self.diff3.setItemText(0, "dx")

    def metodos_de_cada_unidad(self):
        queMetodo = self.comboBox_2.currentIndex()
        queUnidad = self.comboBox.currentIndex()

        self.pushButton_5.setVisible(False)
        self.pushButton_6.setVisible(False)
        self.tableWidget_2.setVisible(False)
        self.radioButton.setVisible(False)
        self.radioButton_2.setVisible(False)
        self.radioButton_3.setVisible(False)
        self.radioButton_4.setVisible(False)
        self.label_9.setVisible(False)
        self.comboBox_3.setVisible(False)
        self.label_14.setVisible(False)
        self.lineEdit_6.setVisible(False)
        self.label_12.setVisible(False)
        self.pushButton_10.setVisible(False)
        self.pushButton_11.setVisible(False)
        self.label_13.setVisible(False)
        self.funcion_uni4.setVisible(False)
        self.puntoInicial_uni4.setVisible(False)
        self.h_uni4.setVisible(False)
        self.label_funcion_uni4.setVisible(False)
        self.label_puntoInicial_uni4.setVisible(False)
        self.label_h_uni4.setVisible(False)
        self.pushButton_6.setGeometry(QtCore.QRect(85, 127, 65, 40))
        self.pushButton_5.setGeometry(QtCore.QRect(10, 127, 65, 40))
        self.label_nivel_uni4.setVisible(False)
        self.nivel_uni4.setVisible(False)
        self.funcion_txt.setVisible(False)
        self.lbl_integral1.setVisible(False)
        self.lbl_integral2.setVisible(False)
        self.lbl_integral3.setVisible(False)
        self.a0.setVisible(False)
        self.a1.setVisible(False)
        self.a2.setVisible(False)
        self.b0.setVisible(False)
        self.b1.setVisible(False)
        self.b2.setVisible(False)
        self.diff1.setVisible(False)
        self.diff2.setVisible(False)
        self.diff3.setVisible(False)
        self.lbl_integral_normal.setVisible(False)
        self.a0_normal.setVisible(False)
        self.b0_normal.setVisible(False)
        self.label_ver_tabla.setVisible(False)
        self.label_14.setText('Evaluar en')
        self.label_6.setText("#3")
        self.label_puntoInicial_uni4.setText("Punto Inicial")
        self.label_7.setText("Cifras significativas")
        self.lbl_cmb.setVisible(False)
        self.cmb_doble_triple.setVisible(False)
        self.cajaTexto.setVisible(False)
        self.tableWidget.setVisible(False)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(9)
        self.tableWidget.clear()
        self.lineOrden.setVisible(False)
        self.lblOrden.setVisible(False)

        if queUnidad == 0:  # unidad 1

            self.label_4.setText("#1")
            self.label_5.setText("#2")
            self.label_4.setVisible(True)
            self.label_3.setVisible(True)
            self.label_2.setVisible(True)
            self.label_7.setVisible(True)
            self.lineEdit_2.setVisible(True)
            self.lineEdit_5.setVisible(True)

            # <-------- Ocultamos lo demas ------------->
            self.lineEdit.setVisible(False)
            self.lineEdit_4.setVisible(False)
            self.lineEdit_3.setVisible(False)
            self.label_2.setVisible(False)
            self.label_5.setVisible(False)
            self.label_6.setVisible(False)
            self.cajaTexto.setVisible(False)

        elif queUnidad == 1:  # unidad 2

            self.pushButton_5.setVisible(False)
            self.pushButton_6.setVisible(False)
            self.tableWidget_2.setVisible(False)
            self.radioButton.setVisible(False)
            self.radioButton_2.setVisible(False)
            self.radioButton_3.setVisible(False)
            self.radioButton_4.setVisible(False)
            self.label_9.setVisible(False)
            self.cajaTexto.setVisible(False)


            if queMetodo == 1 or queMetodo == 2 or queMetodo == 6:

                # <---- dejamos solo los componentes que usa metodo biseccion, falsa posicion y secante -->
                self.label_4.setText("#1")
                self.label_5.setText("#2")
                self.label_4.setVisible(True)
                self.label_3.setVisible(True)
                self.label_2.setVisible(True)
                self.label_5.setVisible(True)
                self.label_7.setVisible(True)
                self.lineEdit_2.setVisible(True)
                self.lineEdit_2.setVisible(True)
                self.lineEdit_3.setVisible(True)
                self.lineEdit_5.setVisible(True)
                self.lineEdit.setVisible(True)

                # <-------- Ocultamos lo demas ------------->
                self.lineEdit_4.setVisible(False)
                self.label_6.setVisible(False)

            elif queMetodo >= 3 and queMetodo <= 5:

                # <---- dejamos solo los componentes que usa metodo punto fijo y los de newton -->
                self.label_4.setText("#1")
                self.label_5.setText("#2")
                self.label_4.setVisible(True)
                self.label_2.setVisible(True)
                self.label_3.setVisible(True)
                self.label_2.setVisible(True)
                self.label_7.setVisible(True)
                self.lineEdit_2.setVisible(True)
                self.lineEdit_5.setVisible(True)
                self.lineEdit.setVisible(True)

                # <-------- Ocultamos lo demas ------------->
                self.lineEdit_4.setVisible(False)
                self.lineEdit_3.setVisible(False)
                self.label_5.setVisible(False)

            elif queMetodo == 7:
                # <---- dejamos solo los componentes que usa metodo de cero de polinomios --->
                self.label_4.setText("#1")
                self.label_5.setText("#2")
                self.lineEdit.setVisible(True)
                self.label_2.setVisible(True)
                # <-------- ocultamos lo demas ---------->
                self.label_3.setVisible(False)
                self.label_4.setVisible(False)
                self.label_5.setVisible(False)
                self.label_6.setVisible(False)
                self.label_7.setVisible(False)
                self.lineEdit_2.setVisible(False)
                self.lineEdit_3.setVisible(False)
                self.lineEdit_4.setVisible(False)
                self.lineEdit_5.setVisible(False)

            elif queMetodo == 8:

                self.label_4.setText("#1")
                self.label_4.setVisible(True)
                self.label_3.setVisible(True)
                self.lineEdit_2.setVisible(True)
                self.lineEdit_5.setVisible(True)
                self.label_5.setVisible(False)
                self.label_6.setVisible(False)
                self.label_7.setVisible(True)
                self.lineEdit.setVisible(True)
                self.label_2.setVisible(True)

            elif queMetodo == 9:

                # <---- dejamos solo los componentes que usa metodo muller -->
                self.label_4.setText("#1")
                self.label_5.setText("#2")
                self.label_4.setVisible(True)
                self.label_2.setVisible(True)
                self.label_3.setVisible(True)
                self.label_5.setVisible(True)
                self.label_7.setVisible(True)
                self.lineEdit_2.setVisible(True)
                self.lineEdit_3.setVisible(True)
                self.lineEdit_5.setVisible(True)
                self.lineEdit_4.setVisible(True)
                self.lineEdit.setVisible(True)

            elif queMetodo == 10:

                # <---- dejamos solo los componentes que usa metodo baristown -->
                self.label_4.setText("R")
                self.label_5.setText("S")
                self.label_4.setVisible(True)
                self.label_2.setVisible(True)
                self.label_3.setVisible(True)
                self.label_5.setVisible(True)
                self.lineEdit_2.setVisible(True)
                self.lineEdit_3.setVisible(True)
                self.lineEdit.setVisible(True)
                self.label_7.setVisible(True)
                self.lineEdit_5.setVisible(True)

                # <-------- ocultamos lo demas ---------->

                self.lineEdit_4.setVisible(False)

        elif queUnidad == 2:  # unidad 3

            global cuantasFilasYColumnas
            if queMetodo >= 1 and queMetodo <= 6:
                self.tableWidget_2.setGeometry(QtCore.QRect(170, 120, 704, 81))
                self.label_9.setText("¿Desea ver el polinomio?")
                self.radioButton.setAutoExclusive(False)
                self.radioButton.setChecked(False)
                self.radioButton.setAutoExclusive(True)
                self.radioButton_2.setAutoExclusive(False)
                self.radioButton_2.setChecked(False)
                self.radioButton_2.setAutoExclusive(True)
                self.radioButton_3.setVisible(False)
                self.radioButton_3.setAutoExclusive(True)
                self.radioButton_4.setVisible(False)
                self.radioButton_4.setAutoExclusive(False)
                self.radioButton.setText("Si")
                self.radioButton_2.setText("No")
                self.radioButton.setGeometry(QtCore.QRect(620, 78, 82, 23))
                self.radioButton_2.setGeometry(QtCore.QRect(660, 78, 82, 23))
                self.pushButton_5.setVisible(True)
                self.pushButton_6.setVisible(True)
                self.pushButton_10.setVisible(False)
                self.pushButton_11.setVisible(False)
                self.label_12.setVisible(True)
                self.label_13.setVisible(False)
                self.lineEdit_6.setVisible(False)
                self.label_14.setVisible(False)
                self.cajaTexto.setVisible(False)


            if queMetodo == 1:  # Lineal
                cuantasFilasYColumnas = 3
                self.creacion_tabla_por_defecto_unidad3(4, 0)

            elif queMetodo == 2:  # Cuadratica
                cuantasFilasYColumnas = 4
                self.creacion_tabla_por_defecto_unidad3(5, 0)

            elif queMetodo == 3:  # Lagrange
                cuantasFilasYColumnas = 3
                self.creacion_tabla_por_defecto_unidad3(4, 0)

            elif queMetodo == 4:  # Newton
                cuantasFilasYColumnas = 3
                self.creacion_tabla_por_defecto_unidad3(4, 0)

            elif queMetodo == 5:  # Hermite
                self.tableWidget_2.setGeometry(
                    QtCore.QRect(170, 120, 704, 116))
                self.pushButton_10.setVisible(True)
                self.pushButton_11.setVisible(True)
                self.lineEdit_6.setVisible(True)
                self.label_14.setVisible(True)
                self.label_13.setVisible(True)
                cuantasFilasYColumnas = 2
                self.creacion_tabla_por_defecto_unidad3(3, 1)

            elif queMetodo == 6:  # función spline
                self.label_9.setText(
                    "Seleccione el grado de la función Spline")
                self.radioButton.setAutoExclusive(False)
                self.radioButton.setChecked(False)
                self.radioButton.setAutoExclusive(True)
                self.radioButton_2.setAutoExclusive(False)
                self.radioButton_2.setChecked(False)
                self.radioButton_2.setAutoExclusive(True)
                self.lineEdit_6.setVisible(True)
                self.label_14.setVisible(True)

                self.radioButton_3.setAutoExclusive(False)
                self.radioButton_3.setChecked(False)
                self.radioButton_3.setAutoExclusive(True)

                self.radioButton_4.setAutoExclusive(False)
                self.radioButton_4.setChecked(False)
                self.radioButton_4.setAutoExclusive(True)

                self.radioButton.setText("Grado #0")
                self.radioButton_2.setText("Grado #1")
                self.radioButton_3.setText("Grado #2")
                self.radioButton_4.setText("Grado #3")
                self.radioButton.setGeometry(QtCore.QRect(620, 78, 82, 23))
                self.radioButton_2.setGeometry(QtCore.QRect(700, 78, 82, 23))
                self.radioButton_3.setVisible(True)
                self.radioButton_4.setVisible(True)
                self.tableWidget_2.setGeometry(QtCore.QRect(170, 120, 704, 81))
                cuantasFilasYColumnas = 3
                self.creacion_tabla_por_defecto_unidad3(4, 0)

        elif queUnidad == 3:  # unidad 4
            self.tableWidget_2.setGeometry(QtCore.QRect(170, 140, 704, 81))
            self.pushButton_6.setGeometry(QtCore.QRect(85, 150, 65, 40))
            self.pushButton_5.setGeometry(QtCore.QRect(10, 150, 65, 40))

            if queMetodo == 2:
                self.label_ver_tabla.setVisible(True)
                self.comboBox_3.setVisible(True)
                self.comboBox_3.setCurrentIndex(-1)

            elif queMetodo == 3:
                self.label_ver_tabla.setVisible(True)
                self.comboBox_3.setVisible(True)
                self.comboBox_3.setCurrentIndex(-1)

            elif queMetodo == 4:
                self.label_ver_tabla.setVisible(True)
                self.comboBox_3.setVisible(True)
                self.comboBox_3.setCurrentIndex(-1)

            elif queMetodo == 5:
                self.label_ver_tabla.setVisible(True)
                self.comboBox_3.setVisible(True)
                self.comboBox_3.setCurrentIndex(-1)

            elif queMetodo == 6:
                self.label_ver_tabla.setVisible(True)
                self.comboBox_3.setVisible(True)
                self.comboBox_3.setCurrentIndex(-1)

            elif queMetodo == 7:
                self.comboBox_2.setCurrentIndex(0)
                self.label_ver_tabla.setVisible(False)
                self.comboBox_3.setVisible(False)

            elif queMetodo == 8:
                self.label_ver_tabla.setVisible(True)
                self.comboBox_3.setVisible(True)
                self.comboBox_3.setCurrentIndex(-1)

            elif queMetodo == 9:
                self.label_ver_tabla.setVisible(True)
                self.comboBox_3.setVisible(True)
                self.comboBox_3.setCurrentIndex(-1)

            elif queMetodo == 10:
                self.label_ver_tabla.setVisible(True)
                self.comboBox_3.setVisible(True)
                self.comboBox_3.setCurrentIndex(-1)

            elif queMetodo == 11:
                self.label_funcion_uni4.setVisible(True)
                self.funcion_uni4.setVisible(True)
                self.label_puntoInicial_uni4.setVisible(True)
                self.puntoInicial_uni4.setVisible(True)
                self.label_h_uni4.setVisible(True)
                self.h_uni4.setVisible(True)
                self.label_nivel_uni4.setVisible(True)
                self.nivel_uni4.setVisible(True)

            elif queMetodo == 13:
                self.label_ver_tabla.setVisible(True)
                self.comboBox_3.setVisible(True)
                self.comboBox_3.setCurrentIndex(-1)

            elif queMetodo == 14:
                self.label_ver_tabla.setVisible(True)
                self.comboBox_3.setVisible(True)
                self.comboBox_3.setCurrentIndex(-1)

            elif queMetodo == 15:
                self.lbl_cmb.setVisible(True)
                self.cmb_doble_triple.setVisible(True)

            elif queMetodo == 16:
                self.label_ver_tabla.setVisible(True)
                self.comboBox_3.setVisible(True)
                self.comboBox_3.setCurrentIndex(-1)

            elif queMetodo == 17:
                self.label_ver_tabla.setVisible(True)
                self.comboBox_3.setVisible(True)
                self.comboBox_3.setCurrentIndex(-1)

            elif queMetodo == 18:
                self.funcion_uni4.setVisible(True)
                self.lbl_integral_normal.setVisible(True)
                self.a0_normal.setVisible(True)
                self.b0_normal.setVisible(True)

            elif queMetodo == 19:
                self.label_puntoInicial_uni4.setText('n: ')
                self.funcion_uni4.setVisible(True)
                self.label_puntoInicial_uni4.setVisible(True)
                self.puntoInicial_uni4.setVisible(True)
                self.lbl_integral_normal.setVisible(True)
                self.a0_normal.setVisible(True)
                self.b0_normal.setVisible(True)

            elif queMetodo == 20:
                self.label_puntoInicial_uni4.setText('nivel: ')
                self.funcion_uni4.setVisible(True)
                self.label_puntoInicial_uni4.setVisible(True)
                self.puntoInicial_uni4.setVisible(True)
                self.lbl_integral_normal.setVisible(True)
                self.a0_normal.setVisible(True)
                self.b0_normal.setVisible(True)

            elif queMetodo == 21:
                self.label_puntoInicial_uni4.setText('n: ')
                self.funcion_uni4.setVisible(True)
                self.label_puntoInicial_uni4.setVisible(True)
                self.puntoInicial_uni4.setVisible(True)
                self.lbl_integral_normal.setVisible(True)
                self.a0_normal.setVisible(True)
                self.b0_normal.setVisible(True)

            elif queMetodo == 22:
                self.label_puntoInicial_uni4.setText('Tolerancia: ')
                self.funcion_uni4.setVisible(True)
                self.label_puntoInicial_uni4.setVisible(True)
                self.puntoInicial_uni4.setVisible(True)
                self.lbl_integral_normal.setVisible(True)
                self.a0_normal.setVisible(True)
                self.b0_normal.setVisible(True)

            elif queMetodo == 23:
                self.funcion_uni4.setVisible(True)
                self.lbl_integral_normal.setVisible(True)
                self.a0_normal.setVisible(True)
                self.b0_normal.setVisible(True)
            else:
                self.comboBox_2.setCurrentIndex(0)
                self.label_ver_tabla.setVisible(False)
                self.comboBox_3.setVisible(False)

        elif queUnidad == 4:  # unidad 5

            if queMetodo >= 1 and queMetodo <= 5:
                self.label_4.setText("T0")
                self.label_5.setText("Y0")
                self.label_6.setText("T1")
                self.label_7.setText("N:")
                self.label_4.setVisible(True)
                self.label_2.setVisible(True)
                self.label_3.setVisible(True)
                self.label_5.setVisible(True)
                self.label_7.setVisible(True)
                self.label_6.setVisible(True)
                self.lineEdit_2.setVisible(True)
                self.lineEdit_3.setVisible(True)
                self.lineEdit_5.setVisible(True)
                self.lineEdit_4.setVisible(True)
                self.lineEdit.setVisible(True)

            elif queMetodo >= 6 and queMetodo <= 7:
                self.label_4.setText("T0")
                self.label_5.setText("Y0")
                self.label_6.setText("T1")
                self.label_7.setText("N:")
                self.label_4.setVisible(True)
                self.label_2.setVisible(True)
                self.label_3.setVisible(True)
                self.label_5.setVisible(True)
                self.label_7.setVisible(True)
                self.label_6.setVisible(True)
                self.lineEdit_2.setVisible(True)
                self.lineEdit_3.setVisible(True)
                self.lineEdit_5.setVisible(True)
                self.lineEdit_4.setVisible(True)
                self.lineEdit.setVisible(True)
                self.lineOrden.setVisible(True)
                self.lblOrden.setVisible(True)

    # Metodos que controlan las tablas ó que trabajan con las tablas
    def creacion_tabla_por_defecto_unidad3(self, columnas, si_es_hermite):
        # Limpiamos la tabla

        unidad = self.comboBox.currentIndex()

        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(0)

        self.pushButton_5.setVisible(True)
        self.pushButton_6.setVisible(True)

        # Configuramos la tabla
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(38)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(60)

        if si_es_hermite == 0:
            # Definimos las dimensiones

            if unidad == 2:
                # Mostramos los radio button
                self.radioButton.setVisible(True)
                self.radioButton_2.setVisible(True)
                self.label_9.setVisible(True)
            else:
                # N0 mostramos los radio button
                self.radioButton.setVisible(False)
                self.radioButton_2.setVisible(False)
                self.label_9.setVisible(False)

            self.tableWidget_2.setColumnCount(columnas)
            self.tableWidget_2.setRowCount(2)

            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)

            brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
            brush.setStyle(QtCore.Qt.NoBrush)

            brush_2 = QtGui.QBrush(QtGui.QColor(134, 135, 208))
            brush_2.setStyle(QtCore.Qt.SolidPattern)

            for x in range(0, 2):
                for y in range(0, columnas):
                    item = QtWidgets.QTableWidgetItem()
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setFont(font)
                    item.setBackground(brush)
                    item.setForeground(brush_2)
                    
                    if y == 0 and x == 0:
                        salida = "X"
                        item.setText(salida)
                        self.tableWidget_2.setItem(x, y,item)
                        self.tableWidget_2.setColumnWidth(y, 8)

                    elif y == 0 and x == 1:
                        salida = "Y"
                        item.setText(salida)
                        self.tableWidget_2.setItem(x, y, item)
                        self.tableWidget_2.setColumnWidth(y, 8)
                    else:
                        self.tableWidget_2.setItem(x, y, item)

            self.tableWidget_2.setVisible(True)

        else:

            if unidad == 2:
                # Mostramos los radio button
                self.radioButton.setVisible(True)
                self.radioButton_2.setVisible(True)
                self.label_9.setVisible(True)
            else:
                # Mostramos los radio button
                self.radioButton.setVisible(False)
                self.radioButton_2.setVisible(False)
                self.label_9.setVisible(False)

            # Definimos las dimensiones
            self.tableWidget_2.setColumnCount(columnas)
            self.tableWidget_2.setRowCount(3)
            self.tableWidget_2.verticalHeader().setDefaultSectionSize(38)
            self.tableWidget_2.horizontalHeader().setDefaultSectionSize(100)

            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)

            brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
            brush.setStyle(QtCore.Qt.NoBrush)

            brush_2 = QtGui.QBrush(QtGui.QColor(134, 135, 208))
            brush_2.setStyle(QtCore.Qt.SolidPattern)

            for x in range(0, 2):
                for y in range(0, columnas):
                    item = QtWidgets.QTableWidgetItem()
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setFont(font)
                    item.setBackground(brush)
                    item.setForeground(brush_2)

                    if y == 0 and x == 0:
                        salida = "X"
                        item.setText(salida)
                        self.tableWidget_2.setItem(
                            x, y, item)
                    elif y == 1 and x == 0:
                        salida = "Y"
                        item.setText(salida)
                        self.tableWidget_2.setItem(
                            x, y, item)
                    elif y == 2 and x == 0:
                        salida = "Y'"
                        item.setText(salida)
                        self.tableWidget_2.setItem(
                            x, y, item)
                    else:
                        self.tableWidget_2.setItem(x, y, item)

            self.tableWidget_2.setVisible(True)

    def insertar_datos_a_tabla_unidad1(self, metodo):
        
        cmb = self.comboBox_2.currentIndex()
        punto = self.lineEdit_2.text()
        cifras = self.lineEdit_5.text()
        control = 1


        if cmb == 0 and punto == '' and cifras == '':
            self.mensajesAlerta(0,3)
            control = 0
        elif cmb == 0 and punto != '' and cifras != '':
            self.mensajesAlerta(0,2)
            control = 0
        elif cmb != 0 and punto != '' and cifras == '':
            self.mensajesAlerta(0,1)
            control = 0
        elif cmb != 0 and punto == '' and cifras != '':
            self.mensajesAlerta(0,0)
            control = 0
        elif cmb != 0 and punto == '' and cifras == '':
            self.mensajesAlerta(0,3)
            control = 0

        

        if control == 1:
            cifras = float(cifras)
            punto = float(punto)

            if metodo == 1:
                lst = metodos_uni1.metodo1(punto,cifras)
            
            elif metodo == 2:
                lst = metodos_uni1.metodo2(punto,cifras)

            elif metodo == 3:
                lst = metodos_uni1.metodo3(punto,cifras)

            elif metodo == 4:
                lst = metodos_uni1.metodo4(punto,cifras)

            elif metodo == 5:
                lst = metodos_uni1.metodo5(punto,cifras)

            elif metodo == 6:
                lst = metodos_uni1.metodo6(punto,cifras)

            elif metodo == 7:
                lst = metodos_uni1.metodo7(punto,cifras)
            
            elif metodo == 8:
                lst = metodos_uni1.metodo8(punto,cifras)
            
            elif metodo == 9:
                lst = metodos_uni1.metodo9(punto,cifras)
            
            elif metodo == 10:
                lst = metodos_uni1.metodo10(punto,cifras)
            
            elif metodo == 11:
                lst = metodos_uni1.metodo11(punto,cifras)

            self.tableWidget.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
            rows = len(lst)  # Numero de filas
            columns = len(lst[0])  # Numero de columnas
            len_Col = int(930/columns)  # Tamaño que tendran las columnas

            # Aplicamos unas configuraciones a la tabla
            self.tableWidget.setColumnCount(columns)
            self.tableWidget.setRowCount(rows)
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.horizontalHeader().setVisible(False)
            self.tableWidget.setVisible(True)

            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)

            brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
            brush.setStyle(QtCore.Qt.NoBrush)

            brush_2 = QtGui.QBrush(QtGui.QColor(134, 135, 208))
            brush_2.setStyle(QtCore.Qt.SolidPattern)


            for row in range(rows):  # Primer for recorre las filas en lst
                # Segundo for recorre las columnas en lst
                for column in range(columns):
                    if row == 0:  # Encabezado o header

                        item = QtWidgets.QTableWidgetItem()
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        item.setFont(font)
                        item.setBackground(brush)
                        item.setForeground(brush_2)
                        item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)

                        salida = lst[row][column]
                        item.setText(str(salida))

                        self.tableWidget.setItem(row, column, item)
                        self.tableWidget.setColumnWidth(column, len_Col)
                    else:

                        item = QtWidgets.QTableWidgetItem()
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        item.setFont(font)
                        item.setBackground(brush)
                        item.setForeground(brush_2)
                        item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                    
                        if column == 0:
                            salida = (lst[row][column])
                            item.setText(str(salida))
                            self.tableWidget.setItem(row, column, item)
                            self.tableWidget.setColumnWidth(column, len_Col)
                        else:

                            if row == 1 and column == 2:
                                salida = lst[row][column]
                                item.setText(str(salida))
                                self.tableWidget.setItem(row, column,item)
                                self.tableWidget.setColumnWidth(column, len_Col)
                            else:
                                salida = "%.5f" % float(lst[row][column])
                                item.setText(str(salida))
                                self.tableWidget.setItem(row, column, item)
                                self.tableWidget.setColumnWidth(column, len_Col)

    def insertar_datos_a_tabla_unidad2(self, metodo):

        # Puntos a evaluar, funcion en la que evaluaremos y las cifras que se usaran
        x1 = self.lineEdit_2.text()  # Primer punto a evaluar
        x2 = self.lineEdit_3.text()  # Segundo punto a evaluar
        x3 = self.lineEdit_4.text()  # Tercer punto a evaluar
        funcion = self.lineEdit.text()  # función a evaluar
        cifras = self.lineEdit_5.text()  # numero de cifras significativas

        # Si nos devuelven la palabra: 'falsisimo' estan vacios
        x1Prueba = metodos.pedirValoresIniciales(x1)
        x2Prueba = metodos.pedirValoresIniciales(x2)
        x3Prueba = metodos.pedirValoresIniciales(x3)
        cifrasPrueba = metodos.pedirCifrasSignificativas(cifras)

        control = 0

        # Limpiamos la tabla antes de llenarla
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
        brush.setStyle(QtCore.Qt.NoBrush)

        brush_2 = QtGui.QBrush(QtGui.QColor(134, 135, 208))
        brush_2.setStyle(QtCore.Qt.SolidPattern)

        # tabla de biseccion - hasta secante
        if metodo >= 1 and metodo <= 6:

            if metodo == 1 or metodo == 2 or metodo == 6:
                
                if metodo != 0 and x1 == '' and x2 == '' and funcion == '' and cifras == '':
                    self.mensajesAlerta(1,1)
                    control = 1
                elif metodo != 0 and x1 != '' and x2 != '' and funcion == '' and cifras != '':
                    self.mensajesAlerta(1,2)
                    control = 1
                elif metodo != 0 and x1 == '' and x2 != '' and funcion != '' and cifras != '':
                    self.mensajesAlerta(1,3)
                    control = 1
                elif metodo != 0 and x1 != '' and x2 == '' and funcion != '' and cifras != '':
                    self.mensajesAlerta(1,4)
                    control = 1
                elif metodo != 0 and x1 != '' and x2 != '' and funcion != '' and cifras == '':
                    self.mensajesAlerta(1,7)
                    control = 1
                elif metodo != 0 and (x1 == '' or x2 == '' or funcion == '' or cifras == ''):
                    self.mensajesAlerta(1,6)
                    control = 1

            elif metodo == 3 or metodo == 4 or metodo == 5:

                if metodo != 0 and x1 == '' and funcion == '' and cifras == '':
                    self.mensajesAlerta(1,1)
                    control = 1
                elif metodo != 0 and x1 != '' and funcion == '' and cifras != '':
                    self.mensajesAlerta(1,2)
                    control = 1
                elif metodo != 0 and x1 == '' and funcion != '' and cifras != '':
                    self.mensajesAlerta(1,3)
                    control = 1
                elif metodo != 0 and x1 != '' and funcion != '' and cifras == '':
                    self.mensajesAlerta(1,7)
                    control = 1
                elif metodo != 0 and (x1 == '' or funcion == '' or cifras == ''):
                    self.mensajesAlerta(1,6)
                    control = 1

            
            if control == 0:

                # Llamamos al metodo que corresponda para obtener la respuesta y la guardamos en lst
                if metodo == 1:
                    lst = metodos.metodoBiseccion(
                        x1Prueba, x2Prueba, funcion, cifrasPrueba)
                elif metodo == 2:
                    lst = metodos.metodoFalsaPosicion(
                        x1Prueba, x2Prueba, funcion, cifrasPrueba)
                elif metodo == 3:
                    lst = metodos.metodoPuntoFijo(x1Prueba, funcion, cifrasPrueba)
                elif metodo == 4:
                    lst = metodos.metodoNewtonRaphson(
                        x1Prueba, funcion, cifrasPrueba)
                elif metodo == 5:
                    lst = metodos.metodoNewtonRaphsonMejorado(
                        x1Prueba, funcion, cifrasPrueba)
                elif metodo == 6:
                    lst = metodos.metodoSecante(
                        x1Prueba, x2Prueba, funcion, cifrasPrueba)

                # Insertamos los valores de lst en la tabla de respuestas

                self.tableWidget.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
                rows = len(lst)  # Numero de filas
                columns = len(lst[0])  # Numero de columnas
                len_Col = int(930/columns) # Tamaño que tendran las columnas

                # Aplicamos unas configuraciones a la tabla
                self.tableWidget.setColumnCount(columns)
                self.tableWidget.setRowCount(rows)
                self.tableWidget.verticalHeader().setVisible(False)
                self.tableWidget.horizontalHeader().setVisible(False)
                self.tableWidget.setVisible(True)

                for row in range(rows):  # Primer for recorre las filas en lst
                    # Segundo for recorre las columnas en lst
                    for column in range(columns):

                        item = QtWidgets.QTableWidgetItem()
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        item.setFont(font)
                        item.setBackground(brush)
                        item.setForeground(brush_2)
                        item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)

                        if row == 0:  # Encabezado o header
                            salida = lst[row][column]
                            item.setText(str(salida))
                            self.tableWidget.setItem(row, column, item)
                            self.tableWidget.setColumnWidth(column, len_Col)
                        else:
                            if column == 0:
                                salida = (lst[row][column])
                                item.setText(str(salida))
                                self.tableWidget.setItem(row, column, item)
                                self.tableWidget.setColumnWidth(column, len_Col)
                            else:
                                salida = "%.5f" % float(lst[row][column])
                                item.setText(str(salida))
                                self.tableWidget.setItem(row, column, item)
                                self.tableWidget.setColumnWidth(column, len_Col)

        # tabla de ceros de polinomios
        elif metodo == 7:

            if metodo != 0 and  funcion == '':
                self.mensajesAlerta(1,2)
                control = 1

            if control == 0:

                # Esta lista contiene los numeros que acompañan a las x
                lista_Coeficientes = metodos.coefs(self.lineEdit.text())
                largo = len(lista_Coeficientes)

                if largo >= 2 and largo <= 5:
                    if largo == 2:  # Lineal
                        a = 0
                        b = 0
                        c = 0
                        d = lista_Coeficientes[1]
                        e = lista_Coeficientes[0]
                    elif largo == 3:  # Cuadratico
                        a = 0
                        b = 0
                        c = lista_Coeficientes[2]
                        d = lista_Coeficientes[1]
                        e = lista_Coeficientes[0]
                    elif largo == 4:  # Cubico
                        a = 0
                        b = lista_Coeficientes[3]
                        c = lista_Coeficientes[2]
                        d = lista_Coeficientes[1]
                        e = lista_Coeficientes[0]
                    elif largo == 5:  # Cuartico
                        a = lista_Coeficientes[4]
                        b = lista_Coeficientes[3]
                        c = lista_Coeficientes[2]
                        d = lista_Coeficientes[1]
                        e = lista_Coeficientes[0]

                    lst = metodos.factorizar(a, b, c, d, e)

                    columns = len(lst)  # Numero de columnas
                    rows = 2  # Numero de filas
                    
                    # Controlamos el tamaño que tendra cada columna de forma variable y no estatica 
                    tamanioColumnas = 0
                    listaTamanio = []
                    contadorTamanio = 0
                    for x in range(0, columns):
                        listaTamanio.append(len(str(lst[x]))*7)
                        contadorTamanio += len(str(lst[x]))*7

                    listaTamanio.sort()

                    # Aplicamos unas configuraciones a la tabla
                    self.tableWidget.setColumnCount(columns)
                    self.tableWidget.setRowCount(rows)
                    self.tableWidget.verticalHeader().setVisible(False)
                    self.tableWidget.horizontalHeader().setVisible(False)
                    self.tableWidget.setVisible(True)

                    for row in range(rows):  # Primer for controla las filas
                        # Segundo for controla las columnas
                        for column in range(columns):
                            item = QtWidgets.QTableWidgetItem()
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            item.setFont(font)
                            item.setBackground(brush)
                            item.setForeground(brush_2)
                            item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                            if row == 0:  # cabezera o header
                                salida = "raiz #"+str(column+1)
                                item.setText(salida)
                                self.tableWidget.setItem(row, column, item)
                                if contadorTamanio < 930:
                                    tamanioColumnas = float(listaTamanio[len(listaTamanio)-1])
                                    self.tableWidget.setColumnWidth(
                                        column, tamanioColumnas)
                                else:
                                    tamanioColumnas = len(str(lst[column]))*7
                                    self.tableWidget.setColumnWidth(
                                        column, tamanioColumnas)
                            else:
                                salida = str(lst[column])
                                item.setText(str(salida))
                                self.tableWidget.setItem(row, column, item)
                                if contadorTamanio < 930:
                                    tamanioColumnas = float(listaTamanio[len(listaTamanio)-1])
                                    self.tableWidget.setColumnWidth(
                                        column, tamanioColumnas)
                                else:
                                    tamanioColumnas = len(str(lst[column]))*7
                                    self.tableWidget.setColumnWidth(column, tamanioColumnas)
                else:
                    print("Intento ingresar una función mayor a x^4 o menor a x^1")

        # tabla Horner
        elif metodo == 8:

            control = 0

            if metodo != 0 and x1 == '' and funcion == '' and cifras == '':
                    self.mensajesAlerta(1,1)
                    control = 1
            elif metodo != 0 and x1 != '' and funcion == '' and cifras != '':
                self.mensajesAlerta(1,2)
                control = 1
            elif metodo != 0 and x1 == '' and funcion != '' and cifras != '':
                self.mensajesAlerta(1,3)
                control = 1
            elif metodo != 0 and x1 != '' and funcion != '' and cifras == '':
                self.mensajesAlerta(1,7)
                control = 1
            elif metodo != 0 and (x1 == '' or funcion == '' or cifras == ''):
                self.mensajesAlerta(1,6)
                control = 1


            if control == 0:

                self.tableWidget.setVisible(True)
                lista_Coeficientes = metodos.coefs(self.lineEdit.text())
                lst = metodos.metodoHorner(
                    lista_Coeficientes, x1Prueba, cifrasPrueba)

                rows = len(lst)  # Numero de filas
                columns = len(lst[0])  # Numero de columnas
                len_Col = int(930/columns)  # Tamaño de las columnas

                # Aplicamos unas configuraciones a la tabla
                self.tableWidget.setColumnCount(columns)
                self.tableWidget.setRowCount(rows)
                self.tableWidget.verticalHeader().setVisible(False)
                self.tableWidget.horizontalHeader().setVisible(False)

                for row in range(rows):  # Primer for controla las filas
                    for column in range(columns):  # Segundo for controla las columnas

                        item = QtWidgets.QTableWidgetItem()
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        item.setFont(font)
                        item.setBackground(brush)
                        item.setForeground(brush_2)
                        item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)

                        if row == 0:  # header o encabezado
                            salida = lst[row][column]
                            item.setText(salida)
                            self.tableWidget.setItem(row, column, item)
                            self.tableWidget.setColumnWidth(column, len_Col)
                        else:
                            if column == 0:
                                salida = "%.0f" % (lst[row][column])
                                item.setText(str(salida))
                                self.tableWidget.setItem(row, column, item)
                                self.tableWidget.setColumnWidth(column, len_Col)
                            else:
                                salida = "%.5f" % float(lst[row][column])
                                item.setText(str(salida))
                                self.tableWidget.setItem(row, column, item)
                                self.tableWidget.setColumnWidth(column, len_Col)

        # tabla de muller
        elif metodo == 9:

            control = 0

            if metodo != 0 and x1 == '' and x2 == '' and x3 == '' and funcion == '' and cifras == '':
                    self.mensajesAlerta(1,1)
                    control = 1
            elif metodo != 0 and x1 != '' and x2 != '' and x3 != '' and funcion == '' and cifras != '':
                self.mensajesAlerta(1,2)
                control = 1
            elif metodo != 0 and x1 == '' and x2 != '' and x3 != '' and funcion != '' and cifras != '':
                self.mensajesAlerta(1,3)
                control = 1
            elif metodo != 0 and x1 != '' and x2 == '' and x3 != '' and funcion != '' and cifras != '':
                self.mensajesAlerta(1,4)
                control = 1
            elif metodo != 0 and x1 != '' and x2 != '' and x3 != '' and funcion != '' and cifras == '':
                self.mensajesAlerta(1,7)
                control = 1
            elif metodo != 0 and x1 != '' and x2 != '' and x3 == '' and funcion != '' and cifras != '':
                self.mensajesAlerta(1,5)
                control = 1
            elif metodo != 0 and (x1 == '' or x2 == '' and x3 == '' or funcion == '' or cifras == ''):
                self.mensajesAlerta(1,6)
                control = 1



            if control == 0:
                lst = metodos.metodoMuller(
                    funcion, x1Prueba, x2Prueba, x3Prueba, cifrasPrueba)

                rows = len(lst)  # Numero de filas
                columns = len(lst[0])  # Numero de columnas
                len_Col = int(930/columns)  # Tamaño de las columnas

                # Aplicamos unas configuraciones a la tabla
                self.tableWidget.setColumnCount(columns)
                self.tableWidget.setRowCount(rows)
                self.tableWidget.verticalHeader().setVisible(False)
                self.tableWidget.horizontalHeader().setVisible(False)

                for row in range(rows):  # primer for controla las filas
                    for column in range(columns):  # Segundo for controla las columnas
                    
                        item = QtWidgets.QTableWidgetItem()
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        item.setFont(font)
                        item.setBackground(brush)
                        item.setForeground(brush_2)
                        item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                        
                        if row == 0:
                            salida = lst[row][column]
                            item.setText(salida)
                            self.tableWidget.setItem(row, column, item)
                            self.tableWidget.setColumnWidth(column, len_Col)
                        else:
                            if column == 0:
                                salida = "%.0f" % (lst[row][column])
                                item.setText(str(salida))
                                self.tableWidget.setItem(
                                    row, column, item)
                                self.tableWidget.setColumnWidth(column, len_Col)
                            else:
                                salida = "%.5f" % float(lst[row][column])
                                item.setText(str(salida))
                                self.tableWidget.setItem(
                                    row, column, item)
                                self.tableWidget.setColumnWidth(column, len_Col)

        # tabla de bairstown
        elif metodo == 10:

            control = 0

            if metodo != 0 and x1 == '' and x2 == '' and funcion == '' and cifras == '':
                self.mensajesAlerta(1,1)
                control = 1
            elif metodo != 0 and x1 != '' and x2 != '' and funcion == '' and cifras != '':
                self.mensajesAlerta(1,2)
                control = 1
            elif metodo != 0 and x1 == '' and x2 != '' and funcion != '' and cifras != '':
                self.mensajesAlerta(1,10)
                control = 1
            elif metodo != 0 and x1 != '' and x2 == '' and funcion != '' and cifras != '':
                self.mensajesAlerta(1,11)
                control = 1
            elif metodo != 0 and x1 != '' and x2 != '' and funcion != '' and cifras == '':
                self.mensajesAlerta(1,7)
                control = 1
            elif metodo != 0 and (x1 == '' or x2 == '' or funcion == '' or cifras == ''):
                self.mensajesAlerta(1,6)
                control = 1

            if control == 0:

                lista_Coeficientes = metodos.coefs(funcion)
                lista_Coeficientes.reverse()

                lst = metodos.metodoBairstow(
                    lista_Coeficientes, x1Prueba, x2Prueba, cifrasPrueba)

                columns = len(lst)

                # Aplicamos unas configuraciones a la tabla
                self.tableWidget.setColumnCount(columns)
                self.tableWidget.setRowCount(2)
                self.tableWidget.verticalHeader().setVisible(False)
                self.tableWidget.horizontalHeader().setVisible(False)
                self.tableWidget.setVisible(True)

                # Controlamos el tamaño que tendra cada columna de forma variable y no estatica como loveniamos haciendo
                tamanioColumnas = 0
                listaTamanio = []
                contadorTamanio = 0
                for x in range(0, columns):
                    listaTamanio.append(len(str(lst[x]))*7)
                    contadorTamanio += len(str(lst[x]))*7

                listaTamanio.sort()

                for row in range(0, 2):
                    for column in range(0, columns):

                        item = QtWidgets.QTableWidgetItem()
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        item.setFont(font)
                        item.setBackground(brush)
                        item.setForeground(brush_2)
                        item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)
                        
                        if row == 0:
                            salida = "Raiz #"+str(column+1)
                            item.setText(salida)
                            self.tableWidget.setItem(
                                row, column, item)
                            if contadorTamanio < 930:
                                tamanioColumnas = float(
                                    listaTamanio[len(listaTamanio)-1])
                                self.tableWidget.setColumnWidth(
                                    column, tamanioColumnas)
                            else:
                                tamanioColumnas = len(str(lst[column]))*7
                                self.tableWidget.setColumnWidth(
                                    column, tamanioColumnas)
                        else:
                            salida = str(lst[column])
                            item.setText(str(salida))
                            self.tableWidget.setItem(
                                row, column, item)
                            if contadorTamanio < 930:
                                tamanioColumnas = float(
                                    listaTamanio[len(listaTamanio)-1])
                                self.tableWidget.setColumnWidth(
                                    column, tamanioColumnas)

                            else:
                                tamanioColumnas = len(str(lst[column]))*7
                                self.tableWidget.setColumnWidth(
                                    column, tamanioColumnas)

    def insertar_datos_a_tabla_unidad3(self, metodo, puntos, valor):

        # Limpiamos la tabla
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()

        # Aplicamos unas configuraciones
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)

        if metodo == 1:  # Interpolacion Lineal

            lst = metodos.interpolacionLineal(puntos[0], valor)

            # Verificamos si solo mostraremos el polinomio o el valor
            if self.radioButton.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(2)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Polinomio"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(lst[0])))
                self.tableWidget.setColumnWidth(1, 830)

                self.tableWidget.setItem(
                    1, 0, QtWidgets.QTableWidgetItem("Resultado"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(
                    1, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setVisible(True)


            elif self.radioButton_2.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(1)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Valor"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setVisible(True)
            else:
                self.mensajesAlerta(2,7)

        elif metodo == 2:  # Interpolacion Cuadratica

            lst = metodos.interpolacionCuadratica(puntos[0], puntos[1], valor)

            if self.radioButton.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(2)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Polinomio"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(lst[0])))
                self.tableWidget.setColumnWidth(1, 830)

                self.tableWidget.setItem(
                    1, 0, QtWidgets.QTableWidgetItem("Resultado"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(
                    1, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setVisible(True)

            elif self.radioButton_2.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(1)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Valor"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setVisible(True)
            else:
                self.mensajesAlerta(2,7)

        elif metodo == 3:  # Interpolacion de lagrange

            lst = metodos.interpolacionLagrange(puntos[0], puntos[1], valor)

            if self.radioButton.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(2)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Polinomio"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(lst[0])))
                self.tableWidget.setColumnWidth(1, 830)

                self.tableWidget.setItem(
                    1, 0, QtWidgets.QTableWidgetItem("Resultado"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(
                    1, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setVisible(True)

            elif self.radioButton_2.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(1)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Valor"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setVisible(True)

            else:
                self.mensajesAlerta(2,7)

        elif metodo == 4:  # Interpolacion de newton

            lst = metodos.interpolacionNewton(puntos[0], puntos[1], valor)

            if self.radioButton.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(2)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Polinomio"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(lst[0])))
                self.tableWidget.setColumnWidth(1, 830)

                self.tableWidget.setItem(
                    1, 0, QtWidgets.QTableWidgetItem("Resultado"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(
                    1, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setVisible(True)

            elif self.radioButton_2.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(1)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Valor"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setVisible(True)

            else:
                self.mensajesAlerta(2,7)

        elif metodo == 5:  # polinomio de hermite
            lst = metodos.interpolacionHermite(puntos, valor)

            if self.radioButton.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(2)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Polinomio"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(lst[0])))
                self.tableWidget.setColumnWidth(1, 830)

                self.tableWidget.setItem(
                    1, 0, QtWidgets.QTableWidgetItem("Resultado"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(
                    1, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setVisible(True)

            elif self.radioButton_2.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(1)

                self.tableWidget.setItem(
                    0, 0, QtWidgets.QTableWidgetItem("Valor"))
                self.tableWidget.setColumnWidth(0, 100)

                self.tableWidget.setItem(
                    0, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setVisible(True)

            else:
                self.mensajesAlerta(2,7)

        elif metodo == 6:  # funciones splines

            if self.radioButton.isChecked():  # cero

                lst = metodos.trazadoresCubicos(puntos[0], puntos[1], 0, valor)
                rows = len(lst)

                self.tableWidget.setColumnCount(1)
                self.tableWidget.setRowCount(rows)
                for row in range(0, rows):
                    self.tableWidget.setItem(
                        row, 0, QtWidgets.QTableWidgetItem(str(lst[row])))
                    self.tableWidget.setColumnWidth(0, 830)
                
                self.tableWidget.setVisible(True)

            elif self.radioButton_2.isChecked():  # uno

                lst = metodos.trazadoresCubicos(puntos[0], puntos[1], 1, valor)
                rows = len(lst)

                self.tableWidget.setColumnCount(1)
                self.tableWidget.setRowCount(rows)

                for row in range(0, rows):
                    self.tableWidget.setItem(
                        row, 0, QtWidgets.QTableWidgetItem(str(lst[row])))
                    self.tableWidget.setColumnWidth(0, 830)

                self.tableWidget.setVisible(True)

            elif self.radioButton_3.isChecked():  # dos

                lst = metodos.trazadoresCubicos(puntos[0], puntos[1], 2, valor)
                rows = len(lst)

                self.tableWidget.setColumnCount(1)
                self.tableWidget.setRowCount(rows)

                for row in range(0, rows):
                    self.tableWidget.setItem(
                        row, 0, QtWidgets.QTableWidgetItem(str(lst[row])))
                    self.tableWidget.setColumnWidth(0, 830)

                self.tableWidget.setVisible(True)

            elif self.radioButton_4.isChecked():  # tres

                lst = metodos.trazadoresCubicos(puntos[0], puntos[1], 3, valor)
                rows = len(lst)

                self.tableWidget.setColumnCount(1)
                self.tableWidget.setRowCount(rows)

                for row in range(0, rows):
                    self.tableWidget.setItem(
                        row, 0, QtWidgets.QTableWidgetItem(str(lst[row])))
                    self.tableWidget.setColumnWidth(0, 830)

                self.tableWidget.setVisible(True)

            else:
                self.mensajesAlerta(2,7)

    def insertar_datos_a_tabla_unidad4(self, metodo):

        listaX = []
        listaY = []
        puntos = []
        listaXapoyo = []
        listaYapoyo = []
        h = 0
        puntoInicial = 0
        control_mostrar_respuesta = 0

        global cuantasFilasYColumnas, tabla_unidad4_si_no

        # Encontramos puntos de la tabla si los hay
        if tabla_unidad4_si_no == 1:

            for x in range(0, 2):

                for y in range(1, cuantasFilasYColumnas+1):
                    if x == 0:
                        listaX.append(self.tableWidget_2.item(x, y).text())
                    elif x == 1:
                        listaY.append(self.tableWidget_2.item(x, y).text())

            for i in listaX:
                listaXapoyo.append(float(i))

            for i in listaY:
                listaYapoyo.append(float(i))

            puntos = [listaXapoyo, listaYapoyo]
            print(puntos)

        else:
            funcion = self.funcion_uni4.text()
            try:
                puntoInicial = float(self.puntoInicial_uni4.text())
                h = float(self.h_uni4.text())
            except:
                print('')

        if metodo == 2:  # Hacia delante

            if tabla_unidad4_si_no == 0:
                cmb = self.comboBox_3.currentIndex()
                
                if cmb >= 0:
                    if self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() == '':
                        self.mensajesAlerta(3,1)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,2)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,3)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() == '':
                        self.mensajesAlerta(3,4)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' or self.puntoInicial_uni4.text() == '' or self.h_uni4.text() == '':
                        self.mensajesAlerta(3,5)
                        control_mostrar_respuesta = 1

                    else:
                        lst = metodos_uni4.diferenciacion_numerica_adelante(funcion, puntoInicial, h, [])
                else:
                    self.mensajesAlerta(3,13)
                    control_mostrar_respuesta = 1
            else:

                h = float(listaX[1])-float(listaX[0])
                puntoInicial = float(self.lineEdit_6.text())

                lst = metodos_uni4.diferenciacion_numerica_adelante(
                    '', puntoInicial, h, puntos)

        elif metodo == 3: # Hacia atras
            if tabla_unidad4_si_no == 0:

                cmb = self.comboBox_3.currentIndex()
        
                if cmb >= 0:
                    if self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() == '':
                        self.mensajesAlerta(3,1)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,2)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,3)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() == '':
                        self.mensajesAlerta(3,4)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' or self.puntoInicial_uni4.text() == '' or self.h_uni4.text() == '':
                        self.mensajesAlerta(3,5)
                        control_mostrar_respuesta = 1

                    else:
                        lst = metodos_uni4.diferenciacion_numerica_atras(funcion, puntoInicial, h, [])
                else:
                    self.mensajesAlerta(3,13)
                    control_mostrar_respuesta = 1

            else:
                h = float(listaX[1])-float(listaX[0])
                puntoInicial = float(self.lineEdit_6.text())
                lst = metodos_uni4.diferenciacion_numerica_atras(
                    '', puntoInicial, h, puntos)

        elif metodo == 4: # centrada

            if tabla_unidad4_si_no == 0:

                cmb = self.comboBox_3.currentIndex()
                
                if cmb >= 0:
                
                    if self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() == '':
                        self.mensajesAlerta(3,1)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,2)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,3)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() == '':
                        self.mensajesAlerta(3,4)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' or self.puntoInicial_uni4.text() == '' or self.h_uni4.text() == '':
                        self.mensajesAlerta(3,5)
                        control_mostrar_respuesta = 1

                    else:
                        lst = metodos_uni4.diferenciacion_numerica_centrada(funcion, puntoInicial, h, [],0)
                else:
                    self.mensajesAlerta(3,13)
                    control_mostrar_respuesta = 1
            else:
                h = float(listaX[1])-float(listaX[0])
                puntoInicial = float(self.lineEdit_6.text())
                lst = metodos_uni4.diferenciacion_numerica_centrada(
                    '', puntoInicial, h, puntos,0)

        elif metodo == 5: # Tres puntos

            if tabla_unidad4_si_no == 0:

                cmb = self.comboBox_3.currentIndex()
                
                if cmb >= 0:
                
                    if self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() == '':
                        self.mensajesAlerta(3,1)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,2)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,3)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() == '':
                        self.mensajesAlerta(3,4)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' or self.puntoInicial_uni4.text() == '' or self.h_uni4.text() == '':
                        self.mensajesAlerta(3,5)
                        control_mostrar_respuesta = 1

                    else:
                        lst = metodos_uni4.diferenciacion_numerica_tres_puntos(
                            funcion, puntoInicial, h, [])
                else:
                    self.mensajesAlerta(3,13)
                    control_mostrar_respuesta = 1
            else:
                h = float(listaX[1])-float(listaX[0])
                puntoInicial = float(self.lineEdit_6.text())
                lst = metodos_uni4.diferenciacion_numerica_tres_puntos(
                    '', puntoInicial, h, puntos)

        elif metodo == 6: # Cinco Puntos

            if tabla_unidad4_si_no == 0:
                cmb = self.comboBox_3.currentIndex()
                
                if cmb >= 0:
                
                    if self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() == '':
                            self.mensajesAlerta(3,1)
                            control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,2)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,3)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() == '':
                        self.mensajesAlerta(3,4)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' or self.puntoInicial_uni4.text() == '' or self.h_uni4.text() == '':
                        self.mensajesAlerta(3,5)
                        control_mostrar_respuesta = 1

                    else:
                        lst = metodos_uni4.diferenciacion_numerica_cinco_puntos(
                            funcion, puntoInicial, h, [])
                else:
                    self.mensajesAlerta(3,13)
                    control_mostrar_respuesta = 1
            else:
                h = float(listaX[1])-float(listaX[0])
                puntoInicial = float(self.lineEdit_6.text())
                lst = metodos_uni4.diferenciacion_numerica_cinco_puntos(
                    '', puntoInicial, h, puntos)

        elif metodo == 8: # Adelante orden superior 


            if tabla_unidad4_si_no == 0:

                cmb = self.comboBox_3.currentIndex()
                
                if cmb >= 0:
                
                    if self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() == '':
                            self.mensajesAlerta(3,1)
                            control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,2)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,3)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() == '':
                        self.mensajesAlerta(3,4)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' or self.puntoInicial_uni4.text() == '' or self.h_uni4.text() == '':
                        self.mensajesAlerta(3,5)
                        control_mostrar_respuesta = 1

                    else:
                        lst = metodos_uni4.diferenciacion_numerica_adelante_orden_superior(
                            funcion, puntoInicial, h, [])
                else:
                    self.mensajesAlerta(3,13)
                    control_mostrar_respuesta = 1
            else:
                h = float(listaX[1])-float(listaX[0])
                puntoInicial = float(self.lineEdit_6.text())
                lst = metodos_uni4.diferenciacion_numerica_adelante_orden_superior(
                    '', puntoInicial, h, puntos)

        elif metodo == 9: # Atras orden superior

            if tabla_unidad4_si_no == 0:

                cmb = self.comboBox_3.currentIndex()
                
                if cmb >= 0:
                
                    if self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() == '':
                            self.mensajesAlerta(3,1)
                            control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,2)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,3)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() == '':
                        self.mensajesAlerta(3,4)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' or self.puntoInicial_uni4.text() == '' or self.h_uni4.text() == '':
                        self.mensajesAlerta(3,5)
                        control_mostrar_respuesta = 1

                    else:
                        lst = metodos_uni4.diferenicacion_numerica_atras_orden_superior(
                            funcion, puntoInicial, h, [])
                else:
                    self.mensajesAlerta(3,13)
                    control_mostrar_respuesta = 1
            else:
                h = float(listaX[1])-float(listaX[0])
                puntoInicial = float(self.lineEdit_6.text())
                lst = metodos_uni4.diferenicacion_numerica_atras_orden_superior(
                    '', puntoInicial, h, puntos)

        elif metodo == 10: # Centrado orden superio

            if tabla_unidad4_si_no == 0:
                cmb = self.comboBox_3.currentIndex()
                
                if cmb >= 0:
                
                    if self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() == '':
                            self.mensajesAlerta(3,1)
                            control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,2)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() != '':
                        self.mensajesAlerta(3,3)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() == '':
                        self.mensajesAlerta(3,4)
                        control_mostrar_respuesta = 1

                    elif self.funcion_uni4.text() == '' or self.puntoInicial_uni4.text() == '' or self.h_uni4.text() == '':
                        self.mensajesAlerta(3,5)
                        control_mostrar_respuesta = 1

                    else:
                        lst = metodos_uni4.diferenicacion_numerica_centrales_orden_superior(
                            funcion, puntoInicial, h, [])
                else:
                    self.mensajesAlerta(3,13)
                    control_mostrar_respuesta = 1
            else:
                h = float(listaX[1])-float(listaX[0])
                puntoInicial = float(self.lineEdit_6.text())
                lst = metodos_uni4.diferenicacion_numerica_centrales_orden_superior('', puntoInicial, h, puntos)

        elif metodo == 11: # Richardson
                
            if self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() == '' and self.nivel_uni4.text() == '':
                    self.mensajesAlerta(3,9)
                    control_mostrar_respuesta = 1

            elif self.funcion_uni4.text() == '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() != '' and self.nivel_uni4.text() != '':
                self.mensajesAlerta(3,2)
                control_mostrar_respuesta = 1

            elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() == '' and self.h_uni4.text() != '' and self.nivel_uni4.text() != '':
                self.mensajesAlerta(3,3)
                control_mostrar_respuesta = 1

            elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() == '' and self.nivel_uni4.text() != '':
                self.mensajesAlerta(3,4)
                control_mostrar_respuesta = 1

            elif self.funcion_uni4.text() != '' and self.puntoInicial_uni4.text() != '' and self.h_uni4.text() != '' and self.nivel_uni4.text() == '':
                self.mensajesAlerta(3,10)
                control_mostrar_respuesta = 1

            elif self.funcion_uni4.text() == '' or self.puntoInicial_uni4.text() == '' or self.h_uni4.text() == '' or self.nivel_uni4.text() == '':
                self.mensajesAlerta(3,5)
                control_mostrar_respuesta = 1
            
            else:
                nivel = int(self.nivel_uni4.text())
                lst = metodos_uni4.metodo_richardson(funcion, puntoInicial, h, nivel)

        elif metodo == 13: # Trapecio simple
        
            if tabla_unidad4_si_no == 0:
                cmb = self.comboBox_3.currentIndex()
                
                if cmb >= 0:

                    if self.a0_normal.text() == '' and self.b0_normal.text() == '' and funcion == '':
                        self.mensajesAlerta(3,6)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() == '' and self.b0_normal.text() != '' and funcion != '':
                        self.mensajesAlerta(3,7)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() != '' and self.b0_normal.text() == '' and funcion != '':
                        self.mensajesAlerta(3,8)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion == '':
                        self.mensajesAlerta(3,9)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() == '' or self.b0_normal.text() == '' or funcion == '':
                        self.mensajesAlerta(3,5)
                        control_mostrar_respuesta = 1

                    else:
                        a = float(self.a0_normal.text())
                        b = float(self.b0_normal.text())

                        if a > b:
                            self.mensajesAlerta(3,12)
                            control_mostrar_respuesta = 1
                        else:
                            lst = metodos_uni4.regla_del_trapecio_simple(funcion,a,b,[], 0)
                else:
                    self.mensajesAlerta(3,13)
                    control_mostrar_respuesta = 1
            else:
                a = listaXapoyo[len(listaXapoyo)-1]
                b = listaXapoyo[0]

                if a > b:
                    self.mensajesAlerta(3,12)
                    control_mostrar_respuesta = 1
                else:
                    lst = metodos_uni4.regla_del_trapecio_simple(
                    '', a, b, puntos, 0)

        elif metodo == 14: # Trapecio Compuesto
   
            if tabla_unidad4_si_no == 0:
                cmb = self.comboBox_3.currentIndex()
                
                if cmb >= 0:
                    n = self.puntoInicial_uni4.text()

                    if self.a0_normal.text() == '' and self.b0_normal.text() == '' and funcion == '' and n == '':
                        self.mensajesAlerta(3,5)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() == '' and self.b0_normal.text() != '' and funcion != '' and n != '':
                        self.mensajesAlerta(3,7)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() != '' and self.b0_normal.text() == '' and funcion != '' and n != '':
                        self.mensajesAlerta(3,8)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion == '' and n != '':
                        self.mensajesAlerta(3,9)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion != '' and n == '':
                        self.mensajesAlerta(3,10)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() == '' or self.b0_normal.text() == '' or funcion == '' or n == '':
                        self.mensajesAlerta(3,5)
                        control_mostrar_respuesta = 1
                        
                    else:
                        n = int(self.puntoInicial_uni4.text())
                        a = float(self.a0_normal.text())
                        b = float(self.b0_normal.text())
                        
                        if a > b:
                            self.mensajesAlerta(3,12)
                            control_mostrar_respuesta = 1
                        else:
                            lst = metodos_uni4.regla_del_trapecio_compuesta(
                            funcion, a,b,n, [],0)
                else:
                    self.mensajesAlerta(3,13)
                    control_mostrar_respuesta = 1
            else:
                a = listaXapoyo[len(listaXapoyo)-1]
                b = listaXapoyo[0]
                n = len(listaXapoyo)-1
                if a > b:
                    self.Mensajes_error(3,12)
                    control_mostrar_respuesta = 1
                else:
                    lst = metodos_uni4.regla_del_trapecio_compuesta(
                    '', a,b,n, puntos,0)

        elif metodo == 15:  # Integrales dobles y triples 
            self.insertar_datos_a_tabla_unidad4(15)

        elif metodo == 16: # simpson 1/3 simple
                
            if tabla_unidad4_si_no == 0:
                cmb = self.comboBox_3.currentIndex()
                
                if cmb >= 0:

                    if self.a0_normal.text() == '' and self.b0_normal.text() == '' and funcion == '':
                        self.mensajesAlerta(3,6)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() == '' and self.b0_normal.text() != '' and funcion != '':
                        self.mensajesAlerta(3,7)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() != '' and self.b0_normal.text() == '' and funcion != '':
                        self.mensajesAlerta(3,8)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion == '':
                        self.mensajesAlerta(3,9)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() == '' or self.b0_normal.text() == '' or funcion == '':
                        self.mensajesAlerta(3,5)
                        control_mostrar_respuesta = 1

                    else:
                        a = float(self.a0_normal.text())
                        b = float(self.b0_normal.text())
                        if a > b:
                            self.mensajesAlerta(3,12)
                            control_mostrar_respuesta = 1
                        else:
                            lst = metodos_uni4.integracion_simpson_unTercio_simple(
                            funcion, a, b, [], [])
                else:
                    self.mensajesAlerta(3,13)
                    control_mostrar_respuesta = 1
            else:
                a = listaXapoyo[len(listaXapoyo)-1]
                b = listaXapoyo[0]
                if a > b:
                    self.mensajesAlerta(3,12)
                    control_mostrar_respuesta = 1
                else: 
                    lst = metodos_uni4.integracion_simpson_unTercio_simple(
                    '', a, b, listaXapoyo, listaYapoyo)

        elif metodo == 17: # simpson 1/3 compuesto
            
            if tabla_unidad4_si_no == 0:
                cmb = self.comboBox_3.currentIndex()
                if cmb >= 0:
                    n = self.puntoInicial_uni4.text()
                    if self.a0_normal.text() == '' and self.b0_normal.text() == '' and funcion == '' and n == '':
                        self.mensajesAlerta(3,5)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() == '' and self.b0_normal.text() != '' and funcion != '' and n != '':
                        self.mensajesAlerta(3,7)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() != '' and self.b0_normal.text() == '' and funcion != '' and n != '':
                        self.mensajesAlerta(3,8)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion == '' and n != '':
                        self.mensajesAlerta(3,9)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion != '' and n == '':
                        self.mensajesAlerta(3,10)
                        control_mostrar_respuesta = 1
                    elif self.a0_normal.text() == '' or self.b0_normal.text() == '' or funcion == '' or n == '':
                        self.mensajesAlerta(3,5)
                        control_mostrar_respuesta = 1
                        
                    else:
                        a = float(self.a0_normal.text())
                        b = float(self.b0_normal.text())
                        n = int(self.puntoInicial_uni4.text())
                        if a > b:
                            self.mensajesAlerta(3,12)
                            control_mostrar_respuesta = 1
                        else: 
                            lst = metodos_uni4.integracion_simpson_unTercio_compuesta(funcion, a, b, n, [],[])
                else:
                    self.mensajesAlerta(3,13)
                    control_mostrar_respuesta = 1
            else:
                a = listaXapoyo[len(listaXapoyo)-1]
                b = listaXapoyo[0]
                n = len(listaXapoyo)-1
                if a > b:
                    self.mensajesAlerta(3,12)
                else: 
                    lst = metodos_uni4.integracion_simpson_unTercio_compuesta(
                    '', a, b, n, listaXapoyo, listaYapoyo)

        elif metodo == 18: # simpson 3/8 simple

            if self.a0_normal.text() == '' and self.b0_normal.text() == '' and funcion == '':
                self.mensajesAlerta(3,6)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() == '' and self.b0_normal.text() != '' and funcion != '':
                self.mensajesAlerta(3,7)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() == '' and funcion != '':
                self.mensajesAlerta(3,8)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion == '':
                self.mensajesAlerta(3,9)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() == '' or self.b0_normal.text() == '' or funcion == '':
                self.mensajesAlerta(3,5)
                control_mostrar_respuesta = 1
            
            else:
                a = float(self.a0_normal.text())
                b = float(self.b0_normal.text())
                if a > b:
                    self.mensajesAlerta(3,12)
                    control_mostrar_respuesta = 1
                else:
                    lst = metodos_uni4.integracion_simpson_tresOctavos_simple(funcion, a, b)

        elif metodo == 19: # simpson 3/8 compuesto

            n = self.puntoInicial_uni4.text()

            if self.a0_normal.text() == '' and self.b0_normal.text() == '' and funcion == '' and n == '':
                self.mensajesAlerta(3,5)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() == '' and self.b0_normal.text() != '' and funcion != '' and n != '':
                self.mensajesAlerta(3,7)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() == '' and funcion != '' and n != '':
                self.mensajesAlerta(3,8)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion == '' and n != '':
                self.mensajesAlerta(3,9)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion != '' and n == '':
                self.mensajesAlerta(3,10)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() == '' or self.b0_normal.text() == '' or funcion == '' or n == '':
                self.mensajesAlerta(3,5)
                control_mostrar_respuesta = 1
                    
            else:
                a = float(self.a0_normal.text())
                b = float(self.b0_normal.text())
                n = int(self.puntoInicial_uni4.text())

                if a > b:
                    self.mensajesAlerta(3,12)
                    control_mostrar_respuesta = 1
                else:
                    lst = metodos_uni4.integracion_simpson_tresOctavos_compuesta(
                    funcion, a, b, n)

        elif metodo == 20: # rosemberg

            n = self.puntoInicial_uni4.text()

            if self.a0_normal.text() == '' and self.b0_normal.text() == '' and funcion == '' and n == '':
                self.mensajesAlerta(3,5)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() == '' and self.b0_normal.text() != '' and funcion != '' and n != '':
                self.mensajesAlerta(3,7)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() == '' and funcion != '' and n != '':
                self.mensajesAlerta(3,8)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion == '' and n != '':
                self.mensajesAlerta(3,9)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion != '' and n == '':
                self.mensajesAlerta(3,10)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() == '' or self.b0_normal.text() == '' or funcion == '' or n == '':
                self.mensajesAlerta(3,5)
                control_mostrar_respuesta = 1 
            else:
                a = float(self.a0_normal.text())
                b = float(self.b0_normal.text())
                n = int(self.puntoInicial_uni4.text())
                if a > b:
                    self.mensajesAlerta(3,12)
                    control_mostrar_respuesta = 1
                else:
                    lst = metodos_uni4.integracion_rosemberg(funcion, a, b, n)

        elif metodo == 21: # cuadratura gaussiana
            n = self.puntoInicial_uni4.text()

            if self.a0_normal.text() == '' and self.b0_normal.text() == '' and funcion == '' and n == '':
                self.mensajesAlerta(3,5)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() == '' and self.b0_normal.text() != '' and funcion != '' and n != '':
                self.mensajesAlerta(3,7)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() == '' and funcion != '' and n != '':
                self.mensajesAlerta(3,8)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion == '' and n != '':
                self.mensajesAlerta(3,9)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion != '' and n == '':
                self.mensajesAlerta(3,10)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() == '' or self.b0_normal.text() == '' or funcion == '' or n == '':
                self.mensajesAlerta(3,5)
                control_mostrar_respuesta = 1
                
            else:
                a = float(self.a0_normal.text())
                b = float(self.b0_normal.text())
                n = int(self.puntoInicial_uni4.text())
                if a > b:
                    self.mensajesAlerta(3,12)
                    control_mostrar_respuesta = 1
                else:
                    lst = metodos_uni4.integracion_cuadratura_Gaussiana(
                    funcion, a, b, n)

        elif metodo == 22: # simpson adaptativo
            n = self.puntoInicial_uni4.text()

            if self.a0_normal.text() == '' and self.b0_normal.text() == '' and funcion == '' and n == '':
                self.mensajesAlerta(3,5)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() == '' and self.b0_normal.text() != '' and funcion != '' and n != '':
                self.mensajesAlerta(3,7)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() == '' and funcion != '' and n != '':
                self.mensajesAlerta(3,8)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion == '' and n != '':
                self.mensajesAlerta(3,9)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion != '' and n == '':
                self.mensajesAlerta(3,10)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() == '' or self.b0_normal.text() == '' or funcion == '' or n == '':
                self.mensajesAlerta(3,5)
                control_mostrar_respuesta = 1
                
            else:
                a = float(self.a0_normal.text())
                b = float(self.b0_normal.text())
                tolerancia = float(self.puntoInicial_uni4.text())
                if a > b:
                    self.mensajesAlerta(3,12)
                    control_mostrar_respuesta = 1
                else:
                    lst = metodos_uni4.integracion_simpson_unTercio_adaptativo(
                    tolerancia, a, b, funcion)

        elif metodo == 23: # boole

            if self.a0_normal.text() == '' and self.b0_normal.text() == '' and funcion == '':
                self.mensajesAlerta(3,6)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() == '' and self.b0_normal.text() != '' and funcion != '':
                self.mensajesAlerta(3,7)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() == '' and funcion != '':
                self.mensajesAlerta(3,8)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() != '' and self.b0_normal.text() != '' and funcion == '':
                self.mensajesAlerta(3,9)
                control_mostrar_respuesta = 1
            elif self.a0_normal.text() == '' or self.b0_normal.text() == '' or funcion == '':
                self.mensajesAlerta(3,5)
                control_mostrar_respuesta = 1

            else:
                a = float(self.a0_normal.text())
                b = float(self.b0_normal.text())
                if a > b:
                    self.mensajesAlerta(3,12)
                    control_mostrar_respuesta = 1
                else:
                    lst = metodos_uni4.integracion_Boole(a, b, funcion)

        if control_mostrar_respuesta == 0:
            self.tableWidget.setVisible(False)
            self.cajaTexto.setVisible(True)

            # Agregando respuesta a la caja de texto
            salida = ""

            for i in lst:
                salida += "\n"+str(i)+"\n"

            self.cajaTexto.setText(salida)

    def insertar_datos_a_tabla_unidad5(self, metodo):
        # Puntos a evaluar, funcion en la que evaluaremos y las cifras que se usaran
        x1 = self.lineEdit_2.text()  # Primer punto a evaluar
        x2 = self.lineEdit_3.text()  # Segundo punto a evaluar
        x3 = self.lineEdit_4.text()  # Tercer punto a evaluar
        cifras = self.lineEdit_5.text()  # numero de cifras significativas
        funcion = self.lineEdit.text()  # función a evaluar

        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
        brush.setStyle(QtCore.Qt.NoBrush)

        brush_2 = QtGui.QBrush(QtGui.QColor(134, 135, 208))
        brush_2.setStyle(QtCore.Qt.SolidPattern)

        control = 0

        # Limpiamos la tabla antes de llenarla
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)


        # tabla de biseccion - hasta secante
        
        control = 0

        if metodo >= 1 and metodo <= 5:

            if metodo != 0 and x1 == '' and x2 == '' and x3 == '' and funcion == '' and cifras == '':
                    self.mensajesAlerta(4,1)
                    control = 1
            elif metodo != 0 and x1 != '' and x2 != '' and x3 != '' and funcion == '' and cifras != '':
                self.mensajesAlerta(4,2)
                control = 1
            elif metodo != 0 and x1 == '' and x2 != '' and x3 != '' and funcion != '' and cifras != '':
                self.mensajesAlerta(4,3)
                control = 1
            elif metodo != 0 and x1 != '' and x2 == '' and x3 != '' and funcion != '' and cifras != '':
                self.mensajesAlerta(4,4)
                control = 1
            elif metodo != 0 and x1 != '' and x2 != '' and x3 != '' and funcion != '' and cifras == '':
                self.mensajesAlerta(4,7)
                control = 1
            elif metodo != 0 and x1 != '' and x2 != '' and x3 == '' and funcion != '' and cifras != '':
                self.mensajesAlerta(4,5)
                control = 1
            elif metodo != 0 and (x1 == '' or x2 == '' and x3 == '' or funcion == '' or cifras == ''):
                self.mensajesAlerta(4,6)
                control = 1

        elif metodo >= 6 and metodo <= 7:
            orden = self.lineOrden.text()

            if metodo != 0 and x1 == '' and x2 == '' and x3 == '' and funcion == '' and cifras == '' and orden == '':
                    self.mensajesAlerta(4,1)
                    control = 1
            elif metodo != 0 and x1 != '' and x2 != '' and x3 != '' and funcion == '' and cifras != '' and orden == '':
                self.mensajesAlerta(4,2)
                control = 1
            elif metodo != 0 and x1 == '' and x2 != '' and x3 != '' and funcion != '' and cifras != '' and orden == '':
                self.mensajesAlerta(4,3)
                control = 1
            elif metodo != 0 and x1 != '' and x2 == '' and x3 != '' and funcion != '' and cifras != '' and orden == '':
                self.mensajesAlerta(4,4)
                control = 1
            elif metodo != 0 and x1 != '' and x2 != '' and x3 != '' and funcion != '' and cifras == '' and orden == '':
                self.mensajesAlerta(4,7)
                control = 1
            elif metodo != 0 and x1 != '' and x2 != '' and x3 == '' and funcion != '' and cifras != '' and orden == '':
                self.mensajesAlerta(4,5)
                control = 1
            elif metodo != 0 and (x1 == '' or x2 == '' and x3 == '' or funcion == '' or cifras == '' or orden == ''):
                self.mensajesAlerta(4,6)
                control = 1


        if control == 0:

             # Si nos devuelven la palabra: 'falsisimo' estan vacios
            x1Prueba = float((x1))
            x2Prueba = float((x2))
            x3Prueba = float((x3))
            cifrasPrueba = int((cifras))

            # Llamamos al metodo que corresponda para obtener la respuesta y la guardamos en lst
            if metodo == 1:
                lst = metodos_uni5.metodo_Euler_Adelante(funcion, x1Prueba, x2Prueba, x3Prueba, cifrasPrueba)
            elif metodo == 2:
                lst = metodos_uni5.metodo_Euler_Atras(funcion, x1Prueba, x2Prueba, x3Prueba, cifrasPrueba)
            elif metodo == 3:
                lst = metodos_uni5.metodo_Euler_Centrado(funcion, x1Prueba, x2Prueba, x3Prueba, cifrasPrueba)
            elif metodo == 4:
                lst = metodos_uni5.metodo_Euler_Mejorado(funcion, x1Prueba, x2Prueba, x3Prueba, cifrasPrueba)
            elif metodo == 5:
                lst = metodos_uni5.metodo_taylor(funcion, x1Prueba, x2Prueba, x3Prueba, cifrasPrueba)
            elif metodo == 6:
                lst = metodos_uni5.metodo_Runge_Kutta(funcion, x1Prueba, x2Prueba, x3Prueba, cifrasPrueba, float(self.lineOrden.text()))
            elif metodo == 7:
                lst = metodos_uni5.Adam_Bashforth_Moulton(funcion, x1Prueba, x2Prueba, x3Prueba, cifrasPrueba, float(self.lineOrden.text()))

            # Insertamos los valores de lst en la tabla de respuestas

            self.tableWidget.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
            rows = len(lst)  # Numero de filas
            columns = len(lst[0])  # Numero de columnas
            len_Col = int(930/columns)-5 # Tamaño que tendran las columnas

            # Aplicamos unas configuraciones a la tabla
            self.tableWidget.setColumnCount(columns)
            self.tableWidget.setRowCount(rows)
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.horizontalHeader().setVisible(False)

            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)

            brush = QtGui.QBrush(QtGui.QColor(242, 242, 242))
            brush.setStyle(QtCore.Qt.NoBrush)

            brush_2 = QtGui.QBrush(QtGui.QColor(134, 135, 208))
            brush_2.setStyle(QtCore.Qt.SolidPattern)

            for row in range(rows):  # Primer for recorre las filas en Listado_Resultante
                # Segundo for recorre las columnas en Listado_Resultante
                for column in range(columns):
                    item = QtWidgets.QTableWidgetItem()
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setFont(font)
                    item.setBackground(brush)
                    item.setForeground(brush_2)
                    item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable)

                    if row == 0:  # Encabezado o header
                        salida = lst[row][column]
                        item.setText(str(salida))

                        self.tableWidget.setItem(row, column, item)
                        self.tableWidget.setColumnWidth(column, len_Col)
                    else:
                        if column == 0:
                            salida = (lst[row][column])
                            item.setText(str(salida))
                            self.tableWidget.setItem(row, column, item)
                            self.tableWidget.setColumnWidth(column, len_Col)
                        else:
                            salida = "%.5f" % float(lst[row][column])
                            item.setText(str(salida))
                            self.tableWidget.setItem(row, column, item)
                            self.tableWidget.setColumnWidth(column, len_Col)  

            self.tableWidget.setVisible(True)
          
    def control_agregar_columna_tabla_Unidad3(self):
        global cuantasFilasYColumnas
        global etiquetaHermite
        metodo = self.comboBox_2.currentIndex()
        unidad = self.comboBox.currentIndex()
        
        if unidad == 2:
            if metodo == 0:
                print("Seleccione un metodo primero ")

            elif metodo == 1:
                self.mensajesAlerta(2,1)
            else:
                if metodo >= 1 and metodo <= 4:
                    if cuantasFilasYColumnas == 11:
                        self.mensajesAlerta(2,3)
                    else:
                        self.tableWidget_2.insertColumn(cuantasFilasYColumnas+1)
                        cuantasFilasYColumnas += 1

                if metodo == 5:
                    if cuantasFilasYColumnas == 6:
                        self.mensajesAlerta(2,6)
                    else:
                        if etiquetaHermite == "y'":
                            etiquetaHermite += "'"
                            salida = etiquetaHermite
                        else:
                            etiquetaHermite += "'"
                            salida = etiquetaHermite

                        self.tableWidget_2.insertColumn(cuantasFilasYColumnas+1)
                        self.tableWidget_2.setItem(
                            0, cuantasFilasYColumnas+1, QtWidgets.QTableWidgetItem(salida))
                        cuantasFilasYColumnas += 1
                if metodo == 6:
                    if cuantasFilasYColumnas == 11:
                        self.mensajesAlerta(2,3)
                    else:
                        self.tableWidget_2.insertColumn(cuantasFilasYColumnas+1)
                        cuantasFilasYColumnas += 1
         
        elif unidad == 3:
            
            if cuantasFilasYColumnas == 11:
                self.mensajesAlerta(2,3)
            else:
                self.tableWidget_2.insertColumn(cuantasFilasYColumnas+1)
                cuantasFilasYColumnas += 1

    def control_eliminar_columna_tabla_Unidad3(self):
        global cuantasFilasYColumnas
        metodo = self.comboBox_2.currentIndex()

        if metodo == 1:  # lineal
            if cuantasFilasYColumnas == 3:
                self.mensajesAlerta(2,5)
            else:
                self.tableWidget_2.removeColumn(cuantasFilasYColumnas)
                cuantasFilasYColumnas = cuantasFilasYColumnas - 1

        elif metodo == 2:  # Cuadratica
            if cuantasFilasYColumnas == 4:
                self.mensajesAlerta(2,5)
            else:
                self.tableWidget_2.removeColumn(cuantasFilasYColumnas)
                cuantasFilasYColumnas = cuantasFilasYColumnas - 1

        elif metodo == 3:  # Lagrange
            if cuantasFilasYColumnas == 3:
                self.mensajesAlerta(2,5)
            else:
                self.tableWidget_2.removeColumn(cuantasFilasYColumnas)
                cuantasFilasYColumnas = cuantasFilasYColumnas - 1

        elif metodo == 4:  # Newton
            if cuantasFilasYColumnas == 3:
                self.mensajesAlerta(2,5)
            else:
                self.tableWidget_2.removeColumn(cuantasFilasYColumnas)
                cuantasFilasYColumnas = cuantasFilasYColumnas-1

        elif metodo == 5:  # hermite
            if cuantasFilasYColumnas == 2:
                self.mensajesAlerta(2,5)
            else:
                self.tableWidget_2.removeColumn(cuantasFilasYColumnas)
                cuantasFilasYColumnas = cuantasFilasYColumnas-1

        elif metodo == 6:  # trazadores cubicos
            if cuantasFilasYColumnas == 3:
                self.mensajesAlerta(2,5)
            else:
                self.tableWidget_2.removeColumn(cuantasFilasYColumnas)
                cuantasFilasYColumnas = cuantasFilasYColumnas-1

    def control_agregar_fila_tabla_Unidad3(self):
        global filasHermite
        metodo = self.comboBox_2.currentIndex()

        if metodo == 5:
            self.tableWidget_2.insertRow(filasHermite+1)
            filasHermite += 1

    def control_eliminar_fila_tabla_Unidad3(self):
        global filasHermite
        if filasHermite == 2:
            print("se necesitan de al menos un par de valores ")
        else:
            self.tableWidget_2.removeRow(filasHermite)
            filasHermite = filasHermite - 1

    def encontrar_puntos_para_metodos_unidad3(self, metodo):
        global cuantasFilasYColumnas, filasHermite
        listaX = []
        listaY = []
        puntos = []
        listaXapoyo = []
        listaYapoyo = []
        listaValoresHermite = []
        control = 0
        tb_vacia = 0

        if metodo == 5:

            # Agregamos los puntos a listas separadas
            for x in range(0, cuantasFilasYColumnas+1):
                listaX = []
                listaXapoyo = []
                for j in range(1, filasHermite+1):
                    try:
                        listaX.append(self.tableWidget_2.item(j, x).text())
                    except:
                        listaX.append('')
                        
                for x in listaX:
                    if x == '':
                        listaXapoyo.append(x)
                    else:
                        listaXapoyo.append(float(x))

                listaValoresHermite.append(listaXapoyo)

            tb_vacia = 0
            controlX = 0
            controlY = 0

            for i in range(0,len(listaValoresHermite),1):
                for j in range(0,len(listaValoresHermite[i]),1):
                    if i == 0:
                        if listaValoresHermite[i][j] == '':
                            controlX = 1

                    elif i == 1:
                        if listaValoresHermite[i][j] == '':
                            controlY = 1

            if controlX != 0 or controlY != 0:
                tb_vacia = 1

            if tb_vacia == 0:


                if self.lineEdit_6.text() == '':
                    self.mensajesAlerta(2,4)
                    control = 1

                if control == 0:
                    self.insertar_datos_a_tabla_unidad3(
                        5, listaValoresHermite, self.lineEdit_6.text())

            else:
                self.mensajesAlerta(2,2)

        elif metodo == 6:
            # Agregamos los puntos a listas separadas
            for x in range(0,2):
                for y in range(1,cuantasFilasYColumnas+1):
                    print(x,y)
            
            print('\n')
            print(cuantasFilasYColumnas+1)
            print('\n')

            for x in range(0, 2):
                for y in range(1, cuantasFilasYColumnas+1):
                    print(x,y)
                    if x == 0:
                        listaX.append(self.tableWidget_2.item(x, y).text())
                    elif x == 1:
                        listaY.append(self.tableWidget_2.item(x, y).text())


            tb_vacia = 0
            controlX = 0
            controlY = 0

            for i in range(0,2,1):
                for j in range(1,len(listaX),1):
                    if i == 0:
                        if listaX[j] == '':
                            controlX = 1

                    elif i == 1:
                        if listaY[j] == '':
                            controlY = 1

            if controlX != 0 or controlY != 0:
                tb_vacia = 1

            if tb_vacia == 0:

                if self.lineEdit_6.text() == '':
                    self.mensajesAlerta(2,4)
                    control = 1
                
                if control == 0:
                    for i in listaX:
                        listaXapoyo.append(float(i))

                    for i in listaY:
                        listaYapoyo.append(float(i))

                    puntos = [listaXapoyo, listaYapoyo]

                    self.insertar_datos_a_tabla_unidad3(
                        6, puntos, self.lineEdit_6.text())
            else:
                self.mensajesAlerta(2,2)

        else:
            
            # Agregamos los puntos a listas separadas
            for x in range(0, 2):
                for y in range(0, cuantasFilasYColumnas+1):
                    if x == 0:
                        if y != 0:
                            listaX.append(self.tableWidget_2.item(x, y).text())
                    elif x == 1:
                        if y != 0:
                            try:
                                listaY.append(
                                    self.tableWidget_2.item(x, y).text())
                            except:
                                listaY.append('?')

            # Buscamos la posicion donde se desea interpolar
            for i in range(0, len(listaY)):
                if listaY[i] == '?':
                    macht = i

            # Lineal
            if metodo == 1:

                puntos_2 = []
                puntos_2.append(listaX[macht-1])  # X0
                puntos_2.append(listaY[macht-1])  # Y0
                puntos_2.append(listaX[macht+1])  # X1
                puntos_2.append(listaY[macht+1])  # Y1

                puntos = []
                puntos.append(puntos_2)

                self.insertar_datos_a_tabla_unidad3(
                    1, puntos, float(listaX[macht]))

            # Cuadratica
            elif metodo == 2:

                # Creamos las listas que serian los pares x,y
                for i in range(0, len(listaY)):
                    if listaY[i] != '?':
                        try:
                            esNumero = float(listaY[i])
                            if esNumero <= 0 or esNumero >= 0:
                                listaXapoyo.append(float(listaX[i]))
                                listaYapoyo.append(float(listaY[i]))
                        except:
                            funcion = "1*"+str(listaY[i])
                            valor = metodos.evaluarFuncion(funcion, 1, 0, 0)
                            listaXapoyo.append(float(listaX[i]))
                            listaYapoyo.append(float(valor))

                puntos = []
                puntos.append(listaXapoyo)
                puntos.append(listaYapoyo)

                self.insertar_datos_a_tabla_unidad3(2, puntos, listaX[macht])

            # lagrange
            elif metodo == 3:

                # Encontramos los puntos x,y
                for i in range(0, len(listaY)):
                    if listaY[i] != '?':
                        try:
                            esNumero = float(listaY[i])
                            if esNumero <= 0 or esNumero >= 0:
                                listaXapoyo.append(float(listaX[i]))
                                listaYapoyo.append(float(listaY[i]))
                        except:
                            funcion = "1*"+str(listaY[i])
                            valor = metodos.evaluarFuncion(funcion, 1, 0, 0)
                            listaXapoyo.append(float(listaX[i]))
                            listaYapoyo.append(float(valor))

                puntos = []
                puntos.append(listaXapoyo)
                puntos.append(listaYapoyo)

                self.insertar_datos_a_tabla_unidad3(
                    3, puntos, float(listaX[macht]))

            # Newton
            elif metodo == 4:

                # Encontramos los pares x,y
                for i in range(0, len(listaY)):
                    if listaY[i] != '?':
                        try:
                            esNumero = float(listaY[i])
                            if esNumero <= 0 or esNumero >= 0:
                                listaXapoyo.append(float(listaX[i]))
                                listaYapoyo.append(float(listaY[i]))
                        except:
                            funcion = "1*"+str(listaY[i])
                            valor = metodos.evaluarFuncion(funcion, 1, 0, 0)
                            listaXapoyo.append(float(listaX[i]))
                            listaYapoyo.append(float(valor))

                puntos = []
                puntos.append(listaXapoyo)
                puntos.append(listaYapoyo)

                self.insertar_datos_a_tabla_unidad3(
                    4, puntos, float(listaX[macht]))

    # Metodos que se controlan con los botones
    def limpiar_Campos(self):

        # limpiamos los lineEdit
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")

        # limpiamos el combobox
        self.comboBox_2.setCurrentIndex(-1)

        # Limpiamos tablas

        self.tableWidget.clear()
        self.tableWidget_2.clear()

        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)

    def calcular(self):
        unidad = self.comboBox.currentIndex()
        metodo = self.comboBox_2.currentIndex()

        if unidad == 0:  # Metodos de la unidad 1
            if metodo >= 0:
                self.insertar_datos_a_tabla_unidad1(metodo)

        elif unidad == 1:  # Metodos de la unidad 2
            if metodo == 0:
                self.mensajesAlerta(1,0)
            elif metodo >= 1:
                self.insertar_datos_a_tabla_unidad2(metodo)
            
        elif unidad == 2:  # Metodos de la unidad 3
            if metodo == 0:
                self.mensajesAlerta(2,0)
            elif metodo >= 1:  # Metodos de la unidad 3
                self.encontrar_puntos_para_metodos_unidad3(metodo) 

        elif unidad == 3:  # Metodos de la unidad 4
            if metodo >= 0 and metodo  <= 1:
                self.mensajesAlerta(3,0)
            elif metodo >= 2:
                self.insertar_datos_a_tabla_unidad4(metodo)
        
        elif unidad == 4: # Metodos de la unidad 5
            if metodo == 0:
                self.mensajesAlerta(2,0)
            elif metodo >= 1:
                self.insertar_datos_a_tabla_unidad5(metodo)

    def graficar(self):
        x = symbols('x')
        y = symbols('y')
        #8

        queMetodo = self.comboBox_2.currentIndex()
        control = 0

        if self.lineEdit.text() == '':
            self.mensajesAlerta(1,8)
            control = 1

        if control == 0:
            if queMetodo >= 0 and queMetodo <= 6 or queMetodo == 9:
                try:
                    funcion = str(self.lineEdit.text())
                    funcionFinal = ''
                    title = 'Funcion: '+str(self.lineEdit.text())

                    for i in range(0, len(funcion)):
                        if funcion[i] == 'e':
                            if funcion[i+1] == '^':
                                funcionFinal += str(cmath.e)
                            else:
                                funcionFinal += funcion[i]
                        else:
                            funcionFinal += funcion[i]

                    p1 = plot((funcionFinal, (x, -100, 100)), box_background='red', show=False, line_color='#96ADEA',
                            ylabel='Y', xlabel='X', title=title, size=(6, 5), xlim=(-25, 25), ylim=(-25, 25))
                    p1.show()
                except:
                    self.mensajesAlerta(1,9)

            elif queMetodo >= 7 and queMetodo <= 8 or queMetodo == 10:
                try:
                    funcion = str(self.lineEdit.text())
                    funcionFinal = ''
                    title = 'Funcion: '+str(self.lineEdit.text())

                    for i in range(0, len(funcion)):
                        if funcion[i] == 'e':
                            if funcion[i+1] == '^':
                                funcionFinal += str(cmath.e)
                            else:
                                funcionFinal += funcion[i]
                        else:
                            funcionFinal += funcion[i]

                    p1 = plot(funcionFinal, show=False, line_color='#96ADEA', ylabel='Y',
                            xlabel='X', title=title, size=(6, 5), xlim=(-25, 25), ylim=(-25, 25))
                    p1.show()
                except:
                    self.mensajesAlerta(1,9)

    def mensajesAlerta(self,unidad,numero_mensaje):

        if unidad == 0:        # Mensajes de validación unidad 1
            if numero_mensaje == 0:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">!UPS¡ Parece que olvido introducir</span></p><p align=\"center\"><span style=\" font-size:12pt;\">el punto inical</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 1:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">!UPS¡ Parece que olvido introducir</span></p><p align=\"center\"><span style=\" font-size:12pt;\">el numero de cifras significativas</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 2:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">!Hey¡ Parece que se te olvido </span></p><p align=\"center\"><span style=\" font-size:12pt;\">seleccionar un metodo para trabajar</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 3:
                print('si esntre')
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">!MMMMMMM...¡ Parece que </span></p><p align=\"center\"><span style=\" font-size:12pt;\">olvidaste introcucir algo arriba </span></p></body></html>")
                self.main.show()
            
        elif unidad == 1:      # Mensajes de validacion unidad 2
            if numero_mensaje == 0:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">!Hey¡ Creo que olvidamos la</span></p><p align=\"center\"><span style=\" font-size:12pt;\">parte de ingresar los datos</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 1:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Te contare un secreto: </span></p><p align=\"center\"><span style=\" font-size:12pt;\">Luego de seleccionar un metodo</span></p><p align=\"center\"><span style=\" font-size:12pt;\">debes ingresar los datos necesarios</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 2:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Si no me equivoco y suele ser asi</span></p><p align=\"center\"><span style=\" font-size:12pt;\">olvidamos introducir una función</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 3:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">El valor #1 fue muy pequeño...</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Te lo digo porque desaparecio</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 4:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">El valor #2 fue muy pequeño...</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Te lo digo porque desaparecio</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 5:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">El valor #3 fue muy pequeño...</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Te lo digo porque desaparecio</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 6:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Tengo la sencación que olvidamos algo</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Podrias revisar que nos falta?</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 7:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">¡PIENSA RAPIDO!</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Mira a tu derecha y hacia arriba</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 8:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Me gustaria realizar tu grafica</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Pero sin la función no puedo hacerlo</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 9:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Si recibiera una moneda siempre</span></p><p align=\"center\"><span style=\" font-size:12pt;\">que se introduce mal una función</span></p><p align=\"center\"><span style=\" font-size:12pt;\">tendria muchas monedas...</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 10:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Nos falta un valor pero no se cual :c</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Menti si lo se, revisa R</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 11:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Nos falta un valor pero no se cual :c</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Menti si lo se, revisa S</span></p></body></html>")
                self.main.show()

        elif unidad == 2:      # Mensajes de validacion unidad 3
            if numero_mensaje == 0:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Primero debes seleccionar un</span></p><p align=\"center\"><span style=\" font-size:12pt;\">metodo ya que no se que queremos</span></p><p align=\"center\"><span style=\" font-size:12pt;\">calcular exactamente</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 1:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Este metodo solo funciona</span></p><p align=\"center\"><span style=\" font-size:11pt;\">con tres puntos si necesitas más</span></p><p align=\"center\"><span style=\" font-size:11pt;\">podrias usar otro metodo</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 2:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">No estoy seguro del motivo pero</span></p><p align=\"center\"><span style=\" font-size:11pt;\">la tabla esta vacia ó incompleta</span></p><p align=\"center\"><span style=\" font-size:11pt;\">podrias llenarla?</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 3:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Veo que descubriste mi debilidad...</span></p><p align=\"center\"><span style=\" font-size:11pt;\">Si, es trabajar con más</span></p><p align=\"center\"><span style=\" font-size:11pt;\">de once puntos</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 4:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Para que esto funcione necesito</span></p><p align=\"center\"><span style=\" font-size:11pt;\">un valor en el cual evaluar</span></p><p align=\"center\"><span style=\" font-size:11pt;\">el polinomio resultante</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 5:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Te cuento, si eliminas otro punto</span></p><p align=\"center\"><span style=\" font-size:11pt;\">probablemte deje de funcionar</span></p><p align=\"center\"><span style=\" font-size:11pt;\">Y no queremos eso verdad?</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 6:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Solo puedo ofrecer hasta derivada</span></p><p align=\"center\"><span style=\" font-size:12pt;\">de orden numéro cinco</span></p><p align=\"center\"><span style=\" font-size:11pt;\">Tomalo o dejalo...</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 7:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Se que no parecen muy importante</span></p><p align=\"center\"><span style=\" font-size:12pt;\"></span></p>pero debes seleccionar una opción en los <p align=\"center\"><span style=\" font-size:11pt;\">radio button</span></p></body></html>")
                self.main.show()

        elif unidad == 3:      # Mensajes de validacion unidad 4
            if numero_mensaje == 0:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">!Hey¡ Creo que olvidamos la</span></p><p align=\"center\"><span style=\" font-size:12pt;\">parte de seleccionar un metodo</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 1:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Necesito que llenes esos tres</span></p><p align=\"center\"><span style=\" font-size:12pt;\">campos de arriba para poder realizar</span></p><p align=\"center\"><span style=\" font-size:12pt;\">mi trabajo</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 2:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Espero que no olvides las llaves de</span></p><p align=\"center\"><span style=\" font-size:12pt;\">tu casa como acabas de olvidar escribir</span></p><p align=\"center\"><span style=\" font-size:12pt;\">la función</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 3:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Espero que no olvides tu telefono</span></p><p align=\"center\"><span style=\" font-size:12pt;\">tu casa como acabas de olvidar escribir</span></p><p align=\"center\"><span style=\" font-size:12pt;\">el punto inicial</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 4:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Espero que no olvides las llaves de</span></p><p align=\"center\"><span style=\" font-size:12pt;\">tu casa como acabas de olvidar escribir</span></p><p align=\"center\"><span style=\" font-size:12pt;\">el valor de h</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 5:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Podria apostar un millon de dolares</span></p><p align=\"center\"><span style=\" font-size:12pt;\">a que nos falta un campo por llenar</span></p><p align=\"center\"><span style=\" font-size:12pt;\">¿Gane cierto?</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 6:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Te dejare unos pasos a seguir... :</span></p><p align=\"center\"><span style=\" font-size:12pt;\">1)Ingresa los limites de la integral</span></p><p align=\"center\"><span style=\" font-size:12pt;\">2)Escribe una función</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 7:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">El limite inferior se encuentra muy</span></p><p align=\"center\"><span style=\" font-size:12pt;\">pero muy triste</span></p><p align=\"center\"><span style=\" font-size:12pt;\">¿Como pudiste olvidarlo?</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 8:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">El limite superior se encuentra muy</span></p><p align=\"center\"><span style=\" font-size:12pt;\">pero muy triste</span></p><p align=\"center\"><span style=\" font-size:12pt;\">¿Como pudiste olvidarlo?</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 9:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">La leyenda de la super integral</span></p><p align=\"center\"><span style=\" font-size:12pt;\">invisible parece ser real, tristemente</span></p><p align=\"center\"><span style=\" font-size:12pt;\">no puedo resolverla...</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 10:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Me parece que aún nos falta</span></p><p align=\"center\"><span style=\" font-size:12pt;\">ingresar datos que seguramente son</span></p><p align=\"center\"><span style=\" font-size:12pt;\">muy importantes</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 11:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">N = intervalos, juega un papel</span></p><p align=\"center\"><span style=\" font-size:12pt;\">muy importante tanto que si no lo</span></p><p align=\"center\"><span style=\" font-size:12pt;\">ingresas no podre resolverlo</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 12:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">El limite inferior no puede ser</span></p><p align=\"center\"><span style=\" font-size:12pt;\">mayor al limite superior</span></p><p align=\"center\"><span style=\" font-size:12pt;\"></span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 13:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Recuerda que debes seleccionar</span></p><p align=\"center\"><span style=\" font-size:12pt;\">si quieres trabajar con una función</span></p><p align=\"center\"><span style=\" font-size:12pt;\">o con datos</span></p></body></html>")
                self.main.show()

        elif unidad == 4:      # Mensajes de validacion unidad 5
            if numero_mensaje == 0:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">!Hey¡ Creo que olvidamos la</span></p><p align=\"center\"><span style=\" font-size:12pt;\">parte de ingresar los datos</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 1:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Te contare un secreto: </span></p><p align=\"center\"><span style=\" font-size:12pt;\">Luego de seleccionar un metodo</span></p><p align=\"center\"><span style=\" font-size:12pt;\">debes ingresar los datos necesarios</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 2:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Si no me equivoco y suele ser asi</span></p><p align=\"center\"><span style=\" font-size:12pt;\">olvidamos introducir una función</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 3:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">El valor T0 fue muy pequeño...</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Te lo digo porque desaparecio</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 4:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">El valor Y1 fue muy pequeño...</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Te lo digo porque desaparecio</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 5:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">El valor T1 fue muy pequeño...</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Te lo digo porque desaparecio</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 6:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Tengo la sencación que olvidamos algo</span></p><p align=\"center\"><span style=\" font-size:12pt;\">¿Podrias revisar que nos falta?</span></p></body></html>")
                self.main.show()
            elif numero_mensaje == 7:
                self.main = Mensajes_error()
                self.main.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">¡PIENSA RAPIDO!</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Mira a tu derecha y hacia arriba</span></p></body></html>")
                self.main.show()
           
            

            
            
            

