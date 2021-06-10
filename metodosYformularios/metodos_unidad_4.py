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
from sympy.simplify.radsimp import numer
from fractions import Fraction

x = sp.Symbol('x')
e = sp.Symbol('e')

def evaluarFuncion(funcion, valor, seDeriva, ordenDerivada):
    try:
        funcioon = 0
        if seDeriva == 1:
            if ordenDerivada == 1:
                funcioon = sp.sympify(funcion)
                gxValor = sp.diff(funcioon, x).subs([(x, valor), (e, cmath.e)])
                return gxValor
            else:
                funcioon = sp.sympify(funcion)
                gxValor = sp.Derivative(funcion, x, 2).subs([(x, valor), (e, cmath.e)])
                return gxValor
        else:
            resultado = sp.sympify(funcion).subs([(x, valor), (e, cmath.e)])
            return resultado
    except:
        return "falsisimo"

def encontrarDerivada(funcion,queDerivada):
    funcioon = sp.sympify(funcion)
    gxValor = sp.diff(funcioon, x,queDerivada)
    return gxValor
  
def diferenciacionNumericaAdelante(funcion,puntoInicial,h,tablaValores):
    listaResultados = [] #lista donde estaran las respuestas 
    salida = ''

    if funcion != '':
        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = evaluarFuncion(funcion,puntoInicial+h,0,0) + evaluarFuncion(funcion,puntoInicial,0,0)*(-1)

        #guardamos la primera diferencia
        listaResultados.append((numerador1)/h)


        numerador1 = evaluarFuncion(funcion,puntoInicial+(2*h),0,0)*(-1) + evaluarFuncion(funcion,puntoInicial+h,0,0)*(4) + evaluarFuncion(funcion,puntoInicial,0,0)*(-3)
    
        #guardamos la segunda diferencia 
        listaResultados.append(numerador1/(2*h))

        #calculamos los errores para la primera y la segunda diferencia 
        lista_errores = []
        valor_verdadero = evaluarFuncion(funcion,puntoInicial,1,1)
        valor_apro1 = listaResultados[0]
        valor_apro2 = listaResultados[1]

        #primer error 
        listaResultados.append(abs((valor_verdadero-valor_apro1)/valor_verdadero))
        listaResultados.append(listaResultados[2]*100)

        #segundo error 
        listaResultados.append(abs((valor_verdadero-valor_apro2)/valor_verdadero))
        listaResultados.append(listaResultados[4]*100)

        print(listaResultados[0])
        print(listaResultados[1])

    else:
        lista_valores = []
        lista_x = tablaValores[0]
        lista_y = tablaValores[1]

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]+lista_valores[1]*(-1)

        #guardamos la primera diferencia
        listaResultados.append((numerador1)/(h))

        lista_valores = []

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i+2])
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]*(-1) + lista_valores[1]*(4) + lista_valores[-3]

        #guardamos la segunda diferencia
        listaResultados.append((numerador1)/(h*2))
        print(listaResultados)

def diferenciacionNumericaAtras(funcion,puntoInicial,h,tablaValores):
    listaResultados = [] #lista donde estaran las respuestas 
    salida = ''

    if funcion != '':
        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = evaluarFuncion(funcion,puntoInicial,0,0) + evaluarFuncion(funcion,puntoInicial-h,0,0)*(-1)

        #guardamos la primera diferencia
        listaResultados.append((numerador1)/h)


        numerador1 = evaluarFuncion(funcion,puntoInicial,0,0)*(3) + evaluarFuncion(funcion,puntoInicial-h,0,0)*(-4) + evaluarFuncion(funcion,puntoInicial-2*h,0,0)
    
        #guardamos la segunda diferencia 
        listaResultados.append(numerador1/(2*h))

        #calculamos los errores para la primera y la segunda diferencia 
        lista_errores = []
        valor_verdadero = evaluarFuncion(funcion,puntoInicial,1,1)
        valor_apro1 = listaResultados[0]
        valor_apro2 = listaResultados[1]

        #primer error 
        listaResultados.append(abs((valor_verdadero-valor_apro1)/valor_verdadero))
        listaResultados.append(listaResultados[2]*100)

        #segundo error 
        listaResultados.append(abs((valor_verdadero-valor_apro2)/valor_verdadero))
        listaResultados.append(listaResultados[4]*100)

        print(listaResultados[0])
        print(listaResultados[1])

    else:
        lista_valores = []
        lista_x = tablaValores[0]
        lista_y = tablaValores[1]

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i])
                lista_valores.append(lista_y[i-1])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]+lista_valores[1]*(-1)

        #guardamos la primera diferencia
        listaResultados.append((numerador1)/(h))

        lista_valores = []

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i])
                lista_valores.append(lista_y[i-1])
                lista_valores.append(lista_y[i-2])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]*(3) + lista_valores[1]*(-4) + lista_valores[2]

        #guardamos la segunda diferencia
        listaResultados.append((numerador1)/(h*2))
        print(listaResultados)

