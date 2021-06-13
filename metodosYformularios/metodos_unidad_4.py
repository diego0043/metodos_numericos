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
e = sp.Symbol('e')
y = sp.Symbol('y')
z = sp.Symbol('z')

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
  
# <------------- Derivadas de primer orden --------------------->


def diferenciacion_numerica_adelante(funcion,puntoInicial,h,tablaValores):
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

def diferenciacion_numerica_atras(funcion,puntoInicial,h,tablaValores):
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

def diferenciacion_numerica_centrada(funcion,puntoInicial,h,tablaValores):
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

        return listaResultados

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

def diferenciacion_numerica_tres_puntos(funcion,puntoInicial,h,tablaValores):
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

def diferenciacion_numerica_cinco_puntos(funcion,puntoInicial,h,tablaValores):
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
                lista_valores_3.append(lista_y[i-2])
                lista_valores_3.append(lista_y[i-1])
                lista_valores_3.append(lista_y[i+1])
                lista_valores_3.append(lista_y[i+2])

                #valores para cuarta diferencia
                lista_valores_4.append(lista_y[i-3])
                lista_valores_4.append(lista_y[i+2])
                lista_valores_4.append(lista_y[i-1])
                lista_valores_4.append(lista_y[i])
                lista_valores_4.append(lista_y[i+1])
                lista_valores_4.append(lista_y[i+2])

                #valores para quinta diferencia
                lista_valores_5.append(lista_y[i-4])
                lista_valores_5.append(lista_y[i-3])
                lista_valores_5.append(lista_y[i-2])
                lista_valores_5.append(lista_y[i-1])
                lista_valores_5.append(lista_y[i])

                
        #variables donde guardaremos el numerador
        numerador1 = 0

        numerador1 = lista_valores[0]*(-25) + lista_valores[1]*(48) + lista_valores[2]*(-36) + lista_valores[3]*(16) + lista_valores[4]*(-3)
        #guardamos la primera diferencia
        listaResultados.append((numerador1)/(h*12))

        numerador1 = lista_valores_2[0]*(-3) + lista_valores_2[1]*(-10) + lista_valores_2[2]*(18) + lista_valores_2[3]*(-6) + lista_valores_2[4]
        #guardamos la segunda diferencia
        listaResultados.append((numerador1)/(h*12))

        numerador1 = lista_valores_3[0] + lista_valores_3[1]*(-8) + lista_valores_3[2]*(8) + lista_valores_3[3]*(-1) 
        #guardamos la tercera diferencia
        listaResultados.append((numerador1)/(h*12))

        numerador1 = lista_valores_4[0]*(4) + lista_valores_4[1]*(6) + lista_valores_4[2]*(-8) + lista_valores_4[3]*(34) + lista_valores_4[4]*(3)  + lista_valores_4[5]*(34)
        #guardamos la cuarta diferencia
        listaResultados.append((numerador1)/(h*12))

        numerador1 = lista_valores_5[0] + lista_valores_5[1]*(-3) + lista_valores_5[2]*(4) + lista_valores_5[3]*(-36) + lista_valores_5[25]
        #guardamos la quinta diferencia
        listaResultados.append((numerador1)/(h*12))

    
        print(listaResultados)


# <------------- Derivadas de orden superior --------------------->

 ## falta ##
