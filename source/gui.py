from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

N = -1
cx = []
cy = []
Q = -1
CA = []
D = [0]
mode = 0
default = 0

def do_something(window,N,l):
    window.title("Put delivery locations")
    m = int(N/28)
    t = str((m+1)*200)
    window.geometry( t+ 'x700')
    lx = Label(window,text = "x coodinate")
    lx.place(x = 0, y =0)
    ly = Label(window,text = "y coodinate")
    ly.place(x =100, y =0)
    rows = []
    for i in range(N):
        yc = i%28
        xc = int(i/28)
        ex = Entry(window,width = 11)
        ex.place(x = xc*200+50, y = (yc+2)*20, anchor = "center")
        ex.insert(END,'%d' % i)
        ey = Entry(window,width = 11)
        ey.place(x = xc*200+130, y =(yc+2)*20 , anchor = "center")
        ey.insert(END, '%d' % i)
        rows.append([ex,ey])

    def onPress():
        try:
            for i in range(0,N):
                fx = float((rows[i][0]).get())
                fy = float((rows[i][1]).get())
                cx.append(fx)
                cy.append(fy)
            l.configure(text = "got coordinates")
            window.destroy()
        except ValueError:
            messagebox.showinfo('Error', 'Enter valid number of coordinate of '+str(i))

    btn = Button(window, text="Submit", command=onPress)
    btn.place(x=int(t)/2, y=620, anchor="center")
    window.mainloop()

def do_dil(window,Q,l):
    window.title("Put delivery agents")
    m = int(Q/28)
    t = str((m+1)*200)
    window.geometry( t+ 'x700')
    lx = Label(window,text = "name")
    lx.place(x = 0, y =0)
    ly = Label(window,text = "capacity")
    ly.place(x =100, y =0)
    rows = []
    for i in range(Q):
        yc = i%28
        xc = int(i/28)
        ex = Label(window,text = 'agent_%d' % i)
        ex.place(x = xc*200+50, y = (yc+2)*20, anchor = "center")
        ey = Entry(window,width = 11)
        ey.place(x = xc*200+130, y =(yc+2)*20 , anchor = "center")
        ey.insert(END, '%d' % i)
        rows.append(ey)

    def onPress():
        try:
            for i in range(0,Q):
                ci = int(rows[i].get())
                CA.append(ci)
            l.configure(text = "got agents info")
            window.destroy()
        except ValueError:
            messagebox.showinfo('Error', 'Enter valid number of coordinate of '+str(i))

    btn = Button(window, text="Submit", command=onPress)
    btn.place(x=int(t)/2, y=620, anchor="center")
    window.mainloop()
 
def do_demand(window,Q,l):
    window.title("Put delivery agents")
    m = int(Q/28)
    t = str((m+1)*200)
    window.geometry( t+ 'x700')
    lx = Label(window,text = "name")
    lx.place(x = 0, y =0)
    ly = Label(window,text = "demands")
    ly.place(x =100, y =0)
    rows = []
    for i in range(Q):
        yc = i%28
        xc = int(i/28)
        ex = Label(window,text = 'demand_%d' % (i+1))
        ex.place(x = xc*200+50, y = (yc+2)*20, anchor = "center")
        ey = Entry(window,width = 11)
        ey.place(x = xc*200+130, y =(yc+2)*20 , anchor = "center")
        ey.insert(END, '%d' % i)
        rows.append(ey)

    def onPress():
        try:
            for i in range(0,Q):
                di = int(rows[i].get())
                D.append(di)
            l.configure(text = "got demand info")
            window.destroy()
        except ValueError:
            messagebox.showinfo('Error', 'Enter valid number of coordinate of '+str(i))

    btn = Button(window, text="Submit", command=onPress)
    btn.place(x=int(t)/2, y=620, anchor="center")
    window.mainloop()

window = Tk()
window.geometry('1000x500')
window.title("Delivery system")
lbl = Label(window, text="WELCOME!!")
lbl.place(x=500, y=10, anchor="center")

lbl_nodes = Label(window, text="Number of delivery locations (including depot) :") 
lbl_nodes.place(x=320, y=40, anchor="center")

