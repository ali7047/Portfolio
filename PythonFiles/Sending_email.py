import os
import smtplib
import ssl

def send_email(message):
    host = "smtp.gmail.com"
    sender_email = "adil.study.ali7047@gmail.com"
    port = 465
    sender_password = os.getenv("PASSWORD")

    receiver_email = "adil.study.ali7047@gmail.com"

    ssl_key = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=ssl_key) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
        print("Email sent successfully!")


if __name__ == "__main__":
    message = msg = '''\\
         from: Me@my.org
         subject: testing'...
         
         This is a test '''
    send_email(message)