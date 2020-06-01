from tkinter import *
from tkinter import ttk

i = 2

likeCount = 0
commentCount = 0

def runapp():
    root = Toplevel()
    root.title(string='POST - driven app')
    frame1 = Frame(root)
    frame1.pack(side=TOP,fill=X)
    frame2 = Frame(root)
    frame2.pack(side=TOP, fill=X)

    likebar = Frame(frame2)
    likebar.grid(column=0, row=1)

    commentbar = Frame(frame2)

    def likeCounter(x):
        global likeCount
        if x == 0: # add like
            likeCount += 1
        else: # subtract like
            likeCount -= 1
        return likeCount

    def commentCounter():
        global commentCount
        commentCount += 1
        return commentCount

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
            
    def click():
        global btn2_comment, entry, send_btn
        btn2_comment = ttk.Button(likebar, width=9, text='Comment', command=unclick)
        btn2_comment.grid(column=1, row=1, sticky=E,padx=5,pady=5)
        commentbar.grid(column=0,row=2)
        entry = ttk.Entry(commentbar, width=43)
        send_btn = Button(commentbar, text="Send", width=8, command=comment)
        entry.grid(column=0, row=i, sticky=W, padx=5, pady=5)
        send_btn.grid(column=1, row=i, sticky=E, padx=5, pady=5)

    def unclick():
        btn2_comment.grid_remove()
        entry.grid_remove()
        send_btn.grid_remove()
        commentbar.grid_remove()

    def comment():
        global i, commentCount, label2_comment
        if not entry.get():
            print('Input komentarmu')
        else:
            entryString = entry.get()
            entry.delete(0, END)
            commentCount = commentCounter() # add comment number
            label2_comment = Label(likebar, text='%d Comment' %commentCount)
            label2_comment.grid(column=4, row=1, sticky=EW,padx=5,pady=5)
            entry_str = Label(commentbar, text="nama pengguna : " + entryString)
            entry_str.grid(column=0, row=i, sticky=W, padx=5, pady=5)
            entry.grid_remove()
            send_btn.grid_remove()
            i += 1 # add row of comment entry
            entry.grid(column=0, row=i, sticky=W, padx=5, pady=5)
            send_btn.grid(column=1, row=i, sticky=E, padx=5, pady=5)

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
