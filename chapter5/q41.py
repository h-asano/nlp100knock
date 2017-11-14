from collections import defaultdict
from itertools import groupby
import sys

from q40 import Morph, arg_int


class Chunk:
    """cabocha lattice formatファイルから文節を読み込む"""
    __slots__ = ('idx', 'dst', 'morphs', 'srcs')
    
    # * 0 2D 0/0 -0.764522
    def __init__(self, line):
        info = line.rstrip().split()
        self.idx = int(info[1])
        self.dst = int(info[2].rstrip("D"))
        self.morphs = []
        self.srcs = []
    
    def __str__(self):
        return ''.join([morph.surface for morph in self.morphs])
    
    def __repr__(self):
        return 'q41.Chunk({}, {})'.format(self.idx, self.dst)
    
    def srcs_append(self, src_idx):
        """係り元文節インデックスを追加"""
        self.srcs.append(src_idx)
    
    def morphs_append(self, line):
        """形態素を追加"""
        self.morphs.append(Morph(line))
    
    def chunk2str(self):
        """記号を取り除いた文節の表層形を返す"""
        return ''.join([morph.surface for morph in self.morphs if morph.pos != '記号'])
    
    def contain_pos(self, pos):
        """文節中にある品詞が存在するかどうかを返す"""
        return pos in (morph.pos for morph in self.morphs)

    
class Sentence:
    """cabocha lattice formatファイルから文を読み込む。Chunkクラスのヘルパー"""
    __slots__ = ('chunks', 'idx')
    
    def __init__(self, sent_lines):
        self.chunks = []
        ch_append = self.chunks.append
        for line in sent_lines:                    
            if line.startswith('* '):
                ch_append(Chunk(line))
            else:
                self.chunks[-1].morphs_append(line)
        # srcsをappendしたいがためのクラス
        for chunk in self.chunks:
            if chunk.dst != -1:
                self.chunks[chunk.dst].srcs_append(chunk.idx)
    
    def __str__(self):
        return ' '.join([morph.surface for chunk in self.chunks for morph in chunk.morphs])
    
    @classmethod
    def load_cabocha(cls, fi):
        """cabocha lattice formatファイルからSentenceインスタンスを生成"""
        for is_eos, sentence in groupby(fi, key=lambda x: x == 'EOS\n'):
            if not is_eos:
                yield cls(sentence)
    
    def print_dep_idx(self):
        """係り元文節インデックスと係り先文節インデックスを表示"""
        for chunk in self.chunks:
            print('{}:{} => {}'.format(chunk.idx, chunk, chunk.dst))
    
    def print_dep(self):
        """係り元文節と係り先文節の表層をタブ区切りで表示"""
        for chunk in self.chunks:
            if chunk.dst != -1:
                print('{}\t{}'.format(chunk.chunk2str(), self.chunks[chunk.dst].chunk2str()))
                
    def dep_edge(self):
        """pydotで係り受けを出力する用"""
        return [(chunk.chunk2str(), self.chunks[chunk.dst].chunk2str())
                    for chunk in self.chunks if chunk.dst != -1]
                
    def print_noun_verb_dep(self):
        """名詞を含む文節が動詞を含む文節に係るものを抽出"""
        for chunk in self.chunks:
            if chunk.contain_pos('名詞') and self.chunks[chunk.dst].contain_pos('動詞'):
                print('{}\t{}'.format(chunk.chunk2str(), self.chunks[chunk.dst].chunk2str()))
    
    
    def trace_dep_path(self):
        """名詞を含む文節からrootまでの係り受けパスを追跡"""
        path = []
        ph_append = path.append
        for chunk in self.chunks:
            if chunk.contain_pos('名詞'):
                ph_append(chunk)
                d = chunk.dst
                while d != -1:
                    ph_append(self.chunks[d])
                    d = self.chunks[d].dst
                
                yield path
                path.clear()
                    
                    
def main():
    sent_id = arg_int()
    for i, sent in enumerate(Sentence.load_cabocha(sys.stdin), start=1):
        if i == sent_id:
            sent.print_dep_idx()
            break


if __name__ == '__main__':
    main()