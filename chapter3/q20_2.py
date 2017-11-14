import gzip
import json
import sys

with gzip.open('jawiki-country.json.gz') as fi:
    for line in fi:
        wiki_dict = json.loads(line.decode('utf-8'))
        if wiki_dict['title'] == 'イギリス':
            print(wiki_dict.get('text'))