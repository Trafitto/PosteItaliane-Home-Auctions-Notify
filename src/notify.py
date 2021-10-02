import os
from .SMTP_Provider import SMTP_Provider

class EmailNotify():
    def __init__(self):
        self.setup_smtp()
        self.smtp_provider = SMTP_Provider()
    
    def format_message(self, new_home):
        return '''
            Subject: New Auction Inserted: {home}

            This message is automatic
        '''.format(home=new_home)
    
    def setup_smtp(self):
        smtp_login = os.getenv("SENDER_EMAIL")
        if smtp_login and smtp_login.strip():
            self.smtp_login = smtp_login
        else:
            raise Exception(f"SENDER_EMAIL environment value not provided")

        smtp_password = os.getenv("SENDER_PASSWORD")
        if smtp_password and smtp_password.strip():
            self.smtp_password = smtp_password
        else:
            raise Exception(f"SENDER_PASSWORD environment value not provided")

        receiver_address = os.getenv("RECEIVER_EMAIL")
        if receiver_address and receiver_address.strip():
            self.receiver_address = receiver_address
        else:
            raise Exception(f"RECEIVER_EMAIL environment value not provided")

    def send(self, message):
        smtp_session = self.smtp_provider.get_smtp_session(
            self.smtp_login, self.smtp_password
        )
        smtp_session.sendmail(
            self.smtp_login, self.receiver_address, self.format_message(message)
        )
        smtp_session.quit()

        print(f"Mail sent to: {self.receiver_address}")
