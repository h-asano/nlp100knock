import sys

from q41 import Sentence


def main():
    for sentence in Sentence.load_cabocha(sys.stdin):
        sahen_case_arg(sentence)
        
def sahen_case_arg(sent):
    # サ変名詞＋動詞を抽出するためのフラグ
    sahen_flag = 0
    for chunk in sent.chunks:
        for morph in chunk.morphs:
            if sahen_flag == 0 and morph.pos1 == 'サ変接続':
                sahen_flag = 1
                sahen = morph.surface
            elif sahen_flag == 1 and morph.base == 'を' and morph.pos == '助詞':
                sahen_flag = 2
            elif sahen_flag == 2 and morph.pos == '動詞':
                sahen_wo = sahen + 'を'
                verb = morph.base
                particle_chunks = []
                for src in chunk.srcs:
                    # (助詞, 係り元の分節の表層)
                    particle_chunks.extend([(word.base, sent.chunks[src].chunk2str()) for word in sent.chunks[src].morphs 
                                     if word.pos == '助詞'][-1:])
                for j, part_chunk in enumerate(particle_chunks[:]):
                    if sahen_wo in part_chunk[1]:
                        del particle_chunks[j]
                
                if particle_chunks:
                    particle_chunks.sort()
                    particles, chunks = zip(*particle_chunks)
                else:
                    particles, chunks = [], []

                print('{}\t{}\t{}'.format(sahen_wo + verb, ' '.join(particles), ' '.join(chunks)))
                sahen_flag = 0
                break
            else:
                sahen_flag = 0

            
if __name__ == "__main__":
    main()