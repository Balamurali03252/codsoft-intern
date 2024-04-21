import tkinter
from tkinter import *

app = Tk()
app.title("To-Do List")
app.geometry("450x600")
app.resizable(False,False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)
    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)
    except:
        file=open('tasklist.txt','w')
        file.close()

#icon
img_icon=PhotoImage(file="icons/icons8-task-48.png")
app.iconphoto(False,img_icon)

#topbar 
topimage=PhotoImage(file="icons/topbar.png")
Label(app,image=topimage).pack()

dockimage = PhotoImage(file="icons/icons8-menu-30.png")
Label(app,image=dockimage,bg="#3F48CC").place(x=25,y=22)

noteimage = PhotoImage(file="icons/icons8-task-48.png")
Label(app,image=noteimage,bg="#3F48CC").place(x=380,y=16)

heading=Label(app,text="ALL TASK",font="arial 20 bold",fg="white",bg="#3F48CC")
heading.place(x=157,y=21)

#main
frame=Frame(app,width=450,height=50,bg="white")
frame.place(x=0,y=110)

task=StringVar()
task_entry = Entry(frame,width=18,font="arial 15",bd=0)
task_entry.place(x=10,y=10)
task_entry.focus()

button=Button(frame,text="ADD",font="arial 18 bold",width=7,bg="#00A2E8",fg="#fff",bd=0,command=addTask)
button.place(x=338,y=2)

#list
frame1=Frame(app,bd=3,width=800,height=280,bg="#3F48CC")
frame1.pack(pady=(110,0))

listbox = Listbox(frame1,font=('arial',12),width=40,height=16,bg="#3F48CC",fg="white",cursor="hand2",selectbackground="#00A2E8")
listbox.pack(side=LEFT,fill=BOTH)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()


#delete
delete_icon=PhotoImage(file="icons/icons8-delete-48.png")
Button(app,image=delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=15)

app.mainloop()