def diferenciacion_numerica_adelante_orden_superior(funcion,puntoInicial,h,tablaValores):
    listaResultados = [] #lista donde estaran las respuestas 
    salida = ''

    if funcion != '':
        #lista donde guardamos los valores de la primera diferencia

        #variables donde guardaremos el numerador
        numerador1 = 0

        #<------------------ Primera doferencia ----------------------------->
        numerador1 = evaluarFuncion(funcion,puntoInicial+2*h,0,0) + evaluarFuncion(funcion,puntoInicial+h,0,0)*(-2) + evaluarFuncion(funcion,puntoInicial,0,0) 
        listaResultados.append((numerador1)/(h**2))

        numerador1 = evaluarFuncion(funcion,puntoInicial+3*h,0,0) + evaluarFuncion(funcion,puntoInicial+2*h,0,0)*(-3) + evaluarFuncion(funcion,puntoInicial+h,0,0)*(3) + evaluarFuncion(funcion,puntoInicial,0,0)*(-1)
        listaResultados.append(numerador1/(h**3))

        numerador1 = evaluarFuncion(funcion,puntoInicial+4*h,0,0) + evaluarFuncion(funcion,puntoInicial+3*h,0,0)*(-4) + evaluarFuncion(funcion,puntoInicial+2*h,0,0)*(6) + evaluarFuncion(funcion,puntoInicial+h,0,0)*(-4)  + evaluarFuncion(funcion,puntoInicial,0,0)
        listaResultados.append(numerador1/(h**4))


        #<------------------ Segunda diferencia ----------------------------------->
        numerador1 = evaluarFuncion(funcion,puntoInicial+3*h,0,0)*(-1) + evaluarFuncion(funcion,puntoInicial+2*h,0,0)*(4) + evaluarFuncion(funcion,puntoInicial+h,0,0)*(-5) + evaluarFuncion(funcion,puntoInicial,0,0)*(2)
        listaResultados.append((numerador1)/(h**2))

        numerador1 = evaluarFuncion(funcion,puntoInicial+4*h,0,0)*(-3) + evaluarFuncion(funcion,puntoInicial+3*h,0,0)*(14) + evaluarFuncion(funcion,puntoInicial+2*h,0,0)*(24) + evaluarFuncion(funcion,puntoInicial+h,0,0)*(-18) + evaluarFuncion(funcion,puntoInicial,0,0)*(-5)
        listaResultados.append(numerador1/(h**3))

        numerador1 = evaluarFuncion(funcion,puntoInicial+5*h,0,0)*(-2) + evaluarFuncion(funcion,puntoInicial+4*h,0,0)*(11) + evaluarFuncion(funcion,puntoInicial+3*h,0,0)*(-24) + evaluarFuncion(funcion,puntoInicial+2*h,0,0)*(26)  + evaluarFuncion(funcion,puntoInicial+h,0,0)*(-14) + evaluarFuncion(funcion,puntoInicial,0,0)*(3)
        listaResultados.append(numerador1/(h**4))

        #calculamos los errores para la primera y la segunda diferencia
         
        lista_errores = []
        valor_verdadero = evaluarFuncion(funcion,puntoInicial,1,1)

        valor_apro1 = listaResultados[0]
        valor_apro2 = listaResultados[1]
        valor_apro3 = listaResultados[2]

        valor_apro4 = listaResultados[3]
        valor_apro5 = listaResultados[4]
        valor_apro6 = listaResultados[5]

        # <-------------------- primera diferencia ----------------------------->

        #primer error
        listaResultados.append(abs((valor_verdadero-valor_apro1)/valor_verdadero))
        listaResultados.append(listaResultados[6]*100)

        #segundo error 
        listaResultados.append(abs((valor_verdadero-valor_apro2)/valor_verdadero))
        listaResultados.append(listaResultados[8]*100)

        #tercer error 
        listaResultados.append(abs((valor_verdadero-valor_apro3)/valor_verdadero))
        listaResultados.append(listaResultados[10]*100)

         # <-------------------- segunda diferencia ----------------------------->

        #primer error
        listaResultados.append(abs((valor_verdadero-valor_apro1)/valor_verdadero))
        listaResultados.append(listaResultados[12]*100)

        #segundo error 
        listaResultados.append(abs((valor_verdadero-valor_apro2)/valor_verdadero))
        listaResultados.append(listaResultados[14]*100)

        #tercer error 
        listaResultados.append(abs((valor_verdadero-valor_apro3)/valor_verdadero))
        listaResultados.append(listaResultados[16]*100)

        print(listaResultados[0])
        print(listaResultados[1])
        print(listaResultados[2])
        print("\n")
        print(listaResultados[3])
        print(listaResultados[4])
        print(listaResultados[5])
        
    else:
        lista_valores = []
        lista_valores_2 = []
        lista_valores_3 = []
        lista_valores_4 = []
        lista_valores_5 = []
        lista_valores_6 = []
        
        lista_x = tablaValores[0]
        lista_y = tablaValores[1]

        for i in range(0,len(lista_x)):
            if lista_x[i] == puntoInicial:

                # <-------------  valores para primera diferencia ------------------------>
                lista_valores.append(lista_y[i+2])
                lista_valores.append(lista_y[i+1])
                lista_valores.append(lista_y[i])
               
                lista_valores_2.append(lista_y[i+3])
                lista_valores_2.append(lista_y[i+2])
                lista_valores_2.append(lista_y[i+1])
                lista_valores_2.append(lista_y[i])

                lista_valores_3.append(lista_y[i+4])
                lista_valores_3.append(lista_y[i+3])
                lista_valores_3.append(lista_y[i+2])
                lista_valores_3.append(lista_y[i+1])
                lista_valores_3.append(lista_y[i])

                # <--------------- valores para segunda diferencia ------------------------>
                lista_valores_4.append(lista_y[i+3])
                lista_valores_4.append(lista_y[i+2])
                lista_valores_4.append(lista_y[i+1])
                lista_valores_4.append(lista_y[i])

                lista_valores_5.append(lista_y[i+4])
                lista_valores_5.append(lista_y[i+3])
                lista_valores_5.append(lista_y[i+2])
                lista_valores_5.append(lista_y[i+1])
                lista_valores_5.append(lista_y[i])

                lista_valores_6.append(lista_y[i+5])
                lista_valores_6.append(lista_y[i+4])
                lista_valores_6.append(lista_y[i+3])
                lista_valores_6.append(lista_y[i+2])
                lista_valores_3.append(lista_y[i+1])
                lista_valores_3.append(lista_y[i])

        #variables donde guardaremos el numerador
        numerador1 = 0

        # <---------------- Primera diferencia ---------------------->

        numerador1 = lista_valores[0] + lista_valores[1]*(-2) + lista_valores[2]
        listaResultados.append((numerador1)/(h**2))

        numerador1 = lista_valores[0] + lista_valores[1]*(-3) + lista_valores[2]*(3) + lista_valores[3]*(-1) 
        listaResultados.append((numerador1)/(h**3))

        numerador1 = lista_valores[0] + lista_valores[1]*(-4) + lista_valores[2]*(6) + lista_valores[3]*(-4) + lista_valores[4] 
        listaResultados.append((numerador1)/(h**4))

        # <---------------- segunda diferencia ---------------------->

        numerador1 = lista_valores[0]*(-1) + lista_valores[1]*(4) + lista_valores[2]*(-5) + lista_valores[3]*(2)
        listaResultados.append((numerador1)/(h**2))

        numerador1 = lista_valores[0]*(-3) + lista_valores[1]*(14) + lista_valores[2]*(-24) + lista_valores[3]*(18) + lista_valores[4]*(-5)
        listaResultados.append((numerador1)/(h**3))

        numerador1 = lista_valores[0]*(-2) + lista_valores[1]*(11) + lista_valores[2]*(-24) + lista_valores[3]*(26) + lista_valores[4]*(-14) + lista_valores[5]*(3)  
        listaResultados.append((numerador1)/(h**4))

        print(listaResultados)

