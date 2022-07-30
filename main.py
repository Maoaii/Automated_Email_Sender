import os
import json
from ui import EmailSenderUI
from emailsenderbrain import EmailSender

# Set up email to send from
try:
    with open("data.json") as data_file:
        data = json.load(data_file)
        os.environ["EMAIL_SENDER"] = data["EMAIL_SENDER"]
        os.environ["EMAIL_PASSWORD"] = data["EMAIL_PASSWORD"]
except FileNotFoundError:
    print("No such file exists")
    quit()

email_sender = os.environ.get("EMAIL_SENDER")
email_password = os.environ.get("EMAIL_PASSWORD")

# Set up sender
email_sender_brain = EmailSender(email_sender, email_password)

# Set up UI
email_sender_ui = EmailSenderUI(email_sender_brain)
