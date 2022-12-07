import statistics
lst = []
n = int(input("Enter the number of elements in list:"))
for i in range(0,n):
    i = int(input())
    lst.append(i)
print(lst)

m = statistics.mean(lst)
print("Mean=",m)
v = statistics.variance(lst)
print("Variance=",v)
std = statistics.stdev(lst)
print("Standard deviation=",std)