def diferenicacion_numerica_atras_orden_superior(funcion,puntoInicial,h,tablaValores):
    print("falta")

def diferenicacion_numerica_centrales_orden_superior(funcion,puntoInicial,h,tablaValores):
    print("falta")


# <------------- metodo de richardson --------------------->

def metodo_richardson(funcion,puntoInicial,h,nivel):

    #lista con respuestas
    listResultados = []

    #lista con los valores de h
    valores_h = []

    #llenamos la lista de valores_h soguiendo esta formula h_n = (h_n-1)/2
    for i in range(0,nivel,1):
        if i == 0:
            valores_h.append(h)
        else:
            valores_h.append((valores_h[i-1])/2)

    #lista donde se encontrara el primer nivel 
    primer_nivel = []
    for i in valores_h:
        valor = diferenciacion_numerica_centrada(funcion,puntoInicial,i,[])
        primer_nivel.append(valor[1])


    #lista que ira cambiando de tamaño con respecto al nivel en el que se encuente 
    lista_cambiante = primer_nivel

    #matriz donde estaran los demas niveles
    matriz_con_niveles = [] 
    matriz_con_niveles.append(primer_nivel)
    lista_nivel = []
    contador_nivel = 3

    for i in range(1,nivel,1):
        for j in range(1,len(lista_cambiante)):
            if i == 1:
                primer_termino = (4/3)*lista_cambiante[j]
                segundo_termino = (-1/3)*lista_cambiante[j-1]
                salida = primer_termino + segundo_termino
                lista_nivel.append(salida)
            elif i == 2:
                primer_termino = (16/15)*lista_cambiante[j]
                segundo_termino = (-1/15)*lista_cambiante[j-1]
                salida = primer_termino + segundo_termino
                lista_nivel.append(salida)
            else:
                primer_termino = ((4**contador_nivel)/((4**contador_nivel)-1))*lista_cambiante[j]
                segundo_termino = ((1)/((4**contador_nivel)-1))*lista_cambiante[j-1]
                salida = primer_termino + segundo_termino
                lista_nivel.append(salida)
            

        matriz_con_niveles.append(lista_nivel)
        lista_cambiante = lista_nivel
        lista_nivel = []
        if i >= 3:
            contador_nivel += 1

    listResultados = matriz_con_niveles

    return listResultados

