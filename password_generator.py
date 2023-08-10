from tkinter import *
import random
import string

root= Tk()
root.geometry("800x800")
root.title("PASSWORD GENERATOR")
root.config(bg="palevioletred")

passstr=StringVar()
pwd_len= IntVar()
username=StringVar()
choice=IntVar()

def get_pass():
    pass1=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
    password=""
    for x in range(pwd_len.get()):
        password=password+random.choice(pass1)
        passstr.set(password)

        
Label(root,text="PASSWORD GENERATOR",font=("Times new roman",20)).pack(pady=5)
Label(root,text="Enter user name",font=("Times new roman",20)).pack(padx=8,pady=8,anchor="w")
Entry(root,textvariable=username,font=("Times new roman",20)).pack(pady=8,padx=8,anchor="center")
Label(root,text="Enter length of password",font=("Times new roman",20)).pack(pady=10,padx=10,anchor="w")
Entry(root,textvariable=pwd_len,font=("Times new roman",20)).pack(pady=10,padx=10,anchor="center")
Radiobutton(root,text='Weak',value=1,font=("Times new roman",15)).pack(pady=14)
Radiobutton(root,text='Medium',value=2,font=("Times new roman",15)).pack(pady=16)
Radiobutton(root,text='Strong',value=3,font=("Times new roman",15)).pack(pady=18)
Button(root,text="Generate Password",command=get_pass,font=("Times new roman",20)).pack(pady=19)
Entry(root,textvariable=passstr,font=("Times new roman",20)).pack(pady=2)

root.mainloop()