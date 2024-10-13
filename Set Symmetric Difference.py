def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = symmetric_difference(set_a, set_b)
print(f"Symmetric difference between {set_a} and {set_b} is: {result}")
