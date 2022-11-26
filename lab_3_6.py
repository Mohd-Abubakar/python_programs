lst = []
n = int(input("Enter the number:"))
for i in range(0,n):
    i = int(input())
    lst.append(i)
print('Entered list is', lst)
max = 0
res = lst[0]
for i in lst:
    freq = lst.count(i)
    if freq > max:
        max = freq
        res = i
print('Most frequent number is:',res)