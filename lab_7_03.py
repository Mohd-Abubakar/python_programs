a = float(input('Enter the 1 site of triangle:'))
b = float(input('Enter the 2 site of triangle:'))
c = float(input('Enter the 3 site of triangle:'))
if a+b>=c and b+c>=a and c+a>=b:
    print('Triangle is formed')
else:
    print('Triangle is not formed')
s = (a+b+c)/2
res = s*(s-a)*(s-b)*(s-c)
print('Area of a triangle is',res)
