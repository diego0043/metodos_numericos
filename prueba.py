'''
import numpy as np
from numpy.polynomial import Polynomial as P
from meto2 import *

salida = [16,0,-20,1,5,-0.5]
print(salida)

p = P(salida)
raices = p.roots()

for x in range(len(raices)):
    print(raices[x])



texto = "jdjdcjdcdcj"
lista = [("(jpla)")]
print(lista[0])
print(len(lista[0])*6)


texto = "( jose PErs )"
salidaBuena = ""

for x in texto:
    if x == "(" :
        salidaBuena += ""
    elif x == ")":
        salidaBuena += ""
    else:
        salidaBuena += x

print(salidaBuena)
hola = "printrfrfnrfr"

print(hola[0])
#salida = [16,0,-20,1,5,-0.5]


#Graficas 3d
from sympy import symbols
from sympy.plotting import plot3d
x, y = symbols('x y')

#salida = sp.solve(16*x**5-20*x**3+x**2+5*x-0.5)
#print(salida)
fun = x**2
plot3d(fun)

from sympy import plot_implicit, symbols, Eq, And
x , y = symbols('x y')
p1 = plot_implicit(16*x**5-20*x**3+x**2+5*x-0.5,x_var=x)

import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import meto2 as mt

coeficientes = mt.coefs("16x^5-20x^3+x^2+5x-1")
polimio = Polynomial(coef=coeficientes)
poliDerivado = polimio.deriv()
poliInte = polimio.integ()

print(poliInte)

#x = np.arange(start= -50, stop=51, step=1)
#plt.plot(x,polimio(x))
#.show()
'''

import cmath
print(type(cmath.e))


