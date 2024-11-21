from tkinter import *

def convert_to_cm():
    inches = entry_inches.get()
    if inches.isdigit() or (inches.replace('.', '', 1).isdigit() and inches.count('.') < 2): 
        cm = float(inches) * 2.54
        label_result.config(text=f"{cm:.2f} cm")
    else:
        label_result.config(text="Invalid input")

window = Tk()
window.title("Length Converter App")
window.geometry("400x200")
window.configure(bg="#E0FFFF")

label_prompt = Label(
    window, 
    text="Enter length in inches:", 
    font=("Arial", 12, "bold"), 
    fg="#333333", 
    bg="#E0FFFF"
)
label_prompt.pack(pady=10)

entry_inches = Entry(window, font=("Arial", 12), justify="center")
entry_inches.pack(pady=5)

btn_convert = Button(
    window, 
    text="Convert to cm", 
    font=("Arial", 12, "bold"), 
    fg="#333333", 
    bg="#B2DFEE", 
    command=convert_to_cm
)
btn_convert.pack(pady=10)

label_result = Label(
    window, 
    text="", 
    font=("Arial", 14, "bold"), 
    fg="#333333", 
    bg="#E0FFFF"
)
label_result.pack(pady=10)

window.mainloop()
