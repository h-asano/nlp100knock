# [[File:Battle of Waterloo 1815.PNG| のようになっている
import re
import sys

pat = re.compile(r'([fF]ile:|ファイル:)(?P<filename>.+?)\|')
for line in sys.stdin:
    for m in pat.finditer(line):
        print(m.group('filename'))