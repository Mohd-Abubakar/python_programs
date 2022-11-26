l1 = []
n = int(input("Enter the number:"))
for i in range(0,n):
    i = int(input())
    l1.append(i)
print('Entered list is', l1)
print('Elements in ascending order:')
l1.sort()
print(l1)
print('Elements in descending order:')
l1.sort(reverse=True)
print(l1)