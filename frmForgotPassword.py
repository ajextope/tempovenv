import tkinter 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import THEMES, ThemedTk
import string, random
import os
import frmChangeForgot
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from myclass import dbConnection as db
def forgotPassword():
     
    def sendMail():
        tokens = string.ascii_letters + string.digits + string.punctuation
        rs = ''.join(random.sample(tokens,10))
        load_dotenv()
        gmail_username = os.getenv('GMAIL_USERNAME')
        gmail_password = os.environ.get('GMAIL_PASSWORD')
        host = 'smtp.gmail.com'
        port = 587 #ssl  or 586 tls
        # to = ['tempodigitalculture@gmail.com','afolabitemitay64@gmail.com', 'omodeleoluwaseund26@gmail.com','jazzykenedy37@gmail.com','tosinoluwamodimu@gmail.com','brightabimbola45@gmail.com']
        
        subject = 'Forgot Password tokens'


        messageMailer = MIMEMultipart('alternative')
        messageMailer['From'] = gmail_username
        messageMailer['To'] = emailVar.get()
        messageMailer['Subject']=subject

        text= """\
            Hi,
        Check out the new post on the Mailtrap blog:
        SMTP Server for Testing: Cloud-based or Local?
        https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/
        Feel free to let us know what content would be useful for you!
            """
        html = """\
            <html lang="en">

        <head>
            <title>Document</title>
            <style>
                .btn {
                    padding: 12px 10px;
                    border-radius: 10px;
                    border: none;
                    background-color: #0c2549;
                    color: #fff;
                }
                h2{
                    font-size:40px;
                    color: red;
                    font-weight: 900;
                }
                
                h1 {
                    font-size: 46px;
                    text-align: center;
                    color: tomato;
                    font-weight: bold;
                }
            </style>
        </head>

        <body>

            <h1>Forgot Password</h1>
            <h4>Please ensure you copy the below tokens to verify your change password account.</h4>
            <h2> %s </h2>
            <p>
                Don't reveal your tokens to anyone.
            </p>
        </body>

        </html>
            """ %(rs)


        textPart = MIMEText(text,'plain')
        htmlPart = MIMEText(html, 'html')

        messageMailer.attach(textPart)
        messageMailer.attach(htmlPart)

        try: 
            to = emailVar.get()
            if(len(to.strip()) < 1):
                return 
            
            with smtplib.SMTP(host,port) as smtp_server:
                smtp_server.starttls()
                smtp_server.ehlo()
                smtp_server.login(gmail_username,gmail_password)
                smtp_server.ehlo()
                smtp_server.sendmail(gmail_username,to,messageMailer.as_string())  
                smtp_server.close()     
                
                #database connection saved 
                mydb = db.dbConnection()
                dqQuery= mydb.saveToken(to,rs)
                messagebox.showinfo('Feedback', 'Check your email to proceed. Token sent')
                rt.destroy()
                frmChangeForgot.showForgot(to)
                
            
        except:
            print('Error in sending message')


    __frameTop= '#fff'
    __frameBottom= '#214254'
    #Starting Tk function for drawing the interface
    rt = Toplevel()
    rt.grab_set()
    rt.focus_force()
    rt.title('Forgot Password - CBT')
    width = 375
    height = 170
    sw = rt.winfo_screenwidth()
    sh = rt.winfo_screenheight()
    x = sw // 2 - width // 2
    y = sh // 2 - height // 2
    rt.geometry(f'{width}x{height}+{x}+{y}')
    rt.resizable(0, 0)


    # controls 
    lblEmail = ttk.Label(rt, text='Email Address')
    lblEmail.place(x=40, y=20)

    emailVar= StringVar()
    txtEmail = ttk.Entry(rt, width=50, textvariable=emailVar)
    txtEmail.place(x=40, y=40,bordermode='outside',height=40)

    btnFogot = ttk.Button(rt, text='Verfiy Email', command=sendMail)
    btnFogot.place(x=267, y=90)
    
    
    
    rt.mainloop()


