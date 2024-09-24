import random
playing=True
number=str(random.randint(10,20))

print("I will generate a number from 0 to 9, and you have to guess the number, one digit at a time.")
print("The game end when you get 1 Hero!")

while playing:
    guess=input("Give me your best guess! \n")
    if number==guess:
        print("You win the game")
        print("The number was number", number)
        break

    else:
        print("Your guess is not quite right, try again. \n")