l = []
sum=0
print('Enter the marks of 5 subject')
for i in range(5):
    i = int(input())
    l.append(i)
for i in l:
    sum = sum+i
per = (sum/500)*100
print('percentage is '+str(per) +'%')
