import sys

from q41 import Sentence


def main():
    for sentence in Sentence.load_cabocha(sys.stdin):
        case_pattern(sentence)
        
def case_pattern(sent):
    for chunk in sent.chunks:
        for morph in chunk.morphs:
            if morph.pos == '動詞':
                verb = morph.base
                particles = [] # 助詞のリスト
                for src in chunk.srcs:
                    # 分節内で一番右の助詞を追加していく
                    particles.extend([word.base for word in sent.chunks[src].morphs 
                                         if word.pos == '助詞'][-1:])
                particles.sort()
                print('{}\t{}'.format(verb, ' '.join(particles)))
                # 一番左の動詞しか使わないのでさっさと抜ける
                break

            
if __name__ == "__main__":
    main()