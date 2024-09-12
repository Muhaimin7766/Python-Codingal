string=input("PLease enter your own word:")
character=input("Please enter your own character:")
i=0
count=0
while(i<len(string)):
    if(string[i]==character):
        count=count+1
    i=i+1
print("The total number of times", character, "has occured=",count)