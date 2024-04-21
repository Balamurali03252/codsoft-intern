from tkinter import *
from random import randint

root = Tk()
root.title("Password-Generator!")
#root.iconbitmap('C:\Users\ARUNACHALAM\OneDrive\Desktop\Password_generator_GUI\icons\icons8-password-26.png')
root.geometry("500x300")

def new_rand():
    #clear our entry box
    pw_entry.delete(0,END)
    #get pw_length and convert into integer 
    pw_length = int(my_entry.get())
    my_password = ''
    for x in range(pw_length):
        my_password += chr(randint(33,126))
 
    #output password to the screen
    pw_entry.insert(0, my_password) 


def clip():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())


#icon
img_icon=PhotoImage(file="icons\icons8-password-26.png")
root.iconphoto(False,img_icon)

#label_frame
lf = LabelFrame(root, text="How many Characters?")
lf.pack(pady=20)

#create entry box to designate no of character
my_entry = Entry(lf,font=("Times",24))
my_entry.pack(padx=20,pady=20)

#create entry box for our returned password
pw_entry = Entry(root, text='',font=("Helvetica",24))
pw_entry.pack(pady=20)

#create a frame for our buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

#create out buttons
my_buttons = Button(my_frame, text="Generate strong Password", command=new_rand)
my_buttons.grid(row=0,column=0,padx=10)

clip_button = Button(my_frame, text="Copy to Clipboard", command=clip)
clip_button.grid(row=0,column=1,padx=10)








root.mainloop()

