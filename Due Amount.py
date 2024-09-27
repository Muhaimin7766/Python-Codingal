def calculate_due_amount(total_bill, amount_paid):
    due_amount = total_bill - amount_paid
    return due_amount

total_bill = float(input("Enter the total bill amount: "))
amount_paid = int(input("Enter the amount paid: "))

due_amount = calculate_due_amount(total_bill, amount_paid)

print(f"The remaining due amount is: {due_amount}")