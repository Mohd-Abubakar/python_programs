def has_duplicate(lst):
    l1 = len(lst)
    l = set(lst)
    l2 = len(l)
    if l1 != l2:
       return True
    else:
        return False

lst = [1,2,2,3,4]
res = has_duplicate(lst)
print(res)
