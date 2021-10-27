import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return math.sin(100*x)*math.exp(-x**2)*math.cos(2*x)

def  integ(f, a, b, n):
	h=(b-a)/n
	k=0.0
	x=a + h
	for i in range(1,n//2 + 1):
		k += 4*f(x)
		x += 2*h
	x = a + 2*h
	for i in range(1,n//2):
		k += 2*f(x)
		x += 2*h
	return (h/3)*(f(a)+f(b)+k)

print (round(integ(f, 0.0, 3.0, 200),3))



xnew=np.linspace(100,1000,100) 
ynew=[]

for i in range(100):
	ynew.append(integ(f, 0.0, 3.0, int(xnew[i]))-0.01)

plt.plot(xnew,ynew)
plt.grid(True)
plt.show()
