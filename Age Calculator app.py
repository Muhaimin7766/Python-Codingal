from tkinter import *
from datetime import datetime

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        birth_date = datetime(year, month, day)
        today = datetime.now()
        age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        result_var.set(f"You are {age_years} years old!")
    except ValueError:
        result_var.set("Invalid input. Please enter valid numbers.")

root = Tk()
root.title("Age Calculator App")
root.geometry("400x300")

canvas = Canvas(root, width=400, height=300, bg="#e0f7fa", highlightthickness=0)
canvas.place(x=0, y=0)

for x in range(0, 400, 100):
    for y in range(0, 300, 100):
        canvas.create_text(x + 50, y + 50, text="+", font=("Helvetica", 60), fill="#cfd8dc")
        canvas.create_text(x + 50, y + 80, text="-", font=("Helvetica", 50), fill="#cfd8dc")

title_label = Label(root, text="Age Calculator", font=("Helvetica", 20, "bold"), bg="#e0f7fa", fg="#00796b")
title_label.place(x=100, y=10)

frame = Frame(root, bg="#e0f7fa")
frame.place(x=70, y=60)

Label(frame, text="Day:", font=("Helvetica", 14), bg="#e0f7fa", fg="#004d40").grid(row=0, column=0, padx=5, pady=5)
day_entry = Entry(frame, font=("Helvetica", 14), width=5)
day_entry.grid(row=0, column=1, padx=5, pady=5)

Label(frame, text="Month:", font=("Helvetica", 14), bg="#e0f7fa", fg="#004d40").grid(row=1, column=0, padx=5, pady=5)
month_entry = Entry(frame, font=("Helvetica", 14), width=5)
month_entry.grid(row=1, column=1, padx=5, pady=5)

Label(frame, text="Year:", font=("Helvetica", 14), bg="#e0f7fa", fg="#004d40").grid(row=2, column=0, padx=5, pady=5)
year_entry = Entry(frame, font=("Helvetica", 14), width=5)
year_entry.grid(row=2, column=1, padx=5, pady=5)

result_var = StringVar()
result_label = Label(root, textvariable=result_var, font=("Helvetica", 16), bg="#e0f7fa", fg="#00796b")
result_label.place(x=70, y=180)

calculate_button = Button(root, text="Calculate Age", font=("Helvetica", 14), bg="#00796b", fg="white", command=calculate_age)
calculate_button.place(x=140, y=230)

root.mainloop()
