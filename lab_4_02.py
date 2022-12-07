def lisrh(l1,n,key):
    for i in range(0,n):
        if l1[i] == key:
            return i
    return -1

l1 = []
n = int(input("Enter the length of a list:"))
for i in range(0,n):
    i = int(input())
    l1.append(i)
print('List=',l1)
key = int(input('Enter the key value to be search:'))
lin = lisrh(l1,n,key)
if lin == -1:
    print('Element not found')
else:
    print('Element found at ' + str(lin+1) + ' position')
