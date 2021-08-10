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
dentro_GP = ''
dentro_FIN = ''

texto_fora = open("fora.txt", "r")
texto_dentro_GP = open("dentro_GP.txt", "r")
texto_dentro_FIN = open("dentro_FIN.txt", "r")

def manda_email(recieve, message):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
            server.login(sender, password)
            server.sendmail(sender, recieve, message.encode(encoding = "latin1"))
            

for i in texto_fora:
    fora+=i

for el in texto_dentro_GP:
    dentro_GP+=el

for el in texto_dentro_FIN:
    dentro_FIN+=el


for d in data:
    recieve = d['email']
    if d["i/o"]==0:
        print('enviando...')
    
        manda_email(recieve, fora)
        
        print("enviado")
    else:
        if d["sessão"] == "Gestão de Pessoas":
            print('enviando...')
            manda_email(recieve, dentro_GP.format(hora = d["horário"], dia = d["dia"]))
            print('enviado')

        elif d["sessão"] == "Finanças":
            print('enviando...')
            manda_email(recieve, dentro_FIN.format(hora = d["horário"], dia = d["dia"]))
            print('enviado')
