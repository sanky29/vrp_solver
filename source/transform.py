import sys
import numpy as np
import matplotlib.pyplot as plt

def convert(x):
	c = np.square(np.array(x))
	ans = np.identity(len(x))
	for i in range(0,len(c)):
		for j in range(0,len(c[0])):
			ans[i][j] = (c[0][i] + c[0][j] - c[i][j])/2
	return ans

def transform(m1):
	m = convert(m1)
	x = np.linalg.eig(m.T.dot(m))
	i = np.identity(m.shape[0])
	v = x[1].T
	m1 = sys.float_info[3]
	m2 = 0.0
	i1 = 0
	i2 = 0
	for i in range(0,len(x[0])):
		if m1 < x[0][i]:
			i1 = i
			m1 = x[0][i]
		elif m2 < x[0][i]:
			i2 = i
			m2 = x[0][i]
	ans = np.zeros((2,len(m)))
	d = np.zeros((2,2))
	d[0][0] = np.sqrt(np.sqrt(x[0][i1]))
	d[1][1] = np.sqrt(np.sqrt(x[0][i2]))
	ans[0] = v[i1]
	ans[1] = v[i2]
	ans = (ans.T).dot(d)
	plt.plot(ans.T[0],ans.T[1], 'ro')
	k = 0
	for x,y in zip(ans.T[0],ans.T[1]):
		plt.annotate(str(k),(x,y),textcoords = "offset points",xytext =(0,10),ha='center')
		k = k+1 
	plt.show()
	return (ans)

#give distance matrix as input to the transform and using svd it computes x,y co ordinate
#0: Delhi, 1: Mumbai, 2: Hyderabad, 3: Kolkata, 4: jaipur, 5: guhawati
y = np.array(["Delhi","Mumbai","Hyderabad","Kolkata","jaipur","guhawati","chennai"])
x = np.array([[0,1418,1586,1532,274,1932,2210],[1418,0,710,2179,1148,2753,1338],[1586,710,0,1505,1453,2380,626],[1532,2179,1505,0,1551,1027,1678],[274,1148,1453,1551,0,1952,2077],[1932,2753,2380,1027,1952,0,2678],[2210,1338,626,1678,2077,2678,0]])
c = transform(x)
print(x)
d = np.identity(7)
for i in range(0,7):
	for j in range(0,7):
		d[i][j] = np.sqrt((c[i][0]-c[j][0])**2.0 + (c[i][1]-c[j][1])**2.0)
print(d)
a = np.sum(x)*49
error = (np.sum(np.square(d-x)))/a*100
print(error)