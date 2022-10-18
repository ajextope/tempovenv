import os
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from ttkthemes import THEMES, ThemedTk
from tkcalendar import *
from tkinter import filedialog as f
from PIL import ImageTk,Image
import myclass.dbConnection as db
import bcrypt


#globar variable design
filename = ''
#function declaration 
def uploadPassport():
    global filename
    filename =f.askopenfilename(initialdir=os.getcwd(),defaultextension='.jpg',title='Open file for Upload',filetypes=[('Jpeg File (.jpg)','*.jpg'),('Png File (*.png', '*.png')])
    #using PIL 
    myimage = Image.open(filename)
    newimage= myimage.resize((100, 100))
    img =ImageTk.PhotoImage(image=newimage)
    lblPassport.config(image=img, width=100, height=100)
    lblPassport.image = img
    
    #getting the current working path from os Module
    currentPath = os.getcwd() + '/uploads'
    #saving the image folder
    newimage.save(currentPath + '/' + emailVar.get() + '.jpg')
    
def submit_records():
    global filename
    dbQuery = db.dbConnection()

    if(dbQuery.empty(examnoVar.get()) == True or dbQuery.empty(surnameVar.get()) == True or dbQuery.empty(othernameVar.get())== True or dbQuery.empty(genderVar.get())==True or dbQuery.empty(emailVar.get())== True or dbQuery.empty(dobVar.get())== True or dbQuery.empty(maritalVar.get())== True or dbQuery.empty(passwordVar.get())==True or dbQuery.empty(filename) == True):
        messagebox.showwarning('Empyt Field', 'The field is required please fill.')
        return
    
    if(dbQuery.match(passwordVar.get(),repeatPassVar.get()) == False):
        messagebox.showwarning('UnMatch Password', 'The password does not match.')
        return

    if(dbQuery.checkEmail(emailVar.get())== True):
        messagebox.showwarning('Record Exist', 'The email used is already exist!')
        return
    
    
    sql = "INSERT INTO `users`(`exam_no`, `surname`, `othernames`, `gender`, `email`, `date_of_birth`, `marital_status`, `passport`, `password`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    pwd = passwordVar.get()
    pwd= pwd.encode('utf-8')
    encryptPassword = bcrypt.hashpw(pwd,bcrypt.gensalt())
    values = (int(examnoVar.get()),surnameVar.get(),othernameVar.get(),genderVar.get(),emailVar.get(),dobVar.get(),maritalVar.get(),filename,encryptPassword)
    
    dbQuery.queryDB(sql,values)
    
    messagebox.showinfo('Saved Record', 'Examination Record has been saved successfully.')

#constant variable  
__designColor='#45658a'
__formColor = '#fff'


rt = ThemedTk(theme='adapta', themebg=True)
rt.title('Registeration Form - Computer Based Test')
width = 920
height = 470

#configuration for design  
rt.columnconfigure(0, weight=1)
rt.columnconfigure(1,weight=1)
rt.rowconfigure(0, weight=1)

#geometry design size
sw = rt.winfo_screenwidth()
sh = rt.winfo_screenheight()
x = sw // 2 - width // 2
y = sh // 2 - height // 2
rt.geometry(f'{width}x{height}+{x}+{y}')
rt.resizable(0, 0)
# rt.state('zoomed')
#Initialize style in ttk 
style = ttk.Style()
style.configure('frmdesign.TFrame', background=__designColor)
style.configure('frmform.TFrame', background=__formColor)
style.configure('frmPassword.TFrame')



#frame designa dn frame form on root window
frmdesign = ttk.Frame(rt, style='frmdesign.TFrame')
frmform = ttk.Frame(rt, style='frmform.TFrame')

#Variable for String TKinter 
examnoVar = StringVar()
surnameVar = StringVar()
othernameVar= StringVar()
genderVar = StringVar()
emailVar = StringVar()
dobVar = StringVar()
maritalVar = StringVar()
passwordVar = StringVar()
repeatPassVar = StringVar()



#Display the frame using grid geometry 
frmdesign.grid(row=0, column=0, sticky='WENS')
frmform.grid(row=0, column=1,sticky='WENS')

#divide the frmForm into two 2/3
frmform.rowconfigure(0, weight=1)
frmform.columnconfigure(0,weight=1)
frmform.columnconfigure(1,weight=3)

frmPassword = ttk.Frame(frmform, style='frmPassword.TFrame')
frmformField = ttk.Frame(frmform)
frmformField.grid(row=0, column=0, sticky='WENS')
frmPassword.grid(row=0, column=1, sticky='WENS')

