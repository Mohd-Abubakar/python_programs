x = [[2,5,6],[5,8,1],[9,1,2]]
y = [[1,2,3],[4,5,6],[7,8,9]]
res = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        res[i][j] = x[i][j] + y[i][j]

for r in res:
    print(r)