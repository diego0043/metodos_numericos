from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QTableWidget,QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu,QActionGroup, QAction, QMessageBox)
from PyQt5 import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from metodosYformularios import *
import metodosYformularios.meto2 as metodos
import matplotlib.pyplot as plt
import numpy as np
import math as mt

counter = 0

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
        MainWindow.setMinimumSize(QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(200, 0, 1000, 31))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(730, 10, 16, 16))
        self.pushButton_6.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton_6.setMaximumSize(QtCore.QSize(17, 17))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton {\n""border: none;\n""background-color: rgb(167, 227, 171);\n""border-radius: 8px;\n""}\n""QPushButton:hover { \n""background-color: rgb(55, 255, 0);\n""}")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(760, 10, 16, 16))
        self.pushButton_7.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton_7.setMaximumSize(QtCore.QSize(17, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("QPushButton {\n""border: none;\n""background-color: rgb(246, 180, 180);\n""border-radius: 8px;\n""}\n""QPushButton:hover {        \n""background-color: rgba(255, 0, 0, 150);\n""}")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(700, 10, 16, 16))
        self.pushButton_8.setMinimumSize(QtCore.QSize(16, 16))
        self.pushButton_8.setMaximumSize(QtCore.QSize(17, 17))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("QPushButton {\n""border: none;\n""border-radius: 8px;\n""background-color: rgb(246, 221, 164);\n""}\n""QPushButton:hover {    \n""background-color: rgb(255, 255, 0);\n""}")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_6")
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(134, 155, 208);")
        self.label_3.setGeometry(QtCore.QRect(400, 30, 211, 16))
        self.label_3.setObjectName("label_3")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 80, 21, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(134, 155, 208);")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 120, 20, 20))
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(134, 155, 208);")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 80, 21, 16))
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(134, 155, 208);")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(660, 30, 191, 20))
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(134, 155, 208);")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(134, 155, 208);")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(620, 30, 220, 16))
        self.label_9.setObjectName("label_8")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(134, 155, 208);")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 31, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid;\n"
