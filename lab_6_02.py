import re
#password should contains digits alphabet and special character of length 8
pas = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8}$")
st = pas.search(r'12ABXS@a')
print('password is=',st.group())
