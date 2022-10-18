import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


load_dotenv()
gmail_username = os.getenv('GMAIL_USERNAME')
gmail_password = os.environ.get('GMAIL_PASSWORD')
host = 'smtp.gmail.com'
port = 587 #ssl  or 586 tls
# to = ['tempodigitalculture@gmail.com','afolabitemitay64@gmail.com', 'omodeleoluwaseund26@gmail.com','jazzykenedy37@gmail.com','tosinoluwamodimu@gmail.com','brightabimbola45@gmail.com']
to='tempodigitalculture@gmail.com'
subject = 'Python Email Testing Tool'


messageMailer = MIMEMultipart('alternative')
messageMailer['From'] = gmail_username
messageMailer['To'] = to
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
        
        h1 {
            font-size: 46px;
            text-align: center;
            color: tomato;
            font-weight: bold;
        }
    </style>
</head>

<body>

    <h1>Congratulations!</h1>
    <h4>You are highly welcome to our official website</h4>
    <p>
        Please be informed that our computer based examination will come up very soon and you will be notifed at due date. Thank you.
    </p>
    <button class="btn">Visit Website</button>
</body>

</html>
    """


textPart = MIMEText(text,'plain')
htmlPart = MIMEText(html, 'html')

messageMailer.attach(textPart)
messageMailer.attach(htmlPart)

try: 
     with smtplib.SMTP(host,port) as smtp_server:
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(gmail_username,gmail_password)
        smtp_server.ehlo()
        smtp_server.sendmail(gmail_username,to,messageMailer.as_string())  
        smtp_server.close()     
        print('Message has been sent')
       
except:
     print('Error in sending message')
    