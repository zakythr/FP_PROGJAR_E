from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import login_interface as li
from datetime import datetime 


def runapp(namaemail):
    def sendpost():
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H-%M")
        filename = namaemail +"_"+timestamp
        isistatus = insertStatus.get('1.0','end-1c')
        f = open("db/" +filename+".txt", "a")
        f.write(isistatus)
        f.close()
        messagebox.showinfo("post status", "post status berhasil")
        master.destroy()



    master = Tk()
    master.title("What's on your mind?")
    status = Label(master, text="Status: ", width=6)
    status.pack(side=LEFT, anchor=N, padx=5, pady=5)
    insertStatus = Text(master)
    insertStatus.pack(fill=BOTH, pady=5, padx=5, expand=True)
    tombolKirim = Button(master, text="Kirim", command=sendpost)
    tombolKirim.pack(side=RIGHT, padx=5, pady=5)
    tombolCancel = Button(master, text="Cancel", command=master.quit)
    tombolCancel.pack(side=RIGHT)
    master.mainloop()



