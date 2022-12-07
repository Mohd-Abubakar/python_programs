def is_sorted(lst):
    if lst == sorted(lst):
        return True
    else:
        return False

r = is_sorted([1,2,3,4,5])
print(r)
