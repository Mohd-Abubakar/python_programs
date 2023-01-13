import re
p = 'My name is Abubakar'
s = re.sub(' ','_',p)
s1 = re.sub('_',' ',p)
print('Original Text:',p,'\nResulted Text:',s)
print('Original Text:',s,'\nResulted Text:',s1)
