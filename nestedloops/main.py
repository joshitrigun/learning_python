import re
str = 'bob.com'
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print(match.group())
else :
    print('the email is not valid')