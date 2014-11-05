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
        self.list_own_repos()

    def create_repo(self, repoName):
        headers = {'content-type': 'application/json'}
        params = json.dumps({"name" : repoName, "auto_init":True})
        create_repo = requests.post(self.base_url + '/user/repos', auth=self.auth, data=params)
        print(json.dumps(create_repo.json()))

    def get_hot_repos(self):
        pp = pprint.PrettyPrinter(indent=4)
        uri = "/search/repositories"
        hot_repos = requests.get(self.base_url+uri+"?q=games+in:description+language:python&sort=updated&order=asc", headers=self.headers)
        resp = hot_repos.json()
        #pdb.set_trace()
        rand = randrange(0,10)
        pp.pprint(resp)
        return resp['items'][rand]

    def list_own_repos(self):
        pp = pprint.PrettyPrinter(indent=4)
        uri = "/user/repos"
        my_repos = requests.get(self.base_url+uri, auth=self.auth)
        if my_repos.status_code !=200:
            raise TypeError("There was a problem logging you in. Please check that you've entered your credentials properly.")
        else:
            return my_repos.json()


    def update_progress(self, progress):
        #pdb.set_trace()
        print('\r[{0}] {1}%'.format('#'*int(progress/10), progress, end=''))


    def fork_repo(self, random_repo):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(random_repo['full_name'])
        resp = requests.post(random_repo['forks_url'], auth=self.auth)
        return resp.status_code

    def checkDoubleRepo(self, my_reps, my_random_rep):
        pp = pprint.PrettyPrinter(indent=4)
        list_rep_name = [l['full_name'].split("/")[1] for l in my_reps]
        #pdb.set_trace()
        if my_random_rep['full_name'].split("/")[1] in list_rep_name:
            return True
            #print(l['full_name'].split("/")[1])
        else:
            return False

    def checkRepoHasForks(self, repo):
        if repo["forks"] > 1:
            return True
        else:
            return False

    def test(self):
        pp = pprint.PrettyPrinter(indent=4)
        resp = requests.get('https://api.github.com/user')
        pp.pprint(resp.json())
