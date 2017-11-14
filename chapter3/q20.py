import json
import sys


for line in sys.stdin:
    wiki_dict = json.loads(line)
    if wiki_dict['title'] == 'イギリス':
        print(wiki_dict.get('text'))