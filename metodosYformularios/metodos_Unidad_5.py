import decimal
from numpy.lib.shape_base import column_stack
import sympy as sp
import numpy as np
import math
import cmath
import re
from sympy import cos, sin, tan, cot, sec, csc, sinh, cosh, tanh, csch, sech, coth, ln
from numpy.polynomial import Polynomial as P
from sympy.core.function import expand
from sympy.simplify.radsimp import fraction, numer
from fractions import Fraction

x = sp.Symbol('x')
t = sp.Symbol('t')
e = sp.Symbol('e')
y = sp.Symbol('y')
z = sp.Symbol('z')


def evaluarFuncionX(funcion, valor, seDeriva, ordenDerivada):
    try:
        funcioon = 0
        if seDeriva == 1:
            if ordenDerivada == 1:
                funcioon = sp.sympify(funcion)
                gxValor = sp.diff(funcioon, x).subs([(x, valor), (e, cmath.e)])
                return gxValor
            else:
                funcioon = sp.sympify(funcion)
                gxValor = sp.Derivative(funcion, x, 2).subs(
                    [(x, valor), (e, cmath.e)])
                return gxValor
        else:
            resultado = sp.sympify(funcion).subs([(x, valor), (e, cmath.e)])
            return resultado
    except:
        return "falsisimo"


def evaluarFuncion(funcion, valor, valor2, seDeriva, ordenDerivada):
    try:
        funcioon = 0
        if seDeriva == 1:
            if ordenDerivada == 1:
                funcioon = sp.sympify(funcion)
                gxValor = sp.diff(funcioon, x).subs([(x, valor), (e, cmath.e)])
                return gxValor
            else:
                funcioon = sp.sympify(funcion)
                gxValor = sp.Derivative(funcion, x, 2).subs(
                    [(x, valor), (e, cmath.e)])
                return gxValor
        else:
            resultado = sp.sympify(funcion).subs(
                [(x, valor), (e, cmath.e), (y, valor2)])
            return resultado
    except:
        return "falsisimo"


def encontrarDerivada(funcion, queDerivada):
    funcioon = sp.sympify(funcion)
    gxValor = sp.diff(funcioon, x, queDerivada)
    return gxValor


# <-------------------------------- metodos de Euler ------------------------------>
def metodo_Euler_Adelante(funcion, x_Inicial, y_Inicial, x_Final, n_intervalos):

    # Variables a utilizar
    lista_Salida_Final = []  # Lista para guardar la salida mostrada en el formulario
    lista_X = []  # Lista para almacenar los valores de x
    lista_Y = []  # Lista para almacenar los valores de y
    h = (x_Final-x_Inicial)/n_intervalos  # Pasos para el siguiente x

    # Agregamos el primer x
    lista_X.append(x_Inicial)
    # Agregamos los x faltantes
    for i in range(1, n_intervalos+1, 1):
        lista_X.append(lista_X[i-1]+h)

    # Agregamos el primer y
    lista_Y.append(y_Inicial)
    # Agregamos los y faltantes
    for i in range(1, n_intervalos+1, 1):
        lista_Y.append(evaluarFuncion(
            funcion, lista_X[i-1], lista_Y[i-1], 0, 0).evalf())

    # Agregamos la primera iteracion de la respuesta final

    lista_Salida_Final.append("Iteracion: "+str(1)+"\n" +
                              "X: "+str(lista_X[0])+"\n" +
                              "Yn: "+str(lista_Y[0])+"\n")

    # Iniciamos las siguientes iteraciones
    for i in range(1, len(lista_X), 1):
        lista_Salida_Final.append("Iteracion: "+str(i+1)+"\n" +
                                  "X: "+str(lista_X[i])+"\n" +
                                  "Yn: "+str(lista_Y[i-1]+h*lista_Y[i])+"\n")

    for i in lista_Salida_Final:
        print(i)
    '''
    '''


metodo_Euler_Adelante("(-20*y)+7*e^(-0.5*x)", 0, 5, 0.02, 2)

# <-------------------------------- metodo de Taylor ------------------------------>

# <-------------------------------- metodo de Runge Kutta ------------------------------>
