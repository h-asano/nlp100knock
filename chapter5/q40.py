import argparse
from itertools import groupby
from string import printable
import sys


class Morph:
    """cabocha lattice formatファイルの1行を読み込む"""
    __slots__ = ('surface', 'pos', 'pos1', 'base')
    exceptions = frozenset(printable)
    # 吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ
    def __init__(self, line):
        self.surface, temp = line.rstrip().split('\t')
        inf = temp.split(',')
        self.pos = inf[0]
        self.pos1 = inf[1]
        # 4章同様, 半角文字の基本形問題
        if self.surface in self.exceptions:
            self.base = self.surface
        else:
            self.base = inf[6]
    @classmethod
    def load_cabocha(cls, fi):
        """cabocha lattice formatファイルからMorphインスタンスを生成"""
        for is_eos, sentence in groupby(fi, key=lambda x: x == 'EOS\n'):
            if not is_eos:
                yield [cls(line) for line in sentence if not line.startswith('* ')]
                # startswith('*')だと表層形が「*」のときにまずい
    
    def __str__(self):
        return self.surface
    
    def __repr__(self):
        return 'q40.Morph({})'.format(', '.join((self.surface, self.pos, self.pos1, self.base)))
    

def main():
    sent_idx = arg_int()
    for i, sent_lis in enumerate(Morph.load_cabocha(sys.stdin), start=1):
        if i == sent_idx:
            print(*sent_lis)
            print(repr(sent_lis))
            break

def arg_int():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', default='1', type=int)
    args = parser.parse_args()
    return args.number


if __name__ == '__main__':
    main()