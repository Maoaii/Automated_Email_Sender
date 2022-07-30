import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:

    def __init__(self, email_sender, email_password):
        # Port
        self.PORT = 587

        self.email_sender = email_sender
        self.email_password = email_password

    def send_email(self, receivers, receiver, email_subject, email_body):
        # Set up mime
        msg = MIMEMultipart()

        # Set up email sender, receiver, subject and body
        msg['From'] = self.email_sender
        msg['To'] = receivers[receiver]
        msg['Subject'] = email_subject
        msg.attach(MIMEText(email_body, 'plain'))

        # Send the email
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', self.PORT)
        server.starttls()
        server.login(self.email_sender, self.email_password)
        server.sendmail(self.email_sender, receivers[receiver], text)
        server.quit()
