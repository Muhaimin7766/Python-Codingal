test_dict={'Cristiano Ronaldo' : 2, 'is the' : 2, 'best' : 2, 'for the' : 2, 'Ballon D OR' : 1}
print("The oroiginal dictionary: "+ str(test_dict))
K=2
res=0
for key in test_dict:
    if test_dict[key]==K:
        res=res+1

print("Frequency of K is : "+ str(res))