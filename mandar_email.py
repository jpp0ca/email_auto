import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user = "test.do.poca@gmail.com"
password = "voufazerumteste00"
port = 465
host = "smtp.gmail.com"

recieve = "jppoca27@gmail.com"

x = open("Email.txt", 'r')
string = ''
for i in x:
    string += i

context = ssl.create_default_context()


# server = smtplib.SMTP(host, port)

# server.ehlo()
# server.starttls()
# server.login(user, password)

# message = string.format("Ã")
# email_msg = MIMEMultipart()
# email_msg['From'] = user
# email_msg['To'] = recieve
# email_msg['Subject'] = 'Você'

# email_msg.attach(MIMEText(message, 'plain'))

# print('Enviando mensagem...')
# server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string(), mail_options = ("SMTPUTF8"))
# print('Mensagem enviada!')

# print("enviando...")
# server.send_message(email_msg, email_msg['From'], email_msg['To'], mail_options = ("SMTPUTF8"))
# print("enviado")

print("enviando...")
with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    server.login(user, password)
    a = string.format('Ã')
    server.sendmail(user, recieve, a)

print('enviado')