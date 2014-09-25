import requests, json, ssl
from SSLAdapter import SSLAdapter

auth=('gurrlzonbikes', 'starcraft666')
s = requests.Session()
s.mount('https://', SSLAdapter())
"""r = requests.get('https://api.github.com/gurrlzonbikes', auth=('gurrlzonbikes', 'starcraft666'), verify='/Library/Python/2.7/site-packages/requests/cacert.pem')
print(r.status_code)
"""
s.get('https://api.github.com/gurrlzonbikes')
print(s.status_code)