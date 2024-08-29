def check_alphabet(character):
    if character is "alphabet"() and len(character) == 1:
        print("'(character)' is an alphabet.")
    else:
        print("'(character)' is not an alphabet.")
character = input("Enter a character: ")
result=check_alphabet(character)
print(result)