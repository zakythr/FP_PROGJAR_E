from tkinter import *
from tkinter import ttk
import login_interface as login


def runprofile(nama_akun):
    print(nama_akun)
    
    root = Toplevel()
    root.title("Profil")
    root.geometry("350x350")
    
    frame1 = Frame(root)
    frame2 = Frame(root)
    
    img = PhotoImage(file="../img/profile/default.png")   
    photo = img.subsample(2,2)   
    a = Label(frame1, image = photo)
    a.grid(column=0, row=0, sticky=NSEW, padx=5, pady=5, columnspan=4)
    a.pack(side = LEFT)
    
    username = Label(frame2, text= nama_akun)
    username.pack(side = LEFT)
    
    frame1.pack()
    frame2.pack()
    
    root.mainloop()
    
