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

from metodosYformularios import meto2 

meto2.diferenciacionNumericaAdelante('ln(x)',5,0.1)