import os
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedTk, THEMES
import frmChangePassword, login
import html
from myclass.quiz_data import questions_model
from myclass.qModel import Questions
from myclass.QuizBrain import Quiz
import myclass.dbConnection as db
import frmRegisteredUsers as ru
#constant variable  
__designColor='#45658a'
__formColor = '#fff'



myexamNo=''
current_q=None
quiz= None
def loadExamForm(exam_no):
    global myexamNo, quiz
    myexamNo = exam_no
    rt = ThemedTk(theme='adapta', themebg=True)
    rt.title('Computer Based Test ')
    width = 800
    height = 470
    #configuration for design  
    rt.columnconfigure(0, weight=1)
    rt.rowconfigure(0,weight=1)
    rt.rowconfigure(1, weight=4)
    rt.state('zoomed')
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
    style.configure('frmdesign.TFrame',background=__designColor, foreground=__formColor)
    style.configure('question.TLabel', font=(12))
    style.configure('lblaccount.TLabel', background=__designColor, foreground='#fff', font=(10))

    #loading exam query from api and Question class model 
    question_bank =[]
    for questions in questions_model:
        choices=[]
        question= html.unescape(questions['question'])
        correct_answer = html.unescape(questions['correct_answer']) 
        for wrong in questions['incorrect_answers']:
            choices.append(html.unescape(wrong))
        choices.append(correct_answer)
        random.shuffle(choices)
        question_bank.append(Questions(question,correct_answer,choices))
    
    quiz=Quiz(question_bank)
    global current_q 
    current_q= quiz.next_question()
   
   #submit text 
    def submit_test():
        global myexamNo
        examNo = myexamNo
        mydb = db.dbConnection()
        global current_q, quiz
        if(mydb.submit_exam(examNo,quiz.score)):
            btnSubmit.config(state='disabled')
            messagebox.showinfo('Exam Completed', 'Your exam Score has been submitted.')
            wrong, scores, percentage=  quiz.get_scores()
            messagebox.showinfo('Exam Complete', f'You score {scores} out of 20 questions\n with percentage of {percentage}\n you got {wrong} wrong.')
            return
         
    
        
    #ending exam model
    def getSelectedItem(*args):
        global myexamNo
        selItem = cmbaccount.get()
        if(selItem == 'Logout'):
            rt.destroy()
            login.loginApp()
        elif (selItem=='Change Password'):
            frmChangePassword.ChangePassword(rt, myexamNo)
        elif (selItem =='View Users'):
            ru.reg_users()
    
    def next_question():
        global current_q, quiz
        quiz.check_answer(selRadio.get())
        if(quiz.isComplete()):  
            current_q= quiz.next_question()
            lblQuestion.config(text=current_q)
            radio1.config(text=quiz.current_question.choices[0], value=quiz.current_question.choices[0])
            radio2.config(text=quiz.current_question.choices[1],value=quiz.current_question.choices[1])
            radio3.config(text=quiz.current_question.choices[2],value=quiz.current_question.choices[2])
            radio4.config(text=quiz.current_question.choices[3],value=quiz.current_question.choices[3])
        else:
           
            return
        
    frmdesign = ttk.Frame(rt,style='frmdesign.TFrame')
    frmExam =ttk.Frame(rt)

    #display frames on Root window 
    frmdesign.grid(row=0, column=0, sticky='WENS')
    frmExam.grid(row=1, column=0,sticky='WENS')
    cmbaccount = StringVar()

    cmbAccount = ttk.Combobox(frmdesign, textvariable=cmbaccount, state='readonly', values=('Change Password', 'Logout','View Users'),)
    cmbAccount.place(relx=0.8, rely=0.3, width=200)
    cmbaccount.set('My Account')
    cmbAccount.bind('<<ComboboxSelected>>',getSelectedItem)

    lblAccount = ttk.Label(frmdesign, text='Choose Operation', style='lblaccount.TLabel')
    lblAccount.place(rely=0.4,relx=0.69)
    #display questions and options
    frmexamFrame = ttk.Frame(frmExam,relief='raised', border=1)
    frmexamFrame.place(x=300,y=40,width=800, height=350)
    lblQuestion = ttk.Label(frmexamFrame, text='Who is the president of Nigeria?', wraplength=600, style='question.TLabel')
    lblQuestion.place(x=80, y=37)
    #String var variable 
    selRadio = StringVar()

    radio1 = ttk.Radiobutton(frmexamFrame,text='Obi Cubana', value='A', variable=selRadio)
    radio1.place(x=80, y=80)
    radio2 = ttk.Radiobutton(frmexamFrame,text='Muritala Muhammed',value='B', variable=selRadio)
    radio2.place(x=80, y=120)
    radio3 = ttk.Radiobutton(frmexamFrame,text='Olusegun Obasanjo',value='C',variable=selRadio)
    radio3.place(x=80, y=160)
    radio4 = ttk.Radiobutton(frmexamFrame,text='Peter Obi',value='D',variable=selRadio)
    radio4.place(x=80, y=200)

    # btnPrevious = ttk.Button(frmExam, text='Prev Question', command='')
    # btnPrevious.place(x=800, y=330)
    btnNext = ttk.Button(frmExam, text='Next Question', command=next_question)
    btnNext.place(x=900, y=330)

    btnSubmit = ttk.Button(frmExam, text='Submit', command=submit_test)
    btnSubmit.place(x=1000, y=330)

    
   
    lblQuestion.config(text=current_q)
    radio1.config(text=quiz.current_question.choices[0], value=quiz.current_question.choices[0])
    radio2.config(text=quiz.current_question.choices[1],value=quiz.current_question.choices[1])
    radio3.config(text=quiz.current_question.choices[2],value=quiz.current_question.choices[2])
    radio4.config(text=quiz.current_question.choices[3],value=quiz.current_question.choices[3])



    # cmbaccount.trace('w', getSelectedItem)
    rt.mainloop()