# <------------- Integración numérica --------------------->

def regla_del_trapecio_simple(funcion,a,b,tablaValores): #Diego
    listaResultados = []

    if funcion != '':

        numerador = evaluarFuncion(funcion,a,0,0) + evaluarFuncion(funcion,b,0,0)
        evaluacion = (b-a)*(numerador/2)

        listaResultados.append(evaluacion)

        return listaResultados

    else: #Para cuando trabajamos con puntos y no con funciones 

        tamanio = len(tablaValores[0])
        listaX = tablaValores[0]
        listaY = tablaValores[1]

        if tamanio == 2:
            resultado = (listaX[1]-listaX[0])*((listaY[0]+listaY[1])/2)
            listaResultados.append(resultado)
            print(listaResultados)
            return listaResultados

        else:
            print("Para resolver mediante el trapecio simple solo se utilizan 2 puntos")

def regla_del_trapecio_compuesta(funcion,a,b,n,tablaValores): #Diego
    
    #respuesta
    listaResultados = []

    if funcion != '':

        h = Fraction((b-a),n)
        aa = a

        lista_con_valor_h = []
        lista_evaluaciones = []
        sumatoria_puntos_medios = 0

        for i in range(0,n+1,1):
            lista_con_valor_h.append(aa)
            lista_evaluaciones.append(evaluarFuncion(funcion,lista_con_valor_h[i],0,0))
            if i >= 1 and i <= n-1:
                sumatoria_puntos_medios += lista_evaluaciones[i]

            #Aumentamos el valor de a en h    
            aa += h

        resultado = (b-a)*((lista_evaluaciones[0] + 2*sumatoria_puntos_medios + lista_evaluaciones[n]))/(2*n)

        listaResultados.append(resultado)
        return listaResultados

    else:

        sumatoria_puntos_medios = 0
        listaX = tablaValores[0]
        listaY = tablaValores[1]
        tamanio = len(listaX)-1


        for i in range(0,tamanio+1,1):
            if i >= 1 and i <= tamanio-1:

                sumatoria_puntos_medios += listaY[i]

        resultado = (b-a)*(listaY[0] + 2*sumatoria_puntos_medios + listaY[tamanio])/(2*tamanio)

        listaResultados.append(resultado)
        print(listaResultados)
        return listaResultados

