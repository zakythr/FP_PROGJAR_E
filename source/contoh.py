# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 00:19:05 2020

@author: ASUS
"""

from tkinter import *
from tkinter import ttk
import login_interface as login

nama_akun = login.getNamaAkun()


def on_closing():
    if messagebox.askokcancel("Keluar", "Apakah anda ingin keluar?"):
        root.destroy()

root = Tk()
root.title("window")
root.geometry("350x350")
def additem():
    items.set(items.get() + 1)

f = Frame(root)

items = IntVar()
items.set(14)

l0 = Label(f, text="I have")
l1 = Label(f, textvariable=items)
l2 = Label(f, text="items")

b = Button(root, text="Add item", command=additem)

l0.pack(side=LEFT)
l1.pack(side=LEFT)
l2.pack(side=LEFT)

f.pack()
b.pack()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
    

    
