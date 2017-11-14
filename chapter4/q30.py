import argparse
from itertools import groupby
from pprint import pprint
import sys
from string import printable

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)
    args = parser.parse_args()
    for i, sent_lis in enumerate(read_mecab(sys.stdin)):
        if i == args.number:
            pprint(sent_lis)
        elif i > args.number:
            break

            
def read_mecab(fi):
    exceptions = set(printable)
    def sent2inf(sent):
        sent_lis = []
        lappend = sent_lis.append
        for line in sent:
            line_dic = {}
            surface, right = line.rstrip().split('\t')
            inf = right.split(',')
            line_dic['surface'] = surface
            line_dic['pos'] = inf[0]
            line_dic['pos1'] = inf[1]
            # 半角文字は基本形がおかしくなる可能性
            if surface[0] in exceptions:
                line_dic['base'] = surface
            else:
                line_dic['base'] = inf[6]
            lappend(line_dic)
        return sent_lis
    
    
    for is_eos, sentence in groupby(fi, lambda s: s.startswith('EOS')):
        if not is_eos:
            yield sent2inf(sentence)

            
if __name__ == '__main__':
    main()
