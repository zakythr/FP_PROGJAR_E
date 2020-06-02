from tkinter import *
from tkinter import ttk
import login_interface as login
from os import path
import shutil
import os

pathprofile="../img/profile/"

def runprofile(nama_akun):
    print(nama_akun)
    
    root = Toplevel()
    root.title("Profil")
    root.geometry("350x350")
    
    frame1 = Frame(root)
    frame2 = Frame(root)
    frame3 = Frame(root)
    
    if(path.exists(pathprofile+nama_akun+".png")):
        img = PhotoImage(file="../img/profile/"+nama_akun+".png")   
    else:
        img = PhotoImage(file="../img/profile/default.png")  
    photo = img.subsample(2,2)
    a = Label(frame1, image = photo)
    a.grid(column=0, row=0, sticky=NSEW, padx=5, pady=5, columnspan=4)
    a.pack(side = LEFT)   
    
    username = Label(frame2, text= nama_akun)
    username.pack(side = LEFT)
    
    def unggah():
        try:
            if(path.exists(pathprofile+nama_akun+".png")):
                os.remove(pathprofile+nama_akun+".png")
            pathfotoprofil = pathfoto.get()
            shutil.copy(pathfotoprofil,"../img/profile/"+nama_akun+".png")
            root.destroy()
            runprofile(nama_akun)
            print(pathfotoprofil)
        except Exception as e:
            ttk.Label(frame3, text="Tidak terdapat gambar").grid(column=11, row=2, sticky=W)
    
    pathfoto = StringVar()
    
    ttk.Label(frame3, text="Path File: ").grid(column=0, row=1, sticky=W)
    account_text = ttk.Entry(frame3, width=30, textvariable=pathfoto)
    account_text.grid(column=2, row=1, sticky=(W, E))
    ttk.Label(frame3, text="(harus berekstensi png)").grid(row=3, sticky=W)
    ttk.Button(frame3, text = "Unggah", command = unggah).grid(row = 10, sticky=N, columnspan=5)
    
    frame1.pack()
    frame2.pack()
    frame3.pack()
    
    root.mainloop()
    
#runprofile("into")