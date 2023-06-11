import smtplib

from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_mail():
    message = MIMEMultipart()
    message["From"] = "testgbpostmarina@mail.ru"
    message["To"] = "testgbpostmarina@mail.ru"
    message["Subject"] = "Test report"
    mypass = "838ufsAIr3fa99fxg43f"
    text = "Test result"

    message.attach(MIMEText(text))
    with open('log.txt', 'rb') as f:
        attachment = MIMEApplication(f.read(), Name="log.txt")
        message.attach(attachment)

    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
    server.login(message["From"], mypass)
    text = message.as_string()
    server.sendmail(message["From"], message["To"], text)
    server.quit()

