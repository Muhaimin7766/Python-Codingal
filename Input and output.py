Amount=int(input("Please Enter Amount For Withdraw:"))

note1=Amount//100
note2=(Amount%100)//50
note3=((Amount%100)%50)//10

print("notes of 100 rupee",note1)
print("notesof 50 rupee",note2)
print("notes of 10 rupee",note3)