import requests
from bs4 import BeautifulSoup
from .settings import AUCTION_URL
import logging


class Scraper():
    def __init__(self):
        self.request = requests.get(AUCTION_URL)
        self.request.raise_for_status()

    def scrape(self):
        soup = BeautifulSoup(self.request.content, 'html.parser')

        town_list_parent = soup.find('div', id='alloggi_legge_56093__gare_in_corso-parent')
        

        homes = town_list_parent.find_all('a')
        town_list = town_list_parent.find_all('a', class_="accordion-toggle collapsed")
        for h in homes:
            print(h)
        for t in town_list:  
            print(t.text)
        
       
        #logging.info(homes_link.text)