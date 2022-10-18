
import tkinter 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import THEMES, ThemedTk
from myclass import dbConnection
import bcrypt

exanimation_no=''
def ChangePassword(parent, exano_number):
    global exanimation_no
    exanimation_no = exano_number
    def clearBoxes():
        oldPassword.set('')
        newPassword.set('')
        repeatPassword.set('')
    
    def change():
        global exanimation_no
        old = oldPassword.get()
        new= newPassword.get()
        repeat= repeatPassword.get()
        #render null value 
        old = old.strip()
        new = new.strip()
        repeat= repeat.strip()
        
        if (not old) or (not new) or (not repeat):
            messagebox.showwarning('Blank Field', 'Please fill in the blank field(s).')
            return
        
        dbQuery = dbConnection.dbConnection()
        if(dbQuery.changePasswordDB(exanimation_no)==False):
            messagebox.showinfo('Not Found', 'User Information Not Found.')
            return
        row = dbQuery.changePasswordDB(exanimation_no)
        oldpass = row[8]
        oldpass = oldpass.encode('utf-8')
        if(newPassword.get() != repeatPassword.get()):
            messagebox.showwarning('Unmatch Password', 'Password enter does not Match.')
            return
        newpass = oldPassword.get()
        newpass = newpass.encode('utf-8')
        result = bcrypt.checkpw(newpass,oldpass)
        print(result)
        if (result):
            
            query = "UPDATE users SET password=%s WHERE exam_no=%s"
            pwd = newPassword.get()
            pwd= pwd.encode('utf-8')
            mynewPassword =bcrypt.hashpw(pwd,bcrypt.gensalt())
            con= dbQuery.getConnection()
            cursor = con.cursor()
            cursor.execute(query,(mynewPassword,exanimation_no))
            con.commit()
            con.close()
            messagebox.showinfo('Change Password', 'Password has been changed successfully.')
            clearBoxes()
        else:
            messagebox.showinfo('Not Found', 'User Information Not Found.')
            
            
        
        
    __frameTop= '#fff'
    __frameBottom= '#214254'
    #Starting Tk function for drawing the interface
    rt = Toplevel(parent)
    rt.title('Change Password - CBT')
    rt.focus_force()
    rt.grab_set()
    width = 475
    height = 230
    sw = rt.winfo_screenwidth()
    sh = rt.winfo_screenheight()
    x = sw // 2 - width // 2
    y = sh // 2 - height // 2
    rt.geometry(f'{width}x{height}+{x}+{y}')
    rt.resizable(0, 0)
    
    lbltitle = ttk.Label(rt,text='CHANGE PASSWORD', justify='center')
    lbltitle.place(relx=0.4, rely=0.1)
    
    lbloldPassword = ttk.Label(rt,text='Old Password:')
    lbloldPassword.place(x=40, y=60)
    lblNewPassword = ttk.Label(rt,text='New Password:')
    lblNewPassword.place(x=40,y=100 )
    lblRepeatPassword = ttk.Label(rt,text='Repeat Password:')
    lblRepeatPassword.place(x=40, y=140)
    #variables for textfield
    oldPassword= StringVar()
    newPassword=StringVar()
    repeatPassword= StringVar()
    
    txtOldpassword = ttk.Entry(rt, width=50, show='&', textvariable=oldPassword)
    txtOldpassword.place(x=133, y=55, height=30)
  
    txtnewPassword= ttk.Entry(rt,width=50, textvariable=newPassword,show='&')
    txtnewPassword.place(x=133,y=94, height=30)
    
    txtrepeatPassword= ttk.Entry(rt, width=50, textvariable=repeatPassword,show='&')
    txtrepeatPassword.place(x=133, y=136, height=30)
    
    btnClear = ttk.Button(rt, text='Clear All', command=clearBoxes)
    btnClear.place(x=233, y=175)
    
    btnChange = ttk.Button(rt, text='Change Password', command=change)
    btnChange.place(x=327, y=175)
    rt.mainloop()
