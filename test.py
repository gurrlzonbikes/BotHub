import requests, json, ssl


cacert = '/Library/Python/2.7/site-packages/requests/cacert.pem'
r = requests.get('https://api.github.com/gurrlzonbikes', auth=('gurrlzonbikes', 'starcraft666'), verify='/Library/Python/2.7/site-packages/requests/cacert.pem')
print(r.status_code)