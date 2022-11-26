frnd = {'mohammed':'14-11-2002','kishor':'12-10-2002'}
print(frnd)
name = input('Enter the name of friend:')
bday = input('Enter the bday of friend:')
frnd[name] = bday
frnd.get(name,bday)
print(frnd)