def trapecio_para_dobles_y_triples(funcion,lista_a,lista_b,n,orden_integral):

    #lista con respuestas
    listaResultados = []

    if orden_integral == 2: #integral doble
        a = lista_a[0]
        b = lista_b[0] 
        h = (b-a)/n
        hh = a

        lista_operaciones_de_evaluarX = []
        valores_sumados = 0
        lista_h = []

        for i in range(0,n+1,1):
            lista_h.append(hh)
            hh += h

        for i in range(0,n+1,1):
            resultado = sp.sympify(funcion).subs(x, lista_h[i])
            lista_operaciones_de_evaluarX.append(resultado)
            if i >= 1 and i<= n-1:
                valores_sumados += lista_operaciones_de_evaluarX[i]

        valores_sumados_simplificados = sp.expand(valores_sumados)

        funcion_encontrada = ((b-a)/(2*n))*(lista_operaciones_de_evaluarX[0] + 2*valores_sumados_simplificados + lista_operaciones_de_evaluarX[n])
        print('primera funcion encontrada:  ------------> ',funcion_encontrada)
        funcion_encontrada = sp.expand(funcion_encontrada)

        # Se resuelve la siguiente integral con el polinomio que encontramos 

        a = lista_a[1]
        b = lista_b[1] 
        h = (b-a)/n
        hh = a

        lista_operaciones_de_evaluarX = []
        valores_sumados = 0
        lista_h = []

        for i in range(0,n+1,1):
            lista_h.append(hh)
            hh += h

        for i in range(0,n+1,1):
            resultado = sp.sympify(funcion_encontrada).subs(y, lista_h[i])
            lista_operaciones_de_evaluarX.append(resultado)
            if i >= 1 and i<= n-1:
                valores_sumados += lista_operaciones_de_evaluarX[i]


        resultado = ((b-a)/(2*n))*(lista_operaciones_de_evaluarX[0] + 2*valores_sumados + lista_operaciones_de_evaluarX[n])
        print('valor encontrado:  ------------>', resultado)
        listaResultados.append(resultado)
    
    elif orden_integral == 3: #Integral Triple
        a = lista_a[0]
        b = lista_b[0] 
        h = (b-a)/n
        hh = a

        lista_operaciones_de_evaluarX = []
        valores_sumados = 0
        lista_h = []

        for i in range(0,n+1,1):
            lista_h.append(hh)
            hh += h

        for i in range(0,n+1,1):
            resultado = sp.sympify(funcion).subs(x, lista_h[i])
            lista_operaciones_de_evaluarX.append(resultado)
            if i >= 1 and i<= n-1:
                valores_sumados += lista_operaciones_de_evaluarX[i]

        valores_sumados_simplificados = sp.expand(valores_sumados)

        funcion_encontrada = ((b-a)/(2*n))*(lista_operaciones_de_evaluarX[0] + 2*valores_sumados_simplificados + lista_operaciones_de_evaluarX[n])
        funcion_encontrada = sp.expand(funcion_encontrada)
        
        print('primera funcion encontrada: ------------> ',funcion_encontrada)
        # Se resuelve la siguiente integral con el polinomio que encontramos 

        a = lista_a[1]
        b = lista_b[1] 
        h = (b-a)/n
        hh = a

        lista_operaciones_de_evaluarX = []
        valores_sumados = 0
        lista_h = []

        for i in range(0,n+1,1):
            lista_h.append(hh)
            hh += h

        for i in range(0,n+1,1):
            resultado = sp.sympify(funcion_encontrada).subs(y, lista_h[i])
            lista_operaciones_de_evaluarX.append(resultado)
            if i >= 1 and i<= n-1:
                valores_sumados += lista_operaciones_de_evaluarX[i]
                
        valores_sumados_simplificados = sp.expand(valores_sumados)

        funcion_encontrada_2 = ((b-a)/(2*n))*(lista_operaciones_de_evaluarX[0] + 2*valores_sumados_simplificados + lista_operaciones_de_evaluarX[n])
        funcion_encontrada_2 = sp.expand(funcion_encontrada_2)
        print('segunda funcion encontrada: ------------> ',funcion_encontrada_2)

        # Se resuelve la siguiente integral con el polinomio que encontramos 

        a = lista_a[2]
        b = lista_b[2] 
        h = (b-a)/n
        hh = a

        lista_operaciones_de_evaluarX = []
        valores_sumados = 0
        lista_h = []

        for i in range(0,n+1,1):
            lista_h.append(hh)
            hh += h


        for i in range(0,n+1,1):
            resultado = sp.sympify(funcion_encontrada_2).subs(z, lista_h[i])
            lista_operaciones_de_evaluarX.append(resultado)
            if i >= 1 and i<= n-1:
                valores_sumados += lista_operaciones_de_evaluarX[i]

        resultado = ((b-a)/(2*n))*(lista_operaciones_de_evaluarX[0] + 2*valores_sumados + lista_operaciones_de_evaluarX[n])
        listaResultados.append(resultado)
        print('valor encontrado: ------------> ',resultado)
        return listaResultados

