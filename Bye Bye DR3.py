valid = False
while not valid:
    try:
        n=int(input("Enter a number: "))
        while n%3==0:

            print("Bye Bye DR3")
        valid=True
    except ValueError:
        print("Invalid")