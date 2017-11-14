import sys
import json


import requests

baseinf = json.loads(sys.stdin.read())
r = requests.get('https://commons.wikimedia.org/w/api.php',
                 {'action': 'query', 'prop': 'imageinfo', 'iiprop': 'url',
                  'format': 'json', 'titles': 'File:{}'.format(baseinf['国旗画像'])})
data = r.json()
print(data['query']['pages']['347935']['imageinfo'][0]['url'])