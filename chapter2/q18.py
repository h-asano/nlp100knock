# 降順では元と変わらないので、元と「逆順」にソート
import sys


sorted_list = sorted(sys.stdin, key=lambda x: float(x.split('\t')[2]))
for elem in sorted_list:
    print(elem, end='')