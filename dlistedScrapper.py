__author__ = 'Tual'
import requests
import datetime

# Get a date object
today = datetime.date.today()

class dlistedScrapper:

    def __init__(self):
        self.base_url = "http://dlisted.com"

    def get_yesterday_archives(self):
        # Get a date object
        today = datetime.date.today()
        print(today)



