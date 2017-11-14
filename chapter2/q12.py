import sys


with open('col1.txt', 'w') as col1,\
     open('col2.txt', 'w') as col2:
    for line in sys.stdin:
        cols = line.split('\t')
        col1.write(cols[0] + '\n')
        col2.write(cols[1] + '\n')