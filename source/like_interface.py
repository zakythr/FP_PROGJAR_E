from tkinter import *
from tkinter import ttk

def like():
    global jumlahLike
    jumlahLike += 1
    tambah = jumlahLike
    button = Button(mainframe, text="Liked", bg='green', width=9)
    button.grid(row=3, column=0)
    ttk.Label(mainframe, text="%d Liked" % tambah).grid(row=3, column=4)

root = Tk()
root.title("POST - driven app")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
jumlahLike = 25

logo = PhotoImage(file="yuki.png")
photoimage = logo.subsample(2, 2)

w1 = Label(mainframe, image=photoimage).grid(row=0, column=0, columnspan=10, rowspan=3, sticky=W+E+N+S, padx=5, pady=5)
ttk.Button(mainframe, text="Like", command=like).grid(row=3, column=0)
ttk.Button(mainframe, text="Comment").grid(row=3, column=1)
ttk.Label(mainframe, text="                 ").grid(row=3, column=2)
ttk.Label(mainframe, text="                 ").grid(row=3, column=3)
ttk.Label(mainframe, text="%d Liked" % jumlahLike).grid(row=3, column=4)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()