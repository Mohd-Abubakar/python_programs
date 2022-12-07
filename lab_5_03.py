def middle(lst):
    x = slice(1,-1)
    return lst[x]

lst = [1,2,3,4,5]
res = middle(lst)
print(res)
