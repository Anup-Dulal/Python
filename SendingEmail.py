import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('user name','password')

server.sendmail('sender email','recevier email', 'message')
print('Mail sent')