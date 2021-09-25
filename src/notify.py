import smtplib
import ssl
from .settings.settings import SMTP_PORT, SMTP_SERVER, SENDER_EMAIL, DEFAULT_RECIVER_EMAIL, EMAIL_PASSWORD, DEFAULT_EMAIL_PROVIDER, OUTLOOK, HOTMAIL


class EmailNotify():
    def __init__(self, reciver_email=None, provider=DEFAULT_EMAIL_PROVIDER):
        self.smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

        if provider == OUTLOOK or provider == HOTMAIL:
            self.smtp_server.starttls()

        self.sender_email = SENDER_EMAIL
        self.receiver_email = DEFAULT_RECIVER_EMAIL if reciver_email is None else reciver_email
        self.password = EMAIL_PASSWORD

    def format_message(self, new_home):
        self.message = '''
            Subject: New Auction Inserted: {home}

            This message is automatic
        '''.format(home=new_home)

    def send(self, new_home):
        self.format_message(new_home)

        self.smtp_server.ehlo()
        self.smtp_server.login(self.sender_email, self.password)
        self.smtp_server.sendmail(
            self.sender_email, self.receiver_email, self.message)
        self.smtp_server.quit()
