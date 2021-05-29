from metodosYformularios.meto2 import *

listaX = [-1,-2] #Puntos de x
listaY = [-11,2] #puntos de y
listaDiff = ['',5] #valores de la primera derivada 

listaVAlores = [listaX,listaY,listaDiff]


def hermite(lista_valores, punto_evaluar):
    #lista_valores contendra los valores de x,y y las derivadas ya sea la primera o la quinta
    valores_x = []
    valores_y = []
    lista_apollo_diff = []
    valores_diff = []

    print(len(lista_valores))
    print(len(lista_valores[0]))

    for i in range(0,len(lista_valores)):
        for j in range(0,len(lista_valores[0])):
            if i == 0: #valores de x
                valores_x.append(lista_valores[i][j])
            elif i == 1: #valores de y
                valores_y.append(lista_valores[i][j])
            else: #todos los valores de las derivadas
                print(i,j)
                lista_apollo_diff.append(lista_valores[i][j])

    
    valores_diff.append(lista_apollo_diff)
    print(listaX)
    print(listaY) 
    print(valores_diff)   

hermite(listaVAlores,1)
    