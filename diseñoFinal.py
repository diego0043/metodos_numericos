from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QTableWidget,QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu,QActionGroup, QAction, QMessageBox)
from PyQt5 import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_splash_screen import Ui_SplashScreen
import meto2 as metodos
import matplotlib.pyplot as plt
import numpy as np
import math as mt
import sys
import platform

counter = 0

app = QtWidgets.QApplication(sys.argv)
tamanioInicialTabla = 183
posicionX = 1
posicionY = 1
cuantasFilasYColumnas = 3


#Dentro de esta clase declaramos todos nuestros componentes 
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setWindowIcon(QtGui.QIcon('recursos/mac.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 20, 171, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 60, 21, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 100, 20, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(530, 60, 21, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(660, 20, 151, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(620, 20, 200, 16))
        self.label_9.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 31, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.activated[str].connect(self.metodosPorUnidad)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 60, 51, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(470, 100, 51, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(550, 60, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(660, 60, 51, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 261, 931, 200))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(90, 75, 823, 81))
        self.tableWidget_2.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 180, 100, 50))
        self.pushButton.setStyleSheet("background-color: rgb(242, 242, 242);\n""border:opx;\n""background-image : url(recursos/btnCalcular.png);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 180, 100, 50))
        self.pushButton_2.setStyleSheet("border:opx;\n""background-color: rgb(242, 242, 242);\n""background-image : url(recursos/btnCancelar.png);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 510, 100, 50))
        self.pushButton_3.setStyleSheet("background-color: rgb(242, 242, 242);\n""border:opx;\n""background-image : url(recursos/btnGraficar.png);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 510, 100, 50))
        self.pushButton_4.setStyleSheet("background-color: rgb(242, 242, 242);\n""border:opx;\n""background-image : url(recursos/btnExportar.png);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 80, 32, 32))
        self.pushButton_5.setStyleSheet("background-color: rgb(242, 242, 242);\n""border:opx;\n""background-image : url(recursos/agregar.png);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 120, 32, 32))
        self.pushButton_6.setStyleSheet("background-color: rgb(242, 242, 242);\n""border:opx;\n""background-image : url(recursos/quitar.png);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 90, 91, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 120, 131, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(242, 242, 242);\n""image: url(recursos/barra2.png);\n""border:0px")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(240, 50, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.activated[str].connect(self.metodosUnidades)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 101, 16))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(620, 40, 82, 17))# posicion x , posicion y , largo, ancho
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(700, 40, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(780, 40, 82, 17))
        self.radioButton_3.setObjectName("radioButton")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(860, 40, 82, 17))
        self.radioButton_4.setObjectName("radioButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Analisis Númerico"))
        self.label_3.setText(_translate("MainWindow", "Puntos en los que vamos a evaluar"))
        self.label_4.setText(_translate("MainWindow", "#1"))
        self.label_5.setText(_translate("MainWindow", "#2"))
        self.label_6.setText(_translate("MainWindow", "#3"))
        self.label_7.setText(_translate("MainWindow", "Numero de cifras significativas"))
        self.label_8.setText(_translate("MainWindow", "¿Que unidad?"))
        self.label_9.setText(_translate("MainWindow", "Seleccione el grado de la función spline"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5"))
        self.label_2.setText(_translate("MainWindow", "Ingresa la funcion"))
        self.label.setText(_translate("MainWindow", "Seleccione el metodo"))
        self.pushButton.clicked.connect(self.calcular)
        self.pushButton_2.clicked.connect(self.limpiarCampos)
        self.pushButton_3.clicked.connect(self.graficar)
        self.pushButton_5.clicked.connect(self.agregarColumna)
        self.pushButton_6.clicked.connect(self.eliminarColumna)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTextElideMode(Qt.ElideRight)
        #self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.tableWidget_2.setVisible(False)
        self.radioButton.setText(_translate("MainWindow", "Grado #0"))
        self.radioButton_2.setText(_translate("MainWindow", "Grado #1"))
        self.radioButton_3.setText(_translate("MainWindow", "Grado #2"))
        self.radioButton_4.setText(_translate("MainWindow", "Grado #3"))

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
        self.lineEdit.setVisible(False)
        self.lineEdit_2.setVisible(False)
        self.lineEdit_3.setVisible(False)
        self.lineEdit_4.setVisible(False)
        self.lineEdit_5.setVisible(False)
        self.pushButton_5.setVisible(False)
        self.pushButton_6.setVisible(False)
        self.radioButton.setVisible(False)
        self.radioButton_2.setVisible(False)
        self.radioButton_3.setVisible(False)
        self.radioButton_4.setVisible(False)
        self.label_9.setVisible(False)

    # En este metodo vamos a capturar la posicion del primer combobox y luego dependiendo
    # de cual este seleccionado asi se llenara el otro combobox

    def metodosPorUnidad(self):
        cual = self.comboBox.currentIndex()
        self.tableWidget_2.setVisible(False)
        self.pushButton_5.setVisible(False)
        self.pushButton_6.setVisible(False)
        self.radioButton.setVisible(False)
        self.radioButton_2.setVisible(False)
        self.label_9.setVisible(False)
        
        if cual == 0: #Metodos de la primera unidad 
            self.comboBox_2.setGeometry(QtCore.QRect(240, 50, 161, 21))
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
            self.comboBox_2.setGeometry(QtCore.QRect(240, 50, 141, 21))
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
        
        elif cual == 2: #Metodos de la unidad 3
            self.comboBox_2.setGeometry(QtCore.QRect(360, 20, 161, 21))

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

            #Mostramos el comboBox 
            self.comboBox_2.setVisible(True)
            self.label.setVisible(True)
            

            #Ocultamos todo
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

    def configuracionTablaUnidad3(self,columnas):
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(0)
        self.pushButton_5.setVisible(True)
        self.pushButton_6.setVisible(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(38)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget_2.setColumnCount(columnas)
        self.tableWidget_2.setRowCount(2)
        self.radioButton.setVisible(True)
        self.radioButton_2.setVisible(True)
        self.label_9.setVisible(True)
        #self.tableWidget_2.horizontalHeader().setDefaultSectionSize(70)

        for x in range(0,2):
            for y in range(0,3):
                if y == 0 and x == 0:
                    salida = "    X"
                    self.tableWidget_2.setItem(x, y, QtWidgets.QTableWidgetItem(salida))
                    self.tableWidget_2.setColumnWidth(y, 8)
                elif y == 0 and x == 1:
                    salida = "    Y"
                    self.tableWidget_2.setItem(x, y, QtWidgets.QTableWidgetItem(salida))
                    self.tableWidget_2.setColumnWidth(y, 8)
                else:
                    salida = ""
                    self.tableWidget_2.setItem(x, y, QtWidgets.QTableWidgetItem(salida))

        self.tableWidget_2.setVisible(True)

    def metodosUnidades(self):

        queMetodo = self.comboBox_2.currentIndex()
        queUnidad = self.comboBox.currentIndex()

        if queUnidad == 0:

            self.pushButton_5.setVisible(False)
            self.pushButton_6.setVisible(False)
            self.tableWidget_2.setVisible(False)
            self.radioButton.setVisible(False)
            self.radioButton_2.setVisible(False)
            self.radioButton_3.setVisible(False)
            self.radioButton_4.setVisible(False)
            self.label_9.setVisible(False)
            
            # <---- dejamos solo los componentes que usa metodo punto fijo y los de newton -->
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
            
        elif queUnidad == 1:

            self.pushButton_5.setVisible(False)
            self.pushButton_6.setVisible(False)
            self.tableWidget_2.setVisible(False)
            self.radioButton.setVisible(False)
            self.radioButton_2.setVisible(False)
            self.radioButton_3.setVisible(False)
            self.radioButton_4.setVisible(False)
            self.label_9.setVisible(False)

            if queMetodo >=1 and queMetodo <= 2:

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

            elif queMetodo >= 3 and queMetodo <= 6:

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
                self.label_6.setVisible(False)

            elif queMetodo >= 7 and queMetodo <= 8:
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
                self.label_6.setVisible(True)

            elif queMetodo == 10:

                 # <---- dejamos solo los componentes que usa metodo muller -->
                self.label_4.setText("R")
                self.label_5.setText("S")
                self.label_4.setVisible(True)
                self.label_2.setVisible(True)
                self.label_3.setVisible(True)
                self.label_5.setVisible(True)
                self.lineEdit_2.setVisible(True)
                self.lineEdit_3.setVisible(True)
                self.lineEdit.setVisible(True)



                # <-------- ocultamos lo demas ---------->

                self.lineEdit_5.setVisible(False)
                self.lineEdit_4.setVisible(False)
                self.label_6.setVisible(False)
                self.label_7.setVisible(False)

        elif queUnidad == 2: #Configuramos la tabla

            global cuantasFilasYColumnas

            #Deseleccionamos los radio button

            
            if queMetodo >= 1 and queMetodo <= 5:
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
                self.radioButton.setGeometry(QtCore.QRect(620, 40, 82, 17))
                self.radioButton_2.setGeometry(QtCore.QRect(660,40,82,17))
                
                
            else:
                self.label_9.setText("Seleccione el grado de la función Spline")
                self.radioButton.setAutoExclusive(False)
                self.radioButton.setChecked(False)
                self.radioButton.setAutoExclusive(True)
                self.radioButton_2.setAutoExclusive(False)
                self.radioButton_2.setChecked(False)
                self.radioButton_2.setAutoExclusive(True)

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
                self.radioButton.setGeometry(QtCore.QRect(620, 40, 82, 17))
                self.radioButton_2.setGeometry(QtCore.QRect(700,40,82,17))
                self.radioButton_3.setVisible(True)
                self.radioButton_4.setVisible(True)

            if queMetodo == 1:#Lineal
                cuantasFilasYColumnas = 3
                self.configuracionTablaUnidad3(4)     
            elif queMetodo == 2:#Cuadratica
                cuantasFilasYColumnas = 4
                self.configuracionTablaUnidad3(5)
            elif queMetodo == 3:#Lagrange
                cuantasFilasYColumnas = 3
                self.configuracionTablaUnidad3(4)
            elif queMetodo == 4:#Newton
                cuantasFilasYColumnas = 3
                self.configuracionTablaUnidad3(4)
            elif queMetodo == 5:#Hermite
                cuantasFilasYColumnas = 3
                self.configuracionTablaUnidad3(4)
            elif queMetodo == 6:#función spline grado 0
                cuantasFilasYColumnas = 3
                self.configuracionTablaUnidad3(5)

    def limpiarCampos(self, MainWindow):
        # aun falta poner los campos correctamente
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.comboBox_2.setCurrentIndex(-1)
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        
    def graficar(self, MainWindow):
        queMetodo = self.comboBox_2.currentIndex()
        if queMetodo >= 0 and queMetodo <= 6 or queMetodo == 9:
            x = []
            y = []
            i = 0

            for j in range(-50, 51):
                x.append(i)
                y.append(i)

            try:
                def f1(x):
                    funcion = metodos.evaluarFuncion(
                        self.lineEdit.text(), x, 0, 0)
                    return funcion

                # asignamos un rango de valores a graficar
                var = range(start=-100, stop=100,step=0.01)

                plt.plot(var, [f1(i) for i in var], label='Funcion 1')

                plt.xlim(-50, 50)
                plt.ylim(-50, 50)

                plt.plot(x, y)
                plt.axvline(0, color='r')
                plt.axhline(0, color='r')

                plt.xlabel("Eje X")
                plt.ylabel("Eje Y")
                plt.grid()
                plt.title("Representacion de la función")
                # colocamos la leyenda en la parte inferior derecha
                plt.show()
            except:
                print("Algo salio mal")

        elif queMetodo >=7 and queMetodo <= 8 or queMetodo == 10:

            coeficientes = metodos.coefs(self.lineEdit.text())
            coeficientes.reverse()

            print(coeficientes)

            tamanio = len(coeficientes)

            funGraficar = ""

            #Hacemos una funcion que si se pueda graficar 
            for x in  range(len(coeficientes)):
                if coeficientes[x] != 0:
                    if coeficientes[x] > 0:
                        if x == 0:
                            funGraficar += str(coeficientes[x]) + "*x^"+str(tamanio-1)
                            tamanio = tamanio -1
                        else:
                            if x == (len(coeficientes)-1):
                                funGraficar += "+" + str(coeficientes[x])
                                tamanio = tamanio -1
                            else:
                                funGraficar += "+" + str(coeficientes[x]) + "*x^"+str(tamanio-1)
                                tamanio = tamanio -1
                    else:
                        if x == (len(coeficientes)-1):
                                funGraficar += str(coeficientes[x])
                                tamanio = tamanio -1
                        else:
                            funGraficar += str(coeficientes[x]) + "*x^"+str(tamanio-1)
                            tamanio = tamanio -1
                else:
                    funGraficar +=  "+0*x^"+str(tamanio-1)
                    tamanio = tamanio -1

            print(funGraficar)

            x = []
            y = []
            i = 0

            for j in range(-50, 51):
                x.append(i)
                y.append(i)

            try:
                def f1(x):
                    funcion = metodos.evaluarFuncion(funGraficar, x, 0, 0)
                    return funcion

                # asignamos un rango de valores a graficar
                var = range(-100, 100)

                plt.plot(var, [f1(i) for i in var], label='Funcion 1')

                plt.xlim(-50, 50)
                plt.ylim(-50, 50)

                plt.plot(x, y)
                plt.axvline(0, color='r')
                plt.axhline(0, color='r')

                plt.xlabel("Eje X")
                plt.ylabel("Eje Y")
                plt.grid()
                plt.title("Representacion de la función")
                # colocamos la leyenda en la parte inferior derecha
                plt.show()
            except:
                print("Algo salio mal")

    def agregarColumna(self):
        global  cuantasFilasYColumnas
        metodo = self.comboBox_2.currentIndex()

        if metodo == 0:
            print("Seleccione un metodo primero ")
        elif metodo == 1:
            print("Solamente se puede trabajar con 2 puntos")
        else:
            if cuantasFilasYColumnas == 13:
                print("Maximo numero de columnas alcanzado")
            else:
                self.tableWidget_2.insertColumn(cuantasFilasYColumnas+1)
                cuantasFilasYColumnas += 1
     
    def eliminarColumna(self):
        global cuantasFilasYColumnas
        metodo = self.comboBox_2.currentIndex()

        if metodo == 1: #lineal
            if cuantasFilasYColumnas == 3:
                print("Se necesitan al menos 2 puntos")
            else:
                self.tableWidget_2.removeColumn(cuantasFilasYColumnas)
                cuantasFilasYColumnas = cuantasFilasYColumnas - 1

        elif metodo == 2:#Cuadratica
            if cuantasFilasYColumnas == 4:
                print("Se necesitan al menos 3 puntos")
            else:
                self.tableWidget_2.removeColumn(cuantasFilasYColumnas)
                cuantasFilasYColumnas = cuantasFilasYColumnas - 1

        elif metodo == 3:#Lagrange
            if cuantasFilasYColumnas == 3:
                print("Se necesitan al menos 2 puntos")
            else:
                self.tableWidget_2.removeColumn(cuantasFilasYColumnas)
                cuantasFilasYColumnas = cuantasFilasYColumnas - 1
            
        elif metodo == 4:#Newton
            if cuantasFilasYColumnas == 3:
                print("Se neecesitan al menos 2 puntos")
            else:
                self.tableWidget_2.removeColumn(cuantasFilasYColumnas)
                cuantasFilasYColumnas = cuantasFilasYColumnas-1

    def calcular(self, MainWindow):

        unidad = self.comboBox.currentIndex()
        metodo = self.comboBox_2.currentIndex()

        if unidad == 0:#Unidad 1
            print("Aún falta esta parte :c")

        elif unidad == 1: #Parte unidad 2
            if metodo == 1: #Biseccion
                self.corroborarDatos(MainWindow, metodo, self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_5.text())
            elif metodo == 2:#Falsa posicion
                self.corroborarDatos(MainWindow, metodo, self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_5.text())
            elif metodo == 3:#Punto fijo
                self.corroborarDatos(MainWindow, metodo, self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_5.text())
            elif metodo == 4:#Newton
                self.corroborarDatos(MainWindow, metodo, self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_5.text())
            elif metodo == 5:#Newton mejorado
                self.corroborarDatos(MainWindow, metodo, self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_5.text())
            elif metodo == 6:#secante
                self.corroborarDatos(MainWindow, metodo, self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_5.text())
            elif metodo == 7:#cero polinomios
                self.ceroPolinomios(MainWindow, self.lineEdit.text())
            elif metodo == 8:#Horner
                self.crearTable(MainWindow, metodo, 0, 0, 0, 0)
            elif metodo == 9:#Muller
                self.crearTable(MainWindow, metodo, 0, 0, 0, 0)
            elif metodo == 10:#Bairstown
                self.crearTable(MainWindow, metodo, 0, 0, 0, 0)

            



        elif unidad == 2: #Parte unidad 3
            global cuantasFilasYColumnas 
            listaX = []
            listaY = []
            puntos = []
            listaXapoyo = []
            listaYapoyo = []
            enXoY = 0

            #Buscamos el valor donde falta X ó Y,  que sera donde vamos a interpolar 
            for x in range(0,2):
                for y in range(0,cuantasFilasYColumnas+1):
                    if x == 0:
                        if y != 0:
                            listaX.append(self.tableWidget_2.item(x,y).text())
                    elif x == 1:
                        if y != 0:
                            try:
                                listaY.append(self.tableWidget_2.item(x,y).text())
                            except:
                                listaY.append('?')



            for i in range(0,len(listaY)):
                if listaY[i] == '?':
                    macht = i

            

            if metodo == 1: #Llamamos al metodo de interpolación lineal

                puntos_2 = []
                puntos_2.append(listaX[macht-1])#X0
                puntos_2.append(listaY[macht-1])#Y0
                puntos_2.append(listaX[macht+1])#X1
                puntos_2.append(listaY[macht+1])#Y1

                puntos = []
                puntos.append(puntos_2)

                self.crearTablaUnidad3(1,puntos,float(listaX[macht]))

                '''

                self.creatTableUnidad3(1,listaXapoyo,listaYapoyo,listaX[macht])
                if self.radioButton.isChecked():
                    print("Mostrar polinomio")
                else:
                    puntos.append(listaX[macht-1])#X0
                    puntos.append(listaY[macht-1])#Y0
                    puntos.append(listaX[macht+1])#X1
                    puntos.append(listaY[macht+1])#Y1


                    metodos.interpolacionLineal(puntos, listaX[macht])
                '''

            elif metodo == 2:#Llamamos al metodo de interpolacion cuadrática
                

                for i in range(0,len(listaY)):
                    if listaY[i] != '?':
                        try:
                            esNumero = float(listaY[i])
                            if esNumero<=0 or esNumero>=0:
                                listaXapoyo.append(float(listaX[i]))
                                listaYapoyo.append(float(listaY[i]))
                        except:
                            funcion = "1*"+str(listaY[i])
                            valor = metodos.evaluarFuncion(funcion,1,0,0)
                            listaXapoyo.append(float(listaX[i]))
                            listaYapoyo.append(float(valor))
                        

                puntos = []
                puntos.append(listaXapoyo)
                puntos.append(listaYapoyo)

                self.crearTablaUnidad3(2,puntos,listaX[macht])

                '''

                lst = metodos.interpolacionCuadratica(listaXapoyo,listaYapoyo, listaX[macht])

                if self.radioButton.isChecked():
                    print(lst[0])
                    print(lst[1])
                elif self.radioButton_2.isChecked():
                    print(lst[1])
                else:
                    print("Seleccione una acción en los radio button")
                '''
                        
            elif metodo == 3:#Llamamos al metodo de interpolacion de la lagrange
                for i in range(0,len(listaY)):
                    if listaY[i] != '?':
                        try:
                            esNumero = float(listaY[i])
                            if esNumero<=0 or esNumero>=0:
                                listaXapoyo.append(float(listaX[i]))
                                listaYapoyo.append(float(listaY[i]))
                        except:
                            funcion = "1*"+str(listaY[i])
                            valor = metodos.evaluarFuncion(funcion,1,0,0)
                            listaXapoyo.append(float(listaX[i]))
                            listaYapoyo.append(float(valor))
                print(listaXapoyo)
                print(listaYapoyo)

                puntos = []
                puntos.append(listaXapoyo)
                puntos.append(listaYapoyo)

                self.crearTablaUnidad3(3,puntos,float(listaX[macht]))

            elif metodo == 4:#Llamamos al metodo de interpolacion de la newton
                for i in range(0,len(listaY)):
                    if listaY[i] != '?':
                        try:
                            esNumero = float(listaY[i])
                            if esNumero<=0 or esNumero>=0:
                                listaXapoyo.append(float(listaX[i]))
                                listaYapoyo.append(float(listaY[i]))
                        except:
                            funcion = "1*"+str(listaY[i])
                            valor = metodos.evaluarFuncion(funcion,1,0,0)
                            listaXapoyo.append(float(listaX[i]))
                            listaYapoyo.append(float(valor))
                

                puntos = []
                puntos.append(listaXapoyo)
                puntos.append(listaYapoyo)

                self.crearTablaUnidad3(4,puntos,float(listaX[macht]))
                    
    def ceroPolinomios(self, MainWindow, funcion):
        self.corroborarDatos(MainWindow, 7, 0, 0, 0, 0)

    def corroborarDatos(self, MainWindow, queMetodo, funcionTXT, X1, X2, cifTXT):
        # <---- Validamos que sean numeros ------->
        x1 = metodos.pedirValoresIniciales(X1)
        x2 = metodos.pedirValoresIniciales(X2)
        pasa = ""

        cuantasVariables = 0

        if queMetodo == 1 or queMetodo == 2 or queMetodo == 6:
            cuantasVariables = 2
        elif queMetodo == 3 or queMetodo == 4 or queMetodo == 5:
            cuantasVariables = 1
        elif queMetodo == 7:
            self.crearTable(MainWindow, 7, 0, 0, 0, 0)

        if cuantasVariables == 2:
            if x1 == "falsisimo" or x2 == "falsisimo":
                print("Los valores iniciales son incorrectos")
            else:
                try:
                    funcion = metodos.evaluarFuncion(funcionTXT, 1, 0, 0)
                    pasa = "pasa"
                except:
                    pasa = "No pasa"
                if pasa == "No pasa":
                    print("La funcion no es valida")
                else:
                    cifras = metodos.pedirCifrasSignificativas(cifTXT)
                    if cifras == "Falso":
                        print("Ingreso un dato no incorrecto en cifras")
                    else:
                        if queMetodo == 1:  # Biseccion
                            self.crearTable(MainWindow, 1, x1, x2, funcionTXT, cifras)
                        elif queMetodo == 2:  # Falsa Posicion
                            self.crearTable(MainWindow, 2, x1, x2, funcionTXT, cifras)
                        elif queMetodo == 6:  # secante
                            self.crearTable(MainWindow, 6, x1, x2, funcionTXT, cifras)
        if cuantasVariables == 1:
            if x1 == "falsisimo":
                print("Los valores iniciales son incorrectos")
            else:
                try:
                    funcion = metodos.evaluarFuncion(funcionTXT, 1, 0, 0)
                    pasa = "pasa"
                except:
                    pasa = "No pasa"
                if pasa == "No pasa":
                    print("La funcion no es valida")
                else:
                    cifras = metodos.pedirCifrasSignificativas(cifTXT)
                    if cifras == False:
                        print("Ingreso un dato no incorrecto en cifras")
                    else:
                        if queMetodo == 3:
                            # Falsa posicion
                            self.crearTable(MainWindow, 3, x1,x2, funcionTXT, cifras)
                        elif queMetodo == 4:
                            self.crearTable(MainWindow, 4, x1, x2, funcionTXT, cifras)  # newton
                        elif queMetodo == 5:
                            # newton mejorado
                            self.crearTable(MainWindow, 5, x1, x2, funcionTXT, cifras)
    
    def configuracionTabla(self,MainWindow,rows,columns):
        self.tableWidget.setColumnCount(columns)
        self.tableWidget.setRowCount(rows)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalScrollMode()

    def crearTable(self, MainWindow, metodo, x1, x2, funcion, cifras):
        unidad = self.comboBox.currentIndex()
        if unidad == 1:
            if metodo == 1: 
                lst = metodos.metodoBiseccion(x1, x2, funcion, cifras)
            elif metodo == 2:
                lst = metodos.metodoFalsaPosicion(x1, x2, funcion, cifras)
            elif metodo == 3:
                lst = metodos.metodoPuntoFijo(x1, funcion, cifras)
            elif metodo == 4:
                lst = metodos.metodoNewtonRaphson(x1, funcion, cifras)
            elif metodo == 5:
                lst = metodos.metodoNewtonRaphsonMejorado(x1, funcion, cifras)
            elif metodo == 6:
                print("estoy en secante")
                lst = metodos.metodoSecante(x1, x2, funcion, cifras)

            elif metodo == 7: #Metodo para crear tabla de cero de polinomios
                listaCoeficientes = metodos.coefs(self.lineEdit.text())
                largo = len(listaCoeficientes)
                if largo > 5:
                    print("Funcion mayor a cuartica")
                else:
                    if largo == 5:
                        a = listaCoeficientes[4]
                        b = listaCoeficientes[3]
                        c = listaCoeficientes[2]
                        d = listaCoeficientes[1]
                        e = listaCoeficientes[0]
                        lst = metodos.factorizar(a, b, c, d, e)
                    elif largo == 4:
                        a = 0
                        b = listaCoeficientes[3]
                        c = listaCoeficientes[2]
                        d = listaCoeficientes[1]
                        e = listaCoeficientes[0]
                        lst = metodos.factorizar(a, b, c, d, e)
                    elif largo == 3:
                        a = 0
                        b = 0
                        c = listaCoeficientes[2]
                        d = listaCoeficientes[1]
                        e = listaCoeficientes[0]
                        lst = metodos.factorizar(a, b, c, d, e)
                    elif largo == 2:
                        a = 0
                        b = 0
                        c = 0
                        d = listaCoeficientes[1]
                        e = listaCoeficientes[0]
                        lst = metodos.factorizar(a, b, c, d, e)
                    elif largo == 1:
                        print("Esta no es una funcion >:v ")
                    # Creando la tabla para cero de polinomios
                    if largo <= 5:
                        columns = len(lst)
                        rows = 2

                        tamanioColumnas = int(930/columns)

                        self.configuracionTabla(MainWindow, rows, columns)

                        for row in range(rows):
                            for column in range(columns):
                                if row == 0:
                                    salida = "raiz #"+str(column+1)
                                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                    self.tableWidget.setColumnWidth(column, tamanioColumnas)
                                else:
                                    salida = str(lst[column])
                                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                    self.tableWidget.setColumnWidth(column, tamanioColumnas)

            elif metodo == 8:  # Metodo para crear tabla de horner
                lista = metodos.coefs(self.lineEdit.text())
                print(lista)
                lst = metodos.metodoHorner(lista, float(self.lineEdit_2.text()), float(self.lineEdit_5.text()))

                rows = len(lst)
                columns = len(lst[0])

                tamanioColumnas = int(930/columns)

                self.configuracionTabla(MainWindow, rows, columns)

                for row in range(rows):
                    for column in range(columns):
                        if row == 0:
                            salida = lst[row][column]
                            self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                            self.tableWidget.setColumnWidth(column, tamanioColumnas)
                        else:
                            if column == 0:
                                salida = "%.0f" % (lst[row][column])
                                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                self.tableWidget.setColumnWidth(column, tamanioColumnas)
                            else:
                                salida = "%.5f" % float(lst[row][column])
                                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                self.tableWidget.setColumnWidth(column, tamanioColumnas)

            elif metodo == 9:  # Metodo para crear tabla de müller
                # Creamos la lista completa con todas las iteraciones
                # Metodo muller me devuelve todas las iteraciones
                lst = metodos.metodoMuller(self.lineEdit.text(), self.lineEdit_2.text(),self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text())

                rows = len(lst)  # Capturamos cuantas filas hay
                columns = len(lst[0])  # Capturamos cuantas columnas hay

                # dividimos el ancho de la tabla entre las columnas

                self.configuracionTabla(MainWindow, rows, columns)
                tamanioColumnas = 930/columns

                for row in range(rows):
                    for column in range(columns):
                        if row == 0:
                            salida = lst[row][column]
                            # Asignamos los valores del metodo en las casillas de la tabla
                            self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                            self.tableWidget.setColumnWidth(column, tamanioColumnas)

                            # Asignamos el tamaño que necesita la columna
                        else:
                            if column == 0:
                                salida = "%.0f" % (lst[row][column])
                                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                self.tableWidget.setColumnWidth(column, tamanioColumnas)
                            else:
                                salida = "%.5f" % float(lst[row][column])
                                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                self.tableWidget.setColumnWidth(column, tamanioColumnas)
                    
            elif metodo == 10:  # metodo para crear tabla de bairstown

                #Creamos una lista con los coeficientes de la funcion ingresada por el usuario y la ordenamos de mayor a menor 
                coeficientes = metodos.coefs(self.lineEdit.text())
                coeficientes.reverse()

                lst = metodos.metodoBairstow(coeficientes,self.lineEdit_2.text(),self.lineEdit_3.text(),3)

                columns = len(lst)

                self.tableWidget.setRowCount(2)
                self.tableWidget.setColumnCount(columns)
                self.tableWidget.verticalHeader().setVisible(False)
                self.tableWidget.horizontalHeader().setVisible(False)

                tamanioColumnas = 0
                listaTamanio = []
                contadorTamanio = 0
                for x in range(0,columns):
                    listaTamanio.append(len(str(lst[x]))*7)
                    contadorTamanio += len(str(lst[x]))*7

                listaTamanio.sort()

                #self.configuracionTabla(MainWindow,2,columns)

                for row in range(0,2):
                    for column in range(0,columns):
                        if row == 0:
                            salida = "Raiz #"+str(column+1)
                            self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(salida))
                            if contadorTamanio < 930:
                                tamanioColumnas = float(listaTamanio[len(listaTamanio)-1])
                                self.tableWidget.setColumnWidth(column, tamanioColumnas)
                            else:
                                tamanioColumnas = len(str(lst[column]))*7
                                self.tableWidget.setColumnWidth(column, tamanioColumnas)
                        else:
                            salida = str(lst[column])
                            self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(salida))
                            if contadorTamanio < 930:
                                tamanioColumnas = float(listaTamanio[len(listaTamanio)-1])
                                self.tableWidget.setColumnWidth(column, tamanioColumnas)

                            else:
                                tamanioColumnas = len(str(lst[column]))*7
                                self.tableWidget.setColumnWidth(column, tamanioColumnas)

            if metodo >= 1 and metodo <= 6:  # Imprime de biseccion hasta secante
                self.tableWidget.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
                rows = len(lst)
                columns = len(lst[0])
                tamanioColumnas = int(930/columns)-3

                self.configuracionTabla(MainWindow,rows,columns)

                for row in range(rows):
                    for column in range(columns):
                        if row == 0:
                            salida = lst[row][column]
                            self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                            self.tableWidget.item(row,column).setBackground(QtGui.QColor(11,133,192))
                            self.tableWidget.setColumnWidth(column, tamanioColumnas)
                        else:
                            if column == 0:
                                salida = (lst[row][column])
                                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                self.tableWidget.setColumnWidth(column, tamanioColumnas)
                            else:
                                salida = "%.5f" % float(lst[row][column])
                                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                self.tableWidget.setColumnWidth(column, tamanioColumnas)

    def crearTablaUnidad3(self, metodo,puntos,valor):

        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()

        if metodo == 1:#Interpolacion Lineal 

            lst = metodos.interpolacionLineal(puntos[0], valor)

            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.horizontalHeader().setVisible(False)
            self.tableWidget.horizontalScrollMode()
            
            #Verificamos si solo mostraremos el polinomio o el valor 
            if self.radioButton.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(2)

                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Polinomio"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(lst[0])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem("Resultado"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)
              
            elif self.radioButton_2.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(1)

                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Valor"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)
            else:
                print("Seleccione una acción en los radio button")

        elif metodo == 2:#Interpolacion Cuadratica 

            lst = metodos.interpolacionCuadratica(puntos[0], puntos[1], valor)
            
            
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.horizontalHeader().setVisible(False)
            self.tableWidget.horizontalScrollMode()

            if self.radioButton.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(2)

                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Polinomio"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(lst[0])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem("Resultado"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)

            elif self.radioButton_2.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(1)

                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Valor"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)
            else:
                print("Seleccione una acción en los radio button")

        elif metodo == 3:#Interpolacion de lagrange

            lst = metodos.interpolacionLagrange(puntos[0], puntos[1], valor)

            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.horizontalHeader().setVisible(False)
            self.tableWidget.horizontalScrollMode()

            if self.radioButton.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(2)

                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Polinomio"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(lst[0])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem("Resultado"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)

            elif self.radioButton_2.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(1)

                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Valor"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)

            else:
                print("Seleccione una acción en los radio button")

        elif metodo == 4:#Interpolacion de lagrange

            lst = metodos.interpolacionNewton(puntos[0], puntos[1], valor)
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.horizontalHeader().setVisible(False)
            self.tableWidget.horizontalScrollMode()

            if self.radioButton.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(2)

                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Polinomio"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(lst[0])))
                self.tableWidget.setColumnWidth(1, 830)
                self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem("Resultado"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)

            elif self.radioButton_2.isChecked():

                self.tableWidget.setColumnCount(2)
                self.tableWidget.setRowCount(1)

                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Valor"))
                self.tableWidget.setColumnWidth(0, 100)
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(lst[1])))
                self.tableWidget.setColumnWidth(1, 830)

            else:
                print("Seleccione una acción en los radio button")


# desde esta linea hasta la 818 es para la pantalla de inicio y aún hay un error al correrlo

#Pantalla de carga Splash del inicio
class SplashScreen(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(2)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> ING XENIA")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>CARGANDO</strong> METODOS"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>CARGANDO</strong> INTERFAZ DE USUARIO"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter
        global app

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW

            app.exec_()
            self.close()
            del app



        
            
            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())
      
            # CLOSE SPLASH SCREEN
            

        # INCREASE COUNTER
        counter += 1

if __name__ == "__main__":
    '''
    #LO que estaba antes 
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    '''

    window = SplashScreen()
    sys.exit(app.exec_())

