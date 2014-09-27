import requests, json, ssl
from SSLAdapter import SSLAdapter

"""print(SSLAdapter)
s = requests.Session()
s.mount('https://', SSLAdapter())"""

auth=('gurrlzonbikes', 'starcraft666')

r = requests.get('https://api.github.com/repos/gurrlzonbikes/BotHub')
bothub_repo = r.json()
#print(json.dumps(bothub_repo, sort_keys=True))

list_rep = requests.get('https://api.github.com/users/gurrlzonbikes/repos')
repo_for_her = list_rep.json()
#print(json.dumps(repo_for_her, sort_keys=True))

withauth = requests.get('https://api.github.com/user', auth=('gurrlzonbikes', 'starcraft666'))
success = withauth.json()
#print(json.dumps(success, sort_keys=True))

input = {"name" : "Fordwidwi", "auto_init":True}
create_repo = requests.post('https://api.github.com/user/repos', auth=('gurrlzonbikes', 'starcraft666'), data=input)
print(create_repo.text)
#print(json.dumps(repo_for_her, sort_keys=True))

