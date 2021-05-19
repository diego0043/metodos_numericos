from meto2 import *

listaA = [1.3,1.6,1.9]
listaB = [0.6200860,0.4554022,0.2818186]
listaC = [-0.5220232,-0.5698959,-0.5811571]
#listaB = [1,2.74,7.38,20.08,54.59,148.41,403.42]
#listaA = [-2,-1,1,2]
#listaB = [-5,1,1,7]



interpolacionHermite(listaA,listaB,listaC)


'''
Lo que estaba en el else
 for j in range(contador,n,1):
                numerador = 1
                denominador = 1
                numerador = numerador*(listaApollo2[j-1]-listaApollo2[j-2])
                denominador = denominador*(xi[contador]-xi[contador-2])
                listaApollo.append(numerador/denominador)
                contador = contador + 1

            listaApollo2 = []
            for z in range(0,len(listaApollo)):
                if z == 0: 
                    listaApollo2.append(listaApollo[z])
                    listadeB.append(listaApollo2[z])
                else:
                    listaApollo2.append(listaApollo[z])

            contador3 += 1
            contador = contador3

            
            
            listaApollo = []

            print("lista de b: ",listadeB)

'''