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


x = sp.Symbol('x')
e = sp.Symbol('e')

#Función para validar que los valores inicales de algunas funciones sean numeros
def pedirValoresIniciales(x):
    bandera = 0
    try:
        salida = float(x)
        bandera = 1
    except:
        bandera = 0
    if bandera == 1:
        return salida
    else:
        return "falsisimo"

#Esta funcion nos devuelve una lista de raices para el metodo de bairstow
def ordenPolinomio(x,lista):
    listaResultados = []
    if x == 3:
        raicesFaltantes = factorizar(0, 0, lista[0], lista[1], lista[2])
        listaResultados.append(raicesFaltantes[0])
        listaResultados.append(raicesFaltantes[1])

                #Si es una funcion cubica
    elif x == 4:
        raicesFaltantes = factorizar(0,lista[0], lista[1], lista[2], lista[3])
        listaResultados.append(raicesFaltantes[0])
        listaResultados.append(raicesFaltantes[1])
        listaResultados.append(raicesFaltantes[2])

                #Si es una funcion cuadratica o bicuadrada
    elif x == 5:
        raicesFaltantes = factorizar(lista[0], lista[1], lista[2], lista[3], lista[4])
        listaResultados.append(raicesFaltantes[0])
        listaResultados.append(raicesFaltantes[1])
        listaResultados.append(raicesFaltantes[2])
        listaResultados.append(raicesFaltantes[3])

    return listaResultados

#De momento ya no la estamos usando
def pedirFuncion(tipoEvaluacion, funcion):
    bandera = 0
    while bandera == 0:
        y = ""
        fx = ""
        try:
            if tipoEvaluacion == 1:
                fx = eval(funcion)
                bandera = 1
            else:
                y = funcion
                y = "x+"+y
                fx = eval(y)
                bandera = 1
        except:
            bandera = 0
        if bandera == 1:
            return fx
        else:
            return False

#Valida que las cifras significativas sea un numero entero
def pedirCifrasSignificativas(cifras):
    bandera = 0
    while bandera == 0:
        try:
            cifras = int(cifras)
            bandera = 1
        except:
            bandera = 0
        if bandera == 1:
            return cifras
        else:
            return "falsisimo"

#Esta funcion nos evalua una funcion en un valor ya sea que haya que derivar o no
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

#Calculamos el error Ea
def calcularEa(xr, xrAnterior):
    resultado = (abs(xr-xrAnterior)/xr)*100
    if resultado < 0:
        resultado = resultado*-1
    return resultado

#Esta metodo nos va a devolver los coeficientes de un polinomio 
def coefs(entrada):
    regexp = r"(-?\d*)(x?)(?:(?:\^|\*\*)(\d))?"
    c = {}
    for coef, x, exp in re.findall(regexp, entrada):
        # print(coef, x, exp)
        if not coef and not x:
            continue
        if x and not coef:
            coef = '1'
        if x and coef == "-":
            coef = "-1"
        if x and not exp:
            exp = '1'
        if coef and not x:
            exp = '0'
        exp = ord(exp) & 0x000F
        c[exp] = float(coef)
    grado = max(c)
    coeficientes = [0.0] * (grado+1)
    for g, v in c.items():
        coeficientes[g] = v
    return coeficientes

#Metodo de matriz crammer
def despejarEcuaciones(valor1,valor2,valor3,valor4,valor5,valor6):
    #determinante total del sistema
    D = (valor1*valor5)-(valor4*valor2)

    #determinante de X
    Dx = (valor3*valor5)-(valor6*valor2)

    #determinante de Y
    Dy = (valor1*valor6)-(valor4*valor3)

    x1 = Dx/D #Primer Valor
    x2 = Dy/D #Segundo Valor

    lista = [x1,x2]

    return lista
  
#Hacemos 2 divisiones sinteticas para bairstow
def divisionSinteticaBairstown(coeficientes,a,b):

    #En estas listas guardaremos los resultados al efectuar la division sintetica 
    primerosResultados = []
    segundosResultados = []

    #Numero de coeficientes del polinomio que viene desde bairstown
    numeroVariables = len(coeficientes)
    

    #Primera division 
    for i in range(0,numeroVariables-1):
        if i == 0:
            primerosResultados.append(coeficientes[i])
        else:
            primerosResultados.append((primerosResultados[i-1]*a)+coeficientes[i])

    #Segunda division
    for i in range(0,numeroVariables-2):
        if i == 0:
            segundosResultados.append(primerosResultados[i])
        else:
            segundosResultados.append((segundosResultados[i-1]*b)+primerosResultados[i])

    #La segunda lista es la que nos interesa 
    
    return segundosResultados

def MetRaiz(radicando, indice):
    salida = float((radicando)**(1/indice))
    return salida

def metodoBiseccion(x1, x2, func, cifr):
    print(x1,x2)
    funcion = func
    cifSig = cifr
    es = (10**(2-cifSig))/2
    ea = 0
    listaResultados = []
    listaResultados.append(
        ["Iteracion", "X1", "X2", "Xr", "F(x1)", "F(x2)", "F(x1)*F(Xr)", "Ea"])
    valorAnterior = 0
    salida = 0
    contador = 0
    iteracion = 1

    while salida == 0:
        if contador == 0:
            contador = 1
            xr = (x1 + x2) / 2
            fx1 = evaluarFuncion(funcion, x1, 0, 0)
            fxr = evaluarFuncion(funcion, xr, 0, 0)
            fx1Porfxr = fx1 * fxr
            if fx1Porfxr == 0:
                listaResultados.append(
                    [iteracion, x1, x2, xr, fx1, fxr, fx1Porfxr, ea])
                salida = 1
            else:
                if fx1Porfxr < 0:
                    listaResultados.append(
                        [iteracion, x1, x2, xr, fx1, fxr, fx1Porfxr, ea])
                    x2 = xr
                    valorAnterior = xr
                else:
                    listaResultados.append(
                        [iteracion, x1, x2, xr, fx1, fxr, fx1Porfxr, ea])
                    x1 = xr
                    valorAnterior = xr
        else:
            iteracion += 1
            xr = (x1 + x2) / 2
            fx1 = evaluarFuncion(funcion, x1, 0, 0)
            fxr = evaluarFuncion(funcion, xr, 0, 0)
            fx1Porfxr = fx1 * fxr
            ea = calcularEa(xr, valorAnterior)
            if ea < es:
                listaResultados.append(
                    [iteracion, x1, x2, xr, fx1, fxr, fx1Porfxr, ea])
                salida = 1
            else:
                if fx1Porfxr == 0:
                    listaResultados.append(
                        [iteracion, x1, x2, xr, fx1, fxr, fx1Porfxr, ea])
                    salida = 1
                else:
                    if fx1Porfxr < 0:
                        listaResultados.append(
                            [iteracion, x1, x2, xr, fx1, fxr, fx1Porfxr, ea])
                        x2 = xr
                        valorAnterior = xr
                    else:
                        listaResultados.append(
                            [iteracion, x1, x2, xr, fx1, fxr, fx1Porfxr, ea])
                        x1 = xr
                        valorAnterior = xr

    return listaResultados

