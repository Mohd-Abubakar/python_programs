n = 3
a = [[4,4,5],[5,7,9],[1,4,5]]
d1 = sum(a[i][i] for i in range(n))
d2 = sum(a[i][n-i-1] for i in range(n))
print(str(d1)+ ' '+ str(d2))