spin_nodes = Spinbox(window, from_=0, to=100, width=5)
spin_nodes.place(x=490, y=40, anchor="center")

bt_node = Label()

def show_graph():
    global cx
    global cy
    plt.scatter(cx[1:], cy[1:], c='b')
    for i in range(0,N):
        plt.annotate('%d' % i, (cx[i]+2, cy[i]))
    plt.plot(cx[0], cy[0], c='r', marker='s')
    plt.axis('equal')
    plt.show()
def clicked_nodes():
    global N
    N = int(spin_nodes.get())
    if(N <= 0):
        messagebox.showinfo('Error', 'Enter valid number of nodes')
    else:
        temp = Label(window, text = '          ', fg= 'green')
        temp.place(x = 800, y = 40, anchor = 'center')
        bt_node.destroy()
        b = Button(window, text = "show graph", command = show_graph)
        b.place(x = 900, y = 40, anchor = 'center')
        do_something(Toplevel(window),N,temp)
        
bt_node = Button(window, text="Give coordinates", command=clicked_nodes)
bt_node.place(x=600, y=40, anchor="center")



lbl_delivery = Label(window, text="Number of delivery agents :") 
lbl_delivery.place(x=320, y=80, anchor="center")

spin_agent = Spinbox(window, from_=0, to=100, width=5)
spin_agent.place(x=490, y=80, anchor="center")


bt_dil = Label()
def clicked_delivery():
    global Q
    Q = int(spin_agent.get())
    if(Q <= 0):
        messagebox.showinfo('Error', 'Enter valid number of delivery agents')
    else:
        temp = Label(window, text = '          ', fg= 'green')
        temp.place(x = 800, y = 80, anchor = 'center')
        bt_dil.destroy()
        do_dil(Toplevel(window),Q,temp)
        
bt_dil = Button(window, text="Give agent info", command=clicked_delivery)
bt_dil.place(x=600, y=80, anchor="center")


bt_demand = Label()
def clicked_demand():
    global N
    if(N <= 1):
        messagebox.showinfo('Error', 'Enter valid number of delivery locations')
    else:
        temp = Label(window, text = '       ', fg= 'green')
        temp.place(x = 500, y = 120, anchor = 'center')
        bt_demand.destroy()
        do_demand(Toplevel(window),N-1,temp)


#the demand buttton
bt_demand = Button(window, text="Add demand", command=clicked_demand)
bt_demand.place(x=490, y=120, anchor="center")


la_mode = Label(window, text= "mode of solver (prefered construction hursetic)")
la_mode.place(x = 200, y = 160 , anchor = 'center')

v = IntVar()
v.set(0)

def choose_mode():
    global mode
    mode = v.get()

bconst = Radiobutton(window, text="construction hursetic", variable=v,  command=choose_mode,value= 0)
bconst.place(x = 500, y = 160, anchor = 'center')
bcplex = Radiobutton(window, text="cplex", variable=v,  command=choose_mode,value= 1)
bcplex.place(x = 700, y = 160, anchor = 'center')



intype = Label(window, text= "use default input?")
intype.place(x = 200, y = 200 , anchor = 'center')

v2 = IntVar()
v2.set(0)

def choose_in():
    global default
    default = v2.get()

dno = Radiobutton(window, text="no", variable=v2,  command=choose_in,value= 0)
dno.place(x = 500, y = 200, anchor = 'center')
dyes = Radiobutton(window, text="yes", variable=v2,  command=choose_in,value= 1)
dyes.place(x = 700, y = 200, anchor = 'center')

def final_solve():
    global N,Q,D
    if (default == 0):
        if (N < 1):
            messagebox.showinfo('Error', 'Delivery locations should be more than one')
        elif (Q <= 0):
            messagebox.showinfo('Error', 'Delivery agents should be more than zero')
        elif (len(D) != N):
            messagebox.showinfo('Error', 'Enter demand')
        else:
            window.destroy()
    else:
        window.destroy()

bt_solve = Button(window, text="Solve", command=final_solve)
bt_solve.place(x=490, y=240, anchor="center")


def main():
    global window
    window.mainloop()
main()
print (N, cx, cy, Q, CA, mode, default)