def diferenciacionNumericaCentrada(funcion,puntoInicial,h,tablaValores):
    listaResultados = [] #lista donde estaran las respuestas 
    salida = ''

    if funcion != '':
        #lista donde guardamos los valores de la primera diferencia

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = evaluarFuncion(funcion,puntoInicial+h,0,0) + evaluarFuncion(funcion,puntoInicial-h,0,0)*(-1)

        #guardamos la primera diferencia
        listaResultados.append((numerador1)/(2*h))


        numerador1 = evaluarFuncion(funcion,puntoInicial+2*h,0,0)*(-1) + evaluarFuncion(funcion,puntoInicial+h,0,0)*(8) + evaluarFuncion(funcion,puntoInicial-h,0,0)*(-8) + evaluarFuncion(funcion,puntoInicial-2*h,0,0)
    
        #guardamos la segunda diferencia 
        listaResultados.append(numerador1/(12*h))

        #calculamos los errores para la primera y la segunda diferencia 
        lista_errores = []
        valor_verdadero = evaluarFuncion(funcion,puntoInicial,1,1)
        valor_apro1 = listaResultados[0]
        valor_apro2 = listaResultados[1]

        #primer error 
        listaResultados.append(abs((valor_verdadero-valor_apro1)/valor_verdadero))
        listaResultados.append(listaResultados[2]*100)

        #segundo error 
        listaResultados.append(abs((valor_verdadero-valor_apro2)/valor_verdadero))
        listaResultados.append(listaResultados[4]*100)

        print(listaResultados[0])
        print(listaResultados[1])

    else:
        lista_valores = []
        lista_x = tablaValores[0]
        lista_y = tablaValores[1]

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i-1])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]+lista_valores[1]*(-1)

        #guardamos la primera diferencia
        listaResultados.append((numerador1)/(h*2))

        lista_valores = []

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i+2])
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i-1])
                lista_valores.append(lista_y[i-2])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]*(-1) + lista_valores[1]*(8) + lista_valores[2]*(-8) + lista_valores[3]

        #guardamos la segunda diferencia
        listaResultados.append((numerador1)/(h*12))
        print(listaResultados)

def diferenciacionNumericaTresPuntos(funcion,puntoInicial,h,tablaValores):
    listaResultados = [] #lista donde estaran las respuestas 
    salida = ''

    if funcion != '':
        #lista donde guardamos los valores de la primera diferencia

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = evaluarFuncion(funcion,puntoInicial+h,0,0) + evaluarFuncion(funcion,puntoInicial-h,0,0)*(-1)

        #guardamos la primera diferencia
        listaResultados.append((numerador1)/(2*h))


        numerador1 = evaluarFuncion(funcion,puntoInicial,0,0)*(-3) + evaluarFuncion(funcion,puntoInicial+h,0,0)*(4) + evaluarFuncion(funcion,puntoInicial+2*h,0,0)*(-1)
    
        #guardamos la segunda diferencia 
        listaResultados.append(numerador1/(2*h))

        #calculamos los errores para la primera y la segunda diferencia 
        lista_errores = []
        valor_verdadero = evaluarFuncion(funcion,puntoInicial,1,1)
        valor_apro1 = listaResultados[0]
        valor_apro2 = listaResultados[1]

        #primer error 
        listaResultados.append(abs((valor_verdadero-valor_apro1)/valor_verdadero))
        listaResultados.append(listaResultados[2]*100)

        #segundo error 
        listaResultados.append(abs((valor_verdadero-valor_apro2)/valor_verdadero))
        listaResultados.append(listaResultados[4]*100)

        print(listaResultados[0])
        print(listaResultados[1])

    else:
        lista_valores = []
        lista_x = tablaValores[0]
        lista_y = tablaValores[1]

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i-1])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]+lista_valores[1]*(-1)

        #guardamos la primera diferencia
        listaResultados.append((numerador1)/(h*2))

        lista_valores = []

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:
                lista_valores.append(lista_y[i])
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i+2])

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]*(-3) + lista_valores[1]*(4) + lista_valores[2]*(-1) 

        #guardamos la segunda diferencia
        listaResultados.append((numerador1)/(h*2))
        print(listaResultados)