"    border-radius: 7px;\n"
"    border-color: #96adea;\n"
"    background-color: rgb(242, 242, 242);\n"
"    color : #1905ff;\n"
"\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid \'#96adea\';\n"
"    selection-background-color: #96adea;\n"
"    background-color: rgb(242, 242, 242);\n"
"    color: \'ffffff\'\n"
"}\n"
"QComboBox:hover{\n"
"    border-color: #1905ff;\n"
"\n"
"}\n"
"\n"
"")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.activated[str].connect(self.cambiar_metodos_cmb2)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 75, 51, 24))
        self.lineEdit_2.setStyleSheet("background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(font)


        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)


        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(430, 115, 51, 24))
        self.lineEdit_3.setStyleSheet("background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(530, 75, 51, 24))
        self.lineEdit_4.setStyleSheet("background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(660, 70, 51, 24))
        self.lineEdit_5.setStyleSheet("background-color: rgb(242, 242, 242);\n""image: url(recursos/barra.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setFont(font)

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
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid;\n"
"    border-radius: 20px;\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"    border-color: rgb(150, 173, 234);\n"
"    color: \'#96ADEA\'\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 173, 234);\n"
"    color: \'#ffffff\';\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 180, 100, 50))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    border: 2px solid;\n"
"    color: \'#E88989\';\n"
"    border-color: rgb(232, 137, 137);\n"
"    border-radius: 20px;\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(232, 137, 137);\n"
"    color: \'#ffffff\'\n"
"\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 510, 100, 50))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    border: 2px solid;\n"
"    border-radius: 20px;\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"    border-color: rgb(150, 173, 234);\n"
"    color: \'#96ADEA\'\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(150, 173, 234);\n"
"    color: \'#ffffff\';\n"
"}\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 100, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(134, 155, 208);")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 130, 131, 24))
        self.lineEdit.setStyleSheet("background-color: rgb(242, 242, 242);\n""image: url(recursos/barra2.png);\n""border:0px;\n""color:  rgb(232, 137, 137)")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(font)

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 50, 141, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    border: 1px solid;\n"
"    border-radius: 7px;\n"
"    border-color: #96adea;\n"
"    background-color: rgb(242, 242, 242);\n"
"    color : #1905ff;\n"
"\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid \'#96adea\';\n"
"    selection-background-color: #96adea;\n"
"    background-color: rgb(242, 242, 242);\n"
"    color: \'ffffff\'\n"
"}\n"
"QComboBox:hover{\n"
"    border-color: #1905ff;\n"
"\n"
"}\n"
"\n"
"")
        self.comboBox_2.activated[str].connect(self.metodos_de_cada_unidad)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 30, 140, 16))
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(134, 155, 208);")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(620, 50, 82, 17))# posicion x , posicion y , largo, ancho
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(700, 50, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(780, 55, 82, 17))
        self.radioButton_3.setObjectName("radioButton")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(860, 55, 82, 17))
        self.radioButton_4.setObjectName("radioButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        self.label_3.setText(_translate("MainWindow", "Puntos en los que vamos a evaluar"))
        self.label_4.setText(_translate("MainWindow", "#1"))
        self.label_5.setText(_translate("MainWindow", "#2"))
        self.label_6.setText(_translate("MainWindow", "#3"))
        self.label_7.setText(_translate("MainWindow", "Numero de cifras significativas"))
        self.label_8.setText(_translate("MainWindow", "¿Que unidad?"))
        self.label_9.setText(_translate("MainWindow", "Seleccione el grado de la función spline"))
        self.pushButton.setText(_translate("MainWindow", "CALCULAR"))
        self.pushButton_2.setText(_translate("MainWindow", "LIMPIAR"))
        self.pushButton_3.setText(_translate("MainWindow", "GRAFICAR"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5"))
        self.label_2.setText(_translate("MainWindow", "Ingresa la funcion"))
        self.label.setText(_translate("MainWindow", "Seleccione el metodo"))
        self.pushButton.clicked.connect(self.calcular)
        self.pushButton_2.clicked.connect(self.limpiar_Campos)
        self.pushButton_3.clicked.connect(self.graficar)
        self.pushButton_5.clicked.connect(self.control_agregar_columna_tabla_Unidad3)
        self.pushButton_6.clicked.connect(self.control_eliminar_columna_tabla_Unidad3)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTextElideMode(Qt.ElideRight)
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

    def cambiar_metodos_cmb2(self):
        cual = self.comboBox.currentIndex()
        self.tableWidget_2.setVisible(False)
        self.pushButton_5.setVisible(False)
        self.pushButton_6.setVisible(False)
        self.radioButton.setVisible(False)
        self.radioButton_2.setVisible(False)
        self.label_9.setVisible(False)
        
        if cual == 0: #Metodos de la primera unidad 
            self.comboBox_2.setGeometry(QtCore.QRect(200, 60, 161, 21))
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
            self.comboBox_2.setGeometry(QtCore.QRect(200, 60, 141, 21))
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
            self.comboBox_2.setGeometry(QtCore.QRect(360, 30, 161, 21))

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

    def metodos_de_cada_unidad(self):
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
                self.radioButton.setGeometry(QtCore.QRect(620, 55, 82, 17))
                self.radioButton_2.setGeometry(QtCore.QRect(660,55,82,17))
                
                
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
                self.radioButton.setGeometry(QtCore.QRect(620, 55, 82, 17))
                self.radioButton_2.setGeometry(QtCore.QRect(700,55,82,17))
                self.radioButton_3.setVisible(True)
                self.radioButton_4.setVisible(True)

            if queMetodo == 1:#Lineal
                cuantasFilasYColumnas = 3
                self.creacion_tabla_por_defecto_unidad3(4)     
            elif queMetodo == 2:#Cuadratica
                cuantasFilasYColumnas = 4
                self.creacion_tabla_por_defecto_unidad3(5)
            elif queMetodo == 3:#Lagrange
                cuantasFilasYColumnas = 3
                self.creacion_tabla_por_defecto_unidad3(4)
            elif queMetodo == 4:#Newton
                cuantasFilasYColumnas = 3
                self.creacion_tabla_por_defecto_unidad3(4)
            elif queMetodo == 5:#Hermite
                cuantasFilasYColumnas = 3
                self.creacion_tabla_por_defecto_unidad3(4)
            elif queMetodo == 6:#función spline grado 0
                cuantasFilasYColumnas = 3
                self.creacion_tabla_por_defecto_unidad3(5)

    #Metodos que controlan las tablas ó que trabajan con las tablas 
    def creacion_tabla_por_defecto_unidad3(self,columnas):
        #Limpiamos la tabla
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(0)

        self.pushButton_5.setVisible(True)
        self.pushButton_6.setVisible(True)

        #Configuramos la tabla
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(38)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(60)

        #Definimos las dimensiones 
        self.tableWidget_2.setColumnCount(columnas)
        self.tableWidget_2.setRowCount(2)

        #Mostramos los radio button
        self.radioButton.setVisible(True)
        self.radioButton_2.setVisible(True)
        self.label_9.setVisible(True)

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

    def insertar_datos_a_tabla_unidad2(self,metodo):

        #Puntos a evaluar, funcion en la que evaluaremos y las cifras que se usaran
        x1 = self.lineEdit_2.text()        #Primer punto a evaluar
        x2 = self.lineEdit_3.text()        #Segundo punto a evaluar
        x3 = self.lineEdit_4.text()        #Tercer punto a evaluar
        funcion = self.lineEdit.text()     #función a evaluar
        cifras  = self.lineEdit_5.text()   #numero de cifras significativas 

        #Hacemos una pequeña validacion para corroborar que los valores seán correctos

        #Si nos devuelven la palabra: 'falsisimo' estan malos 
        x1Prueba = metodos.pedirValoresIniciales(x1)
        x2Prueba = metodos.pedirValoresIniciales(x2)
        x3Prueba = metodos.pedirValoresIniciales(x3)
        cifrasPrueba = metodos.pedirCifrasSignificativas(cifras)
           
        #Limpiamos la tabla antes de llenarla
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        #tabla de biseccion - hasta secante
        if metodo >= 1 and metodo <= 6:

            # Llamamos al metodo que corresponda para obtener la respuesta y la guardamos en lst
            if metodo == 1:
                lst = metodos.metodoBiseccion(x1Prueba,x2Prueba,funcion,cifrasPrueba)
            elif metodo == 2:
                lst = metodos.metodoFalsaPosicion(x1Prueba,x2Prueba,funcion,cifrasPrueba)
            elif metodo == 3:
                lst = metodos.metodoPuntoFijo(x1Prueba,funcion,cifrasPrueba)
            elif metodo == 4:
                lst = metodos.metodoNewtonRaphson(x1Prueba,funcion,cifrasPrueba)
            elif metodo == 5:
                lst = metodos.metodoNewtonRaphsonMejorado(x1Prueba,funcion,cifrasPrueba)
            elif metodo == 6:
                lst = metodos.metodoSecante(x1Prueba,x2Prueba,funcion,cifrasPrueba)

            #Insertamos los valores de lst en la tabla de respuestas 

            self.tableWidget.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
            rows    = len(lst)              #Numero de filas
            columns = len(lst[0])           #Numero de columnas
            len_Col = int(930/columns)-5    #Tamaño que tendran las columnas

            #Aplicamos unas configuraciones a la tabla 
            self.tableWidget.setColumnCount(columns)
            self.tableWidget.setRowCount(rows)
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.horizontalHeader().setVisible(False)

            for row in range(rows): #Primer for recorre las filas en lst
                for column in range(columns): #Segundo for recorre las columnas en lst
                    if row == 0: #Encabezado o header
                        salida = lst[row][column]
                        self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                        self.tableWidget.item(row,column).setBackground(QtGui.QColor(11,133,192))
                        self.tableWidget.setColumnWidth(column, len_Col)
                    else:
                        if column == 0:
                            salida = (lst[row][column])
                            self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                            self.tableWidget.setColumnWidth(column, len_Col)
                        else:
                            salida = "%.5f" % float(lst[row][column])
                            self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                            self.tableWidget.setColumnWidth(column, len_Col)
        
        #tabla de ceros de polinomios
        elif metodo == 7:

            #Esta lista contiene los numeros que acompañan a las x
            lista_Coeficientes = metodos.coefs(self.lineEdit.text())
            largo = len(lista_Coeficientes)

            if largo >=2 and largo <= 5:
                if largo == 2: #Lineal
                    a = 0
                    b = 0
                    c = 0
                    d = lista_Coeficientes[1]
                    e = lista_Coeficientes[0]
                elif largo == 3: #Cuadratico
                    a = 0
                    b = 0
                    c = lista_Coeficientes[2]
                    d = lista_Coeficientes[1]
                    e = lista_Coeficientes[0]
                elif largo == 4: #Cubico
                    a = 0
                    b = lista_Coeficientes[3]
                    c = lista_Coeficientes[2]
                    d = lista_Coeficientes[1]
                    e = lista_Coeficientes[0]
                elif largo == 5: #Cuartico
                    a = lista_Coeficientes[4]
                    b = lista_Coeficientes[3]
                    c = lista_Coeficientes[2]
                    d = lista_Coeficientes[1]
                    e = lista_Coeficientes[0]
                
                lst = metodos.factorizar(a, b, c, d, e)

                columns = len(lst)              #Numero de columnas 
                rows = 2                        #Numero de filas 
                len_Col = int(930/columns)-5    #Tamaño de cada columna

                #Aplicamos unas configuraciones a la tabla 
                self.tableWidget.setColumnCount(columns)
                self.tableWidget.setRowCount(rows)
                self.tableWidget.verticalHeader().setVisible(False)
                self.tableWidget.horizontalHeader().setVisible(False)

                for row in range(rows): #Primer for controla las filas 
                        for column in range(columns): #Segundo for controla las columnas 
                            if row == 0: #cabezera o header 
                                salida = "raiz #"+str(column+1)
                                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                self.tableWidget.setColumnWidth(column, len_Col)
                            else:
                                salida = str(lst[column])
                                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                                self.tableWidget.setColumnWidth(column, len_Col)
            else:
                print("Intento ingresar una función mayor a x^4 o menor a x^1")

        #tabla Horder 
        elif metodo == 8:
            lista_Coeficientes = metodos.coefs(self.lineEdiit.text())
            lst = metodos.metodoHorner(lista_Coeficientes,x1Prueba,cifrasPrueba)

            rows    = len(lst)              #Numero de filas
            columns = len(lst[0])           #Numero de columnas
            len_Col = int(930/columns)-5    #Tamaño de las columnas

            #Aplicamos unas configuraciones a la tabla 
            self.tableWidget.setColumnCount(columns)
            self.tableWidget.setRowCount(rows)
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.horizontalHeader().setVisible(False)

            for row in range(rows): #Primer for controla las filas
                for column in range(columns): #Segundo for controla las columnas 
                    if row == 0: #header o encabezado
                        salida = lst[row][column]
                        self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                        self.tableWidget.setColumnWidth(column, len_Col)
                    else:
                        if column == 0:
                            salida = "%.0f" % (lst[row][column])
                            self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                            self.tableWidget.setColumnWidth(column, len_Col)
                        else:
                            salida = "%.5f" % float(lst[row][column])
                            self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                            self.tableWidget.setColumnWidth(column, len_Col)

        #tabla de muller
        elif metodo == 9:
            lst = metodos.metodoMuller(funcion,x1Prueba,x2Prueba,x3Prueba,cifrasPrueba)

            rows    = len(lst)              #Numero de filas
            columns = len(lst[0])           #Numero de columnas
            len_Col = int(930/columns)-5    #Tamaño de las columnas

            #Aplicamos unas configuraciones a la tabla 
            self.tableWidget.setColumnCount(columns)
            self.tableWidget.setRowCount(rows)
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.horizontalHeader().setVisible(False)

            for row in range(rows): #primer for controla las filas 
                for column in range(columns): #Segundo for controla las columnas 
                    if row == 0:
                        salida = lst[row][column]
                        self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                        self.tableWidget.setColumnWidth(column, len_Col)
                    else:
                        if column == 0:
                            salida = "%.0f" % (lst[row][column])
                            self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                            self.tableWidget.setColumnWidth(column, len_Col)
                        else:
                            salida = "%.5f" % float(lst[row][column])
                            self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(salida)))
                            self.tableWidget.setColumnWidth(column, len_Col)

        #tabla de bairstown
        elif metodo == 10:

            lista_Coeficientes = metodos.coefs(funcion)
            lista_Coeficientes.reverse()

            lst = metodos.metodoBairstow(lista_Coeficientes,x1Prueba,x2Prueba,cifrasPrueba)

            columns = len(lst) 

            #Aplicamos unas configuraciones a la tabla 
            self.tableWidget.setColumnCount(columns)
            self.tableWidget.setRowCount(2)
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.horizontalHeader().setVisible(False)

            #Controlamos el tamaño que tendra cada columna de forma variable y no estatica como loveniamos haciendo
            tamanioColumnas = 0
            listaTamanio = []
            contadorTamanio = 0
            for x in range(0,columns):
                listaTamanio.append(len(str(lst[x]))*7)
                contadorTamanio += len(str(lst[x]))*7

            listaTamanio.sort()

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

    def insertar_datos_a_tabla_unidad3(self,metodo,puntos,valor):

        #Limpiamos la tabla
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()

        #Aplicamos unas configuraciones 
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)

        if metodo == 1:#Interpolacion Lineal 

            lst = metodos.interpolacionLineal(puntos[0], valor)
            
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

    def control_agregar_columna_tabla_Unidad3(self):
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

    def control_eliminar_columna_tabla_Unidad3(self):
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

        elif metodo == 5:#hermite
            if cuantasFilasYColumnas == 3:
                print("Se neecesitan al menos 2 puntos")
            else:
                self.tableWidget_2.removeColumn(cuantasFilasYColumnas)
                cuantasFilasYColumnas = cuantasFilasYColumnas-1

        elif metodo == 6:#trazadores cubicos
            if cuantasFilasYColumnas == 3:
                print("Se neecesitan al menos 2 puntos")
            else:
                self.tableWidget_2.removeColumn(cuantasFilasYColumnas)
                cuantasFilasYColumnas = cuantasFilasYColumnas-1

    def encontrar_puntos_para_metodos_unidad3(self,metodo):
        global cuantasFilasYColumnas 
        listaX = []
        listaY = []
        puntos = []
        listaXapoyo = []
        listaYapoyo = []
       
        #Agregamos los puntos a listas separadas 
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
        
        #Buscamos la posicion donde se desea interpolar
        for i in range(0,len(listaY)):
                if listaY[i] == '?':
                    macht = i

        #Lineal
        if metodo == 1: 

            puntos_2 = []
            puntos_2.append(listaX[macht-1])#X0
            puntos_2.append(listaY[macht-1])#Y0
            puntos_2.append(listaX[macht+1])#X1
            puntos_2.append(listaY[macht+1])#Y1

            puntos = []
            puntos.append(puntos_2)

            self.insertar_datos_a_tabla_unidad3(1,puntos,float(listaX[macht]))

        #Cuadratica
        elif metodo == 2:

            #Creamos las listas que serian los pares x,y
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

            self.insertar_datos_a_tabla_unidad3(2,puntos,listaX[macht])

        #lagrange
        elif metodo == 3:

            #Encontramos los puntos x,y
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

            self.insertar_datos_a_tabla_unidad3(3,puntos,float(listaX[macht]))

        #Newton
        elif metodo == 4:

            #Encontramos los pares x,y
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

            self.insertar_datos_a_tabla_unidad3(4,puntos,float(listaX[macht]))

    #Metodos que se controlan con los botones 

    def limpiar_Campos(self):

        #limpiamos los lineEdit
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")
        self.ui.lineEdit_3.setText("")
        self.ui.lineEdit_4.setText("")
        self.ui.lineEdit_5.setText("")

        #limpiamos el combobox
        self.ui.comboBox_2.setCurrentIndex(-1)

        #Limpiamos tablas

        self.ui.tableWidget.clear()
        self.ui.tableWidget_2.clear()

    def calcular(self):
        unidad = self.comboBox.currentIndex()
        metodo = self.comboBox_2.currentIndex()

        if unidad   == 0: #Metodos de la unidad 1
            print("aun falta esta parte")
        elif unidad == 1: #Metodos de la unidad 2
            if metodo == 1: #Biseccion
                self.insertar_datos_a_tabla_unidad2(1)
            elif metodo == 2:#Falsa posicion
                self.insertar_datos_a_tabla_unidad2(2)
            elif metodo == 3:#Punto fijo
                self.insertar_datos_a_tabla_unidad2(3)
            elif metodo == 4:#Newton
                self.insertar_datos_a_tabla_unidad2(4)
            elif metodo == 5:#Newton mejorado
                self.insertar_datos_a_tabla_unidad2(5)
            elif metodo == 6:#secante
                self.insertar_datos_a_tabla_unidad2(6)
            elif metodo == 7:#cero polinomios
                self.insertar_datos_a_tabla_unidad2(7)
            elif metodo == 8:#Horner
                self.insertar_datos_a_tabla_unidad2(8)
            elif metodo == 9:#Muller
                self.insertar_datos_a_tabla_unidad2(9)
            elif metodo == 10:#Bairstown
                self.insertar_datos_a_tabla_unidad2(10)
            
        elif unidad == 2: #Metodos de la unidad 3
            if metodo == 1:
                self.encontrar_puntos_para_metodos_unidad3(1)
            elif metodo == 2:
                self.encontrar_puntos_para_metodos_unidad3(2)
            elif metodo == 3:
                self.encontrar_puntos_para_metodos_unidad3(3)
            elif metodo == 4:
                self.encontrar_puntos_para_metodos_unidad3(4)

    def graficar(self):
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
                    funcion = metodos.evaluarFuncion(self.lineEdit.text(), x, 0, 0)
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













    
