class Student:
    __schoolName="Sunnydale"

    def __init__(self, name, age):
        self.__name=name

    def __display(self):
        print('This is private method')

std=Student("Farah", 25)
print(std.__schoolName)