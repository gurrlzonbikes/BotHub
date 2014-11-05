__author__ = 'Tual'

from MeBot import MeBot

def start_boting():
    bot = MeBot()
    bot.fork_repo_safely()
    if bot.fork_repo_safely() == False:
        start_boting()
    else:
        print("Bravo! Go check out your new world changing contribution to the sea of shit that is the internet")