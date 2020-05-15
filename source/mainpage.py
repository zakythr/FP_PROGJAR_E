from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def runapp():
    
    class windowclass():
        def __init__(self, master):
            self.master = master
            self.btn = ttk.Button(master, text="Profile", command=self.command)
            self.btn.pack()

        def command(self):
            self.master.withdraw()
            toplevel = Toplevel(self.master)
            toplevel.geometry("350x350")
            app = Demo2(toplevel)
            

    class Demo2:
        def __init__(self, master):
            self.master = master
            self.frame = ttk.Frame(self.master)
            self.quitButton = ttk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
            self.quitButton.pack()
            self.frame.pack()
        def close_windows(self):
            self.master.destroy()

    def on_closing():
        if messagebox.askokcancel("Keluar", "Apakah anda ingin keluar?"):
            root.destroy()
            
    root = Tk()
    root.title("window")
    root.geometry("350x350")
    cls = windowclass(root)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()