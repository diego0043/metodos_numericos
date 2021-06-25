import cmath
import math
import sympy as sp
from tabulate import tabulate
from decimal import *
import sympy as sp

x = sp.Symbol('x')
t = sp.Symbol('t')
e = sp.Symbol('e')
y = sp.Symbol('y')
z = sp.Symbol('z')


def calcularEa(xr, xrAnterior):
    resultado = (abs(xr-xrAnterior)/xr)*100
    if resultado < 0:
        resultado = resultado*-1
    return resultado


def metodo1(punto, cifras):
    listaResultados = []
    salida = 0
    valorAnterior = 0
    iteracion = 0
    valor = 0.0
    es = (10**(2-cifras))/2
    ea = 0
    signo = -1

    # cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea', 'Es']
    listaResultados.append(header)

    while salida == 0:

        if iteracion == 0:
            valor = 1
            valorAnterior = valor

            listaResultados.append([iteracion+1, valor, "N/A", es])

            iteracion += 1

        else:
            numerador = punto**(iteracion)
            denominador = iteracion*math.e**(iteracion)

            if iteracion >= 2:
                valor = valor + (numerador/denominador)*(signo)
                signo = signo*-1
            else:
                valor = valor + (numerador/denominador)

            ea = calcularEa(valor, valorAnterior)

            listaResultados.append(
                [iteracion+1, valor, ea, es])

            valorAnterior = valor

            iteracion += 1

            if ea <= es:
                salida = 1

    return listaResultados


def metodo2(punto, cifras):
    listaResultados = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 2

    # cabezera de tabla
    header = ['ITERACIÓN', 'VALOR', 'Ea', 'Es']
    listaResultados.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            # Primera iteracion
            listaResultados.append([iteracion, 1, 'N/A', es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**(2*exponente))/math.factorial(exponente)
            ea = calcularEa(valor, valorAnterior)

            # agremamos las iteraciones
            listaResultados.append([iteracion, valor, ea, es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1

    return listaResultados


def metodo3(punto, cifras):
    listaResultados = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 3

    # cabezera de tabla
    header = ['ITERACIÓN', 'VALOR', 'Ea', 'Es']
    listaResultados.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = punto

            # Primera iteracion
            listaResultados.append([iteracion, valor, 'N/A', es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += ((-1**exponente)/math.factorial((2*exponente)+1)
                      )*punto**((2*exponente)+1)
            ea = calcularEa(valor, valorAnterior)

            # agremamos las iteraciones
            listaResultados.append([iteracion, valor, ea, es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1

    return listaResultados


def metodo4(punto, cifras):
    listaResultados = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 2

    # cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea', 'Es']
    listaResultados.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            # Primera iteracion
            listaResultados.append([iteracion, valor, 'N/A', es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += ((-1**exponente)/math.factorial(2*exponente)) * \
                punto**(2*exponente)
            ea = calcularEa(valor, valorAnterior)

            # agremamos las iteraciones
            listaResultados.append([iteracion, valor, ea, es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1

    return listaResultados


def metodo5(punto, cifras):
    listaResultados = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 1

    # cabezera de tabla
    header = ['ITERACIÓN', 'VALOR', 'Ea', 'Es']
    listaResultados.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            # Primera iteracion
            listaResultados.append([iteracion, valor, 'N/A', es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**exponente)/math.factorial(exponente)
            ea = calcularEa(valor, valorAnterior)

            # agremamos las iteraciones
            listaResultados.append([iteracion, valor, ea, es])

            valorAnterior = valor
            iteracion += 1
            exponente += 1

            if ea <= es:
                salida = 1

    return listaResultados


def metodo6(punto, cifras):
    listaResultados = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 3

    # cabezera de tabla
    header = ['ITERACIÓN', 'VALOR', 'Ea', 'Es']
    listaResultados.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = punto

            # Primera iteracion
            listaResultados.append([iteracion, valor, 'N/A', es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**exponente)/math.factorial(exponente)
            ea = calcularEa(valor, valorAnterior)

            # agremamos las iteraciones
            listaResultados.append([iteracion, valor, ea, es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1

    return listaResultados


def metodo7(punto, cifras):
    listaResultados = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 2

    # cabezera de tabla
    header = ['ITERACIÓN', 'VALOR', 'Ea', 'Es']
    listaResultados.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            # Primera iteracion
            listaResultados.append([iteracion, valor, 'N/A', es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**exponente)/math.factorial(exponente)
            ea = calcularEa(valor, valorAnterior)

            # agremamos las iteraciones
            listaResultados.append([iteracion, valor, ea, es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1

    return listaResultados


def metodo8(punto, cifras):
    listaResultados = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 3

    # cabezera de tabla
    header = ['ITERACIÓN', 'VALOR', 'Ea', 'Es']
    listaResultados.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = punto

            # Primera iteracion
            listaResultados.append([iteracion, valor, 'N/A', es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += ((math.factorial(2*exponente))/(2**exponente *
                      math.factorial(exponente))**2)*((punto**(2*exponente)+1)/(2*exponente)+1)
            ea = calcularEa(valor, valorAnterior)

            # agremamos las iteraciones
            listaResultados.append([iteracion, valor, ea, es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1

    return listaResultados


def metodo9(punto, cifras):
    listaResultados = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 2

    # cabezera de tabla
    header = ['ITERACIÓN', 'VALOR', 'Ea', 'Es']
    listaResultados.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = punto

            # Primera iteracion
            listaResultados.append([iteracion, valor, 'N/A', es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += ((-1**(exponente-1))/exponente)*(punto**exponente)
            ea = calcularEa(valor, valorAnterior)

            # agremamos las iteraciones
            listaResultados.append([iteracion, valor, ea, es])
            valorAnterior = valor
            iteracion += 1
            exponente += 1

            if ea <= es:
                salida = 1

    return listaResultados


def metodo10(punto, cifras):
    listaResultados = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 2

    # cabezera de tabla
    header = ['ITERACIÓN', 'VALOR', 'Ea', 'Es']
    listaResultados.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            # Primera iteracion
            listaResultados.append([iteracion, valor, 'N/A', es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += ((-1**exponente)*punto**(2*exponente))
            ea = calcularEa(valor, valorAnterior)

            # agremamos las iteraciones
            listaResultados.append([iteracion, valor, ea, es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1

    return listaResultados


def metodo11(punto, cifras):
    listaResultados = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 3

    # cabezera de tabla
    header = ['ITERACIÓN', 'VALOR', 'Ea', 'Es']
    listaResultados.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = punto

            # Primera iteracion
            listaResultados.append([iteracion, valor, 'N/A', es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += ((-1**exponente)*punto**((2*exponente)+1)/(2*exponente)+1)
            ea = calcularEa(valor, valorAnterior)

            # agremamos las iteraciones
            listaResultados.append([iteracion, valor, ea, es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1

    return listaResultados
