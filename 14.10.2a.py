import numpy as np
import matplotlib.pyplot as plt

L = 20
time = 18
N = 41
h = 0.5
print('Введите число Куранта')
C = float(input())
tau = h * C
print (tau)
x = np.linspace(h, L, N-1)
t = np.linspace(h, time, int(time/tau))
sin = []
Y=[]

def ny():
	return np.sin(4*np.pi*x/L)
Y = ny()
for i in range(int(time/tau)):
	sin.append(np.sin(4*np.pi*(x-t[i])/L))


temp = np.zeros(N-1)
th=int(time/tau)
plt.figure(figsize=(12, 7))
for j in range(th):
	for i in range(N-1):
		temp[i] = Y[i] + tau/h * (Y[i-1] - Y[i])
	for i in range(N-1):
		Y[i] = temp[i]
	if (j==0):
		plt.subplot(2, 3, 1)
		plt.title('t = ' + str(round((j)*tau)))
		plt.plot(x, Y/Y.max(), label = 'численное')
		plt.plot(x, sin[j], label = 'аналитическое')
	if (j==int(0.2*th)):
		plt.subplot(2, 3, 2)
		plt.title('t = ' + str(round((j)*tau)))
		plt.plot(x, Y/Y.max(), label = 'численное')
		plt.plot(x, sin[j], label = 'аналитическое')
	if j==int(0.4*th):
		plt.subplot(2, 3, 3)
		plt.title('t = ' + str(round((j)*tau)))
		plt.plot(x, Y/Y.max(), label = 'численное')
		plt.plot(x, sin[j], label = 'аналитическое')
	if j==int(0.6*th):
		plt.subplot(2, 3, 4)
		plt.title('t = ' + str(round((j)*tau)))
		plt.plot(x, Y/Y.max(), label = 'численное')
		plt.plot(x, sin[j], label = 'аналитическое')
	if j==int(0.8*th):
		plt.subplot(2, 3, 5)
		plt.title('t = ' + str(round((j)*tau)))
		plt.plot(x, Y/Y.max(), label = 'численное')
		plt.plot(x, sin[j], label = 'аналитическое')
	if j==(th-1):
		plt.subplot(2, 3, 6)
		plt.title('t = ' + str(round((j+1)*tau)))
		plt.plot(x, Y/Y.max(), label = 'численное')
		plt.plot(x, sin[j], label = 'аналитическое')
plt.legend();
plt.show()
