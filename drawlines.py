from Tkinter import *

master = Tk()

w = Canvas(master, width=500, height=500)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
crl = "#ff0ff"
w.create_line( 10,10,20,20, fill="#ff00ff")
w.create_rectangle(50, 25, 150, 75, fill="blue")

mainloop()
