import logging
import sys
from src.spider import Scraper
from src.db.db import Db
from src.notify import EmailNotify 


def check_new_home():
    db = Db()

    for data in db.get_all():
        if not data.value:
            print(f'Finded new home to notify {data.key}')
            # TODO: Notify user
            db.set(data.key, True) # Save the status

        



if __name__ == "__main__":
    Scraper().scrape()
    check_new_home()
    EmailNotify().send('OLA')