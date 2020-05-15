from tkinter import *
from tkinter import ttk

master = Tk()
status = Label(master, text="Status: ", width=6)
status.pack(side=LEFT, anchor=N, padx=5, pady=5)
insertStatus = Text(master)
insertStatus.pack(fill=BOTH, pady=5, padx=5, expand=True)
master.mainloop()