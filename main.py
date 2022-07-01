from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import data  # File with email and password from which you want to send emails

# Port
PORT = 587

# Set up email sender
email_sender = data.email_sender
email_password = data.sender_password

# Window setup
window = Tk()
window.config(width=1000, height=700)
window.config(padx=50, pady=20)
window.title("Automated Email Sender")

# Text box for email subject writing
email_subject_box = Text(width=50, height=3)
email_subject_box.config(padx=10, pady=10)
email_subject_box.focus()
email_subject_box.insert(END, "Subject")
email_subject_box.place(x=500, y=0)

# Text box for email body writing
email_body_box = Text(width=50, height=30)
email_body_box.config(padx=10, pady=10)
email_body_box.focus()
email_body_box.insert(END, "Body")
email_body_box.place(x=500, y=100)

# Text box for email receivers
receiver_box = Text(width=40, height=10)
receiver_box.config(padx=10, pady=10)
receiver_box.insert(END, "Receiver emails (one email per line)")
receiver_box.place(x=0, y=0)

# Text box for names
names_box = Text(width=50, height=10)
names_box.config(padx=10, pady=10)
names_box.insert(END, "Names (one name per email per line)")
names_box.place(x=0, y=200)

# Text box for dates
dates_box = Text(width=50, height=10)
dates_box.config(padx=10, pady=10)
dates_box.insert(END, "Dates (one date per email per line)")
dates_box.place(x=0, y=360)

# Checkbutton for automatic name placeholder replacement
name_placeholder_state = IntVar()
name_placeholder_checkbutton = Checkbutton(text="Name Placeholder?",
                                           variable=name_placeholder_state)
name_placeholder_state.get()
name_placeholder_checkbutton.place(x=0, y=600)

# Checkbutton for automatic date placeholder replacement
date_placeholder_state = IntVar()
date_placeholder_checkbutton = Checkbutton(text="Date Placeholder?",
                                           variable=date_placeholder_state)
date_placeholder_state.get()
date_placeholder_checkbutton.place(x=0, y=620)


# Button to send email
def send_email():
    has_name_placeholder = name_placeholder_state.get() == 1
    has_date_placeholder = date_placeholder_state.get() == 1

    receivers = receiver_box.get("1.0", END).split()  # Transform into a list
    email_subject = email_subject_box.get("1.0", END)

    if has_name_placeholder:
        names = names_box.get("1.0", END).split()  # Transform into a list
    if has_date_placeholder:
        dates = dates_box.get("1.0", END).split()  # Transform into a list

    # For every person we want to send an email to
    for receiver in range(0, len(receivers)):
        email_body = email_body_box.get("1.0", END)
        # If there are placeholders, replace them with relevant keywords
        if has_name_placeholder:
            email_body = email_body.replace("[name]", f"{names[receiver]}")
        if has_date_placeholder:
            email_body = email_body.replace("[date]", f"{dates[receiver]}")

        # Set up mime
        msg = MIMEMultipart()
        # Set up email sender, receiver, subject and body
        msg['From'] = email_sender
        msg['To'] = receivers[receiver]
        msg['Subject'] = email_subject
        msg.attach(MIMEText(email_body, 'plain'))

        # Send the email
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', PORT)
        server.starttls()
        server.login(email_sender, email_password)
        server.sendmail(email_sender, receivers[receiver], text)
        server.quit()


save_email_button = Button(text="Send email", command=send_email)
save_email_button.place(x=630, y=550)

window.mainloop()
