import numpy as np
import matplotlib.pyplot as plt
import random
import sys

file = open("dataset2/"+ sys.argv[1],"r")

s = file.readline()
s = file.readline()
i = s.index(",",40)
no_of_vehicles = int(s[40:i])

s = file.readline()
s = file.readline()
n = int(s[12:])

s = file.readline()
s = file.readline()
Q = int(s[11:])

s = file.readline()
s = file.readline()
t = s.split(' ')
x0 = int(t[2])
y0 = int(t[3])

x = np.array([0]*n)
y = np.array([0]*n)

for i in range(1,n):
	s = file.readline()
	t = s.split(' ')
	x[i] = int(t[2])-x0
	y[i] = int(t[3])-y0

s = file.readline()
s = file.readline()
demand = np.array([0]*n)
for i in range(1,n):
	s = file.readline()
	t = s.split(' ')
	demand[i] = t[1]
print(demand)

file.close()

f = open("graph.data", "w")
f.write("n\n")
f.write(str(n)+'\n')
f.write("type_of_vehicle\n")
f.write(str(1)+'\n')
f.write("capacities\n")
f.write(str(Q) + "\n")
f.write("no._of_vehivcle\n")
f.write(str(no_of_vehicles) + '\n')
f.write("nodes\n")
for i in range(0,n):
	f.write(str(x[i]) + " " + str(y[i]) + " "+ str(demand[i])+'\n')
f.close()

plt.scatter(x[1:], y[1:], c='b')
plt.plot(x[0], y[0], c='r', marker='s')
plt.show()
