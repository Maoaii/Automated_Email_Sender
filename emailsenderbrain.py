import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTPAuthenticationError, SMTPRecipientsRefused
from tkinter import messagebox


class EmailSender:

    def __init__(self, email_sender, email_password):
        # Port
        self.PORT = 587

        # Set up sender
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

        try:
            server.login(self.email_sender, self.email_password)
        except SMTPAuthenticationError:
            # The user email or password is invalid
            messagebox.showwarning(title="Sender not available", message="User email or password is invalid.")
            quit()

        successfully_sent = None
        try:
            server.sendmail(self.email_sender, receivers[receiver], text)
        except SMTPRecipientsRefused:
            # One or more recipients aren't valid
            successfully_sent = False
        else:
            # Message sent successfully
            successfully_sent = True

        server.quit()

        return successfully_sent
