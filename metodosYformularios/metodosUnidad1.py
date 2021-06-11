import cmath
import math 
import sympy as sp
from tabulate import tabulate


def calcularEa(xr, xrAnterior):
    resultado = (abs(xr-xrAnterior)/xr)*100
    if resultado < 0:
        resultado = resultado*-1
    return resultado

def metodo5(punto,cifras):
    listaResultados = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 1

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    listaResultados.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            #Primera iteracion 
            listaResultados.append([iteracion,1,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**exponente)/math.factorial(exponente)
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            listaResultados.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 1

            if ea <= es:
                salida = 1
            

    return listaResultados

def metodo6(punto,cifras):
    listaResultados = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 3

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    listaResultados.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = punto

            #Primera iteracion 
            listaResultados.append([iteracion,valor,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**exponente)/math.factorial(exponente)
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            listaResultados.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1
            

    return listaResultados

def metodo7(punto,cifras):
    listaResultados = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 2

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    listaResultados.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            #Primera iteracion 
            listaResultados.append([iteracion,valor,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**exponente)/math.factorial(exponente)
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            listaResultados.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1
            

    return listaResultados

def metodo7(punto,cifras):
    listaResultados = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 2

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    listaResultados.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            #Primera iteracion 
            listaResultados.append([iteracion,valor,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**exponente)/math.factorial(exponente)
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            listaResultados.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1
            

    return listaResultados

salida = metodo7(4,3) 
print(tabulate(salida,tablefmt="github",colalign=("center",)))




   