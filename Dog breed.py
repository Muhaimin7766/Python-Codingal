class Dog:
    species = "Canis lupus familiaris"  

    def __init__(self, breed, name):
        self.breed = breed  
        self.name = name    
    def display_info(self):
        print(f"Dog's Name: {self.name}, Breed: {self.breed}, Species: {Dog.species}")

dog1 = Dog("Golden Retriever", "Buddy")
dog2 = Dog("Bulldog", "Max")

dog1.display_info()
dog2.display_info()
