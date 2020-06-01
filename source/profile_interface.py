from tkinter import *
from tkinter import ttk
import login_interface as login


#nama_akun = login.getNamaAkun()

def runprofile():
    
    def on_closing():
        if messagebox.askokcancel("Keluar", "Apakah anda ingin keluar?"):
            root.destroy()
    
    root = Tk()
    root.title("Profil")
    root.geometry("350x350")
    
    frame1 = Frame(root)
    frame2 = Frame(root)
    
    img = PhotoImage(file="../img/profile/default.png")   
    img = img.subsample(2,2)   
    a = Label(frame1, image = img)
    a.grid(column=0, row=0, sticky=NSEW, padx=5, pady=5, columnspan=4)
    a.pack(side = LEFT)
    
    username = Label(frame2, text= "aaaa")
    username.pack(side = LEFT)
    
    frame1.pack()
    frame2.pack()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
    

        