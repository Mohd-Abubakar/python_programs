s = input('Enter the string of 4 character:')
for i in s:
    print(i)
for i in s:
    s.replace(s[i],s[i+1])
print(s)
