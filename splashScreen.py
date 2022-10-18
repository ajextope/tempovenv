import tkinter
from tkinter import ttk
from tkinter import *
from ttkthemes import THEMES, ThemedTk
import login
# End of module importation

#function loading  
def progress():
    pb['value'] +=25
    if pb['value'] == 100:
        pb.stop()
        rt.destroy()
        login.loginApp()
        return
    pb.after(1000, progress)
#Colours and conetents importation 
__primary = '#282828'
description = '''Computer Based Test (CBT) is new software developed by Tempo Digital Culture to help youth to know more about how to write an examination using computer system. This software is licensed under the GPL rules and regulatory body which subject other developers to work on this software using this content only for educational purposes. Any alteration, copying and distribution of this software without the consent of the developers or this Organization is highly PROHIBITED.'''

#Starting Tk function for drawing the interface
rt = ThemedTk(theme='adapta', themebg=True)
width = 475
height = 322
sw = rt.winfo_screenwidth()
sh = rt.winfo_screenheight()
x = sw // 2 - width // 2
y = sh // 2 - height // 2
rt.geometry(f'{width}x{height}+{x}+{y}')
rt.resizable(0, 0)
rt.overrideredirect(True)

#Printing out THEMES name in a file 
# f = open('theme.txt', 'w')
# print(THEMES,file=f)

#Placing Logo and Icons 
logobg = PhotoImage(file='./img/tempo-120.png')

#placing content on frame
splashFrame = ttk.Frame(rt,width=400)
splashFrame.pack(pady=10)

#Initializing styling for ttk elements
style = ttk.Style()
style.configure('label1.TLabel', font=('roboto', 18, 'bold'), foreground=__primary)
style.configure('description.TLabel', font=('roboto',8,'normal'))
style.configure('copyright.TLabel',foreground=__primary, font=('roboto',10,'normal'))
#placing Label on the SplashFrame 
splashLabel1 = ttk.Label(splashFrame, text='COMPUTER BASED TEST', style='label1.TLabel')
splashLabel1.pack(pady=5)

#Placing Logo label 
splashLogoLabel = ttk.Label(splashFrame,image=logobg)
splashLogoLabel.pack(pady=15)

#Frmae for description 
descriptionFrame = ttk.Frame(rt, width=460)
descriptionFrame.pack()
#placing content on desscription frame 
lblDescription = ttk.Label(descriptionFrame, text= description,wraplength=390, justify='center', style='description.TLabel')
lblDescription.pack(pady=5)

lblcopyright = ttk.Label(rt, text= 'Developed Tempo Digital Culture - 2022', justify='center', style='copyright.TLabel')
lblcopyright.pack(pady=5)

pb = ttk.Progressbar(rt,mode='determinate',orient='horizontal',maximum=100,value=0)
pb.pack(side='bottom', fill='x', expand=True)

#starting the loading content 
progress()
#end loading
rt.mainloop()
