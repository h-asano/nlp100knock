import sys
from collections import Counter
from pprint import pprint

from q30 import read_mecab


def get_freq():
    word_freq = Counter(word['surface'] for sent_lis in read_mecab(sys.stdin) 
                            for word in sent_lis)
    return word_freq.most_common(10)


if __name__ == '__main__':
    pprint(get_freq())