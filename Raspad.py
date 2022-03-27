import numpy as np
import matplotlib.pyplot as plt

print('Введите время моделирования')
time = float(input())
y = 5/3
t = 1e-4
p_1 = 1e6
r_1 = 13
p_2 = 1e5
r_2 = 1.3
N = 100
h = 2*10/(N-1)

r = np.empty(N)
p = np.empty(N)
for i in range (int(N/2)+1):
	r[i]=r_1
	p[i]=p_1
for i in range (int(N/2)+1,N):
	r[i]=r_2
	p[i]=p_2
W = np.array([r, np.zeros(N), p/(y-1)])


temp = W
for j in range(int(time/t)):
	for i in range(1,N-1):
		u = (W[1]/W[0])[i]
		e = (W[2]/W[0])[i]
		c = ((W[2]/W[0])**0.5*np.sqrt(y**2-y))[i]
		A = np.array([[0, 1, 0],[-u**2, 2*u, y-1],[-e*u*y, e*y, u]])
		O = np.array([[-u*c, c, y-1],[-c**2, 0, y-1],[u*c, -c, y-1]])
		R = np.array([[1/2/c**2, -1/c**2, 1/2/c**2],[(c+u)/2/c**2, -u/c**2, (-c+u)/2/c**2],[1/2/(y-1), 0, 1/2/(y-1)]])
		L = np.array([[abs(u+c), 0, 0],[0, abs(u), 0],[0, 0, abs(u-c)]])
		v = np.array([W[0][i], W[1][i], W[2][i]])
		vp = np.array([W[0][i-1], W[1][i-1], W[2][i-1]])
		vn = np.array([W[0][i+1], W[1][i+1], W[2][i+1]])
		v_new = v - t*A@(vn-vp)/2/h+t/2/h*R@L@O@(vn-2*v+vp)
		for z in range(3):
			temp[z][i] = v_new[z]
	for i in range(3):
		temp[i][0] = temp[i][1]
		temp[i][N-1] = temp[i][N-2]
	W = temp
X = np.linspace(-10,10, N)


plt.figure(figsize=(12, 7))

plt.subplot(2, 2, 1)
plt.title('Распределение плотности')
plt.plot(X, W[0], '.')
plt.subplot(2, 2, 2)
plt.title('Распределение скорости')
plt.plot(X, W[1]/W[0],'.')
plt.subplot(2, 2, 3)
plt.title('Распределение давления')
plt.plot(X, W[2]*(y-1),'.')
plt.subplot(2, 2, 4)
plt.title('Распределение энергии')
plt.plot(X, W[2]/W[0],'.')

plt.show()
