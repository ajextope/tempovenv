import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import myclass.dbConnection as db


myEmail =''
def showForgot(email):
    def clearBox():
        email.set('')
        token.set('')
        newpassword.set('')
        repeatPassword.set('')
        
    def change():
        if (email.get() and token.get() and newpassword.get() and repeatPassword.get()):
            if newpassword.get() == repeatPassword.get():
               mydb = db.dbConnection()
               
               if(mydb.changeDb(newpassword.get(),email.get(), token.get()) == True):
                     messagebox.showinfo('Updated Record', 'Record has been updated successfully.')              
            else:
                messagebox.showwarning('Unmatch Password', 'Password entered does NOT match.')
                return
        else:
            messagebox.showinfo('Blank Field', 'Field(s) are required.')
            return
       
        
        
    global myEmail 
    myEmail= email
    __frameTop= '#fff'
    __frameBottom= '#214254'
    #Starting Tk function for drawing the interface
    rt= Toplevel()
    rt.grab_set()
    rt.focus_force()
    rt.title('New Password Form - CBT')
    width = 450
    height = 250
    sw = rt.winfo_screenwidth()
    sh = rt.winfo_screenheight()
    x = sw // 2 - width // 2
    y = sh // 2 - height // 2
    rt.geometry(f'{width}x{height}+{x}+{y}')
    rt.resizable(0, 0)


    lbltitle = ttk.Label(rt,text='FORGOT PASSWORD', justify='center')
    lbltitle.place(relx=0.4, rely=0.04)

    lblEmail = ttk.Label(rt,text='Email:')
    lblEmail.place(x=40, y=60)
    lblTokens = ttk.Label(rt,text='Token Received:')
    lblTokens.place(x=40,y=100 )
    lblNewPassword = ttk.Label(rt,text='New Password:')
    lblNewPassword.place(x=40, y=140)
    lblRepeat = ttk.Label(rt,text='Repeat Password:')
    lblRepeat.place(x=40, y=180)

    #variables for textfield
    email= StringVar()
    token=StringVar()
    newpassword= StringVar()
    repeatPassword= StringVar()

    txtEmail = ttk.Entry(rt, width=50, textvariable=email, state='readonly')
    txtEmail.place(x=133, y=55, height=30)

    txtToken= ttk.Entry(rt,width=50, show='&', textvariable=token)
    txtToken.place(x=133,y=94, height=30)

    txtnewPassword= ttk.Entry(rt, width=50, textvariable=newpassword, show='&')
    txtnewPassword.place(x=133, y=136, height=30)

    txtrepeat= ttk.Entry(rt, width=50, show='&', textvariable=repeatPassword)
    txtrepeat.place(x=133, y=176, height=30)

    btnClear = ttk.Button(rt, text='Clear All', command=clearBox)
    btnClear.place(x=233, y=215)

    btnChange = ttk.Button(rt, text='Change', command=change)
    btnChange.place(x=327, y=215)

    email.set(myEmail)
    rt.mainloop()