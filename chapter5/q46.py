import sys

from q41 import Sentence


def main():
    for sentence in Sentence.load_cabocha(sys.stdin):
        pred_case_arg(sentence)
        
def pred_case_arg(sent):
    for chunk in sent.chunks:
        for morph in chunk.morphs:
            if morph.pos == '動詞':
                verb = morph.base
                particle_chunks = []
                for src in chunk.srcs:
                    # (助詞, 係り元の分節の表層)
                    particle_chunks.extend([(word.base, sent.chunks[src].chunk2str()) 
                                            for word in sent.chunks[src].morphs if word.pos == '助詞'][-1:])
                if particle_chunks:
                    particle_chunks.sort()
                    particles, chunks = zip(*particle_chunks)
                else:
                    particles, chunks = [], []
                
                print('{}\t{}\t{}'.format(verb, ' '.join(particles), ' '.join(chunks)))
                break

            
if __name__ == "__main__":
    main()