def csum(l):
    l2 = []
    le = len(l)
    l2 = [sum(l[0:i:1]) for i in range(0, le+1)]
    return l2[1:]

l = [1,2,3,4,5]
print (csum(l))
