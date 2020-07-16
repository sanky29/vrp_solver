import numpy as np 
import matplotlib.pyplot as plt
from docplex.mp.model import Model
rnd = np.random
rnd.seed(0)


file1 = open("graph.data","r")
s = file1.readline()
s = file1.readline()
n = int(s)
s = file1.readline()
s =  file1.readline()
s = file1.readline()
s =  file1.readline()
Q = []
while(s.strip() != 'no._of_vehivcle'):
	Q.append(int(s.strip()))
	s = file1.readline()
nv = []
s = file1.readline()
while(s.strip() != 'nodes'):
	nv.append(int(s.strip()))
	s = file1.readline()

s = file1.readline()
loc_x = []
loc_y = []
temp = []
for i in range(0,n):
	s = s.strip()
	t = s.split(' ')
	loc_x.append(float(t[0]))
	loc_y.append(float(t[1]))
	temp.append(int(t[2]))
	s = file1.readline()
N = [i for i in range(1,n)]
V = [0]+N
q = {i: temp[i] for i in N}
T = [i for i in range(0,len(Q))]

SA = [(i, j) for i in V for j in V if i != j]
A = [(k,i, j) for k in T for i in V for j in V if i != j]
c = {(i, j): np.hypot(loc_x[i]-loc_x[j], loc_y[i]-loc_y[j]) for i, j in SA}
UA = [(k,i) for k in T for i in V]
mdl = Model('CVRP')

x = mdl.binary_var_dict(A, name='x')

u = mdl.continuous_var_dict(UA, name='u')

for k in T:
	for i in V:
		u[k,i].set_ub(Q[k])

mdl.minimize(mdl.sum(c[i, j]*(mdl.sum(x[k,i,j] for k in T)) for i, j in SA))

mdl.add_constraints(mdl.sum(x[k, i, j] for k in T for j in V if j != i) == 1 for i in N)
mdl.add_constraints(mdl.sum(x[k, i, j] for k in T for i in V if i != j) == 1 for j in N)

mdl.add_constraints(mdl.sum(x[k, i, j] for i in V if i != j) == mdl.sum(x[k, j, i] for i in V if i != j) for j in V for k in T)

mdl.add_indicator_constraints(mdl.indicator_constraint(x[k,i,j], u[k,i]+q[j] == u[k,j]) for k in T for i, j in SA if i != 0 and j != 0)
mdl.add_constraints((mdl.sum(x[k,0,i] for i in N) <= nv[k]) for k in T)
#mdl.add_constraints(mdl.sum(u[k,i] for k in T) >= q[i] for i in N)
mdl.add_indicator_constraints(mdl.indicator_constraint(x[k,i,j] , u[k,j] >= q[j]) for k in T for i in V for j in N if i != j)

mdl.parameters.timelimit = 200
solution = mdl.solve(log_output=True)
active_arcs = [a for a in A if x[a].solution_value > 0.9]

f = open("vrp.sol", "w")
for i in T:
	s = ""
	a = {b[1] : b[2] for b in active_arcs if b[0] == i}
	print (a)
	s = ("agent_%d 0 " % i)
	if(len(a) > 0):
		t = str(a[0])
		while(t != '0'):
			s = s + t + ' '
			t = str(a[int(t)])
		s = s + "0\n"
		f.write(s)
f.close()