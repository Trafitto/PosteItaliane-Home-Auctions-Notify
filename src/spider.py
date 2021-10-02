import requests
from bs4 import BeautifulSoup
from .settings import AUCTION_URL
from .db.db import Db

class Scraper():
    def __init__(self):
        self.request = requests.get(AUCTION_URL)
        self.request.raise_for_status()
        self.homes = []

    def scrape(self):

        soup = BeautifulSoup(self.request.content, 'html.parser')

        town_list_parent = soup.find('div', id='alloggi_legge_56093__gare_in_corso-parent')
        

        all_links = town_list_parent.find_all('a')
        town_links = town_list_parent.find_all('a', class_="accordion-toggle collapsed")

        for home in all_links:
            if home not in town_links:
                self.homes.append(home.text)
        
        self._update_data()
    
    def _update_data(self):
        db = Db()
        first_load = True
        if not db.is_empty():
            first_load = False

        for home in self.homes:
            if first_load:
                db.set(home, True)
            else:
                if db.key_exist(home):
                    continue
                db.set(home, False)
