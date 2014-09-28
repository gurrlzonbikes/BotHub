import requests, json
import tkinter

user = input("Die name??!")
pwd = input("Password?")
auth=(user, pwd)

r = requests.get('https://api.github.com/repos/gurrlzonbikes/BotHub')
bothub_repo = r.json()
#print(json.dumps(bothub_repo, sort_keys=True))

list_rep = requests.get('https://api.github.com/users/gurrlzonbikes/repos')
repo_for_her = list_rep.json()
#print(json.dumps(repo_for_her, sort_keys=True))

withauth = requests.get('https://api.github.com/user', auth=auth)
success = withauth.json()
#print(json.dumps(success, sort_keys=True))

headers = {'content-type': 'application/json'}
params = {"name" : "Fordwidwi", "auto_init":True}
#create_repo = requests.post('https://api.github.com/user/repos', auth=('gurrlzonbikes', 'starcraft666'), data=json.dumps(params))
#print(json.dumps(create_repo.json()))
#print(json.dumps(repo_for_her, sort_keys=True))

get_hot_repos = requests.get("https://api.github.com/search/repositories")
resp = get_hot_repos.json()
print(json.dumps(resp, sort_keys=True))
