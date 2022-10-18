import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import bcrypt
from ttkthemes import THEMES, ThemedTk
import myclass.dbConnection as db
import frmExam
import frmForgotPassword


def loginApp():
    # examNumber=0
    def showForgot(*args):
        frmForgotPassword.forgotPassword()
        
        
    def signIn():
        global examNumber
        dbQuery = db.dbConnection()
        if(dbQuery.empty(examNoVar.get()) ==True or dbQuery.empty(passwordVar.get()) == True):
            messagebox.showwarning('Empty Field', 'The field(s) are required.')
            return
        if(not dbQuery.validate('^[0-9]*$',examNoVar.get())):
            messagebox.showwarning('Invalid Format', 'Number is expected.')
            return
            
        rs = dbQuery.getLogin(examNoVar.get())
        if rs==None:
            messagebox.showerror('Error Login', 'Password or Exam No is INVALID')
            return
        
        examNumber= examNoVar.get()
        hash_pass = rs[8]
        pwd = passwordVar.get()
        result=bcrypt.checkpw(pwd.encode('utf-8'),hash_pass.encode('utf-8'))
        if(result):
            messagebox.showinfo('Success', 'Your login is successful.')
            examNoVar.set('')
            passwordVar.set('')
            rt.destroy()
            frmExam.loadExamForm(examNumber)
            
        else:
            messagebox.showerror('Error Login', 'Password or Exam No is INVALID')
            
    
    
    __frameTop= '#fff'
    __frameBottom= '#214254'
    #Starting Tk function for drawing the interface
    rt = ThemedTk(theme='adapta', themebg=True)
    rt.title('Login - Computer Based Test')
    width = 375
    height = 442
    sw = rt.winfo_screenwidth()
    sh = rt.winfo_screenheight()
    x = sw // 2 - width // 2
    y = sh // 2 - height // 2
    rt.geometry(f'{width}x{height}+{x}+{y}')
    rt.resizable(0, 0)

    logobg = PhotoImage(file='./img/tempo-120.png')

    #divide the root into two parallel row
    rt.rowconfigure(0,weight=1)
    rt.rowconfigure(1,weight=4)
    rt.columnconfigure(0,weight=1)

    #styling the content  
    style = ttk.Style()

    style.configure('frame_top.TFrame', background=__frameTop)
    style.configure('frame_bottom.TFrame', background=__frameBottom)
    style.configure('title.TLabel', background=__frameTop, foreground='#d70a0a', font=('roboto', 24, 'bold', 'underline'))
    style.configure('description.TLabel', foreground=__frameBottom, background='#fff', font=('roboto', 10)) 

    style.configure('formframe.TFrame',background=__frameBottom)
    style.configure('formLabel.TLabel',background=__frameBottom, foreground='#fff', font=('roboto', 12))

    style.configure('formEntry.TEntry', font=('roboto', 12))
    style.configure('register.TLabel', foreground='#fff', background=__frameBottom, font=('roboto', 9, 'normal'))
    style.configure('reg.TLabel', foreground='#34edd1', background=__frameBottom, font=('roboto', 9, 'underline', 'bold'), highlightedforeground='red' )
    style.configure('btn.TButton', font=('6'))

    #placing frame on the root window Tk
    frame_top= ttk.Frame(rt, style='frame_top.TFrame')
    frame_bottom = ttk.Frame(rt, style='frame_bottom.TFrame')

    #display the frames on the root windows using grid geometry
    frame_top.grid(row=0, column=0, sticky='WENS')
    frame_bottom.grid(row=1, column=0, sticky='WENS', ipadx=10)

    lblLogo = ttk.Label(frame_top, image=logobg)
    lblLogo.pack(pady=3)
    lblTitle = ttk.Label(frame_top, text='Sign In', style='title.TLabel')
    lblTitle.pack(side='top', pady=7)

    lblDescription = ttk.Label(frame_top, text='Please fill in all the boxes below. All field(s) are required.', style='description.TLabel', wraplength=300)
    lblDescription.pack(pady=2)

    style.configure('forgot.TLabel', background=__frameBottom, font=('10'))
    
    
    #controls on frame Bottom 
    formFrame = ttk.Frame(frame_bottom, style='formframe.TFrame')
    formFrame.pack(pady=20, ipadx=10, ipady=10)

    lblExamNo = ttk.Label(formFrame, text='Exam No:',style='formLabel.TLabel')
    lblPassword = ttk.Label(formFrame, text='Password:', style='formLabel.TLabel')
    lblExamNo.grid(row=0,column=0, columnspan=2, sticky='we', pady=5, padx=5)
    lblPassword.grid(row=1, column=0,columnspan=2,sticky='we', pady=5,padx=5)
    examNoVar = StringVar()
    passwordVar= StringVar()
    #Entry control Widgets 
    txtExamNo = ttk.Entry(formFrame, justify='center', width=28,font=('arial', 12, 'bold'), textvariable=examNoVar)
    txtPassword = ttk.Entry(formFrame,show='x', justify='center', width=28, font=('arial', 10, 'bold'), textvariable=passwordVar)

    txtExamNo.grid(row=0, column=2, sticky='WE', pady=5, ipady=5)
    txtPassword.grid(row=1, column=2, sticky='WE', pady=5, ipady=5)
    
   
    
    txtSubmit = ttk.Button(formFrame, text='Sign In', style='btn.TButton', command=signIn)
    txtSubmit.grid(row=2,column=1,columnspan=2,sticky='E')

    #frame_other 
    frameRegister = ttk.Frame(frame_bottom, width=340)
    frameRegister.pack(side='left', anchor='e')

    lblregister = ttk.Label(frameRegister, text='Not yet Register', style='register.TLabel')
    lblregister.grid(row=0, column=0)
    lblreg = ttk.Label(frameRegister, text='Click here?', style='reg.TLabel',cursor='wait')
    lblreg.grid(row=0, column=1)
   
    forgot = ttk.Label(frameRegister, text='Forgot Password?', style='reg.TLabel',cursor='wait')
    forgot.grid(row=0, column=2, padx=5)
    

    forgot.bind('<Button-1>', showForgot)
    rt.mainloop()
