decimal_number = int(input("Enter a decimal number: "))
binary_string = ""
while decimal_number > 0:
    remainder = decimal_number % 2
    binary_string = str(remainder) + binary_string
    decimal_number = decimal_number // 2
print("The binary representation is:", binary_string)