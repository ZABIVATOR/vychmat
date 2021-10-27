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

def f(x):
	return x*math.exp(-x**2)-AB

def s(x0,x1):#metod sekushei
	fx0 = f(x0)
	fx1 = f(x1)
	xx=[]
	while abs(x1-x0) > e/2:
		x2=(x0*fx1-x1*fx0)/(fx1-fx0)
		x0=x1
		x1=x2
		fx0=fx1
		fx1=f(x2)
		xx.append(x1)
	return xx
yr=[]
yl=[]
XLEFT=s(0,0.8)
XRIGHT=s(1,2)

nl=len(XLEFT)
nr=len(XRIGHT)
print("x1 = ", round(XLEFT[nl-1], 3))
print("x2 = ", round(XRIGHT[nr-1], 3))
print("Ответ: x2 - x1 = ", round(XRIGHT[nr-1]-XLEFT[nl-1], 3))
for i in range(nr):
	XRIGHT[i]=abs(XRIGHT[i]-1.3588)
	yr.append(i)
for i in range(nl):
	XLEFT[i]=abs(XLEFT[i]-0.2256)
	yl.append(i)


plt.plot(yl,XLEFT,yr,XRIGHT)

plt.grid(True)
plt.show()
