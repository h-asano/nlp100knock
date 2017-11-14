"""
'が2, 3, 5個連続していた場合、'を取り除く
"""
import json
import re
import sys
from pprint import pprint

def main():
    dic = json.loads(sys.stdin.read())
    dic = no_emphasis(dic)
    pprint(dic)
    # sys.stdout.write(json.dumps(dic))

def no_emphasis(dic):
    for key, value in dic.items():
        for n in (5, 3, 2):
            eliminated = value.split("'" * n)
            div, mod = divmod(len(eliminated), 2)
            if div > 0 and mod != 0:
                value = ''.join(eliminated)
                dic[key] = value
                break
        # print(key, value,file=sys.stderr)
    return dic

if __name__ == '__main__':
    main()