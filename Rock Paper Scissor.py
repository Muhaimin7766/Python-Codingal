import random
options=["Rock", "Paper", "Scissors"]
user_choice=input("Chose Rock, Paper or Scissors: ")
computer_choice=random.choice(options)
print("You choose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice==computer_choice:
    print("Tie")
elif user_choice=="Rock" and computer_choice=="Scissors":
    print("W")
elif user_choice=="Paper" and computer_choice=="Rock":
    print("W")
elif user_choice=="Scissors" and computer_choice=="Paper":
    print("W")
else:
    print("L")