import os
from src.settings.private import *

AUCTION_URL='https://www.poste.it/alloggi.html'

HOTMAIL_DOMAINS_LIST = ["live.com", "hotmail.com", "hotmail.it", "live.it"]
HOTMAIL_SMTP_CONFIG = {
    "host": "smtp-mail.outlook.com",
    "port": 587,
    "requires_auth": True
}

GOOGLE_DOMAINS_LIST = ["gmail.com"]
GOOGLE_SMTP_CONFIG = {
    "host": "smtp.gmail.com",
    "port": 587,
    "requires_auth": True
}

SMTP_CONFIG_MAP = {
    "hotmail": HOTMAIL_SMTP_CONFIG,
    "gmail": GOOGLE_SMTP_CONFIG
}