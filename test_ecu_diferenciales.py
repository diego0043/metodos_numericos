import sympy 
from scipy import integrate


# Resolviendo ecuación diferencial
# defino las incognitas
x = sympy.Symbol('x')
y = sympy.Function('y')

# expreso la ecuacion
# definiendo la ecuación
eq = 1.0/2 * (y(x)**2 - 1)

# Condición inicial
ics = {y(0): 2}

# Resolviendo la ecuación
edo_sol = sympy.dsolve(y(x).diff(x) - eq)
print(edo_sol)
