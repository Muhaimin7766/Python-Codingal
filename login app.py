from tkinter import *

root = Tk()
root.title('Login App')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360, bg="#000000")
frame.place(x=20, y=0)

lbl1 = Label(frame, text="Full Name", bg="#3895D3", fg='white', width=12)
lbl2 = Label(frame, text="Email Id", bg="#3895D3", fg='white', width=12)
lbl3 = Label(frame, text="Enter Password", bg="#3895D3", fg='white', width=12)

lbl1.place(x=20, y=20)
lbl2.place(x=20, y=80)
lbl3.place(x=20, y=140)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="'")

name_entry.place(x=150, y=20)
email_entry.place(x=150, y=80)
pass_entry.place(x=150, y=140)

def display():
    name = name_entry.get()
    greet = "Hey " + name
    message = "\nCongratulations for your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(root, bg="#BEBEBE", fg="black", height=5, width=35)
textbox.place(y=250)

btn = Button(root, text="Create Account", command=display, bg="red", fg="white")
btn.place(x=130, y=210)

root.mainloop()
