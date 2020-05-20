from tkinter import Frame, Tk, BOTH, Text, Menu, END, filedialog, Button, Label, LEFT, RIGHT, N
from tkinter import ttk

class membuatStatus(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.window = parent
        self.initUI()

    def initUI(self):
        self.window.title("What's on your mind?")
        self.pack(fill=BOTH, expand=True)

        self.status()
        self.tombol()
        self.buatMenubar()
    
    def status(self):
        teksField = Frame(self)
        teksField.pack(fill=BOTH, expand=True)

        self.teks = Label(teksField, text="Status :", width=6)
        self.teks.pack(side=LEFT, anchor=N, padx=5, pady=5)

        self.masukkanKeWindow = Text(teksField)
        self.masukkanKeWindow.pack(fill=BOTH, pady=5, padx=5, expand=True)

    def tombol(self):
        tombolTutup = Button(self, text="Kirim", command=self.quit)
        tombolTutup.pack(side=RIGHT, padx=5, pady=5)

        tombolOke = Button(self, text="Cancel", command=self.quit)
        tombolOke.pack(side=RIGHT)
    
    def buatMenubar(self):
        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.bukaFile)
        menubar.add_cascade(label="File", menu=fileMenu)
    
    def bukaFile(self):
        tipeFile = [('Python files', '*.py'), ('All files', '*')]
        bukaFile = filedialog.Open(self, filetypes=tipeFile)
        isiFile = bukaFile.show()

        if isiFile != '':
            teks = self.bacaFile(isiFile)
            self.masukkanKeWindow.insert(END, teks)

    def bacaFile(self, namaFile):
        f = open(namaFile, "r")
        teks = f.read()
        return teks


if __name__ == '__main__':
    root = Tk()
    root.geometry("300x450")
    app = membuatStatus(root)
    root.mainloop()