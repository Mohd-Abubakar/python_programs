lst = []
n = int(input('Enter the number:'))
for i in range(0,n):
    i = int(input())
    lst.append(i)
print('The elements in the list are', lst)

m = int(input('Enter the repeated element in the list to be removed:'))

for j in lst:
    if j==m:
        lst.remove(m)
print(lst)