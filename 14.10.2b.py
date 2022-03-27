import numpy as np
import matplotlib.pyplot as plt

L = 20
time = 18
N = 41
h = 0.5
Co = float(input())
T = h * Co
x = np.linspace(h, L, N-1)
t = np.linspace(0, time, int(time/T))
sin = []
Y=[]

def ny():
	return np.sin(4*np.pi*x/L)
Y = ny()
for i in range(int(time/T)):
	sin.append(np.sin(4*np.pi*(x-t[i])/L))

temp = np.zeros(N-1)
th=int(time/T)
plt.figure(figsize=(12, 7))
for j in range(int(time/T)):
	for i in range(N-1):
		if i == 0:
			a = (Y[1] - Y[N-2])*(-1/(2*h))
			b = (Y[1] - 2*Y[0] + Y[N-2])*(T/(2*h**2))
		elif i == N-2:
			a = (Y[0] - Y[N-3])*(-1/(2*h))
			b = (Y[0] - 2*Y[N-2] + Y[N-3])*(T/(2*h**2))
		else:
			a = (Y[i+1] - Y[i-1])*(-1/(2*h))
			b = (Y[i+1] - 2*Y[i] + Y[i-1])*(T/(2*h**2))
		temp[i] = Y[i] + (a+b)*T
	for i in range(N-1):
		Y[i] = temp[i]
	if (j==0):
		plt.subplot(2, 3, 1)
		plt.title('t = ' + str(round((j)*T)))
		plt.plot(x, Y/Y.max(), label = 'численное')
		plt.plot(x, sin[j], label = 'аналитическое')
	if (j==int(0.2*th)):
		plt.subplot(2, 3, 2)
		plt.title('t = ' + str(round((j)*T)))
		plt.plot(x, Y/Y.max(), label = 'численное')
		plt.plot(x, sin[j], label = 'аналитическое')
	if j==int(0.4*th):
		plt.subplot(2, 3, 3)
		plt.title('t = ' + str(round((j)*T)))
		plt.plot(x, Y/Y.max(), label = 'численное')
		plt.plot(x, sin[j], label = 'аналитическое')
	if j==int(0.6*th):
		plt.subplot(2, 3, 4)
		plt.title('t = ' + str(round((j)*T)))
		plt.plot(x, Y/Y.max(), label = 'численное')
		plt.plot(x, sin[j], label = 'аналитическое')
	if j==int(0.8*th):
		plt.subplot(2, 3, 5)
		plt.title('t = ' + str(round((j)*T)))
		plt.plot(x, Y/Y.max(), label = 'численное')
		plt.plot(x, sin[j], label = 'аналитическое')
	if j==(th-1):
		plt.subplot(2, 3, 6)
		plt.title('t = ' + str(round((j+1)*T)))
		plt.plot(x, Y/Y.max(), label = 'численное')
		plt.plot(x, sin[j], label = 'аналитическое')
plt.legend();
plt.show()