def diferenciacionNumericaCincoPuntos(funcion,puntoInicial,h,tablaValores):
    listaResultados = [] #lista donde estaran las respuestas 
    salida = ''

    if funcion != '':
        #lista donde guardamos los valores de la primera diferencia

        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = evaluarFuncion(funcion,puntoInicial,0,0)*(-25) + evaluarFuncion(funcion,puntoInicial+h,0,0)*(48) + evaluarFuncion(funcion,puntoInicial+2*h,0,0)*(-36) + evaluarFuncion(funcion,puntoInicial+3*h,0,0)*(16) + evaluarFuncion(funcion,puntoInicial+4*h,0,0)*(-3)
        #guardamos la primera diferencia
        listaResultados.append((numerador1)/(12*h))

        numerador1 = evaluarFuncion(funcion,puntoInicial-h,0,0)*(-3) + evaluarFuncion(funcion,puntoInicial,0,0)*(-10) + evaluarFuncion(funcion,puntoInicial+h,0,0)*(18) + evaluarFuncion(funcion,puntoInicial+2*h,0,0)*(-6) + evaluarFuncion(funcion,puntoInicial+3*h,0,0)
        #guardamos la segunda diferencia 
        listaResultados.append(numerador1/(12*h))

        numerador1 = evaluarFuncion(funcion,puntoInicial-2*h,0,0) + evaluarFuncion(funcion,puntoInicial-h,0,0)*(-8) + evaluarFuncion(funcion,puntoInicial+h,0,0)*(8) + evaluarFuncion(funcion,puntoInicial+2*h,0,0)*(-1) 
        #guardamos la Tercera diferencia 
        listaResultados.append(numerador1/(12*h))

        numerador1 = evaluarFuncion(funcion,puntoInicial-3*h,0,0)*(4) + evaluarFuncion(funcion,puntoInicial+2*h,0,0)*(6) + evaluarFuncion(funcion,puntoInicial-h,0,0)*(-8) + evaluarFuncion(funcion,puntoInicial,0,0)*(34) + evaluarFuncion(funcion,puntoInicial+h,0,0)*(3) + evaluarFuncion(funcion,puntoInicial+2*h,0,0)*(34)
        #guardamos la cuarta diferencia 
        listaResultados.append(numerador1/(12*h))

        numerador1 = evaluarFuncion(funcion,puntoInicial-4*h,0,0) + evaluarFuncion(funcion,puntoInicial-3*h,0,0)*(-3) + evaluarFuncion(funcion,puntoInicial-2*h,0,0)*(4) + evaluarFuncion(funcion,puntoInicial-h,0,0)*(-36) + evaluarFuncion(funcion,puntoInicial,0,0)*(25)
        #guardamos la quinta diferencia 
        listaResultados.append(numerador1/(12*h))

        #calculamos los errores para la primera y la segunda diferencia 
        lista_errores = []
        valor_verdadero = evaluarFuncion(funcion,puntoInicial,1,1)
        valor_apro1 = listaResultados[0]
        valor_apro2 = listaResultados[1]
        valor_apro3 = listaResultados[2]
        valor_apro4 = listaResultados[3]
        valor_apro5 = listaResultados[4]

        #primer error 
        listaResultados.append(abs((valor_verdadero-valor_apro1)/valor_verdadero))
        listaResultados.append(listaResultados[2]*100)

        #segundo error 
        listaResultados.append(abs((valor_verdadero-valor_apro2)/valor_verdadero))
        listaResultados.append(listaResultados[4]*100)

        #tercer error 
        listaResultados.append(abs((valor_verdadero-valor_apro3)/valor_verdadero))
        listaResultados.append(listaResultados[4]*100)

        #cuarto error 
        listaResultados.append(abs((valor_verdadero-valor_apro4)/valor_verdadero))
        listaResultados.append(listaResultados[4]*100)

        #quinto error 
        listaResultados.append(abs((valor_verdadero-valor_apro5)/valor_verdadero))
        listaResultados.append(listaResultados[4]*100) 

        print(listaResultados[0])
        print(listaResultados[1])
        print(listaResultados[2])
        print(listaResultados[3])
        print(listaResultados[4])

    else:
        lista_valores = []
        lista_valores_2 = []
        lista_valores_3 = []
        lista_valores_4 = []
        lista_valores_5 = []

        lista_x = tablaValores[0]
        lista_y = tablaValores[1]

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:

                #valores para primera diferencia
                lista_valores.append(lista_y[i])
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i+2])
                lista_valores.append(lista_y[i+3])
                lista_valores.append(lista_y[i+4])

                #valores para segunda diferencia
                lista_valores_2.append(lista_y[i-1])
                lista_valores_2.append(lista_y[i])
                lista_valores_2.append(lista_y[i+1])
                lista_valores_2.append(lista_y[i+2])
                lista_valores_2.append(lista_y[i+3])

                #valores para tercera diferencia
                lista_valores_2.append(lista_y[i-2])
                lista_valores_2.append(lista_y[i-1])
                lista_valores_2.append(lista_y[i+1])
                lista_valores_2.append(lista_y[i+2])

                #valores para cuarta diferencia
                lista_valores_2.append(lista_y[i-3])
                lista_valores_2.append(lista_y[i+2])
                lista_valores_2.append(lista_y[i-1])
                lista_valores_2.append(lista_y[i])
                lista_valores_2.append(lista_y[i+1])
                lista_valores_2.append(lista_y[i+2])

                #valores para quinta diferencia
                lista_valores_2.append(lista_y[i-4])
                lista_valores_2.append(lista_y[i-3])
                lista_valores_2.append(lista_y[i-2])
                lista_valores_2.append(lista_y[i-1])
                lista_valores_2.append(lista_y[i])

                
        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]*(-25) + lista_valores[1]*(48) + lista_valores[2]*(-36) + lista_valores[3]*(16) + lista_valores[4]*(-3)
        #guardamos la primera diferencia
        listaResultados.append((numerador1)/(h*12))

        numerador1 = lista_valores[0]*(-3) + lista_valores[1]*(-10) + lista_valores[2]*(18) + lista_valores[3]*(-6) + lista_valores[4]
        #guardamos la segunda diferencia
        listaResultados.append((numerador1)/(h*12))

        numerador1 = lista_valores[0] + lista_valores[1]*(-8) + lista_valores[2]*(8) + lista_valores[3]*(-1) 
        #guardamos la tercera diferencia
        listaResultados.append((numerador1)/(h*12))

        numerador1 = lista_valores[0]*(4) + lista_valores[1]*(6) + lista_valores[2]*(-8) + lista_valores[3]*(34) + lista_valores[4]*(3)  + lista_valores[5]*(34)
        #guardamos la cuarta diferencia
        listaResultados.append((numerador1)/(h*12))

        numerador1 = lista_valores[0] + lista_valores[1]*(-3) + lista_valores[2]*(4) + lista_valores[3]*(-36) + lista_valores[25]
        #guardamos la quinta diferencia
        listaResultados.append((numerador1)/(h*12))

    
        print(listaResultados)

# <------------- Derivadas de orden superior --------------------->

       


            


