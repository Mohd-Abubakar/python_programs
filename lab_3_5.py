lst1 = []
lst2 = []
lst = [12,'abc','xyz',10,44,'nmp']

for e in lst:
    if type(e)==int:
        lst1.append(e)
    elif type(e)==str:
        lst2.append(e)

print('Integer list:',lst1)
print('String list:',lst2)