def metodoFalsaPosicion(x1, x2, func, cifr):
    funcion = func
    cifSig = cifr
    es = (10 ** (2 - cifSig)) / 2
    ea = 0
    listaResultados = []
    listaResultados.append(
        ["Iteracion", "X1", "X2", "F(x1)", "F(x2)", "Xr", "F(xr)", "F(x1)*F(Xr)", "Ea"])
    valorAnterior = 0
    salida = 0
    contador = 0
    iteracion = 1

    while salida == 0:
        if contador == 0:
            contador += 1
            fx1 = evaluarFuncion(funcion, x1, 0, 0)
            fx2 = evaluarFuncion(funcion, x2, 0, 0)
            xr = x1-(fx1*(x1-x2)/(fx1-fx2))
            fxr = evaluarFuncion(funcion, xr, 0, 0)
            fx1Porfxr = fx1*fxr
            if fx1Porfxr == 0:
                listaResultados.append(
                    [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                salida = 1
            else:
                if fx1Porfxr > 0:
                    listaResultados.append(
                        [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                    valorAnterior = xr
                    x1 = xr
                else:
                    listaResultados.append(
                        [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                    valorAnterior = xr
                    x2 = xr
        else:
            iteracion += 1
            fx1 = evaluarFuncion(funcion, x1, 0, 0)
            fx2 = evaluarFuncion(funcion, x2, 0, 0)
            xr = x1 - (fx1 * (x1 - x2) / (fx1 - fx2))
            fxr = evaluarFuncion(funcion, xr, 0, 0)
            fx1Porfxr = fx1 * fxr
            ea = calcularEa(xr, valorAnterior)
            if ea <= es:
                listaResultados.append(
                    [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                salida = 1
            else:
                if fx1Porfxr == 0:
                    listaResultados.append(
                        [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                    salida = 1
                else:
                    if fx1Porfxr > 0:
                        listaResultados.append(
                            [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                        valorAnterior = xr
                        x1 = xr
                    else:
                        listaResultados.append(
                            [iteracion, x1, x2, fx1, fx2, xr, fxr, fx1Porfxr, ea])
                        valorAnterior = xr
                        x2 = xr

    return listaResultados

def metodoPuntoFijo(x1, func, cif):
    funcion = func
    converge = evaluarFuncion(funcion, x1, 1, 1)
    converge = abs(converge)
    listaResultados = []
    listaResultados.append(["Iteracion", "X1", "g(x)", "Ea"])

    if converge < 1:
        cifSig = cif
        es = (10 ** (2 - cifSig)) / 2
        ea = 0
        salida = 0
        iteracion = 1

        while salida == 0:
            gx = evaluarFuncion(funcion, x1, 0, 1)
            if gx == 0:
                print("Surgio un problema : \n La funcion g(x) no puede ser cero")
                salida = 1
            else:
                ea = calcularEa(gx, x1)
                if ea < es:
                    listaResultados.append([iteracion, x1, gx, ea])
                    salida = 1
                else:
                    listaResultados.append([iteracion, x1, gx, ea])
                    x1 = gx
            iteracion += 1
    else:
        return listaResultados

    return listaResultados

def metodoNewtonRaphson(x1, func, cif):
    funcion = func
    valorFx = evaluarFuncion(funcion, x1, 0, 1)
    valorFxPrima = evaluarFuncion(funcion, x1, 1, 1)
    valorFxPrimaSegunda = evaluarFuncion(funcion, x1, 1, 2)

    listaResultados = []
    listaResultados.append(
        ["Iteracion", "Xn", "F(Xn)", "F´(Xn)", "Xn+1", "Ea"])

    convergencia = sp.simplify(
        abs((valorFx*valorFxPrimaSegunda)/(valorFxPrima)**2))
    print(convergencia)
    if (convergencia > 0 and convergencia < 1):
        cifrasSig = cif
        es = (10**(2-cifrasSig))/2

        iteracion = 1
        salida = 0
        XnMasUno = 0
        Xn = x1
        ea = 0

        while salida == 0:
            valorFx = sp.simplify(evaluarFuncion(funcion, Xn, 0, 0))
            valorFxPrima = sp.simplify(evaluarFuncion(funcion, Xn, 1, 1))
            XnMasUno = Xn - (valorFx/valorFxPrima)
            ea = sp.simplify(calcularEa(XnMasUno, Xn))
            if ea < es:
                listaResultados.append(
                    [iteracion, Xn, valorFx, valorFxPrima, XnMasUno, ea])
                salida = 1
            else:
                listaResultados.append(
                    [iteracion, Xn, valorFx, valorFxPrima, XnMasUno, ea])
                iteracion += 1
                Xn = XnMasUno

        return listaResultados

    else:
        return listaResultados

def metodoNewtonRaphsonMejorado(x1, func, cif):
    funcion = func
    valorFx = evaluarFuncion(funcion, x1, 0, 1)
    valorFxPrima = evaluarFuncion(funcion, x1, 1, 1)
    valorFxPrimaSegunda = sp.simplify(evaluarFuncion(funcion, x1, 1, 2))

    listaResultados = []
    listaResultados.append(
        ["Iteracion", "Xn", "F(Xn)", "F´(Xn)", "Xn+1", "Xn+1", "Ea"])

    convergencia = sp.simplify(
        abs((valorFx*valorFxPrimaSegunda)/(valorFxPrima)**2))
    print(convergencia)
    if (convergencia > 0 and convergencia < 1):
        cifrasSig = cif
        es = (10**(2-cifrasSig))/2
        iteracion = 1
        salida = 0
        XnMasUno = 0
        Xn = x1
        ea = 0

        while salida == 0:
            valorFx = sp.simplify(evaluarFuncion(funcion, Xn, 0, 0))
            valorFxPrima = sp.simplify(evaluarFuncion(funcion, Xn, 1, 1))
            valorFxPrimaSegunda = sp.simplify(
                evaluarFuncion(funcion, Xn, 1, 2))
            XnMasUno = Xn - ((valorFx*valorFxPrima) /
                             ((valorFxPrima**2)-(valorFx*valorFxPrimaSegunda)))
            ea = sp.simplify(calcularEa(XnMasUno, Xn))
            print(ea)
            if ea < es:
                listaResultados.append(
                    [iteracion, Xn, valorFx, valorFxPrima, valorFxPrimaSegunda, XnMasUno, ea])
                salida = 1
            else:
                listaResultados.append(
                    [iteracion, Xn, valorFx, valorFxPrima, valorFxPrimaSegunda, XnMasUno, ea])
                iteracion += 1
                Xn = XnMasUno

        return listaResultados

    else:
        return listaResultados

def metodoSecante(x1, x2, func, cif):
    funcion = func
    cifSig = cif
    es = (10 ** (2 - cifSig)) / 2
    ea = 0
    listaResultados = []
    listaResultados.append(
        ["Iteracion", "Xn-1", "Xn", "F(Xn-1)", "F(Xn)", "Xn+1", "Ea"])
    valorAnterior = 0
    salida = 0
    contador = 0
    iteracion = 1
    NmasUno = 0
    valorFuncionNmenosUno = 0
    valorFuncionN = 0

    existeRaiz = evaluarFuncion(funcion, x1, 0, 0) * \
        evaluarFuncion(funcion, x2, 0, 0)
    if existeRaiz < 0:
        while salida == 0:
            if contador == 0:
                valorFuncionNmenosUno = sp.simplify(
                    evaluarFuncion(funcion, x1, 0, 0))
                valorFuncionN = sp.simplify(evaluarFuncion(funcion, x2, 0, 0))
                numerador = valorFuncionN*(x2-x1)
                denominador = valorFuncionN-valorFuncionNmenosUno
                NmasUno = x2-numerador/denominador
                listaResultados.append(
                    [iteracion, x1, x2, valorFuncionNmenosUno, valorFuncionN, NmasUno, ea])
                contador = 1
                x1 = x2
                x2 = NmasUno
                valorAnterior = NmasUno
            else:
                iteracion += 1
                valorFuncionNmenosUno = evaluarFuncion(funcion, x1, 0, 0)
                valorFuncionN = evaluarFuncion(funcion, x2, 0, 0)
                numerador = valorFuncionN*(x2-x1)
                denominador = valorFuncionN-valorFuncionNmenosUno
                NmasUno = x2-numerador/denominador
                ea = calcularEa(NmasUno, valorAnterior)
                if ea < es:
                    listaResultados.append(
                        [iteracion, x1, x2, valorFuncionNmenosUno, valorFuncionN, NmasUno, ea])
                    salida = 1
                else:
                    listaResultados.append(
                        [iteracion, x1, x2, valorFuncionNmenosUno, valorFuncionN, NmasUno, ea])
                    x1 = x2
                    x2 = NmasUno
                    valorAnterior = NmasUno

        return listaResultados
    else:
        return listaResultados

def factorizacionSimple(a, b):
    listaResultados = []
    raiz = (-1*b)/a
    listaResultados.append(["Raiz:", raiz])
    return listaResultados

def factorizarCuadratica(a, b, c):
    dd = b**2-4*a*c

    listaResultados = []

    if dd == 0:  # solo una raiz
        raiz = -b/2*a
        listaResultados.append(raiz)
    elif dd > 0:  # dos raices
        signo = 1
        for i in range(0, 2):
            numerador = -b+(MetRaiz(dd, 2))*signo
            denominador = 2*a
            raiz = numerador/denominador
            listaResultados.append(raiz)
            signo = -1
    elif dd < 0:  # dos raices imaginarias
        signo = 1
        for i in range(0, 2):
            if dd < 0:
                if signo == 1:
                    primerTermino = -b/2*a
                    segundoTermino = (MetRaiz((dd*-1), 2))/2*a
                    salida = segundoTermino**2
                    segundoTerminoB = "%.2f" % float(salida)
                    raiz = str(primerTermino)+"+i√"+str(segundoTerminoB)
                    listaResultados.append(raiz)
                else:
                    primerTermino = -b/2*a
                    segundoTermino = (MetRaiz((dd*-1), 2))/2*a
                    salida = segundoTermino**2
                    segundoTerminoB = "%.2f" % float(salida)
                    raiz = str(primerTermino)+"-i√"+str(segundoTerminoB)
                    listaResultados.append(raiz)
                signo = -1

    return listaResultados

def factorizarBicuadradas(a, b, c):
    aa = float(a)
    bb = float(b)
    cc = float(c)

    dd = (bb**2)-4*aa*cc

    listaResultados = []
    signo = 1

    if dd == 0.0:  # tenemos 2 raices que salen de una raiz
        for i in range(0, 2):
            raizNormal = -bb/2*aa
            if raizNormal < 0:
                raizNueva = (MetRaiz((raizNormal*-1), 2))*signo
                raizSalida = "%.2f" % float(raizNueva)
                salidaRaiz = "i "+str(raizSalida)
            listaResultados.append(salidaRaiz)
            signo = -1

            # <------------------------------------------------------>
            # tendremos 4 raices las cuales derrivan de 2 raices al aplicar la formula cuadratica

    elif dd > 0.0:
        raices = []
        signo = 1
        listaResultados = []

        # En este primer for calculamos las 2 raices iniciales:

        for i in range(0, 2):
            numerador = -bb+(dd**0.5)*signo
            denominador = 2*aa
            raiz = numerador/denominador
            if raiz < 0:
                raiz = raiz*-1
                raizSalida = "%.2f" % float(raiz)
                raices.append(raizSalida)
            else:
                raizSalida = "%.2f" % float(raiz)
                raices.append(raizSalida)

            signo = -1

        # Aqui calculamos las 4 resultantes :
        signo = 1

        for i in range(1, 5):
            if i < 3:
                if signo == 1:
                    raiz = raices[0]
                    raizNueva = "i√"+str(raiz)
                    listaResultados.append(raizNueva)
                else:
                    raiz = raices[0]
                    raizNueva = "-i√"+str(raiz)
                    listaResultados.append(raizNueva)
                signo = signo*-1
            else:
                if signo == 1:
                    raiz = raices[1]
                    raizNueva = "i√"+str(raiz)
                    listaResultados.append(raizNueva)
                else:
                    raiz = raices[1]
                    raizNueva = "-i√"+str(raiz)
                    listaResultados.append(raizNueva)
                signo = signo*-1

        return listaResultados  # Hasta aqui todo funciona perfecto

        # <--------------------------------------------------------------------------->

        # Tendremos 4 raices que seran imaginarias al cuadrado por asi decirlo
    elif dd < 0.0:
        raices = []
        signo = 1
        listaResultados = []

        # En este primer for calculamos las 2 raices iniciales:

        for i in range(0, 2):
            if dd < 0:
                if signo == 1:
                    primerTermino = -bb/2*aa
                    segundoTermino = (dd*-1)
                    segundoTerminoSalida = "%.2f" % float(segundoTermino)
                    raiz = str(primerTermino) + \
                        "+i√("+str(segundoTerminoSalida)+") / "+str(2*aa)
                    raices.append(raiz)
                else:
                    primerTermino = -bb/2*aa
                    segundoTermino = (dd*-1)
                    segundoTerminoSalida = "%.2f" % float(segundoTermino)
                    raiz = str(primerTermino) + \
                        "-i√("+str(segundoTerminoSalida)+") / "+str(2*aa)
                    raices.append(raiz)
                signo = -1

         # Aqui calculamos las 4 resultantes :
        signo = 1

        for i in range(1, 5):
            if i < 3:
                if signo == 1:
                    raiz = raices[0]
                    raizNueva = "i√("+str(raiz)+")"
                    listaResultados.append(raizNueva)
                else:
                    raiz = raices[0]
                    raizNueva = "-i√("+str(raiz)+")"
                    listaResultados.append(raizNueva)
                signo = signo*-1
            else:
                if signo == 1:
                    raiz = raices[1]
                    raizNueva = "i√("+str(raiz)+")"
                    listaResultados.append(raizNueva)
                else:
                    raiz = raices[1]
                    raizNueva = "-i√("+str(raiz)+")"
                    listaResultados.append(raizNueva)
                signo = signo*-1

        return listaResultados

def factorizarCubicas(a, b, c, soloReal):

    listaResultados = []

    p = ((3*b)-(a**2))/3
    q = (2*(a**3)-(9*a*b)+(27*c))/27

    descriminante = ((q/2)**2)+((p/3)**3)

    if(descriminante == 0):
        if(p == 0 and q == 0):
            x1 = "%.2f" % float(-a/3)
            if soloReal == 1:
                listaResultados.append(x1)
            else:
                listaResultados.append(x1)
                listaResultados.append(x1)
                listaResultados.append(x1)
        elif((p*q) != 0):
            x1 = "%.2f" % float((-(3*q)/(2*p))-(a/3))
            x2 = "%.2f" % float((((-4*(p**2))/9*q)-(a/3)))
            if soloReal == 1:
                listaResultados.append(x1)
            else:
                listaResultados.append(x1)
                listaResultados.append(x1)
                listaResultados.append(x2)

    if(descriminante > 0):
        x01 = ((-q/2+(descriminante)**(0.5)))
        x02 = ((-q/2-(descriminante)**(0.5)))

        if x01 < 0:
            x01 = (x01*-1)**(1/3)*(-1)
        else:
            x01 = x01**(1/3)

        if x02 < 0:
            x02 = (x02*-1)**(1/3)*(-1)
        else:
            x02 = x02**(1/3)

        x1 = "%.5f" % float(x01+x02-(a/3))

        # solo devolvemos la raiz real para el metodo de factorizar cuarticas
        if soloReal == 1:
            listaResultados.append(x1)
        else:
            u = (-q/2)+((descriminante)**(0.5))
            v = (-q/2)-((descriminante)**(0.5))

            if u < 0:
                u = (u*-1)**(1/3)*(-1)
            else:
                u = u**(1/3)

            if v < 0:
                v = (v*-1)**(1/3)*(-1)
            else:
                v = v**(1/3)

            x2 = str("%.5f" % float((-((u+v)/2)-(a/3))))+"+" + \
                str("%.5f" % float((((3**0.5)/2)*((u-v)))))+" i"
            x3 = str("%.5f" % float((-((u+v)/2)-(a/3))))+"-" + \
                str("%.5f" % float((((3**0.5)/2)*((u-v)))))+" i"

            listaResultados.append(x1)
            listaResultados.append(x2)
            listaResultados.append(x3)

    if(descriminante < 0):

        teta = math.acos((-q/2)/(-(p/3)**3)**(1/2))
        x1 = 2*((-p/3)**(1/2))*math.cos((teta+2*0*math.pi)/3)-(a/3)
        x2 = 2*((-p/3)**(1/2))*math.cos((teta+2*1*math.pi)/3)-(a/3)
        x3 = 2*((-p/3)**(1/2))*math.cos((teta+2*2*math.pi)/3)-(a/3)

        if soloReal == 1:
            listaResultados.append(x1)
        else:
            listaResultados.append(x1)
            listaResultados.append(x2)
            listaResultados.append(x3)

    return listaResultados

def factorizarCuarticas(a, b, c, d):
    listaResultados = []
    p = ((8*b)-(3*a**2))/8
    q = ((8*c)-(4*a*b)+a**3)/8
    r = ((256*d)-(64*a*c)+(16*(a**2)*b)-(3*a**4))/256

    # Ahora vamos a resolver la ecuacion cubica : U^3-(p/2)*U^2-R*U + (4pR-Q^2)/8 = 0
    #       (p/2) = aa
    #           R = bb
    # (4pR-Q^2)/8 = cc

    aa = -p/2
    bb = -r
    cc = ((4*p*r)-q**2)/8

    u = factorizarCubicas(aa, bb, cc, 1)
    uu = float(u[0])

    v = ((2*uu)-p)**0.5
    w = (q)/(-2*v)

    # primero calcularemos si no nos dara imaginarias o si

    primerTermino = v**2-4*(uu-w)
    segundoTermino = v**2-4*(uu+w)

    if primerTermino < 0:
        primerTermino = primerTermino*-1
        x1 = str(v/2-a/4)+"+(i√"+str(primerTermino)+") /2"
        x2 = str(v/2-a/4)+"-(i√"+str(primerTermino)+") /2"
    else:
        x1 = (((v/2)+(primerTermino**0.5)/2))-(a/4)
        x1 = "%.2f" % float(x1)
        x2 = (((v/2)-(primerTermino**0.5)/2))-(a/4)
        x2 = "%.2f" % float(x2)

    if segundoTermino < 0:
        segundoTermino = segundoTermino*-1
        x3 = str(-v/2-a/4)+"+(i√"+str(primerTermino)+") /2"
        x4 = str(-v/2-a/4)+"-(i√"+str(primerTermino)+") /2"
    else:
        x3 = (((-v/2)+(segundoTermino**0.5)/2))-(a/4)
        x3 = "%.2f" % float(x3)
        x4 = (((-v/2)-(segundoTermino**0.5)/2))-(a/4)
        x4 = "%.2f" % float(x4)

    listaResultados.append(x1)
    listaResultados.append(x2)
    listaResultados.append(x3)
    listaResultados.append(x4)

    return listaResultados

def factorizar(a, b, c, d, e):
    aa = float(a)  # Cuartas
    bb = float(b)  # Cubicas
    cc = float(c)  # Cuadrada
    dd = float(d)  # Normal
    ee = float(e)  # Independiente

    if aa == 0.0 and bb == 0.0 and cc == 0.0:
        factorizacionSimple(dd, ee)
    elif aa == 0.0 and bb == 0.0:
        listaResultado = factorizarCuadratica(cc, dd, ee)
    elif bb == 0.0 and dd == 0.0:
        if a != 1:
            nuevoB = cc/aa
            nuevoC = ee/aa
            listaResultado = factorizarBicuadradas(1, nuevoB, nuevoC)
        else:
            listaResultado = factorizarBicuadradas(aa, cc, ee)

    elif aa == 0.0:
        if a != 1:
            nuevoA = cc/bb
            nuevoB = dd/bb
            nuevoC = ee/bb
            listaResultado = factorizarCubicas(nuevoA, nuevoB, nuevoC, 0)
        else:
            listaResultado = factorizarCubicas(cc, dd, ee, 0)
    else:
        if a != 0.0:
            nuevoA = bb/aa
            nuevoB = cc/aa
            nuevoC = dd/aa
            nuevoD = ee/aa
            listaResultado = factorizarCuarticas(
                nuevoA, nuevoB, nuevoC, nuevoD)
        else:
            listaResultado = factorizarCuarticas(bb, cc, dd, ee)
    return listaResultado

def metodoHorner(lista, valorInicial, cifrasSignificativas):
    listaResultados = []  # Lista de valores a mostrar en la lista que mira el usuario
    header = ["Iteracion", "Xi", "Xi+1", "R", "S", "Ea"]
    listaResultados.append(header)
    lista.reverse()
    # La lista de coeficientes se mueve a otra lista de nombre mas claro
    listaCoeficientes = lista
    numeroMultiplicaciones = len(listaCoeficientes)
    iteracion = 0
    salida = 0
    es = 0.5*(10**(2-cifrasSignificativas))
    ea = 0
    valorAnterior = 0
    valorProximo = float(valorInicial)
    listaConResultados = []  # Lista donde se guardara el resultado de la division sintetica
    listaConResultados2 = []
    R = 0
    S = 0

    # <-----------Luego comenzamos a efectuar las divisiones sinteticas-------->

    while salida == 0:
        iteracion += 1
        listaConResultados.clear()
        listaConResultados2.clear()
        listaConResultados.append(listaCoeficientes[0])

        for i in range(1, numeroMultiplicaciones):  # Primera division sintetica
            listaConResultados.append(
                (listaConResultados[i-1] * valorProximo) + listaCoeficientes[i])
        R = "%.5f" % float(listaConResultados[len(listaConResultados)-1])

        listaConResultados2.append(listaCoeficientes[0])
        for i in range(1, numeroMultiplicaciones-1):  # Segunda division sintetica
            listaConResultados2.append(
                (listaConResultados2[i-1] * valorProximo) + listaConResultados[i])
        S = "%.5f" % float(listaConResultados2[len(listaConResultados2)-1])

        valorAnterior = valorProximo

        valorProximo = valorAnterior - (float(R)/float(S))

        ea = calcularEa(valorProximo, valorAnterior)

        listaResultados.append(
            [iteracion, valorAnterior, valorProximo, R, S, ea])

        if(ea <= es):
            salida = 1

    return listaResultados

def metodoMuller(funcion, valor0, valor1, valor2, cifrasSignificativas):
    # Lista de valores a mostrar en la lista que mira el usuario
    listaResultados = []
    header = ["Iteracion", "X0", "X1", "X2", "Xr", "EA"]
    listaResultados.append(header)

    # Variables ocupadas
    iteracion = 0
    x0 = float(valor0)
    x1 = float(valor1)
    x2 = float(valor2)

    cifr = int(cifrasSignificativas)
    xr = 0.0
    ea = 0
    es = 0.5*(10**(2-cifr))
    salida = 0

    while salida == 0:
        iteracion += 1

        # Calculamos los valores iniciales en la funcion dada.
        fx0 = evaluarFuncion(funcion, x0, 0, 0)
        fx1 = evaluarFuncion(funcion, x1, 0, 0)
        fx2 = evaluarFuncion(funcion, x2, 0, 0)

        # Calculamos h0 y h1
        h0 = x1 - x0
        h1 = x2 - x1

        # Calculamos el valor del amperson
        ampersand0 = (fx1 - fx0) / h0
        ampersand1 = (fx2 - fx1) / h1

        # Calculamos a, b, c
        a = (ampersand1 - ampersand0) / (h1 + h0)
        b = a*h1 + ampersand1
        c = fx2

        # Calculamos el discriminante
        d = ((b**2) - (4*a*c))**(1/2)

        # Condicional para seleccionar signo del xr
        if(abs(b+d) > abs(b-d)):
            xr = x2 + ((-2*c)/(b+d))
        else:
            xr = x2 + ((-2*c)/(b-d))

        ea = calcularEa(xr, x2)

        # print(x0,x1,x2,xr,ea)
        if(ea <= es):
            listaResultados.append([iteracion, x0, x1, x2, xr, ea])
            salida = 1

        else:
            listaResultados.append([iteracion, x0, x1, x2, xr, ea])
            x0 = x1
            x1 = x2
            x2 = xr

    return listaResultados

def metodoBairstow(coeficientes,r,s,cifrasSig):

    largo = len(coeficientes)

    if largo <= 5:
        listaSalida = ordenPolinomio(largo,coeficientes)
        return listaSalida

    elif largo >5:

        try:

            #Variable salida controlara el bucle while hasta que se cumpla la condición
            salida = 0

            iteracion = 0

            #Esta lista sera la que contendra las respuestas 
            listaResultados = []

            #Primero convertimos a número los valores de r y s  
            r = float(r)
            s = float(s)

            #Declaramos Ear y Eas y Es 
            E_ar = 0
            E_as = 0 
            Es = (10 ** (2 - cifrasSig)) / 2

            '''
            Aqui creamos listas para los valores de a,b,c respectivamente porque no sabemos cuantas variables seran ya que eso 
            depende de la función que ingrese el usuario (La ing en nuestro caso) 

            '''
            
            listaA = coeficientes #La lista a es igual a los coeficientes que acompañan a las X en la funcion
            listaB = []
            listaC = []
            

            #Primero creamos una variable para saber cuantas variables b y c tendremos

            while salida == 0:
                numeroVariables = len(listaA)

                #Debemos limpiar las listas siempre al inicio si no van a acumular los datos de todas las iteraciones
                listaB = []
                listaC = []

                iteracion += 1

                
                #Ahora procedemos a llenar los valores de listaB 
                for i in range(0,numeroVariables):
                    if i == 0:
                        listaB.append(listaA[i])
                    elif i == 1:
                        listaB.append(listaA[i] + r*listaB[0])
                    else:
                        listaB.append(listaA[i] + (r*listaB[i-1])+(s*listaB[i-2]))

                #Ahora procedemos a llenar los valores de listaC
                for i in range(0,numeroVariables):
                    if i == 0:
                        listaC.append(listaB[i])
                    elif i == 1:
                        listaC.append(listaB[i] + r*listaC[0])
                    else:
                        listaC.append(listaB[i]+(r*listaC[i-1])+(s*listaC[i-2]))

                '''
                Ahora procedemos a crear las ecuaciones y despejar deltaR y deltaS simplemente lo haremos
                de manera directa mediante el metodo despejarEcuaciones y asi evitamos crear muchas variables innecesarias
                en el metodo

                Primera ecuación: listaC[numeroVariables-3]*deltaR + listaC[1]*deltaS = -1*listaB[numeroVariables-2]
                Segunda ecuación: listaC[numeroVariables-2]*deltaR + listaC[numeroVariables-3]*deltaS = -1*listaB[numeroVariables-1]
                
                c0 = posicion 0   
                c1 = posicion 1   
                c2 = posicion 2       
                c3 = posicion 3   
                c4 = posicion 4
                c5 = posicion 5

                b0 = posicion 0
                b1 = posicion 1
                b2 = posicion 2
                b3 = posicion 3
                b4 = posicion 4

                '''

                listaB.reverse()
                listaC.reverse()

                deltas = despejarEcuaciones(listaC[2], listaC[3], -1*listaB[1], listaC[1], listaC[2],-1*listaB[0])

                # Determinamos los valores actuales de R y S
                r = r + deltas[0]
                s = s + deltas[1]

                #print(listaB)
            # print(listaC)

                # Determinamos los errores
                E_ar = abs(deltas[0]/r)*100
                E_as = abs(deltas[1]/s)*100

                # Hacemos la validacion de si E_ar y E_as < Es salga del bucle
                if E_ar < Es and E_as < Es:

                    #Verificamos si obtendremos raices imaginarias
                    if (r**(2)+4*s) < 0:
                
                        listaA.reverse()
                        p = P(listaA)
                        raicesExtras = p.roots()
                        
                        '''
                        control = 0
                        raizTexto = ""
                        raizBuena = ""

                        while salida2 == 0:
                            if control >= 0 and control<= len(raicesExtras):
                                raizTexto = str(raicesExtras[control])
                                tamanio = len(raizTexto)-1
                                raizBuena = ""
                                if raizTexto[tamanio] == "j" and raizTexto[tamanio-1] == "0" and raizTexto[tamanio-2] == "+":
                                    for x in range(0,tamanio-2):
                                        raizBuena += raizTexto[x]
                                else:
                                    raizBuena = raizTexto
                                
                                listaResultados.append(raizBuena)
                                control += 1
                        
                            else:
                                salida2 = 1
                        '''

                        for x in range(len(raicesExtras)):
                            listaResultados.append(raicesExtras[x])
                
                        salida = 1

                                               
                    #Si (r**2+4*s) > 0 no hay raices imaginarias 
                    else:
                        print("Entrando con positivas")
                        x1 = "%.5f" % float((r+(r**2+4*s)**0.5)/2)
                        x2 = "%.5f" % float((r-(r**2+4*s)**0.5)/2)

                        #Las convertimos de nuevo a número
                        x1 = float(x1)
                        x2 = float(x2)

                        #Agregamos las primeras 2 raices a la lista de respuestas 
                        listaResultados.append(x1)
                        listaResultados.append(x2)

                        polinomioResultante = divisionSinteticaBairstown(listaA, x1, x2)                    
                        ordenPolinomioResultante = len(polinomioResultante)

                        #Si es una funcion mayor o igual a x^5
                        if ordenPolinomioResultante >= 6:

                            p = P(polinomioResultante)
                            raicesExtras = p.roots()

                            #Borramos los parentesis que nos agrega numpy y eliminamos la J cuando no es necesaria
                            tamanio = len(raicesExtras)-1
                            control = 0
                            salida2 = 1
                            

                            while salida2 == 1:
                                if control <= tamanio and control>=0 :
                                    salidaBuena = ""
                                    raizTexto = str(raicesExtras[control])

                                    for x in raizTexto:
                                        if x == "(" :
                                             salidaBuena += ""
                                        elif x == ")":
                                            salidaBuena += ""
                                        else:
                                            salidaBuena += x
                                            
                                    listaResultados.append(salidaBuena)
                                    control = control + 1
                                else:
                                    salida2 = 0

                            salida = 1

                        #Si es una funcion menor o igual a x^4
                        else:
                            raiPo = ordenPolinomio(ordenPolinomioResultante, polinomioResultante)
                            for x in range(len(raiPo)):
                                listaResultados.append(raiPo[x])
                            salida = 1
        except:
            print("Surgio un problema")
        #Lista con todas las raices encontradas
        return listaResultados

def interpolacionLineal(puntos,xx):
    '''
    Formula:  P(x) = F0 + ((F1-F0)/(X1-X0))*(X-X0)
                   = Y0 + (Y1-Y0)/(X1-X0)*(X-X0)

                   VALOR = x
    puntos es una lista que los 2 primeros valores representan X0,Y0
    y los otros 2 representan X1,Y1
    '''
    listaResultados = []
    xx  = float(xx)
    x0 = float(puntos[0])
    y0 = float(puntos[1])
    x1 = float(puntos[2])
    y1 = float(puntos[3])
    polinomio = 0

    valorInterpolado = y0 + ((y1-y0)/(x1-x0))*(xx-x0)

    for i in range(0,2,1):
        if i == 0:
            polinomio = polinomio + y0
        else:
            polinomio = polinomio + ((y1-y0)/(x1-x0))*(x-x0)
    
    polinomioSimple = sp.expand(polinomio)


    listaResultados.append(polinomioSimple)
    listaResultados.append(valorInterpolado)

    return listaResultados

def interpolacionCuadratica(puntosX, puntosY,valorX):

    listaResultados = []

    xi = np.array(puntosX)
    fi = np.array(puntosY)
    
    xx = float(valorX)
    x0 = puntosX[0]
    x1 = puntosX[1]
    x2 = puntosX[2]
    y0 = puntosY[0]
    y1 = puntosY[1]
    y2 = puntosY[2]

    b0 = y0
    b1 = (y1-y0)/(x1-x0)
    b2 = (((y2-y1)/(x2-x1))-b1)/(x2-x0)

    n = len(xi)
    polinomio = 0
    for i in range(0,n,1):
        multiplicador = 1
        if i == 0:
            polinomio = polinomio + b0
        elif i == 1:
            polinomio = polinomio + b1*(x-x0)
        else:
            polinomio = polinomio + b2*(x-x0)*(x-x1)

    polinomioSimple = sp.expand(polinomio)
    salidaValor = evaluarFuncion(polinomioSimple, xx, 0, 0)

    listaResultados.append(polinomioSimple)
    listaResultados.append(salidaValor)

    return listaResultados
   
def interpolacionLagrange(puntosX,puntosY,valor):

    listaResultados = []

    xi = np.array(puntosX)
    fi = np.array(puntosY)

    n = len(xi)
    polinomio = 0
    for i in range(0,n,1):
        numerador = 1
        denominador = 1
        for j in range(0,n,1):
            if i != j:
                numerador = numerador * (x-xi[j])
                denominador = denominador * (xi[i]-xi[j])
                print(numerador)
                print(denominador)
            termino = (numerador/denominador)*fi[i]
        polinomio = polinomio + termino 
    polinomioSimple = sp.expand(polinomio)

    valorSalida = evaluarFuncion(polinomioSimple, valor, 0, 0)
    
    listaResultados.append(polinomioSimple)
    listaResultados.append(valorSalida)

    return listaResultados

def interpolacionNewton(puntosX,puntosY,valor):
    listaResultados = []
    print(puntosX)
    print(puntosY)
 
    xi = np.array(puntosX)
    fi = np.array(puntosY)

    n = len(xi)
    contador = 2 

    #Encontramos los valores de b
    listadeB = []
    listaApollo = []
    listaApollo2 = []
    n2 = len(xi)


    #Desde aca hasta la linea 1322 calculamos los valores de b
    for i in range(0,n,1):
        if i == 0:
            listadeB.append(fi[i])
        elif i == 1:
            #Encontramos b1
            for j in range(1,n,1):
                numerador = 1
                denominador = 1
                numerador = numerador*(fi[j]-fi[j-1])
                denominador = denominador*(xi[j]-xi[j-1])
                listaApollo.append(numerador/denominador)
                listaApollo2.append(numerador/denominador)
                
            listadeB.append(listaApollo[0])
            listaApollo = []

        else:
            for j in range(1,len(listaApollo2)):
                numerador = 1
                denominador = 1
                numerador = numerador*(listaApollo2[j]-listaApollo2[j-1])

                #Simplemente el contador ira aumentando en uno para traer los valores de la lista xi
                denominador = denominador*(xi[contador]-xi[contador-contador])
                listaApollo.append(numerador/denominador)

            #Aumentamos en uno el contador para controlar la posicion de la lista xi
            contador += 1

            listaApollo2 = []

            #Le asignamos los nuevos valores a listaApollo2
            for z in listaApollo:
                listaApollo2.append(z)

            #Agregamos el respectivo valor de b a la listadeB
            listadeB.append(listaApollo2[0])
            
            #Limpiamos la listaApollo para volver a iterar
            listaApollo = []

    #Desde aqui hasta la linea 1339 hacemos el calculo lineal de los valores de (Xn-Xn-1)---x(X0)
    listadeBLineal = []
    bLineal = 1
    contador2 = 2

    for i in range(0,n):
        if i == 0:
            listadeBLineal.append(1)
        elif i == 1:
            listadeBLineal.append((x-xi[i-1]))
        else:
            bLineal = 1
            for j in range(0,contador2):
                bLineal = bLineal*(x-xi[j])
            contador2 += 1
            listadeBLineal.append(bLineal)

    #Realizamos las multiplicaciones y generamos el polinomio simplificado como le gusta a la ing ^.^
    polinomio = 0 
    for i in range(0,len(listadeB)):
        polinomio = polinomio + listadeB[i]*listadeBLineal[i]

    polinomioSimple = sp.expand(polinomio)

    #Evaluamos el polinomio en el valor a interpolar 
    valorInterpolado = evaluarFuncion(polinomioSimple,valor,0,0) 

    listaResultados.append(polinomioSimple)
    listaResultados.append(valorInterpolado)

    return listaResultados

def interpolacionHermite(lista_valores, punto_evaluar):
    # lista_valores contendra los valores de x,y y las derivadas ya sea la primera o la quinta

    valores_x = lista_valores[0]  # Lista de valores de x
    valores_y = lista_valores[1]  # lista de valores de y
    valores_derivadas = []  # lista de valores de derivadas dentro de una matriz
    listaResultados = [] #lista que guardara el polinomio y el valor evaluado 

    # agregando derivadas a matriz: valores_derivadas
    for i in range(2, len(lista_valores), 1):
        # Si tiene una lista sera la primer derivada, si tiene 2 listas sera 1ra y 2da derivada
        valores_derivadas.append(lista_valores[i])

    # Creando tabla para sacar valores para los valores de b (b0,b1,b2)
    valores_b = []  # Se guardaran todos los valores de b (b0,b1,b2)

    columna_deX = []  # Aqui se guardaran los valores de x y sus repeticiones si tenen derivadas
    cualXEs = []  # Aqui se guardaran las posiciones de las x repetidamente, dependiendo de que fila sea

    # Se utilizara para repetir los valores de derivada que utilizaremos en la tabla mas adelante
    derivadasRepetidas = []
    columna_calculada = []  # Columna donde iran los valores calculados
    columna_siguiente = []  # valores proximos a la columna calculada

    # Agregando valores de la columna de X a columna_deX
    contador = 0
    contadorColumna = 0

    # Hasta cuantas derivadas hay de cada derivada
    for i in range(0, len(valores_derivadas[contador]), 1):
        cualXEs.append(i)
        # Agregando valores de la columna de X a columna_deX con todas sus repeticiones
        columna_deX.append(valores_x[contadorColumna])
        # Llenamos la columna_calculada con los valores de F(x) correspondientes
        columna_calculada.append(valores_y[contadorColumna])

        for j in range(0, len(valores_derivadas), 1):  # Hasta cuantas derivadas hay

            if valores_derivadas[j][i] == "":
                # derivadasRepetidas.append("")
                break
            else:
                cualXEs.append(i)
                # Agregando valores de la columna de X a columna_deX con todas sus repeticiones
                columna_deX.append(valores_x[contadorColumna])
                # Llenamos la columna_calculada con los valores de F(x) correspondientes
                columna_calculada.append(valores_y[contadorColumna])

                if j == 0:
                    # Agregamos las derivadas con sus respectivas repeticiones
                    derivadasRepetidas.append(valores_derivadas[j][i])
                    derivadasRepetidas.append(valores_derivadas[j][i])
                else:
                    derivadasRepetidas.append(valores_derivadas[j][i])

        contadorColumna += 1
        contador += 1

    # print(derivadasRepetidas)  # Impreme el contenido de derivadasRepetidas

    # Realizamos operacion de la tabla para sacar los valores de B (b0,b1,b2 etc).
    '''
    De inicio ya tenemos los valores de Y y X para la tabla con todas las repeticiones
    los valores de X en columna_deX
    los valores de Y (F(x)) en columna_calculada <- pero esta tendra que cambiar al calcular los siguientes valores
    '''

    # Variable que guardara el calculo de encontrar las operaciones de la tabla para luego asignarla a columna_siguiente
    valor = 0
    valores_b.append(columna_calculada[0])  # Agregamos b0 que es F(x0)

    contador = 1
    cualColumnaEs = 1
    cualFilaEs = 1

    for i in range(0, len(columna_deX)-1, 1):  # For para manejar columnas
        cualFilaEs = 1+i

        for j in range(0, len(columna_calculada)-1, 1):  # For para manejar filas
            # Calculamos operaciones de la tabla
            valor = 0

            try:

                if j == 0:
                    valor = (
                        columna_calculada[j+1]-columna_calculada[j])/(columna_deX[contador]-columna_deX[j])
                else:
                    valor = (
                        columna_calculada[j+1]-columna_calculada[j])/(columna_deX[contador]-columna_deX[j])

            # Si da indeterminacion colocamos el valor de su derivada/factorial(contador)
            except ZeroDivisionError:
                # Calculamos en que columna vamos para saber que derivada necesitamos

               # Operacion realizada si da 0/0
                for k in range(0, len(valores_derivadas), 1):
                    if k == (cualColumnaEs-1):
                        print(k)
                        valor = valores_derivadas[k][cualXEs[cualFilaEs]] \
                            / math.factorial(cualColumnaEs)

            if j == 0:  # Agregamos el valor inicial a los valores de b
                valores_b.append(valor)

            # Agregamos los valores de la columna siguiente
            columna_siguiente.append(valor)
            cualFilaEs += 1
            contador += 1

        contador = i+1

        # print(cualColumnaEs)
        # print(columna_deX)
        # print(columna_calculada)
        # print(columna_siguiente)
        # print(valores_b)

        # Limpiaremos la columna anterior y le asignaremos los valores de la columna siguiente
        columna_calculada = []
        for j in range(0, len(columna_siguiente), 1):
            columna_calculada.append(columna_siguiente[j])

        # Limpiamos la columna siguiente para calcularlos en la siguiente iteracion
        columna_siguiente = []

        contador += 1
        cualColumnaEs += 1
    # print(derivadasRepetidas)

    # ------------Aca para abajo se arma el polinomio----------------- los valores de b estan en valores_b

    # Lista que tendra todas las multiplicaciones para repertirlas y armar el polinomio Ej:(x-x0)^2*(x-x1)
    multiplicaciones = []
    listaCuantos = []

    '''
    for i in range(0, len(valores_x)-1, 1):  # Armando Polinomio
        contador = 0
        for j in range(0, len(columna_deX)-1, 1):
            
            if valores_x[i] == columna_deX[j+1]:
                contador+=1
            else:
                continue

        for j in range(0,contador,1):
    '''
    variableAyuda = 0
    polinomios = []
    contador = 0
    for i in range(0, len(valores_b), 1):  # Armando Polinomio

        if i == 0:
            # Agregamos el valor de b0 en el polinomio
            polinomio = valores_b[0]
            polinomios.append(valores_b[0])

        elif i == 1:
            variableAyuda = x-columna_deX[contador]
            #print("Variable ", i, ":", variableAyuda)
            polinomio = polinomio+((valores_b[i])*(x-columna_deX[contador]))
            polinomios.append((valores_b[i])*(x-columna_deX[contador]))
            contador += 1

        else:
            variableAyuda = ((variableAyuda) * (x-columna_deX[contador]))
            #print("Variable ", i, ":", variableAyuda)
            polinomio = polinomio+((valores_b[i])*(variableAyuda))
            polinomios.append((valores_b[i])*(variableAyuda))
            contador += 1

    polinomio2 = sp.expand(polinomio)
    listaResultados.append(polinomio2)
    valorEvaluacion = evaluarFuncion(polinomio2,punto_evaluar,0,0)
    listaResultados.append(valorEvaluacion)

    return listaResultados
    
def resolverMatrices(lista,lista2): #metodo para resolver matrices
    #Los determinantes que usaremos
    #
    a = np.matrix(lista)
    b = np.matrix(lista2)

    listaResultados = (a**-1)*b 

    return listaResultados

def trazadoresCubicos(listaX, listaY, tipo,valor):

    listaResultados = []
    intervalos = []
    intervalorsY = []

    n = len(listaX)
    a, b, c, d = sp.symbols('a b c d')

    # Creamos los intervalos con los que vamos a trabajar en sublistas
    # Esto se hace en todos los metodos entonces lo hacemos desde aqui
    for i in range(0, n-1, 1):
        intervalos.append([listaX[i], listaX[i+1]])
        intervalorsY.append([listaY[i], listaY[i+1]])

    if tipo == 0: #funcion spline grado cero
        solucionesEcuaciones = []
        for i in range(0, len(intervalos), 1):
            salida = "Intervalo " + \
                str(intervalos[i])+" ----> "+str(listaY[i])
            solucionesEcuaciones.append(salida)

        for i in solucionesEcuaciones:
            listaResultados.append(i)
        
        return listaResultados

    elif tipo == 1: #funcion spline grado 1

        # Elnúmero de ecuaciones depende del numero de intervalos encontrados
        # De cada intervalo obtendremos 2 ecuaciones las cuales se resuelven entre ellas 2 de una vez

        ecuacionesSimbolicas = []
        soluciones = []

        # Encontramos los valores de a y b respectivamente
        contador = 0
        contador2 = 0

        for i in range(0, len(intervalos), 1):
            D = (intervalos[contador2][contador]*1) - \
                (intervalos[contador2][contador+1]*1)
            Dx = (intervalorsY[contador2][contador]*1) - \
                (intervalorsY[contador2][contador+1]*1)
            Dy = (intervalos[contador2][contador]*intervalorsY[contador2][contador+1]) - (
                intervalos[contador2][contador+1]*intervalorsY[contador2][contador])
            soluciones.append(Dx/D)
            soluciones.append(Dy/D)

            contador2 += 1

        contador3 = 0
        for i in range(0, len(intervalos), 1):
            ecuacionesSimbolicas.append(
                soluciones[contador3]*x+soluciones[contador3+1])
            contador3 += 2

        contador3 = 1
        solucionesEcuaciones = []
        for i in range(0, len(ecuacionesSimbolicas), 1):
            salida = "Intervalo " + \
                str(intervalos[i])+" ----> "+str(ecuacionesSimbolicas[i]) + "; Valor: ----> " +\
                    str(evaluarFuncion(ecuacionesSimbolicas[i],valor,0,0))
            solucionesEcuaciones.append(salida)
           # print(ecuacionesSimbolicas[i])

        for i in solucionesEcuaciones:
            listaResultados.append(i)
        return listaResultados

    elif tipo == 2:  # Funciones spline grado 2

        # Lista que tendra ceros
        listaConCeros = []
        listaCon3Ceros = []

        # Estaran las ecuaciones finales ya con las variables (a,b,c,d) resueltas
        ecuacionesSimbolicas = []

        soluciones = []
        ecuaciones_Para_Matriz = []  # Lista con los valores de la matriz

        YParaMatriz = []  # Lista con los valores de Y para la matriz

        # Agregamos los valores de y a una lista que sera usada en la matriz
        for i in range(0, n-1, 1):
            YParaMatriz.append([listaY[i]])
            YParaMatriz.append([listaY[i+1]])
        # quitamos a0 por que la igualamos a 0
        for i in range(0, n-2, 1):
            YParaMatriz.append([0])

        # Agregamos 0 del total de variables a encontrar
        for i in range(0, len(intervalos)-1, 1):
            for j in range(0, 3, 1):
                listaConCeros.append(0)

        # Agregamos una lista que tenga solamente 4 ceros
        for i in range(0, 3, 1):
            listaCon3Ceros.append(0)

        # Hacemos la lista con los datos para hacer la matriz (las variables: a b c)
        contador = 0
        columna = 0
        multiplicadorDeCeros = 0

        for i in range(0, len(intervalos)*2, 1):
            if i % 2 == 0 and i != 0:
                contador += 1
                multiplicadorDeCeros += 1
                for i in range(0, 3, 1):
                    listaConCeros.pop()

            if i < 2:
                ecuaciones_Para_Matriz.append(
                    [(intervalos[contador][columna]**2), (intervalos[contador][columna]), 1]+listaConCeros)
            elif i >= 2:
                ecuaciones_Para_Matriz.append(
                    (listaCon3Ceros*multiplicadorDeCeros)+[(intervalos[contador][columna]**2), (intervalos[contador][columna]), 1]+listaConCeros)

            if columna == 0:
                columna = 1
            elif columna == 1:
                columna = 0

        # Numero de variables al derivar = len(intervalos) - 1
        columna = 1
        listaConCeros = []
        multiplicadorDeCeros = 0
        # Agregamos 0 del total de variables a encontrar
        for i in range(0, len(intervalos)-2, 1):
            for j in range(0, 3, 1):
                listaConCeros.append(0)

        for i in range(0, len(intervalos)-1, 1):  # Primer derivada
            if i == 0:
                ecuaciones_Para_Matriz.append(
                    [2*(intervalos[i][columna]), 1, 0, -2*(intervalos[i+1][columna-1]), -1, 0]+listaConCeros)
            else:  # Agregamos ceros a la izquierda y vamos eliminando ceros de la derecha
                ecuaciones_Para_Matriz.append(
                    (listaCon3Ceros*multiplicadorDeCeros)+[2*(intervalos[i][columna]), 1, 0, -2*(intervalos[i+1][columna-1]), -1, 0]+listaConCeros)
            multiplicadorDeCeros += 1

            if i < len(intervalos)-2:
                # Eliminamos 4 ceros de la lista que contiene todos los ceros
                for j in range(0, 3, 1):
                    listaConCeros.pop()

        # Libres para igualar una variable a cero
        for i in range(0, len(intervalos)-1, 1):
            for j in range(0, 3, 1):
                listaConCeros.append(0)

        # Eliminaremos a0 de ecuaciones_Para_Matriz, por que se iguala una variable a 0, entonces ya sabemos su valor
        for i in range(0, len(ecuaciones_Para_Matriz), 1):
            del ecuaciones_Para_Matriz[i][0]

        listaDeSoluciones = []  # Lista con las soluciones

        # Resolvemos la matriz llamando al metodo resolverMatrices, guardamos en soluciones
        # pero soluciones es una matriz por eso la pasamos a unas lista llamada listaDeSoluciones
        soluciones = resolverMatrices(
            ecuaciones_Para_Matriz, YParaMatriz)

        # Lista con las respuestas de las variables a b c d
        listaDeSoluciones = np.array(soluciones).flatten().tolist()

        # Le agregamos a0 que igualamos a cero antes de agregar los demas
        listaDeSoluciones[:0] = [0]

        # Aqui formamos las funciones spline ax+b
        contador3 = 0  # El contador nos servira para elegir los valores de a0 b0 c0 etc

        for i in range(0, len(intervalos), 1):
            ecuacionesSimbolicas.append(
                listaDeSoluciones[contador3]*x**2+listaDeSoluciones[contador3+1]*x+listaDeSoluciones[contador3+2])
            contador3 += 3

         # Aca unimos el intervalo con su funcion respectiva para mostrarlo.

        solucionesEcuaciones = []
        for i in range(0, len(ecuacionesSimbolicas), 1):
            salida = "Intervalo " + \
                str(intervalos[i])+" ----> "+str(ecuacionesSimbolicas[i]) + "; Valor: "+\
                    str(evaluarFuncion(ecuacionesSimbolicas[i],valor,0,0))
            solucionesEcuaciones.append(salida)
           # print(ecuacionesSimbolicas[i])

        for i in solucionesEcuaciones:
            listaResultados.append(i)
        return listaResultados

    elif tipo == 3:  # Funciones spline grado 3

        # Lista que tendra ceros
        listaConCeros = []
        listaCon4Ceros = []

        # Estaran las ecuaciones finales ya con las variables (a,b,c,d) resueltas
        ecuacionesSimbolicas = []

        soluciones = []
        ecuaciones_Para_Matriz = []  # Lista con los valores de la matriz

        YParaMatriz = []  # Lista con los valores de Y para la matriz

        for i in range(0, n-1, 1):
            YParaMatriz.append([listaY[i]])
            YParaMatriz.append([listaY[i+1]])

        for i in range(0, n-1, 1):
            YParaMatriz.append([0])
            YParaMatriz.append([0])

        # Agregamos 0 del total de variables a encontrar
        for i in range(0, len(intervalos)-1, 1):
            for j in range(0, 4, 1):
                listaConCeros.append(0)

        # Agregamos una lista que tenga solamente 4 ceros
        for i in range(0, 4, 1):
            listaCon4Ceros.append(0)

        # Hacemos la lista con los datos para hacer la matriz
        contador = 0
        columna = 0
        multiplicadorDeCeros = 0

        for i in range(0, len(intervalos)*2, 1):
            if i % 2 == 0 and i != 0:
                contador += 1
                multiplicadorDeCeros += 1
                for i in range(0, 4, 1):
                    listaConCeros.pop()

            if i < 2:
                ecuaciones_Para_Matriz.append(
                    [(intervalos[contador][columna]**3), (intervalos[contador][columna]**2), (intervalos[contador][columna]), 1]+listaConCeros)
            elif i >= 2:
                ecuaciones_Para_Matriz.append(
                    (listaCon4Ceros*multiplicadorDeCeros)+[(intervalos[contador][columna]**3), (intervalos[contador][columna]**2), (intervalos[contador][columna]), 1]+listaConCeros)

            if columna == 0:
                columna = 1
            elif columna == 1:
                columna = 0

        # Numero de variables al derivar = len(intervalos) - 1
        columna = 1
        listaConCeros = []
        multiplicadorDeCeros = 0
        # Agregamos 0 del total de variables a encontrar
        for i in range(0, len(intervalos)-2, 1):
            for j in range(0, 4, 1):
                listaConCeros.append(0)

        for i in range(0, len(intervalos)-1, 1):  # Primer derivada
            if i == 0:
                ecuaciones_Para_Matriz.append(
                    [3*(intervalos[i][columna]**2), 2*(intervalos[i][columna]), 1, 0, -3*(intervalos[i+1][columna-1]**2), -2*(intervalos[i+1][columna-1]), -1, 0]+listaConCeros)
            else:  # Agregamos ceros a la izquierda y vamos eliminando ceros de la derecha
                ecuaciones_Para_Matriz.append(
                    (listaCon4Ceros*multiplicadorDeCeros)+[3*(intervalos[i][columna]**2), 2*(intervalos[i][columna]), 1, 0, -3*(intervalos[i+1][columna-1]**2), -2*(intervalos[i+1][columna-1]), -1, 0]+listaConCeros)
            multiplicadorDeCeros += 1

            if i < len(intervalos)-2:
                # Eliminamos 4 ceros de la lista que contiene todos los ceros
                for j in range(0, 4, 1):
                    listaConCeros.pop()

        listaConCeros = []
        multiplicadorDeCeros = 0
        # Agregamos 0 del total de variables a encontrar
        for i in range(0, len(intervalos)-2, 1):
            for j in range(0, 4, 1):
                listaConCeros.append(0)

        for i in range(0, len(intervalos)-1, 1):  # Segunda derivada

            if i == 0:
                ecuaciones_Para_Matriz.append(
                    [6*(intervalos[i][columna]), 2, 0, 0, -6*(intervalos[i+1][columna-1]), -2, 0, 0]+listaConCeros)

            else:  # Agregamos ceros a la izquierda y vamos eliminando ceros de la derecha
                ecuaciones_Para_Matriz.append(
                    (listaCon4Ceros*multiplicadorDeCeros)+[6*(intervalos[i][columna]), 2, 0, 0, -6*(intervalos[i+1][columna-1]), -2, 0, 0]+listaConCeros)

            multiplicadorDeCeros += 1

            if i < len(intervalos)-2:
                # Eliminamos 4 ceros de la lista que contiene todos los ceros
                for j in range(0, 4, 1):
                    listaConCeros.pop()

        # Libres que igualamos a cero

        for i in range(0, len(intervalos)-1, 1):
            for j in range(0, 4, 1):
                listaConCeros.append(0)

        ecuaciones_Para_Matriz.append(
            [6*(intervalos[0][0]), 2, 0, 0]+listaConCeros)

        ecuaciones_Para_Matriz.append(
            listaConCeros+[6*(intervalos[len(intervalos)-1][1]), 2, 0, 0])

        listaDeSoluciones = []
        soluciones = resolverMatrices(
            ecuaciones_Para_Matriz, YParaMatriz)  # Resolvemos la matriz
        # Lista con las respuestas de las variables a b c d
        listaDeSoluciones = np.array(soluciones).flatten().tolist()

        # Aqui formamos las funciones spline ax+b
        contador3 = 0

        for i in range(0, len(intervalos), 1):
            ecuacionesSimbolicas.append(
                listaDeSoluciones[contador3]*x**3+listaDeSoluciones[contador3+1]*x**2+listaDeSoluciones[contador3+2]*x+listaDeSoluciones[contador3+3])
            contador3 += 4

         # Aca unimos el intervalo con su funcion respectiva para mostrarlo.
        contador3 = 1
        solucionesEcuaciones = []
        for i in range(0, len(ecuacionesSimbolicas), 1):
            salida = "Intervalo " + \
                str(intervalos[i])+" ----> "+str(ecuacionesSimbolicas[i]) + "; Valor: "+\
                    str(evaluarFuncion(ecuacionesSimbolicas[i],valor,0,0))
            solucionesEcuaciones.append(salida)
           # print(ecuacionesSimbolicas[i])

        for i in solucionesEcuaciones:
            listaResultados.append(i)
        return listaResultados

def encontrarDerivada(funcion,queDerivada):
    print("derivacion")
    funcioon = sp.sympify(funcion)
    gxValor = sp.diff(funcioon, x,queDerivada)
    return gxValor
  
def diferenciacionNumericaAdelante(funcion,puntoInicial,h):
    listaResultados = [] #lista donde estaran las respuestas 

    #lista donde guardamos los valores de la primera diferencia

    #variables donde guardaremos el numerador
    numerador1 = 0

    numerador1 = evaluarFuncion(funcion,puntoInicial+h,0,0) + evaluarFuncion(funcion,puntoInicial,0,0)*(-1)

    #guardamos la primera diferencia
    listaResultados.append((numerador1)/h)


    numerador1 = evaluarFuncion(funcion,puntoInicial+(2*h),0,0)*(-1) + evaluarFuncion(funcion,puntoInicial+h,0,0)*(4) + evaluarFuncion(funcion,puntoInicial,0,0)*(-3)
    numerador2 = sp.expand_log(numerador1,force=True)
    #guardamos la segunda diferencia 
    listaResultados.append(numerador2/(2*h))

    print(listaResultados)

    

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

   # for i in listaResultados:
       # print(i)

