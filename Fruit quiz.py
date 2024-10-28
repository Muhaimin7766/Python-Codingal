import random
class FruitQuiz:
    def __init__(self):
        self.fruits={'apple':'red','orange':'orange','watermelon':'green','banana':'yellow',}
    def quiz(self):
        while (True):
            fruit, colour=random.choice(list(self.fruits.items()))
            print("What is the colour of {}".format(fruit))
            user_answer=input()
            if(user_answer.lower()==colour):
                print("Correct answer")
            else:
                print("Wrong answer")
            
            option=int(input("enter 0, if you want to play the game again, otherwise enter 1: "))
            if (option):
                break
print("Welcome to the fruit quiz!!!")
fq=FruitQuiz()
fq.quiz()
            