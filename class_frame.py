from Tkinter import *

class ABC(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        ABC.make_widgets(self)

    def make_widgets(self):
        self.parent.title("Simple Prog")
        self.parent.title("Simple Prog")
        
root = Tk()
app = ABC(master=root)
app.master.title("Simple Prog")
app.mainloop()
root.destroy()
