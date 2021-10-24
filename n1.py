import math
import numpy as np
import matplotlib.pyplot as plt

def f1(x,y):
	return x**2+y**2-1
def f2(x,y):
	return y-math.tan(x)
def fx1(x):
	return (1-x**2)**(1/2)
def fx2(x):
	return math.tan(x)

F = lambda x,y:[f1(x,y),f2(x,y)] 
J = lambda x,y:np.array([[2*x,2*y],[-1/(math.cos(x)**2),1]])

def new(a0):
	a1=a0-np.linalg.inv(J(*a0))@F(*a0)
	a2=a0
	while abs(a1-a2).all()>10**(-6):
		a2=a1
		a1=a1-np.linalg.inv(J(*a1))@F(*a1)
	return a1 
 
x,y = new(np.array([1, 1]))
print(round(x,6),round(y,6))
#задача симмeтрична
print(round(-x,6),round(-y,6))
#grafik korney

xnew=np.linspace(-1,1,200) 
ynew=[]
ynew2=[]
ynew3=[]
for i in np.arange(-1, 1, 0.01):
	ynew.append(fx1(i))
	ynew3.append(-fx1(i))
	ynew2.append(-fx2(-i))

plt.plot(xnew,ynew,xnew,ynew3,color='green')
plt.plot(xnew,ynew2,color='red')
plt.grid(True)
plt.show()
