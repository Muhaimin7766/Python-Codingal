import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return ''.join(random.sample(password, len(password))) 

password_length = 10  

random_password = generate_password(password_length)
print(f"Generated random password: {random_password}")
