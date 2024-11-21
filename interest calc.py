from tkinter import *

def calculate_interest():
    principal = entry_principal.get()
    time = entry_time.get()
    rate = entry_rate.get()

    if principal.isdigit() and time.isdigit() and rate.replace('.', '', 1).isdigit():
        principal = float(principal)
        time = int(time)
        rate = float(rate)

        simple_interest = (principal * time * rate) / 100
        compound_interest = principal * ((1 + rate / 100) ** time) - principal

        label_result.config(text=f"Simple Interest: ${simple_interest:.2f}\nCompound Interest: ${compound_interest:.2f}")
    else:
        label_result.config(text="Invalid input")

window = Tk()
window.title("Interest Calculator App")
window.geometry("500x500")
window.configure(bg="#DFFFD6")

canvas = Canvas(window, bg="#DFFFD6", highlightthickness=0)
canvas.place(relwidth=1, relheight=1)

# Create staggered $ symbols
for i in range(0, 500, 50):  # Columns
    for j in range(0, 500, 50):  # Rows
        if (i // 50 + j // 50) % 2 == 0:  # Stagger the placement
            canvas.create_text(i + 25, j + 25, text="$", fill="#32CD32", font=("Arial", 18, "bold"))

label_title = Label(
    window, 
    text="Interest Calculator", 
    font=("Arial", 16, "bold"), 
    bg="#DFFFD6", 
    fg="#006400"
)
label_title.pack(pady=10)

label_principal = Label(
    window, 
    text="Principal Amount:", 
    font=("Arial", 12, "bold"), 
    bg="#DFFFD6", 
    fg="#006400"
)
label_principal.pack(pady=5)

entry_principal = Entry(window, font=("Arial", 12), justify="center")
entry_principal.pack(pady=5)

label_time = Label(
    window, 
    text="Time Period (in years):", 
    font=("Arial", 12, "bold"), 
    bg="#DFFFD6", 
    fg="#006400"
)
label_time.pack(pady=5)

entry_time = Entry(window, font=("Arial", 12), justify="center")
entry_time.pack(pady=5)

label_rate = Label(
    window, 
    text="Rate of Interest (%):", 
    font=("Arial", 12, "bold"), 
    bg="#DFFFD6", 
    fg="#006400"
)
label_rate.pack(pady=5)

entry_rate = Entry(window, font=("Arial", 12), justify="center")
entry_rate.pack(pady=5)

btn_calculate = Button(
    window, 
    text="Calculate", 
    font=("Arial", 12, "bold"), 
    bg="#32CD32", 
    fg="white", 
    command=calculate_interest
)
btn_calculate.pack(pady=10)

label_result = Label(
    window, 
    text="", 
    font=("Arial", 14, "bold"), 
    bg="#DFFFD6", 
    fg="#006400"
)
label_result.pack(pady=10)

window.mainloop()
