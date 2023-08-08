import tkinter
from tkinter import*
from tkinter import messagebox 

root=Tk()
root.title("CALCULATOR")
root.geometry("570x590")
root.resizable(0,0)
root.configure(bg="#808080")
equ=""

def show(value):
    global equ
    equ+=value
    lr.config(text=equ)

def clear():
    global equ
    equ=""
    lr.config(text=equ)

def calculate():
    global equ
    res=""
    if equ !="":
        try:
            res=eval(equ)
        except:
            res="error"
            equ=""

    lr.config(text=res)
lr=Label(root,width=23,height=2,text="",font=("times new roman",28),anchor="center",bg="white")
lr.pack(pady=10)

Button(root,text="*",width=8,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:show("*")).place(x=10,y=110)
Button(root,text="-",width=8,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:show("-")).place(x=220,y=110)
Button(root,text="C",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:clear()).place(x=430,y=110)

Button(root,text="7",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:show("7")).place(x=10,y=200)
Button(root,text="8",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:show("8")).place(x=150,y=200)
Button(root,text="9",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:show("9")).place(x=290,y=200)
Button(root,text="/",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:show("/")).place(x=430,y=200)

Button(root,text="4",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:show("4")).place(x=10,y=300)
Button(root,text="5",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:show("5")).place(x=150,y=300)
Button(root,text="6",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:show("6")).place(x=290,y=300)
Button(root,text="+",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:show("+")).place(x=430,y=300)

Button(root,text="1",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:show("1")).place(x=10,y=400)
Button(root,text="2",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:show("2")).place(x=150,y=400)
Button(root,text="3",width=5,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:show("3")).place(x=290,y=400)

Button(root,text="0",width=8,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:show("0")).place(x=10,y=490)
Button(root,text=".",width=8,height=1,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:show(".")).place(x=220,y=490)

Button(root,text="=",width=5,height=3,font=("times new roman",30,"bold"),bd=1,fg="#838B8B",bg="#DCDCDC",command=lambda:calculate()).place(x=430,y=400)

root.mainloop()