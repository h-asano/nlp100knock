import sys
from itertools import groupby

from q30 import read_mecab


def main():
    for i, sent_lis in enumerate(read_mecab(sys.stdin)):
        if i > 20:
            break
        
        for key, group in groupby(sent_lis, lambda word: word['pos']):
            if key == '名詞':
                words = [word['surface'] for word in group]
                if len(words) > 1:
                    print(''.join(words))

                
if __name__ == '__main__':
    main()