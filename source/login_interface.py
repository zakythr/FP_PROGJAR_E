from tkinter import *
from tkinter import ttk
import smtplib
import imaplib
import webbrowser
import config
import mainpage
from tkinter import messagebox
def runapp():
    
    def on_closing():
            if messagebox.askokcancel("Keluar", "Apakah anda ingin keluar?"):
                root.destroy()
    def login():
        try:
            akun = account.get()
            pswrd = password.get()
            mail = imaplib.IMAP4_SSL ("imap.gmail.com")
            mail.login(akun, pswrd)
            ttk.Label(mainframe, text="Login Succesfull").grid(row=9,sticky=N, columnspan=5)
            subject = "Login Berhasil"
            msg = "Selamat , anda berhasil login aplikasi POST-driven app, selamat menikmati"
            send_mail(subject,msg)
            root.withdraw()
            mainpage.runapp(akun)
        except Exception as e:
            ttk.Label(mainframe, text="Login gagal, silahkan cek email dan password").grid(columnspan=5,row=9,sticky=N)

            
    def setup(event):
        webbrowser.open_new(r"https://www.google.com/settings/security/lesssecureapps")

    def send_mail(subject,msg):
        try:
            sendr = account.get()
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(config.EMAIL_ADDRESS,config.PASSWORD)
            message = 'Subject: {}\n\n{}'.format(subject, msg)
            server.sendmail(config.EMAIL_ADDRESS,sendr, message)
            server.quit()
        except:
            print(".")
 
    

    root = Tk()
    root.title("POST - driven app")
    root.iconbitmap(r'lib\app.ico')

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    account = StringVar()
    password = StringVar()

    link = Label(mainframe, text="Less secure app access dinyalakan dahulu", fg="blue", cursor="hand2")
    link.grid(columnspan=2,column=1, row=0, sticky=N)
    link.bind("<Button-1>", setup)


    ttk.Label(mainframe, text="Email: ").grid(column=0, row=1, sticky=W)
    account_text = ttk.Entry(mainframe, width=40, textvariable=account)
    account_text.grid(column=2, row=1, sticky=(W, E))

    ttk.Label(mainframe, text="Password: ").grid(column=0, row=2, sticky=W)
    password_text = ttk.Entry(mainframe, show="*", width=40, textvariable=password)
    password_text.grid(column=2, row=2, sticky=(W, E))

    ttk.Button(mainframe, text="Login", command=login).grid(row=8,sticky=N, columnspan=5)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    account_text.focus()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
    
