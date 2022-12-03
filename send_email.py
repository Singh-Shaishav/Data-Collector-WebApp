from email.mime.text import MIMEText
import smtplib

def send_email(email, height, average_height):
    from_email='shaishav.singh420@gmail.com'
    from_password='mcgnniazonfhgjqb'
    to_email= email

    subject="Height Data Analysis"
    message="Hey there, your height entered is <strong>%s</strong> Cms. On analyzing survey data , the average height is <strong>%s</strong> "% (height, average_height)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['from']=from_email
    msg['to']=to_email

    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)



