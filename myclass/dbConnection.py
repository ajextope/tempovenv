import random
import re
from tkinter import messagebox
import bcrypt
import mysql.connector as mysql
from mysql.connector import Error
class dbConnection:
    
   def getConnection(self):
        try:
           con = mysql.connect(host='localhost', database='cbt', user='root', password='')
           return con
        except Error as err:
            print(err.msg)
        except:
            messagebox.showerror('Database Error', 'Unable to connect to Database')
    
    #inserting into database
   def queryDB(self,query,values=''):
       con= self.getConnection()
       cursor = con.cursor()
       cursor.execute(query,values)
       con.commit()
       con.close()
   
   #closing connection 
   def closeConnection(self):
      con= self.getConnection()
      con.close()
    
   def getLogin(self, examNo):
       try:
            if (self.already_taken(examNo)==True):
               messagebox.showwarning('ALready Taken', 'You\'ve already taken this exam. Please logout.' )
               return 

            con =self.getConnection()
            cursor = con.cursor()
            query = "SELECT * FROM users WHERE exam_no= %s"
            cursor.execute(query,[examNo])
            row=cursor.fetchone()
            return row
       except:
           print('Error Occur')
       finally:
           con.close()


    
   def empty(self,value):
            s = str(value)
            if (len(s.strip()) < 1):
                return True
        
   def validate(self,pattern, value):
            v = re.compile(pattern)
            match = v.match(value)
            if (match == None):
                return False
            else:
                return True
    
   def match(self, password, repeatPassword):
       if (password == repeatPassword):
           return True
       else:
           return False
    
   def generate_code(self,lenght):
       code ="".join(random.sample('0123456789', lenght))
       return code
   
   def checkEmail(self,email):
       con =self.getConnection()
       cursor = con.cursor()
       query = "SELECT email FROM users WHERE email= %s"
       cursor.execute(query,[email])
       row=cursor.fetchone()
       con.close()
       if(row):
           return True
       else:
           return False
       
   def loginDb(self,examNo):
       con =self.getConnection()
       cursor = con.cursor()
       query = "SELECT `exam_no`,`password` FROM users WHERE exam_no= %s"
       cursor.execute(query,[examNo])
       row=cursor.fetchone()
       con.close()
       return row
    
   def changePasswordDB(self,examNo):
       query = "SELECT * FROM users WHERE exam_no=%s"
       con=self.getConnection()
       cursor = con.cursor()
       cursor.execute(query, [examNo])
       row= cursor.fetchone()
       con.close()
       if row==None:
           return False
       else:
           return row
       
   def saveToken(self, email,token):
       con = self.getConnection()
       cursor= con.cursor()
       query= "UPDATE users SET tokens=%s WHERE email= %s"
       cursor.execute(query, (token, email))
       con.commit()
       con.close()
   
   
   def submit_exam(self, examNo,score):
       query =" INSERT INTO exam(exam_no,score,status) VALUES(%s,%s,%s)"
       con = self.getConnection()
       cursor = con.cursor()
       cursor.execute(query, (examNo, score, 'active'))
       con.commit()
       con.close()
       return True
   
   def show_all_users(self):
       con = self.getConnection()
       cursor = con.cursor()
       cursor.callproc('get_all_users')
       
       rs=cursor.stored_results()
       cursor.close()
       if(con.is_connected()):
           con.close()
       return rs
   def already_taken(self, examNO):
       con = self.getConnection()
       cursor= con.cursor()
       cursor.execute("SELECT * FROM exam WHERE exam_no=%s", [examNO])     
       rs=cursor.fetchone() 
       if rs==None:
           return False
       else:
           return True
           
   def changeDb(self,newpassword,email, token):
            con = self.getConnection()
            cursor= con.cursor()
            pwd = str(newpassword)
            pwd= pwd.encode('utf-8')
            mypassword = bcrypt.hashpw(pwd,bcrypt.gensalt())
            query = "UPDATE users SET `password`=%s WHERE email=%s AND tokens=%s"
            cursor.execute(query,[mypassword,email,token])
            con.commit()
            #update toekn and delete 
            mytoken=''
            query2 = "UPDATE users SET tokens=%s WHERE email=%s"
            cursor = con.cursor()
            cursor.execute(query2, (mytoken,email))
            con.commit()
            con.close() 
            return True 