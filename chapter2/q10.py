import sys


i = 0 # 空ファイルを読み込まなければこの行は不要
for i, _ in enumerate(sys.stdin, start=1):
    pass

print(i)