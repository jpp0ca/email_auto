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

def email_dentro(i):
    recieve = i
    message = """\
    Subject: Dentro

    bla bla bla bla

    ASS pocilga
    """
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)
    return

def email_fora(i):

    recieve = i
    message = """\
    Subject: Fora

    bla bla bla bla

    ASS pocilga
    """
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)
    return


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("teste").sheet1

data = sheet.get_all_records()
for d in data:
    if d["i/o"]==0:
        print('enviando...')
        email_fora(d['email'])
        print("enviado")
    else:
        print('enviando...')
        email_dentro(d['email'])
        print("enviado")

