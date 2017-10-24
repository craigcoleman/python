#http://zetcode.com/gui/tkinter/drawing/
from tkinter import Tk, Canvas, Frame, BOTH
def dec3hex2(self,r,g,b):
                ################
                re = str(hex(r))
                re = re[2:len(re)]
                if len(re) < 2:
                        re = "0"+re
                ################
                gr = str(hex(g))
                gr = gr[2:len(gr)]
                if len(gr) < 2:
                        gr = "0"+gr
                ################
                bl = str(hex(b))
                bl = bl[2:len(bl)]
                if len(bl) < 2:
                        bl = "0"+bl
                #print (re,gr,bl)
                ###############
                return "#"+re+gr+bl             

class GraphWin(Frame):
        def __init__(self):
                super().__init__()   
                self.initUI()

        def initUI(self): 
                self.master.title("Colors")        
                self.pack(fill=BOTH, expand=1)
                canvas = Canvas(self)
                x = 0
                while x < 256:
                        y = 0
                        g,b = 0,0
                        for r in range(0,256):
                                hexcolor = dec3hex2(self,r,g,b)
                                #print (hexcolor)
                                canvas.create_line(x, y, x+1, y+1, fill=hexcolor)            
                                canvas.pack(fill=BOTH, expand=1)
                                g = g + 1
                                b = b + 1
                                y = y + 1
                        x = x + 1

def main():
	root = Tk()
        ex = GraphWin()
        root.geometry("500x500+100+100")
        root.mainloop()  

if __name__ == '__main__':
        main()   
