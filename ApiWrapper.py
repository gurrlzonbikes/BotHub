import requests
import json
from random import randrange
import pdb

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
        uri = "/search/repositories"
        hot_repos = requests.get(self.base_url+uri+"?q=games+language:javascript&sort=forks&order=asc", headers=self.headers)
        print(pdb.set_trace())
        resp = hot_repos.json()
        rand = randrange(0,10)
        print(hot_repos)
        #print(resp)
        #return resp[0]