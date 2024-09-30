def check_age():
    try:
        age = int(input("Enter your age: "))

        if age < 0:
            print("Age cannot be negative!")
        else:
            if age % 2 == 0:
                print(f"Your age {age} is even.")
            else:
                print(f"Your age {age} is odd.")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer for age.")

check_age()
