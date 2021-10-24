#t [0,1]
e = 10**(-3)
n=1
f=1
i=0
while f>e:
	i=i+1
	n=n*i
	f=1/n

print('n равно',i , 'при 0 < t < 1')

#t [10,11]
n=1
f=1
a=1
i=0
while f>e:
	i=i+1
	n=n*i
	a=a*11
	f=a/n
print('n равно',i , 'при 10 < t < 11')
