import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

data = pd.read_excel('testset.xlsx')
data2 = pd.read_excel('testset.xlsx', index_col=0, engine='openpyxl')
l = data['EMAIL']
dic = {}

for d in l:
    tem = data2.loc[d]
    dic[d] = tem['MESSAGE']

# Set your email credentials
sender_email = "koundinyaatchyutuni@gmail.com"
password = "rhdepotyvdqwpbnk"  # Replace with your actual Gmail password

for d in l:
    SUBJECT = "TEST MAIL"
    message_text = dic[d]

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = d
    message['Subject'] = SUBJECT

    # Attach the message text
    message.attach(MIMEText(message_text, 'plain'))

    # Connect to Gmail SMTP server
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    # Log in to your Gmail account
    s.login(sender_email, password)

    # Send the email
    s.sendmail(sender_email, d, message.as_string())

    # Quit the SMTP server
    s.quit()
