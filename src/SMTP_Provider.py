import smtplib
import os
from settings.settings import GOOGLE_DOMAINS_LIST, HOTMAIL_DOMAINS_LIST, SMTP_CONFIG_MAP

class SMTP_Provider():
    def __init__(self):
        self.setup_smtp()

    def select_provider(self):
        sender_parts = self.smtp_login.split("@")
        _, domain = sender_parts
        pick_provider = None
        if domain in GOOGLE_DOMAINS_LIST:
            pick_provider = "gmail"
        elif domain in HOTMAIL_DOMAINS_LIST:
            pick_provider = "hotmail"
        else:
            raise Exception(f"domain {domain} not supported")

        return SMTP_CONFIG_MAP[pick_provider]

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
   
    
    def get_smtp_session(self):
        smtp_provider = self.select_provider(self.login)
        smtp_session = smtplib.SMTP(
            smtp_provider.host, 
            smtp_provider.port
        )

        if smtp_provider.requires_auth:
            smtp_session.starttls()
            smtp_session.login(self.smtp_login, self.smtp_password)
            smtp_session.ehlo()

        return smtp_session
        

