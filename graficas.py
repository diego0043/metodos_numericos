from sympy import symbols
from sympy.plotting import plot
import cmath

x = symbols('x')
funcion = 'sin(x)'
p1 = plot(funcion,show=False ,line_color='#96ADEA', ylabel='Y', xlabel= 'X', legend=str(funcion),size=(6,5),xlim=(-25,25),toolbar=None)

p1.show()