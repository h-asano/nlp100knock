import sys

from q40 import arg_int
from q41 import Sentence


def main():
    sent_id = arg_int()
    for i, sent in enumerate(Sentence.load_cabocha(sys.stdin), start=1):
        if i == sent_id:
            for chunks in sent.trace_dep_path():
                print(' -> '.join([chunk.chunk2str() for chunk in chunks]))
            break

if __name__ == '__main__':
    main()