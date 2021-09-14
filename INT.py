import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x=np.array([1,3,6,7])#points
y=np.array([1,9,36,49])#value
X=sp.symbols('X')

def lagranz (x, y):
	Y=0
	for i in range ( len(x) ):
		t=1
		for j in range ( len(x) ):
			if i != j:
				t=t* ( (X-x[j]) /(x[i]-x[j]) )
		Y+= t*y[i]
	return Y

l=sp.simplify(lagranz(x,y))#polinom
xnew=np.linspace(np.min(x),np.max(x),100) 
ynew=[]
for i in range(100):
	ynew.append(l.subs(X, xnew[i]))

print (l)
plt.plot(x,y,'o',xnew,ynew)
plt.grid(True)
plt.show()
