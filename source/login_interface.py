from tkinter import *
from tkinter import ttk
import imaplib
import webbrowser

def login():
    try:
        akun = account.get()
        pswrd = password.get()
        mail = imaplib.IMAP4_SSL ("imap.gmail.com")
        mail.login(akun, pswrd)
        
        ttk.Label(mainframe, text="Login Succesfull").grid(column=4,row=9,sticky=W)

    except Exception as e:
        ttk.Label(mainframe, text="Login gagal, silahkan cek email dan password").grid(column=4,row=9,sticky=W)
        
        
def setup(event):
    webbrowser.open_new(r"https://www.google.com/settings/security/lesssecureapps")
   
    
def runapp():
    root = Tk()
    root.title("POST - driven app")
    root.iconbitmap(r'lib\app.ico')
    
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    
    account = StringVar()
    password = StringVar()
    
    a = Label(mainframe, text="Less secure app access dinyalakan dahulu", fg="blue", cursor="hand2")
    a.grid(columnspan=2,column=3, row=0, sticky=N)
    a.bind("<Button-1>", setup)
    
    
    ttk.Label(mainframe, text="Email: ").grid(column=0, row=1, sticky=W)
    account_entry = ttk.Entry(mainframe, width=30, textvariable=account)
    account_entry.grid(column=4, row=1, sticky=(W, E))
    
    ttk.Label(mainframe, text="Password: ").grid(column=0, row=2, sticky=W)
    password_entry = ttk.Entry(mainframe, show="*", width=30, textvariable=password)
    password_entry.grid(column=4, row=2, sticky=(W, E))
    
    ttk.Button(mainframe, text="Login", command=login).grid(column=4,row=8,sticky=N)
    
    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
    
    account_entry.focus()
    
    root.mainloop()
    