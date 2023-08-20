import smtplib
import pandas as pd
import base64
from Crypto.Cipher import AES
from email.mime.multipart import MIMEMultipart
data=pd.read_excel('testset.xlsx')
data2=pd.read_excel('testset.xlsx',index_col=0, engine='openpyxl')
l=data['EMAIL']
dic={}
# key = b'candyisagoodboyy'
# cipher = AES.new(key, AES.MODE_EAX)
# nonce = cipher.nonce
for d in l:
    tem=data2.loc[d]
    dic[d]=tem['MESSAGE']
# print(l)  
for d in l:
    SUBJECT = "TEST MAIL"   
    T = dic[d].encode('utf-8')
    print(T)
    # T=str(T)
    print(T)
    T=T.decode()
    # T=T.decode()
    print(T)
    T=T.encode()
    # # T = base64.b64decode(T)
    # cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    # TEXT = cipher.decrypt(T)
    message = 'Subject: {}\n\n{}'.format(SUBJECT, T)
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("koundinyaatchyutuni@gmail.com", "rhdepotyvdqwpbnk")
    s.sendmail("koundinyaatchyutuni@gmail.com",d, message)
    # s.send_message(msg)
    s.quit()
