import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "22f2000718@ds.study.iitm.ac.in"
password = "eghr ttrk ktxc yfxu"
message = MIMEMultipart("alternative")
message["From"] = sender_email

def send_email(to, subject, content_body):
    message["Subject"] = subject
    message["To"] = to
    message.attach(MIMEText(content_body, 'html'))

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, to, message.as_string()
        )
