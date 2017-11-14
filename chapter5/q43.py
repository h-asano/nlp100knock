import sys

from q40 import arg_int
from q41 import Sentence


def main():
    sent_id = arg_int()
    for i, sent in enumerate(Sentence.load_cabocha(sys.stdin), start=1):
        if i < sent_id:
            sent.print_noun_verb_dep()
        else:
            break

if __name__ == '__main__':
    main()