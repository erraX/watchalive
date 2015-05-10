#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
from email.MIMEMultipart import MIMEMultipart

def send_mail(receiver, subject, text):
    sender = '271711003@qq.com'
    # smtpserver = 'smtp.163.com'  
    smtpserver = 'smtp.qq.com'  
    username = '271711003@qq.com'  
    password = 'voT3lOf1iLg6Av'

    msg = MIMEText(text)
    msg.set_charset("utf-8")
    msg['Subject'] = subject
    msg['From'] = sender

    smtp = smtplib.SMTP()  
    smtp.connect('smtp.qq.com', '587')
    smtp.ehlo()
    smtp.starttls() 
    smtp.esmtp_features["auth"]="AUTH_LOGIN"
    smtp.login(username, password)  
    for r in receiver:
        msg['To'] = r
        smtp.sendmail(sender, r, msg.as_string())  
    smtp.quit()

if __name__ == "__main__":
    send_mail(['niminjiecide@gmail.com'], 'HELLO U2', 'osidfnoiasdfsdfp[s]dfp[aebk oajfiboarepgjvaioejvioadb')
