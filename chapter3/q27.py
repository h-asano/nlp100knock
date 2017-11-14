"""
[[記事名]]
[[記事名|表示文字]]
[[記事名#節名|表示文字]] 
"""
import json
import re
import sys
from pprint import pprint


from q26 import no_emphasis


def main():
    dic = json.loads(sys.stdin.read())
    dic = no_emphasis(dic)
    dic = eliminate_link(dic)
    pprint(dic)
    # sys.stdout.write(json.dumps(dic))


def eliminate_link(dic):
    pat = re.compile(r"""
        \[\[        # [[
        ([^|]+\|)*  # 記事名|　この部分は無かったり繰り返されたりする
        ([^]]+)\]\] # 表示文字 patにマッチした部分をこいつに置換する
    """, re.VERBOSE)
    for key, value in dic.items():
        value = pat.sub(r'\2', value)
        dic[key] = value
    return dic

if __name__ == '__main__':
    main()