def integracion_simpson_unTercio_simple(): #Milton
    print("falta")
    for i in range(0,10):
        print(i)

def integracion_simpson_unTercio_compuesta(): #Milton
    print("falta")

def integracion_simpson_tresOctavos_simple(): #Milton
    print("falta")

def integracion_simpson_tresOctavos_compuesta(): #Milton
    print("falta")

def integracion_rosemberg(funcion,a,b,nivel): #Diego

    #lista con respuestas
    listaResultados = []

    #lista donde se encontrara el primer nivel 
    primer_nivel = []
    n = 2

    for i in range(0,nivel,1):
        if i == 0:
            valor = regla_del_trapecio_simple(funcion,a,b,[])
            primer_nivel.append((valor[0]).evalf())
        else:
            valor = regla_del_trapecio_compuesta(funcion,a,b,n,[])
            primer_nivel.append(valor[0].evalf())
            n += 2

    #lista que ira cambiando de tamaño con respecto al nivel en el que se encuente 
    lista_cambiante = primer_nivel

    #matriz donde estaran los demas niveles
    matriz_con_niveles = [] 
    matriz_con_niveles.append(primer_nivel)
    lista_nivel = []
    contador_nivel = 3

    for i in range(1,nivel,1):
        for j in range(1,len(lista_cambiante)):
            if i == 1:
                primer_termino = (4/3)*lista_cambiante[j]
                segundo_termino = (-1/3)*lista_cambiante[j-1]
                salida = primer_termino + segundo_termino
                lista_nivel.append(salida)
            elif i == 2:
                primer_termino = (16/15)*lista_cambiante[j]
                segundo_termino = (-1/15)*lista_cambiante[j-1]
                salida = primer_termino + segundo_termino
                lista_nivel.append(salida)
            else:
                primer_termino = ((4**contador_nivel)/((4**contador_nivel)-1))*lista_cambiante[j]
                segundo_termino = ((1)/((4**contador_nivel)-1))*lista_cambiante[j-1]
                salida = primer_termino + segundo_termino
                lista_nivel.append(salida)
            

        matriz_con_niveles.append(lista_nivel)
        lista_cambiante = lista_nivel
        lista_nivel = []
        if i >= 3:
            contador_nivel += 1

    listaResultados = matriz_con_niveles
    for i in listaResultados:
        print(i)

    return listaResultados

def integracion_cuadratura_Gaussiana(funcion,a,b,n): #Diego
    #cada sub-lista va a representar un punto

    lista_Wk = [[2], [1,1], [0.555556,0.888889,0.555556], [0.347855,0.652145,-0.652145,-0.347855], [0.236927,0.478629,0.568889,0.478629,0.236927], [], [], [], [], [], [], []]

    lista_Tk = [[0], [0.57735,-0.57735], [-0.774597,0,0.774597], [-0.861136,-0.339981,0.339981,0.861136], [-0.90618,-0.538469,0,0.538469,0.90618], [], [], [], [], [], [], []]


    lista_variable_Wk = lista_Wk[n-1]
    lista_variable_Tk = lista_Tk[n-1]
    resultado = 0
    punto = 0

    for i in range(0,n,1):
        punto = ((b-a)*lista_variable_Tk[i] + (b+a))/2
        resultado += lista_variable_Wk[i]*evaluarFuncion(funcion,punto,0,0)

    resultado = resultado*(b-a)/2

    print(resultado)
    
def integracion_simpson_unTercio_adaptativo(): #kelvin
    print("falta")

def ultimo():  #kelvin
<<<<<<< HEAD
    print("falta")
=======
    print("me toco a mi")
    print("algo")
>>>>>>> dacc3b3bcf09285796012c61f15fa6068786e0b8
