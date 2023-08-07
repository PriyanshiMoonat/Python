import tkinter as tk
from tkinter import *
from tkinter import messagebox

def add():
    task=ent.get()
    if task != "":
        list.insert(END,task)
        ent.delete(0,END)
    else:
        messagebox.showwarning("please enter a valid task")

def delete():
    try:
        selected_task=list.curselection()
        list.delete(selected_task)
    except:
        messagebox.showwarning("please select a task")
        


root=Tk()
root.title("TO-DO-LIST")
root.geometry("650x400+100+200")
root.resizable(0,0)
root.config(background="#000080")

task=[]

l=Label(root,text="TO-DO-LIST",font=("times new roman",23),height="1",width="400",background="#000080",fg="#FFFFFF")
l.pack()

ent=Entry(root,font=("Times new roman",20),fg="black")
ent.pack(padx=8,pady=8,anchor="center")

f=Frame(root,bg="#FFFFFF")
f.pack(pady=10,anchor="center")

scroll=Scrollbar(f)
scroll.pack(side=RIGHT,fill=Y,anchor="center")

list=Listbox(f,font=("Times new roman",12),width=40,height=10,bd=0,yscrollcommand=scroll.set)
list.pack(side=LEFT,fill=BOTH)
scroll.config(command=list.yview)


add_b=Button(root,text="ADD TASK",font=("Oswald",12),command=add,pady=10,padx=10,height=1,width=10)
add_b.pack(side=LEFT,anchor="center",padx=25)


del_b=Button(root,text="DELETE TASK",font=("Oswald",12),command=delete,padx=10,pady=10,height=1,width=10)
del_b.pack(side=RIGHT,anchor="center",padx=25)


root.mainloop()