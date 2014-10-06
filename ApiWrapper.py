import requests
import json
from random import randrange
import pdb
import pprint

__author__ = 'Tual'

class ApiWrapper:

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.auth = (self.user, self.password)
        self.base_url = "https://api.github.com"
        self.headers = {
            'content-type': 'application/json',
            'Access-Control-Expose-Headers': 'ETag',
            'Accept': 'application/vnd.github.v3+json'

        }

    def create_repo(self, repoName):
        headers = {'content-type': 'application/json'}
        params = json.dumps({"name" : repoName, "auto_init":True})
        create_repo = requests.post(self.base_url + '/user/repos', auth=self.auth, data=params)
        print(json.dumps(create_repo.json()))

    def get_hot_repos(self):
        pp = pprint.PrettyPrinter(indent=4)
        uri = "/search/repositories"
        hot_repos = requests.get(self.base_url+uri+"?q=games+in:description+language:javascript&sort=forks&order=desc", headers=self.headers)
        resp = hot_repos.json()
        rand = randrange(0,10)
        return resp['items'][rand]

    def listOwnRepos(self):
        pp = pprint.PrettyPrinter(indent=4)
        uri = "/user/repos"
        my_repos = requests.get(self.base_url+uri, auth=self.auth)
        return my_repos.json()



    def forkRepo(self, random_repo):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(random_repo['full_name'])
        resp = requests.post(random_repo['forks_url'], auth=self.auth)
        return resp.status_code

    def checkDoubleRepo(self, my_reps, my_random_rep):
        pp = pprint.PrettyPrinter(indent=4)
        mylist = [l['full_name'].split("/")[1] for l in my_reps]
        print(my_random_rep['full_name'].split("/")[1])
        #pp.pprint(mylist)
        """for l in my_reps:
            if l['full_name'].split("/")[1] == my_random_rep['full_name'].split("/")[1]:
                return "This repository already exists, trying to fork another one..."
            else:
                return "Repo forked, everything ok"""
        if my_random_rep['full_name'].split("/")[1] in mylist:
            return "This repository already exists, trying to fork another one..."
            #print(l['full_name'].split("/")[1])
