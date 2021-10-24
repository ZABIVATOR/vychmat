import math
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
from numpy import arange

e = 10**(-3)
x, y = sp.symbols('x y')
y = x*sp.exp(-x**2)
y1=sp.diff(y,x,1)	
y2=sp.diff(y,x,2)

x1,x2 = sp.solve(y1)
#[-sqrt(2)/2, sqrt(2)/2]
#find ymax
xmax=0
print(sp.simplify(y2))

f1=y1.subs(x, x1-1)
f2=y1.subs(x, x2+1)
f3=y1.subs(x, (x1+x2)/2)
if f1>0 and f3<0:
	xmax=x1
if f3>0 and f2<0:
	xmax=x2
fmax = y.subs(x, xmax)

i = 1
x0 = 0.6
print("x 0 = ", round(x0, 3)) 
x1 = x0 -y1.subs(x, x0)/y2.subs(x, x0)
i += 1
print("x 1 = ", round(x1, 3))
while abs(x1-x0) > e:
	i += 1
	x0 = x1
	x1 = x0 - y1.subs(x, x0)/y2.subs(x, x0)
	print("x", i-1, " = ", round(x1, 3))
 
abc=y.subs(x, x1)
print("fmax = ", round(abc, 3))
print("fmax/2 = ", round(abc/2, 3))
AB=abc/2
x1 = 0
while abs(y.subs(x, x1) - AB) > e/2:
	x1 += 0.0001
print("x1 = ", round(x1, 3))
x2 = x1+1
while abs(y.subs(x, x2) -AB) > e/2:
	x2 += 0.0001
print("x2 = ", round(x2, 3))
print("Ответ: x2 - x1 = ", round(x2-x1, 3))
