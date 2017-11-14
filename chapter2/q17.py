import sys


col1 = {line.split()[0] for line in sys.stdin}
for elem in col1:
    print(elem)