#Passport field design 
avatar = PhotoImage(file='./img/default.png')
lblPassport = Label(frmPassword,relief='raised', image=avatar)
lblPassport.place(x=7, y=10)
btnUpload = ttk.Button(frmPassword, text='Browse...', command=uploadPassport)
btnUpload.place(x=12, y=126)

#Design for Forms 
style.configure('title.TLabel', font=('arial', 17, 'bold'), foreground = 'tomato')
style.configure('form.TLabel', font=('arial',11, 'bold'), foreground = '#282828', background='#f7f7f7')

lbltitle= ttk.Label(frmformField, text='Registration Form', style='title.TLabel')
lbltitle.grid(row=0, column=0, columnspan=6, sticky='WE', pady=(10, 3), padx=(10, 0))

logobg = PhotoImage(file='./img/tempo-120.png')

#Form field design  
ttk.Label(frmformField, text='Exam no:', style='form.TLabel').grid(row=1, column=0, pady=(5,5))
txtExamno = ttk.Entry(frmformField,width=40, textvariable=examnoVar, state='readonly')
txtExamno.grid(row=1, column=1, sticky='WE',pady=(0, 5))

ttk.Label(frmformField, text='Surname:', style='form.TLabel').grid(row=2, column=0, pady=(5,5))
txtSurname = ttk.Entry(frmformField, textvariable= surnameVar)
txtSurname.grid(row=2, column=1, sticky='WE',pady=(0, 5))

ttk.Label(frmformField, text='Othernames:', style='form.TLabel').grid(row=3, column=0, pady=(5,5))
txtOthernames = ttk.Entry(frmformField, textvariable=othernameVar)
txtOthernames.grid(row=3, column=1, sticky='WE',pady=(0, 5))

ttk.Label(frmformField, text='Gender:', style='form.TLabel').grid(row=4, column=0, pady=(5,5))
txtGender = ttk.Combobox(frmformField, values=('Male', 'Female'), textvariable=genderVar, state='readonly')
txtGender.grid(row=4, column=1, sticky='WE', pady=(0, 5))

ttk.Label(frmformField, text='Email:', style='form.TLabel').grid(row=5, column=0, pady=(5,5))
txtEmail = ttk.Entry(frmformField,textvariable=emailVar)
txtEmail.grid(row=5, column=1, sticky='WE', pady=(0, 5))

ttk.Label(frmformField, text='Date of Birth:', style='form.TLabel').grid(row=6, column=0, pady=(5,5))
txtdob = DateEntry(frmformField, textvariable=dobVar)
txtdob.grid(row=6, column=1, sticky='WE', pady=(0, 5))

ttk.Label(frmformField, text='Marital Status:', style='form.TLabel').grid(row=7, column=0, pady=(5,5))
txtStatus = ttk.Combobox(frmformField, values=('Single', 'Married', 'Divorced', 'Widow'), state='readonly',textvariable=maritalVar)
txtStatus.grid(row=7, column=1, sticky='WE', pady=(0, 5))

ttk.Label(frmformField, text='Password:', style='form.TLabel').grid(row=8, column=0, pady=(5,5))
txtpassword = ttk.Entry(frmformField, show='x', textvariable=passwordVar)
txtpassword.grid(row=8, column=1, sticky='WE', pady=(0, 5))

ttk.Label(frmformField, text='Repeat Password:', style='form.TLabel').grid(row=9, column=0, pady=(5,5))
txtcpassword = ttk.Entry(frmformField, show='x', textvariable=repeatPassVar)
txtcpassword.grid(row=9, column=1, sticky='WE', pady=(0, 5))



btnSubmit = ttk.Button(frmformField, text='Register',command=submit_records)
btnSubmit.grid(row=10, column=0,columnspan=2, sticky='E')

btnClear = ttk.Button(frmformField, text='Clear')
btnClear.grid(row=11, column=0, columnspan=2, sticky='E')


lbllogo = ttk.Label(frmdesign,image=logobg)
lbllogo.pack(pady=(20,2))
desc= '''Welcome to Computer Based Test Platform where every exam and test are being cinduected through electronic channel. You are required to fill in all the boxes in this form and also upload your 2 by 2 passport. If you have already registered kindly, click on the login button below to proceed to the main page.'''
style.configure('desc.TLabel', foreground='#fff',background=__designColor, font=(8))
lbldesc= ttk.Label(frmdesign, text=desc, wraplength=280,justify='center', style='desc.TLabel')
lbldesc.pack(pady=(30,2))

btnlogin = ttk.Button(frmdesign, text='Login',style='login.TButton')
btnlogin.pack(side='bottom', pady=(0, 10))


dbQuery = db.dbConnection()
result = dbQuery.generate_code(8)
examnoVar.set(result)
rt.mainloop()