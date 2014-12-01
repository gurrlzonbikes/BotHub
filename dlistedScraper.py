__author__ = 'Tual'
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import random
import pdb

# Get a date object
today = date.today()

class dlistedScraper:

    def __init__(self):
        self.base_url = "http://dlisted.com/"


    def get_yesterday_archives(self):
        # Get a date object
        today = date.today()- timedelta(1)
        today_reformat = today.isoformat().replace('-', '/')
        dlisted= requests.get(self.base_url + today_reformat)
        soup = BeautifulSoup(dlisted.content)
        return soup.find_all('h1')

    def get_random_article(self, yesterday_archives):
        random_number = random.randrange(1,len(yesterday_archives) -1)
        #pdb.set_trace()
        random_article_link = yesterday_archives[random_number].a['href']
        #pdb.set_trace()
        response = requests.get(random_article_link)
        soup = BeautifulSoup(response.content)
        return soup

    def get_post(self, front_page):
        [s.extract() for s in front_page('script')]
        random_text= front_page.get_text()
        # break into lines and remove leading and trailing space on each
        lines = list(line.strip() for line in random_text.splitlines())
        # break multi-headlines into a line each
        no_blanks_list = list(filter(None, lines))
        result = random.sample(no_blanks_list, 5)
        #only get sentences longer than 100 char
        sentence_list = list(x for x in result if len(x) > 100)
        if not sentence_list:
            self.get_post(front_page)
        else:
            return sentence_list



