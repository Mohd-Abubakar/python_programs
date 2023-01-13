'''import re
num = re.compile('\+1-\d{3}-\d{3}-\d{4}')
t1 = num.search('Number = +1-354-543-8788')
print('Valid Number=',t1.group())
email = re.compile('\w+@\w+\.com')
t2 = email.search('Email = abubakar1@gmail.com')
print('Valid Email=',t2.group())'''


import re
a = input('Enter a number:')
b = re.compile('\+1-\d{3}-\d{3}-\d{4}')
if b.match(a):
    print('valid Number')
else:
    print('Invalid number')
c = input('Enter the email:')
d = re.compile('\w+@\w+\.com')
if d.match(c):
    print("Valid Email")
else:
    print("Invalid Email")
