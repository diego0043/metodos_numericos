from PySide2.QtWidgets import QMainWindow
from metodosYformularios.diseñoFinal import Ui_MainWindow
from metodosYformularios.diseñoFinal import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    #Metodos que controlan los combobox
    def cambiar_metodos_cmb2(self):
        cual = self.ui.comboBox.currentIndex()
        self.ui.tableWidget_2.setVisible(False)
        self.ui.pushButton_5.setVisible(False)
        self.ui.pushButton_6.setVisible(False)
        self.ui.radioButton.setVisible(False)
        self.ui.radioButton_2.setVisible(False)
        self.ui.label_9.setVisible(False)
        
        if cual == 0: #Metodos de la primera unidad 
            self.ui.comboBox_2.setGeometry(QtCore.QRect(240, 50, 161, 21))
            # Siempre limpiamos el combobox para evitar duplicados o cosas raras
            self.ui.comboBox_2.clear()

            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")

            self.ui.comboBox_2.setItemText(0, "Seleccione un metodo")
            self.ui.comboBox_2.setItemText(1,  "ln(e+x)")
            self.ui.comboBox_2.setItemText(2,  "e^(x^2)")
            self.ui.comboBox_2.setItemText(3,  "sen(x)")
            self.ui.comboBox_2.setItemText(4,  "cos(x)")
            self.ui.comboBox_2.setItemText(5,  "e^x")
            self.ui.comboBox_2.setItemText(6,  "sh(x)")
            self.ui.comboBox_2.setItemText(7,  "ch(x)")
            self.ui.comboBox_2.setItemText(8,  "arcsen(x)")
            self.ui.comboBox_2.setItemText(9,  "ln(1+x)")
            self.ui.comboBox_2.setItemText(10,  "1/(1+x^2)")
            self.ui.comboBox_2.setItemText(11,  "arctg(x)")
            self.ui.comboBox_2.setCurrentIndex(0)

            self.ui.comboBox_2.setVisible(False)
            self.ui.lineEdit_4.setVisible(False)
            self.ui.lineEdit_3.setVisible(False)
            self.ui.label.setVisible(False)
            self.ui.label_2.setVisible(False)
            self.ui.label_5.setVisible(False)
            self.ui.label_6.setVisible(False)
            self.ui.label_3.setVisible(False)
            self.ui.label_4.setVisible(False)
            self.ui.label_5.setVisible(False)
            self.ui.label_6.setVisible(False)
            self.ui.label_7.setVisible(False)
            self.ui.lineEdit.setVisible(False)
            self.ui.lineEdit_2.setVisible(False)
            self.ui.lineEdit_3.setVisible(False)
            self.ui.lineEdit_4.setVisible(False)
            self.ui.lineEdit_5.setVisible(False)
            
          # <----------- Mostramos el combobox donde estan los metodos ---------->
            self.ui.comboBox_2.setVisible(True)
            self.ui.label.setVisible(True)

        elif cual == 1:  # Metodos de la segunda unidad
            self.ui.comboBox_2.setGeometry(QtCore.QRect(240, 50, 141, 21))
            # Siempre limpiamos el combobox para evitar duplicados o cosas raras
            self.ui.comboBox_2.clear()
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")

            self.ui.comboBox_2.setItemText(0,  "Seleccione un metodo")
            self.ui.comboBox_2.setItemText(1,  "Biseccion")
            self.ui.comboBox_2.setItemText(2,  "Falsa Posicion")
            self.ui.comboBox_2.setItemText(3,  "Punto Fijo")
            self.ui.comboBox_2.setItemText(4,  "Newton Raphson")
            self.ui.comboBox_2.setItemText(5,  "Newton Raphson Mejorado")
            self.ui.comboBox_2.setItemText(6,  "Secante")
            self.ui.comboBox_2.setItemText(7,  "Ceros de polinomios")
            self.ui.comboBox_2.setItemText(8,  "Horner")
            self.ui.comboBox_2.setItemText(9, "Muller")
            self.ui.comboBox_2.setItemText(10, "Bairstown")

            self.ui.comboBox_2.setCurrentIndex(0)
            self.ui.comboBox_2.setVisible(False)
            self.ui.lineEdit_4.setVisible(False)
            self.ui.lineEdit_3.setVisible(False)
            self.ui.label.setVisible(False)
            self.ui.label_2.setVisible(False)
            self.ui.label_5.setVisible(False)
            self.ui.label_6.setVisible(False)
            self.ui.label_3.setVisible(False)
            self.ui.label_4.setVisible(False)
            self.ui.label_5.setVisible(False)
            self.ui.label_6.setVisible(False)
            self.ui.label_7.setVisible(False)
            self.ui.lineEdit.setVisible(False)
            self.ui.lineEdit_2.setVisible(False)
            self.ui.lineEdit_3.setVisible(False)
            self.ui.lineEdit_4.setVisible(False)
            self.ui.lineEdit_5.setVisible(False)

          # <----------- Mostramos el combobox donde estan los metodos ---------->
            self.ui.comboBox_2.setVisible(True)
            self.ui.label.setVisible(True)
        
        elif cual == 2: #Metodos de la unidad 3
            self.comboBox_2.setGeometry(QtCore.QRect(360, 20, 161, 21))

            self.ui.comboBox_2.clear()
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.addItem("")
            
            self.ui.comboBox_2.setItemText(0,  "Seleccione un metodo")
            self.ui.comboBox_2.setItemText(1,  "Interpolación Lineal")
            self.ui.comboBox_2.setItemText(2,  "Interpolación cuadratica")
            self.ui.comboBox_2.setItemText(3,  "Interpolación de lagrange")
            self.ui.comboBox_2.setItemText(4,  "Interpolación de Newton")
            self.ui.comboBox_2.setItemText(5,  "Interpolación de Hermite")
            self.ui.comboBox_2.setItemText(6,  "Función Spline")

            #Mostramos el comboBox 
            self.ui.comboBox_2.setVisible(True)
            self.ui.label.setVisible(True)
            

            #Ocultamos todo
            self.ui.label_2.setVisible(False)
            self.ui.label_3.setVisible(False)
            self.ui.label_4.setVisible(False)
            self.ui.label_5.setVisible(False)
            self.ui.label_6.setVisible(False)
            self.ui.label_7.setVisible(False)
            self.ui.lineEdit.setVisible(False)
            self.ui.lineEdit_2.setVisible(False)
            self.ui.lineEdit_3.setVisible(False)
            self.ui.lineEdit_4.setVisible(False)
            self.ui.lineEdit_5.setVisible(False)

    def metodos_de_cada_unidad(self):
        queMetodo = self.ui.comboBox_2.currentIndex()
        queUnidad = self.ui.comboBox.currentIndex()

        if queUnidad == 0:

            self.ui.pushButton_5.setVisible(False)
            self.ui.pushButton_6.setVisible(False)
            self.ui.tableWidget_2.setVisible(False)
            self.ui.radioButton.setVisible(False)
            self.ui.radioButton_2.setVisible(False)
            self.ui.radioButton_3.setVisible(False)
            self.ui.radioButton_4.setVisible(False)
            self.ui.label_9.setVisible(False)
            
            # <---- dejamos solo los componentes que usa metodo punto fijo y los de newton -->
            self.ui.label_4.setText("#1")
            self.ui.label_5.setText("#2")
            self.ui.label_4.setVisible(True)
            self.ui.label_3.setVisible(True)
            self.ui.label_2.setVisible(True)
            self.ui.label_7.setVisible(True)
            self.ui.lineEdit_2.setVisible(True)
            self.ui.lineEdit_5.setVisible(True)

            # <-------- Ocultamos lo demas ------------->
            self.ui.lineEdit.setVisible(False)
            self.ui.lineEdit_4.setVisible(False)
            self.ui.lineEdit_3.setVisible(False)
            self.ui.label_2.setVisible(False)
            self.ui.label_5.setVisible(False)
            self.ui.label_6.setVisible(False)
            
        elif queUnidad == 1:

            self.ui.pushButton_5.setVisible(False)
            self.ui.pushButton_6.setVisible(False)
            self.ui.tableWidget_2.setVisible(False)
            self.ui.radioButton.setVisible(False)
            self.ui.radioButton_2.setVisible(False)
            self.ui.radioButton_3.setVisible(False)
            self.ui.radioButton_4.setVisible(False)
            self.ui.label_9.setVisible(False)

            if queMetodo >=1 and queMetodo <= 2:

                # <---- dejamos solo los componentes que usa metodo biseccion, falsa posicion y secante -->
                self.ui.label_4.setText("#1")
                self.ui.label_5.setText("#2")
                self.ui.label_4.setVisible(True)
                self.ui.label_3.setVisible(True)
                self.ui.label_2.setVisible(True)
                self.ui.label_5.setVisible(True)
                self.ui.label_7.setVisible(True)
                self.ui.lineEdit_2.setVisible(True)
                self.ui.lineEdit_2.setVisible(True)
                self.ui.lineEdit_3.setVisible(True)
                self.ui.lineEdit_5.setVisible(True)
                self.ui.lineEdit.setVisible(True)

                # <-------- Ocultamos lo demas ------------->
                self.ui.lineEdit_4.setVisible(False)
                self.ui.label_6.setVisible(False)

            elif queMetodo >= 3 and queMetodo <= 6:

                # <---- dejamos solo los componentes que usa metodo punto fijo y los de newton -->
                self.ui.label_4.setText("#1")
                self.ui.label_5.setText("#2")
                self.ui.label_4.setVisible(True)
                self.ui.label_2.setVisible(True)
                self.ui.label_3.setVisible(True)
                self.ui.label_2.setVisible(True)
                self.ui.label_7.setVisible(True)
                self.ui.lineEdit_2.setVisible(True)
                self.ui.lineEdit_5.setVisible(True)
                self.ui.lineEdit.setVisible(True)

                # <-------- Ocultamos lo demas ------------->
                self.ui.lineEdit_4.setVisible(False)
                self.ui.lineEdit_3.setVisible(False)
                self.ui.label_5.setVisible(False)
                self.ui.label_6.setVisible(False)

            elif queMetodo >= 7 and queMetodo <= 8:
                # <---- dejamos solo los componentes que usa metodo de cero de polinomios --->
                self.ui.label_4.setText("#1")
                self.ui.label_5.setText("#2")
                self.ui.lineEdit.setVisible(True)
                self.ui.label_2.setVisible(True)
                # <-------- ocultamos lo demas ---------->
                self.ui.label_3.setVisible(False)
                self.ui.label_4.setVisible(False)
                self.ui.label_5.setVisible(False)
                self.ui.label_6.setVisible(False)
                self.ui.label_7.setVisible(False)
                self.ui.lineEdit_2.setVisible(False)
                self.ui.lineEdit_3.setVisible(False)
                self.ui.lineEdit_4.setVisible(False)
                self.ui.lineEdit_5.setVisible(False)

            elif queMetodo == 9:

                # <---- dejamos solo los componentes que usa metodo muller -->
                self.ui.label_4.setText("#1")
                self.ui.label_5.setText("#2")
                self.ui.label_4.setVisible(True)
                self.ui.label_2.setVisible(True)
                self.ui.label_3.setVisible(True)
                self.ui.label_5.setVisible(True)
                self.ui.label_7.setVisible(True)
                self.ui.lineEdit_2.setVisible(True)
                self.ui.lineEdit_3.setVisible(True)
                self.ui.lineEdit_5.setVisible(True)
                self.ui.lineEdit_4.setVisible(True)
                self.ui.lineEdit.setVisible(True)
                self.ui.label_6.setVisible(True)

            elif queMetodo == 10:

                 # <---- dejamos solo los componentes que usa metodo muller -->
                self.ui.label_4.setText("R")
                self.ui.label_5.setText("S")
                self.ui.label_4.setVisible(True)
                self.ui.label_2.setVisible(True)
                self.ui.label_3.setVisible(True)
                self.ui.label_5.setVisible(True)
                self.ui.lineEdit_2.setVisible(True)
                self.ui.lineEdit_3.setVisible(True)
                self.ui.lineEdit.setVisible(True)

                # <-------- ocultamos lo demas ---------->

                self.ui.lineEdit_5.setVisible(False)
                self.ui.lineEdit_4.setVisible(False)
                self.ui.label_6.setVisible(False)
                self.ui.label_7.setVisible(False)

        elif queUnidad == 2: #Configuramos la tabla

            global cuantasFilasYColumnas

            #Deseleccionamos los radio button

            
            if queMetodo >= 1 and queMetodo <= 5:
                self.ui.label_9.setText("¿Desea ver el polinomio?")
                self.ui.radioButton.setAutoExclusive(False)
                self.ui.radioButton.setChecked(False)
                self.ui.radioButton.setAutoExclusive(True)
                self.ui.radioButton_2.setAutoExclusive(False)
                self.ui.radioButton_2.setChecked(False)
                self.ui.radioButton_2.setAutoExclusive(True)
                self.ui.radioButton_3.setVisible(False)
                self.ui.radioButton_3.setAutoExclusive(True)
                self.ui.radioButton_4.setVisible(False)
                self.ui.radioButton_4.setAutoExclusive(False)
                self.ui.radioButton.setText("Si")
                self.ui.radioButton_2.setText("No")
                self.ui.radioButton.setGeometry(QtCore.QRect(620, 40, 82, 17))
                self.ui.radioButton_2.setGeometry(QtCore.QRect(660,40,82,17))
                
                
            else:
                self.ui.label_9.setText("Seleccione el grado de la función Spline")
                self.ui.radioButton.setAutoExclusive(False)
                self.ui.radioButton.setChecked(False)
                self.ui.radioButton.setAutoExclusive(True)
                self.ui.radioButton_2.setAutoExclusive(False)
                self.ui.radioButton_2.setChecked(False)
                self.ui.radioButton_2.setAutoExclusive(True)

                self.ui.radioButton_3.setAutoExclusive(False)
                self.ui.radioButton_3.setChecked(False)
                self.ui.radioButton_3.setAutoExclusive(True)

                self.ui.radioButton_4.setAutoExclusive(False)
                self.ui.radioButton_4.setChecked(False)
                self.ui.radioButton_4.setAutoExclusive(True)

                self.ui.radioButton.setText("Grado #0")
                self.ui.radioButton_2.setText("Grado #1")
                self.ui.radioButton_3.setText("Grado #2")
                self.ui.radioButton_4.setText("Grado #3")
                self.ui.radioButton.setGeometry(QtCore.QRect(620, 40, 82, 17))
                self.ui.radioButton_2.setGeometry(QtCore.QRect(700,40,82,17))
                self.ui.radioButton_3.setVisible(True)
                self.ui.radioButton_4.setVisible(True)

            if queMetodo == 1:#Lineal
                cuantasFilasYColumnas = 3
                self.ui.configuracionTablaUnidad3(4)     
            elif queMetodo == 2:#Cuadratica
                cuantasFilasYColumnas = 4
                self.ui.configuracionTablaUnidad3(5)
            elif queMetodo == 3:#Lagrange
                cuantasFilasYColumnas = 3
                self.ui.configuracionTablaUnidad3(4)
            elif queMetodo == 4:#Newton
                cuantasFilasYColumnas = 3
                self.ui.configuracionTablaUnidad3(4)
            elif queMetodo == 5:#Hermite
                cuantasFilasYColumnas = 3
                self.ui.configuracionTablaUnidad3(4)
            elif queMetodo == 6:#función spline grado 0
                cuantasFilasYColumnas = 3
                self.ui.configuracionTablaUnidad3(5)

    #Metodos que controlan las tablas ó que trabajan con las tablas 
    def creacion_tabla_por_defecto_unidad3(self,columnas):
        #Limpiamos la tabla
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_2.setColumnCount(0)

        self.ui.pushButton_5.setVisible(True)
        self.ui.pushButton_6.setVisible(True)

        #Configuramos la tabla
        self.ui.tableWidget_2.verticalHeader().setVisible(False)
        self.ui.tableWidget_2.horizontalHeader().setVisible(False)
        self.ui.tableWidget_2.verticalHeader().setDefaultSectionSize(38)
        self.ui.tableWidget_2.horizontalHeader().setDefaultSectionSize(60)

        #Definimos las dimensiones 
        self.ui.tableWidget_2.setColumnCount(columnas)
        self.ui.tableWidget_2.setRowCount(2)

        #Mostramos los radio button
        self.ui.radioButton.setVisible(True)
        self.ui.radioButton_2.setVisible(True)
        self.ui.label_9.setVisible(True)

        for x in range(0,2):
            for y in range(0,3):
                if y == 0 and x == 0:
                    salida = "    X"
                    self.ui.tableWidget_2.setItem(x, y, QtWidgets.QTableWidgetItem(salida))
                    self.ui.tableWidget_2.setColumnWidth(y, 8)
                elif y == 0 and x == 1:
                    salida = "    Y"
                    self.ui.tableWidget_2.setItem(x, y, QtWidgets.QTableWidgetItem(salida))
                    self.ui.tableWidget_2.setColumnWidth(y, 8)
                else:
                    salida = ""
                    self.ui.tableWidget_2.setItem(x, y, QtWidgets.QTableWidgetItem(salida))

        self.ui.tableWidget_2.setVisible(True)

    def insertar_datos_a_tabla_unidad2(self,metodo):

        #Puntos a evaluar, funcion en la que evaluaremos y las cifras que se usaran
        x1 = self.ui.lineEdit_2.text()        #Primer punto a evaluar
        x2 = self.ui.lineEdit_3.text()        #Segundo punto a evaluar
        x3 = self.ui.lineEdit_4.text()        #Tercer punto a evaluar
        funcion = self.ui.lineEdit.text()     #función a evaluar
        cifras  = self.ui.lineEdit_5.text()   #numero de cifras significativas 

        #Hacemos una pequeña validacion para corroborar que los valores seán correctos

        #Si nos devuelven la palabra: 'falsisimo' estan malos 
        x1Prueba = metodos.pedirValoresIniciales(x1)
        x2Prueba = metodos.pedirValoresIniciales(x2)
        x3Prueba = metodos.pedirValoresIniciales(x3)
        cifrasPrueba = metodos.pedirCifrasSignificativas(cifras)

        if x1Prueba != "falsisimo" and x2Prueba != "falsisimo" and x3Prueba != "falsisimo" and cifrasPrueba != "falsisimo":
           
            #Limpiamos la tabla antes de llenarla
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setColumnCount(0)
            self.ui.tableWidget.setRowCount(0)

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
        self.tableWidget.setColumnsCount(0)
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

    def limpiarCampos(self):

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
            print("unidad 3")
            if metodo == 1:
                self.encontrar_puntos_para_metodos_unidad3(1)
            elif metodo == 2:
                self.encontrar_puntos_para_metodos_unidad3(2)
            elif metodo == 3:
                self.encontrar_puntos_para_metodos_unidad3(3)
            elif metodo == 4:
                self.encontrar_puntos_para_metodos_unidad3(4)

    def graficas(self):
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













    
