import SMTP_Provider

class EmailNotify():
    def __init__(self):
        self.smtp_provider = SMTP_Provider()
    
    def format_message(self, new_home):
        return '''
            Subject: New Auction Inserted: {home}

            This message is automatic
        '''.format(home=new_home)

    def send(self, message, receiver_email):
        smtp_session = self.smtp_provider.get_smtp_session()
        smtp_session.sendmail(
            self.sender_email,
            self.receiver_email,
            self.format_message(message)
        )
        smtp_session.quit()

        print(f"Mail sent to: {self.receiver_email}")
