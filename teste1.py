import smtplib
from email.message import EmailMessage



x = open("Email.txt", 'r')
string = ''
for i in x:
    string += i

print(type(string))
print(string.format("ã â À").encode(encoding = 'latin1'))

x = string.format("blerg").encode(encoding = 'utf-8')

print(x.decode('utf-8'))

#print(string.encode(encoding='latin1'))