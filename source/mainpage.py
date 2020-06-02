from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import broadcast_interface as p
import login_interface as login
import like_and_comment_interface as li
import profile_interface as profile

def runapp(namaemail):
    print(namaemail)
    
    class windowclass():
        def __init__(self, master):
            self.master = master
            self.btn = ttk.Button(master, text="Profile", command=self.command)
            self.btn.pack()

        def command(self):
            self.nama = namaemail
            profile.runprofile(self.nama)

    class Demo2:
        def __init__(self, master):
            self.master = master
            self.frame = ttk.Frame(self.master)
            self.quitButton = ttk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
            self.quitButton.pack()
            self.frame.pack()
        def close_windows(self):
            self.master.destroy()

    class PostBttn():
        def __init__(self, master):
            self.master = master
            self.btn = ttk.Button(master, text="PostStatus", command=self.command)
            self.btn.pack()

        def command(self):
            self.nama = namaemail
            p.runapp()

    class TimelineBttn():
        def __init__(self, master):
            self.master = master
            self.btn = ttk.Button(master, text="Timeline", command=self.command)
            self.btn.pack()

        def command(self):
            li.runapp()
            
    def on_closing():
        if messagebox.askokcancel("Keluar", "Apakah anda ingin keluar?"):
            root.destroy()

    root = Tk()
    root.title("window")
    root.geometry("350x350")
    wc = windowclass(root)
    ps = PostBttn(root)
    TimelineBttn(root)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
