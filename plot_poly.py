from Tkinter import *
master = Tk()
master.title("PLOT")
w = Canvas(master, width=500, height=500)
w.pack()
crl = "#ff0000"
w.create_rectangle(0, 0, 500,500, fill="#ffffff")

for x in range (-250,250):
	y = x*x + 2*x + 1
	h,k = x + 250, 250 - y
	w.create_line(h,k, h+1,k+1, fill="#000000")
	
xlist=[]
ylist=[]
for x in range (-250,250):
	y = x*x + 3*x - 10
	h,k = x + 250, 250 - y
	xlist.append(x)
	ylist.append(y)
	
for i in (xlist - 1):
	w.create_line(xlist[i],ylist[i], fill="#00ff00")
mainloop()
