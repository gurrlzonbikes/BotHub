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
        #print(resp['items'][rand]['full_name'])
        #print(pdb.set_trace())
        return resp['items'][rand]
        #pp.pprint(len(resp.keys()))
        #print(resp)
        #return resp[0]

    def forkRepo(self):
        pp = pprint.PrettyPrinter(indent=4)
        random_repo = self.get_hot_repos()
        #pp.pprint(random_repo['forks_url'])
        pp.pprint(random_repo['full_name'])
        resp = requests.post(random_repo['forks_url'], auth=self.auth)
        pp.pprint(resp.status_code)