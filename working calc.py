from tkinter import *

def button_click(number):
    current = display.get()
    cursor_position = display.index(INSERT)
    new_text = current[:cursor_position] + str(number) + current[cursor_position:]
    display_var.set(new_text)
    display.icursor(cursor_position + 1)

def animate_button(button):
    button.config(bg="#696969")
    button.after(100, lambda: button.config(bg="black"))

def clear_display():
    display_var.set("")

def calculate():
    try:
        result = eval(display.get())
        display_var.set(str(result))
    except:
        display_var.set("Error")

def backspace():
    cursor_position = display.index(INSERT)
    current = display.get()
    if cursor_position > 0:
        new_text = current[:cursor_position - 1] + current[cursor_position:]
        display_var.set(new_text)
        display.icursor(cursor_position - 1)

def add_operator(operator):
    current = display.get()
    cursor_position = display.index(INSERT)
    new_text = current[:cursor_position] + operator + current[cursor_position:]
    display_var.set(new_text)
    display.icursor(cursor_position + 1)

root = Tk()
root.title("Calculator")
root.geometry("400x600")
root.configure(bg="black")

display_var = StringVar()

display = Entry(root, textvariable=display_var, font=("Helvetica", 20), bg="white", fg="black", justify="right", bd=10)
display.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipady=5)

# Numeric buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
]

for (text, row, col) in buttons:
    btn = Button(
        root,
        text=text,
        font=("Helvetica", 20),
        bg="black",
        fg="white",
        activebackground="#696969",
        activeforeground="white",
        relief=RAISED,
        bd=4,
        command=lambda t=text: button_click(t),
    )
    btn.grid(row=row, column=col, ipadx=20, ipady=10, padx=5, pady=5)

# Add 0 with clear and equals button on its sides
Button(
    root,
    text="Clear",
    font=("Helvetica", 15),
    bg="red",
    fg="white",
    activebackground="#ff6961",
    activeforeground="white",
    relief=RAISED,
    bd=4,
    command=clear_display,
).grid(row=4, column=0, ipadx=15, ipady=10, padx=5, pady=10)

Button(
    root,
    text="0",
    font=("Helvetica", 20),
    bg="black",
    fg="white",
    activebackground="#696969",
    activeforeground="white",
    relief=RAISED,
    bd=4,
    command=lambda: button_click("0"),
).grid(row=4, column=1, ipadx=20, ipady=10, padx=5, pady=10)

Button(
    root,
    text="=",
    font=("Helvetica", 15),
    bg="darkgrey",
    fg="white",
    activebackground="#a9a9a9",
    activeforeground="white",
    relief=RAISED,
    bd=4,
    command=calculate,
).grid(row=4, column=2, ipadx=20, ipady=10, padx=5, pady=10)

# Operator buttons (placed on the right side)
operators = [
    ('+', 1, 3),
    ('-', 2, 3),
    ('*', 3, 3),
    ('/', 4, 3),
]

for (op, row, col) in operators:
    btn = Button(
        root,
        text=op,
        font=("Helvetica", 20),
        bg="lightyellow",
        fg="black",
        activebackground="#f9f9b7",
        activeforeground="black",
        relief=RAISED,
        bd=4,
        command=lambda o=op: add_operator(o),
    )
    btn.grid(row=row, column=col, ipadx=20, ipady=10, padx=5, pady=5)

# Backspace button
Button(
    root,
    text="Backspace",
    font=("Helvetica", 12),
    bg="black",
    fg="white",
    activebackground="#696969",
    activeforeground="white",
    relief=RAISED,
    bd=4,
    command=backspace,
).grid(row=5, column=0, columnspan=4, ipadx=20, ipady=5, padx=5, pady=10)

root.mainloop()
