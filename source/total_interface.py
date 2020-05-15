from tkinter import *
from tkinter import ttk


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("FP PROGJAR E03")
        self.minsize(640,400)
        self.radioButton()

    def radioButton(self):
        
        self.radValues = StringVar()

        self.label = ttk.Label(self, text = "")
        self.label.place(x = 460, y = 220)

        self.btn1 = ttk.Radiobutton(self, text = "Like", value = 1, command = self.click)
        self.btn1.place(x = 20, y = 220)
        
        self.btn2 = ttk.Radiobutton(self, text = "Comment", value = 2, command = self.clickMe)
        self.btn2.place(x = 100, y = 220)

    def click(self):
        self.label.configure(text = "Total Like : 200" )
    
    def clickMe(self):
        self.label.configure(text = "Total Comment : 100" )


if __name__ == '__main__':
    root = Root()
    root.mainloop()