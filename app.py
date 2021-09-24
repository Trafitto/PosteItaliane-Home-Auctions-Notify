import logging
import sys
from src.spider import Scraper
from src.db.db import Db


def check_new_home():
    db = Db()

    for data in db.get_all():
        if not data.value:
            print(data.key)
            print("To notify")

        



if __name__ == "__main__":
    Scraper().scrape()
    check_new_home()