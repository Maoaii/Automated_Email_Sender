import os
from ui import EmailSenderUI
from emailsenderbrain import EmailSender

# Set up email to send from
email_sender = os.environ.get("EMAIL_SENDER")
email_password = os.environ.get("EMAIL_PASSWORD")

# Set up sender
email_sender_brain = EmailSender(email_sender, email_password)

# Set up UI
email_sender_ui = EmailSenderUI(email_sender_brain)
