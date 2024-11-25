from tkinter import *
from tkinter import messagebox

def check_password_strength():
    password = password_entry.get()
    length = len(password)

    if length == 0:
        strength_label.config(text="No Password Entered", fg="red")
        return

    strength = "Weak"
    if length >= 8:
        if any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
            strength = "Strong"
        elif any(char.isdigit() for char in password) or any(char.isalpha() for char in password):
            strength = "Moderate"

    if strength == "Weak":
        color = "red"
    elif strength == "Moderate":
        color = "orange"
    else:
        color = "green"

    strength_label.config(text=f"Password Strength: {strength}", fg=color)

# Create main window
root = Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.configure(bg="lightblue")

# Create widgets
title_label = Label(root, text="Password Strength Checker", font=("Helvetica", 16, "bold"), bg="lightblue")
title_label.pack(pady=10)

password_label = Label(root, text="Enter Password:", font=("Helvetica", 12), bg="lightblue")
password_label.pack()

password_entry = Entry(root, font=("Helvetica", 12), show="*", width=30)
password_entry.pack(pady=5)

check_button = Button(root, text="Check Strength", font=("Helvetica", 12), command=check_password_strength, bg="black", fg="white")
check_button.pack(pady=10)

strength_label = Label(root, text="", font=("Helvetica", 12), bg="lightblue")
strength_label.pack(pady=5)

# Run the application
root.mainloop()
