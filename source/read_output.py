import numpy as np
import matplotlib.pyplot as plt

file1 = open("graph.data","r")
file2 = open("vrp.sol", "r")

s = file1.readline()
s = file1.readline()
n = int(s)
x = np.array([0.0]*n)
y = np.array([0.0]*n)

while( s.strip() != 'nodes'):
	s = file1.readline()

for i in range(0,n):
	s = file1.readline()
	t = s.split(' ')
	x[i] = float(t[0].strip())
	y[i] = float(t[1].strip())

edges = file2.readlines()
colors = []
diff = 1/len(edges)
cutoff = len(edges)/3
for i in range(0,len(edges)):
	if (i < cutoff):
		colors = colors + [(i*diff,0,0)]
	elif(i < 2*cutoff):
		colors = colors + [(np.random.rand(),(i-cutoff)*diff,0)]
	else:
		colors = colors + [(np.random.rand(),np.random.rand(),(i-2*cutoff)*diff)]

k = -1
for l in edges:
	k = k + 1
	l = l.strip()
	t = l.split(' ')
	for i in range(2,len(t)):
		start = int(t[i-1].strip())
		end = int(t[i].strip())
		plt.plot([x[start],x[end]],[y[start],y[end]], color = colors[k])

plt.scatter(x[1:], y[1:], c='b')
plt.plot(x[0], y[0], c='r', marker='s')
plt.show()