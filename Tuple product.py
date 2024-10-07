import math

def tuple_product(numbers):
    return math.prod(numbers)  

numbers_tuple = (1, 6, 3, 4)

result = tuple_product(numbers_tuple)
print(f"The product of the numbers in the tuple {numbers_tuple} is: {result}")
