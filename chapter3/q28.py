import json
import sys
from pprint import pprint

from pypandoc import convert


def main():
    dic = json.loads(sys.stdin.read())
    for key, value in dic.items():
        dic[key] = convert(value, 'plain', format='mediawiki').rstrip()
    
    pprint(dic)

if __name__ == '__main__':
    main()