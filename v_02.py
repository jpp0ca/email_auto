import pandas as pd
import numpy as np
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import smtplib
import ssl

sender = "test.do.poca@gmail.com"
password = "voufazerumteste00"

port = 465

context = ssl.create_default_context()

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("teste").worksheet("emails")

data = sheet.get_all_records()

fora = ''
dentro = ''

texto_fora = open("fora.txt", "r")

texto_dentro = open("dentro.txt", "r")

def manda_email(recieve, message):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
            server.login(sender, password)
            server.sendmail(sender, recieve, message.encode(encoding = "utf-8"), mail_options = ())
            

for i in texto_fora:
    fora+=i

for el in texto_dentro:
    dentro+=el

for d in data:
    recieve = d['email']
    if d["i/o"]==0:
        print('enviando...')
    
        manda_email(recieve, fora)
        
        print("enviado")
    else:
        print('enviando...')

        dentro_formatado = dentro.format(sessao = d["sessão"], dia = d['dia'], hora = d['horário'])

        #print("sem encode")
        #print(dentro_formatado)

        manda_email(recieve, dentro_formatado)
        
        print("enviado")