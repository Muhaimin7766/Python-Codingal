from tkinter import *

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

root = Tk()
root.title("Product Calculator")
root.geometry("400x300")

root.configure(bg="#f0f8ff")  

label1 = Label(root, text="Enter First Number:", bg="#f0f8ff")
label1.pack(pady=10)
entry1 = Entry(root, width=20, bg="#e6ffe6")  
entry1.pack()

label2 = Label(root, text="Enter Second Number:", bg="#f0f8ff")
label2.pack(pady=10)
entry2 = Entry(root, width=20, bg="#e6ffe6")  
entry2.pack()

calculate_button = Button(root, text="Calculate Product", command=calculate_product, bg="#ffcccb")  
calculate_button.pack(pady=20)

result_label = Label(root, text="Product: ", font=("Arial", 14), bg="#ffffe0", fg="black")  
result_label.pack(pady=10)

root.mainloop()
