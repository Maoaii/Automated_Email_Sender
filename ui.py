from tkinter import *
from emailsenderbrain import EmailSender


class EmailSenderUI:

    def __init__(self, email_sender_brain: EmailSender):
        # Set up brain
        self.email_sender_brain = email_sender_brain

        # Window setup
        self.window = Tk()
        self.window.config(width=1000, height=700)
        self.window.config(padx=50, pady=20)
        self.window.title("Automated Email Sender")

        # Text box for email subject writing
        self.email_subject_box = Text(width=50, height=3)
        self.email_subject_box.config(padx=10, pady=10)
        self.email_subject_box.focus()
        self.email_subject_box.insert(END, "Subject")
        self.email_subject_box.place(x=500, y=0)

        # Text box for email body writing
        self.email_body_box = Text(width=50, height=30)
        self.email_body_box.config(padx=10, pady=10)
        self.email_body_box.focus()
        self.email_body_box.insert(END, "Body")
        self.email_body_box.place(x=500, y=100)

        # Text box for email receivers
        self.receiver_box = Text(width=40, height=10)
        self.receiver_box.config(padx=10, pady=10)
        self.receiver_box.insert(END, "Receiver emails (one email per line)")
        self.receiver_box.place(x=0, y=0)

        # Text box for names
        self.names_box = Text(width=50, height=10)
        self.names_box.config(padx=10, pady=10)
        self.names_box.insert(END, "Names (one name per email per line)")
        self.names_box.place(x=0, y=200)

        # Text box for dates
        self.dates_box = Text(width=50, height=10)
        self.dates_box.config(padx=10, pady=10)
        self.dates_box.insert(END, "Dates (one date per email per line)")
        self.dates_box.place(x=0, y=360)

        # Checkbutton for automatic name placeholder replacement
        self.name_placeholder_state = IntVar()
        self.name_placeholder_checkbutton = Checkbutton(text="Name Placeholder?",
                                                        variable=self.name_placeholder_state)
        self.name_placeholder_state.get()
        self.name_placeholder_checkbutton.place(x=0, y=600)

        # Checkbutton for automatic date placeholder replacement
        self.date_placeholder_state = IntVar()
        self.date_placeholder_checkbutton = Checkbutton(text="Date Placeholder?",
                                                        variable=self.date_placeholder_state)
        self.date_placeholder_state.get()
        self.date_placeholder_checkbutton.place(x=0, y=620)

        self.save_email_button = Button(text="Send email", command=self.send_email)
        self.save_email_button.place(x=630, y=550)

        self.window.mainloop()

    def send_email(self):
        has_name_placeholder = self.name_placeholder_state.get() == 1
        has_date_placeholder = self.date_placeholder_state.get() == 1

        receivers = self.receiver_box.get("1.0", END).split()  # Transform into a list
        email_subject = self.email_subject_box.get("1.0", END)

        if has_name_placeholder:
            names = self.names_box.get("1.0", END).split()  # Transform into a list
        if has_date_placeholder:
            dates = self.dates_box.get("1.0", END).split()  # Transform into a list

        for receiver in range(0, len(receivers)):
            email_body = self.email_body_box.get("1.0", END)
            # If there are placeholders, replace them with relevant keywords
            if has_name_placeholder:
                email_body = email_body.replace("[name]", f"{names[receiver]}")
            if has_date_placeholder:
                email_body = email_body.replace("[date]", f"{dates[receiver]}")

            self.email_sender_brain.send_email(receivers, receiver, email_subject, email_body)
