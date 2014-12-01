__author__ = 'Tual'
import subprocess
import os
import re
import pdb
import random
from dlistedScraper import dlistedScraper

class repoManagement:

    def __init__(self):
        self.dlisted = dlistedScraper()

    def clone_repo(self, repo_url):
        #subprocess.call('cd ../', shell=True)
        #subprocess.call(['git clone '+repo_url], shell=True)
        p = subprocess.Popen(['git clone '+repo_url], cwd='/Users/Tual/PycharmProjects', shell=True)
        p.wait()

    def select_random_py_file(self, folder_name):
        cfiles = [os.path.join(root, filename)
          for root, dirnames, filenames in os.walk('/Users/Tual/PycharmProjects/'+folder_name.split("/")[1])
          for filename in filenames if filename.endswith('.py') and not re.match('^__init', filename)]
        test = random.choice(cfiles)
        #pdb.set_trace()
        return random.choice(cfiles)

    def insert_random_in_file(self, file_to_modify):
        file_name = open(file_to_modify, 'r+')
        comment = self.get_comment_strings()
        file_name.write(comment)
        print(file_to_modify + " was just updated")
        file_name.close()

    def get_comment_strings(self):
        yesterday_archive = self.dlisted.get_yesterday_archives()
        article = self.dlisted.get_random_article(yesterday_archive)
        raw_post = self.dlisted.get_post(article)
        concat_post_strings = ' '.join(raw_post)
        return '"""' + concat_post_strings + '"""'

