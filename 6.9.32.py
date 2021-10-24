import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x=np.array([1910,1920,1930,1940,1950,1960,1970,1980,1990,2000])#god
y=np.array([92228496,106021537,123202624,132164569,151325798, 179323175,203211926, 226545805, 248709873,281421906])#naselenie
X=sp.symbols('X')

def int (x, y):
	Y=0
	for i in range ( len(x) ):
		t=1
		for j in range ( len(x) ):
			if i != j:
				t=t* ( (X-x[j]) /(x[i]-x[j]) )
		Y+= t*y[i]
	return Y
l=sp.simplify(int(x,y))#polinom
print('Население США в 2010 году - оригинальное: 308745538')
exnu= l.subs(X, 2010)
print('Экстраполяция методом Ньютона:',exnu)

'''print('input year')
i=int(input())


xnew=np.linspace(np.min(x),np.max(x),100) 
ynew=[]
for i in range(100):
	ynew.append(l.subs(X, xnew[i]))

print (l)
plt.plot(x,y,'o',xnew,ynew)
plt.grid(True)
plt.show()'''


x=[1910,1920,1930,1940,1950,1960,1970,1980,1990,2000]#god
y=[92228496,106021537,123202624,132164569,151325798, 179323175,203211926, 226545805, 248709873,281421906]#naselenie

class CubicSpline:
	def __init__(self, a, b, c, d, x):
		self.b = b
		self.c = c
		self.d = d
		self.x = x
		self.y = y

def solveTriagonalSlae_IMPROVED(x, y):
	n=len(x)
	splines = [CubicSpline(0, 0, 0, 0, 0) for _ in range(0, n)]
	for i in range(0, n):
		splines[i].x = x[i]
		splines[i].y = y[i]
	splines[0].c = splines[n - 1].c = 0.0
	#strait
	alpha = [0.0 for _ in range(0, n - 1)]
	beta  = [0.0 for _ in range(0, n - 1)]
	
	for i in range(1, n - 1):
		hi  = x[i] - x[i - 1]
		hi1 = x[i + 1] - x[i]
		A = hi
		C = 2.0 * (hi + hi1)
		B = hi1
		F = 6.0 * ((y[i + 1] - y[i]) / hi1 - (y[i] - y[i - 1]) / hi)
		z = (A * alpha[i - 1] + C)
		alpha[i] = -B / z
		beta[i] = (F - A * beta[i - 1]) / z
	#rev
	for i in range(n - 2, 0, -1):
		splines[i].c = alpha[i] * splines[i + 1].c + beta[i]
		
	for i in range(n - 1, 0, -1):
		hi = x[i] - x[i - 1]
		splines[i].d = (splines[i].c - splines[i - 1].c) / hi
		splines[i].b = hi * (2.0 * splines[i].c + splines[i - 1].c) / 6.0 + (y[i] - y[i - 1]) / hi
	return splines

def interpolate(splines, x):
	n = len(splines)
	s = CubicSpline(0, 0, 0, 0, 0)
	i = 0
	j = n - 1
	while i + 1 < j:
		k = i + (j - i) // 2
		if x <= splines[k].x:
			j = k
		else:
			i = k
	s = splines[j]
	dx = x - s.x
	return s.y + (s.b + (s.c / 2.0 + s.d * dx / 6.0) * dx) * dx;

excub = interpolate(solveTriagonalSlae_IMPROVED(x, y), 2010)
print('Экстраполяция кубическим сплайном: ', round(excub))

n2010=308745538
print('Погрешность метода Ньютона', round((exnu-n2010)/n2010*100), '%, Погрешность кубического сплайна', round(abs(excub-n2010)/n2010*100, 2), '%')
