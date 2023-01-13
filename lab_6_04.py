import re
p = re.compile('\d{4}-\d{2}-\d{2}')
s = p.sub('2002-11-12','12-11-2002')
print('YYYY-MM-DD to DD-MM-YYYY:',s)
