'''
from sympy import symbols
from sympy.plotting import plot
import cmath

x = symbols('x')
funcion = 'sec(x)'
title = "Grafica de: "+ str(funcion)
p1 = plot(funcion,show=False ,line_color='#96ADEA', ylabel='Y', xlabel= 'X',title=title,size=(6,5),xlim=(-25,25),ylim=(-25,25))

p1.show()
'''

from metodosYformularios import metodos_unidad_4
from fractions import Fraction
import decimal

#metodos_unidad_4.diferenciacionNumericaAdelante('ln(x)',5,0.1)

#metodos_unidad_4.diferenciacionNumericaAtras('ln(x)',5,0.05)

#lista_valores = [[1,1.1,1.2,1.3,1.4,1.5],[2.5,2.436851,2.372895,2.308785,2.245066,2.182179]]
#metodos_unidad_4.diferenciacionNumericaCentrada('',1.3,0.1,lista_valores)   

#metodos_unidad_4.diferenciacionNumericaTresPuntos('ln(x)*sin(x)',3,0.1,[])
#metodos_unidad_4.diferenciacionNumericaCincoPuntos('ln(x)*tan(x)',4.2,0.1,[])
#metodos_unidad_4.diferenciacion_numerica_adelante_orden_superior('cos(x)',2,0.1,[])


#salida = metodos_unidad_4.metodo_richardson('ln(x)',0.7,0.1,5)

#for i in salida:
    #
    # print(i)

#salida = metodos_unidad_4.regla_del_trapecio_compuesta('',0,0.5,6,[[0,0.1,0.2,0.3,0.4,0.5],[1,7,4,3,5,2]])
#(0.3989)*e^-((x^2)/x)

#salida2 = metodos_unidad_4.integracion_rosemberg('e^(x)*ln(x)',1,2,4)

salida = metodos_unidad_4.integracion_cuadratura_Gaussiana('(e^x*sin(x))/(1+x^2)',0,3,3)