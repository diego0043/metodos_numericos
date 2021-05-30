from sympy.functions.elementary.hyperbolic import ReciprocalHyperbolicFunction
from metodosYformularios.meto2 import *

listaX = [-1,-2] #Puntos de x
listaY = [-11,2] #puntos de y
listaDiff = [14,5] #valores de la primera derivada 

listaVAlores = [listaX,listaY,listaDiff]


def hermite(lista_valores, punto_evaluar):
    #lista_valores contendra los valores de x,y y las derivadas ya sea la primera o la quinta
    
    valores_x = [lista_valores[0]] #Lista de valores de x
    valores_y = [lista_valores[1]] #lista de valores de y 
    valores_derivadas = []         #lista de valores de derivadas dentro de una matriz

    # agregando derivadas a matriz: valores_derivadas
    for i in range(2,len(lista_valores),1):
        valores_derivadas.append(lista_valores[i])
    
    # Encontramos tabla de apoyo 
    lista_apolloX = []
    lista_apolloY = []
    lista_apollo_derivadas = []
    control_repeticion_valores = []
    
    #llenamos la lista de apolloX
    for i in range(0,len(valores_derivadas),1):
        if i == 0:
            for i in valores_derivadas[0]:
                se_repite = 0
                if i == '':
                    se_repite = 1
                    lista_apolloX.append(1)

    #llenamos la lista de apolloX y apolloY

    for i in range(0,len(listaX),1): # cada iteración representa un punto en x 
        for i in valores_derivadas[i]:
            print(i)


hermite(listaVAlores,1)
    