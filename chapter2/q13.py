with open('col1.txt') as col1,\
     open('col2.txt') as col2:
    for c1, c2 in zip(col1, col2):
        print('{}\t{}'.format(c1.rstrip('\n'), c2), end='')