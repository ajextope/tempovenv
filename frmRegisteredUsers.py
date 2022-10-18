import tkinter
from tkinter import ttk
from tkinter import *
import myclass.dbConnection as db


def reg_users():
    
    def show_users():
        dbase = db.dbConnection()
        rs=dbase.show_all_users()
        result=''
        for r in rs:
            result=r.fetchall()
    
        for val in result:
            tv.insert('',index=END,values=val)
    

    __frameTop= '#fff'
    __frameBottom= '#214254'
    #Starting Tk function for drawing the interface
    rt = Tk()
    rt.title('Registered Users - CBT')
    rt.focus_force()
    rt.grab_set()
    width = 775
    height = 400
    sw = rt.winfo_screenwidth()
    sh = rt.winfo_screenheight()
    x = sw // 2 - width // 2
    y = sh // 2 - height // 2
    rt.geometry(f'{width}x{height}+{x}+{y}')
    rt.resizable(0, 0)

    frame = ttk.Frame(rt)
    frame.pack(side='top', fill=BOTH)



    tv = ttk.Treeview(frame,height=50, show='headings',style='',columns=['exam_no', 'sname', 'oname', 'gender','email', 'dob','ms'])

    #scrollbar 
    sb = ttk.Scrollbar(frame,orient='horizontal',command=tv.xview)
   
    
    tv.heading('exam_no',text='Examination No',anchor='center')
    tv.heading('sname',text='Surname',anchor='center')
    tv.heading('oname',text='Othernames',anchor='center')
    tv.heading('gender',text='Gender',anchor='center')
    tv.heading('email',text='Email',anchor='center')
    tv.heading('dob',text='Date of Birth',anchor='center')
    tv.heading('ms',text='Marital Status',anchor='center')


    tv.column(0,anchor='center')
    tv.column(1,anchor='center')
    tv.column(2,anchor='center')
    tv.column(3,anchor='center')
    tv.column(4,anchor='center')
    tv.column(5,anchor='center')
    tv.column(6,anchor='center')
    
    
    tv.grid(row=0, column=0, sticky='WENS')
    tv.configure(xscrollcommand=sb.set)
    sb.grid(row=1,column=0, sticky='WE')
  

    show_users()

    rt.mainloop()
    