from tkinter import *
from tkinter import ttk
import os

def click():
    global i
    b = Button(master=mainframe, text="Like", width=10)
    b.grid(column=0, row=3, sticky=W, padx=5, pady=5)

    c = ttk.Button(master=mainframe, text="Comment", width = 10, command=unclick)
    c.grid(column=1, row=3, sticky=EW, padx=5, pady=5)

    d = Label(master=mainframe, text="               ")
    d.grid(column=2, row=3, sticky=EW, padx=5, pady=5)

    e = Label(master=mainframe, text="               ")
    e.grid(column=3, row=3, sticky=EW, padx=5, pady=5)

    f = Label(master=mainframe, text="25 Likes")
    f.grid(column=4, row=3, sticky=E, padx=5, pady=5)
    
    global entry
    entry = ttk.Entry(width=50)
    entry.grid(column=0, row=i, sticky=W, padx=7, pady=5)
    
    global send_b
    send_b = Button(text="Send", width=5, command=comment)
    send_b.grid(column=0, row=i, sticky=E, padx=7, pady=5)

def unclick():
    b = Button(master=mainframe, text="Like", width=10)
    b.grid(column=0, row=3, sticky=W, padx=5, pady=5)

    c = Button(master=mainframe, text="Comment", width = 10, command=click)
    c.grid(column=1, row=3, sticky=EW, padx=5, pady=5)

    d = Label(master=mainframe, text="               ")
    d.grid(column=2, row=3, sticky=EW, padx=5, pady=5)

    e = Label(master=mainframe, text="               ")
    e.grid(column=3, row=3, sticky=EW, padx=5, pady=5)

    f = Label(master=mainframe, text="25 Likes")
    f.grid(column=4, row=3, sticky=E, padx=5, pady=5)

    if 'entry' in globals():
        entry.grid_remove()
        send_b.grid_remove()

def comment():
    global i
    entryString = entry.get()
    entry.delete(0, END)
    entry.grid_remove()
    send_b.grid_remove()
    entry_str = Label(text=entryString)
    entry_str.grid(column=0, row=i, sticky=W, padx=7, pady=5)
    i += 1
    entry.grid(column=0, row=i, sticky=W, padx=7, pady=5)
    send_b.grid(column=0, row=i, sticky=E, padx=7, pady=5)

i = 4

root = Tk()
root.title("POST - driven app")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

logo = PhotoImage(file='../img/like.png')
photoimage = logo.subsample(2, 2)

a = Label(master=mainframe, image=photoimage)
a.grid(column=0, row=0, sticky=NSEW, rowspan=3, columnspan=5)

unclick()

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
