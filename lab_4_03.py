def bi_src(lst,low,high,x):
    if high > low:
        mid = (high+low)//2
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            return bi_src(lst, low, mid - 1, x)
        else:
            return bi_src(lst, mid + 1, high, x)
    else:
        return -1

lst = []
n = int(input("Enter the number of elements in list:"))
for i in range(0,n):
    i = int(input())
    lst.append(i)
print('List=',lst)
x = int(input('Enter the key:'))
res = bi_src(lst,0,n-1,x)
if res != -1:
    print('Element found at ' + str(res+1) + ' position')
else:
    print('Element not found')
