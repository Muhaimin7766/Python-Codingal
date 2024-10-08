s1={2, 3, 1}
s2={'b', 'a', 'c'}
s3=list(zip(s1, s2))
print(s3, "\n")

list1=[20, 40, 80]
list2=[300, 100, 400, 600]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

stocks=['BMW', 'Mercedes', 'Pontiac']
prices=[117999, 90000, 65799]

new_dict={stocks: prices for stocks, prices in zip(stocks, prices)}
print('\n', format(new_dict))