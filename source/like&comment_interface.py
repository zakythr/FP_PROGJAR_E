from tkinter import *
from tkinter import ttk

i = 2

root = Tk()
root.title(string='POST - driven app')

frame1 = Frame(root)
frame1.pack(side=TOP,fill=X)

frame2 = Frame(root)
frame2.pack(side=TOP, fill=X)

def like():
    global btn1_like, label1_like, likeCount
    likeCount = likeCounter(0)
    btn1_like = Button(likebar, width=8, text='Liked', command=unlike, bg='green')
    btn1_like.grid(column=0, row=1, sticky=E,padx=5,pady=5)
    label1_like = Label(likebar, text='%d Like' % likeCount)
    label1_like.grid(column=3, row=1, sticky=EW,padx=5,pady=5)

def unlike():
    global likeCount
    likeCount = likeCounter(1)
    btn1_like.grid_remove()
    label1_like.grid_remove()

def runLikeComment():
    # ***** POST ******
    logo = PhotoImage(file='yuki.png')
    photoimage = logo.subsample(2, 2)

    a = Label(frame1, image=photoimage)
    a.grid(column=0, row=0, sticky=NSEW, padx=5, pady=5, columnspan=4)

    # **** LIKE + COMMENT *******
    btn1 = Button(likebar, width=8, text='Like', command=like)
    btn2 = Button(likebar, width=8, text='Comment', command=click)
    btn1.grid(column=0, row=1, sticky=E,padx=5,pady=5)
    btn2.grid(column=1, row=1, sticky=E,padx=5,pady=5)
    space = Label(likebar, text=' ', width=9)
    space.grid(column=2, row=1, sticky=EW,padx=5,pady=5)
    label1 = Label(likebar, text='%d Like' % likeCount)
    label2 = Label(likebar, text='%d Comment' %commentCount)
    label1.grid(column=3, row=1, sticky=EW, padx=5, pady=5)
    label2.grid(column=4, row=1, sticky=EW, padx=5, pady=5)

    root.mainloop()
