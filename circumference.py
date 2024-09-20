import math

def calculate_circumference(radius):
    """
    This function calculates the circumference of a circle.
    
    Formula: C = 2 * π * radius
    """
    return 2 * math.pi * radius

radius = float(input("Enter the radius of the circle: "))
circumference = calculate_circumference(radius)
print(f"The circumference of the circle is: {circumference:.2f}")