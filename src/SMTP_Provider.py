import smtplib
import os
from .settings import GOOGLE_DOMAINS_LIST, HOTMAIL_DOMAINS_LIST, SMTP_CONFIG_MAP

class SMTP_Provider():
    def select_provider(self, smtp_login):
        sender_parts = smtp_login.split("@")
        _, domain = sender_parts
        pick_provider = None
        if domain in GOOGLE_DOMAINS_LIST:
            pick_provider = "gmail"
        elif domain in HOTMAIL_DOMAINS_LIST:
            pick_provider = "hotmail"
        else:
            raise Exception(f"domain {domain} not supported")
        
        use_provider = SMTP_CONFIG_MAP[pick_provider]
        if not use_provider:
            raise Exception(f"unable to use an SMTP provider")

        return use_provider
    
    def get_smtp_session(self, sender_email, sender_password):
        smtp_provider = self.select_provider(sender_email)
        smtp_session = smtplib.SMTP(
            smtp_provider["host"], 
            smtp_provider["port"]
        )

        if smtp_provider["requires_auth"]:
            try:
                smtp_session.starttls()
                smtp_session.login(sender_email, sender_password)
                smtp_session.ehlo()
            except smtplib.SMTPAuthenticationError:
                print("""
                    mail sending has been denied by Google because your account does not allow less-secure applications\n
                    Learn more at: https://support.google.com/accounts/answer/6010255
                """)

        return smtp_session
        

