
import gui
import numpy as np 
import os
rnd = np.random
gui.main()
arg = []
def dohere():
    global arg
    if(gui.default == 1):
        arg = [10,2,[rnd.randint(1,10) for i in range(0,10)],[rnd.randint(50,100) for i in (0,2)],[1,1],rnd.rand(10)*200,rnd.rand(10)*100,200]
    else:
        arg = [gui.N]
        arg = arg + [gui.Q]
        arg = arg + [gui.D]
        arg = arg + [gui.CA]
        arg = arg + [[1]*(gui.Q)]
        arg = arg + [np.array(gui.cx)]
        arg = arg + [np.array(gui.cy)]
        arg = arg + [200]
dohere()
print (arg)
f = open("graph.data", "w")
f.write("n\n")
f.write(str(arg[0])+'\n')
f.write("type_of_vehicle\n")
f.write(str(arg[1])+'\n')
f.write("capacities\n")
for k in arg[3]:
    f.write(str(k) + "\n")
f.write("no._of_vehivcle\n")
for k in arg[4]:
    f.write(str(k) + "\n")
f.write("nodes\n")
for i in range(0,arg[0]):
    print(i, arg[5][i], arg[6][i], arg[2][i])
    f.write(str(arg[5][i]) + " " + str(arg[6][i]) + " "+ str(arg[2][i])+'\n')
f.close()

if (gui.mode == 1):
    os.system("python cp.py")
    os.system("python read_output.py")
else:
    os.system("construction_hurestic.exe")
    os.system("python read_output.py")