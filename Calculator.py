def add(X,Y):
    return X+Y
def subtract(X,Y):
    return X-Y
def multiply (X,Y):
    return X*Y
def divide(X,Y):
    return X/Y

print("Please enther the choice (a/b/c/d): ")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice=input("Please enther the choice(a/ b/ c/ d): ")
num1=int(input("Please enter the first number: "))
num2=int(input("Please enter the second number: "))

if choice=='a':
    print(num1,"+",num2,"=",add(num1, num2))
elif choice=='b':
    print(num1,"-",num2,"=",subtract(num1, num2))
elif choice=='c':
    print(num1,"*",num2,"=",multiply(num1, num2))
elif choice=='d':
    print(num1,"/",num2,"=",divide(num1, num2))
else:
    print("Invalid input")