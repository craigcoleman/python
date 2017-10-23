from Tkinter import *
import math
master = Tk()
master.title("PLOT")
w = Canvas(master, width=500, height=500)
w.pack()
crl = "#ff0000"
w.create_rectangle(0, 0, 500,500, fill="#ffffff")
w.create_line(0,250,500,250, fill="#0000ff")
w.create_line(250,0,250,500, fill="#ff0000")

xlist=[]
ylist=[]
c = 0
for x in range (-250,250):
	y = 20*math.cos(x)
	h,k = x + 250, 250 - y
	xlist.append(h)
	ylist.append(k)

for i in range(len(xlist) - 1):
	print (xlist[i]," ",ylist[i])
	w.create_line(xlist[i],ylist[i],xlist[i+1],ylist[i+1], fill="#00ff00")

mainloop()
