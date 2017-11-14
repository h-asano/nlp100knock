import sys

from q30 import read_mecab


def main():
    for i, sent_lis in enumerate(read_mecab(sys.stdin)):
        if i > 10:
            break
        
        for word in sent_lis:
            if word['pos'] == '動詞':
                print(word['surface'])

                
if __name__ == '__main__':
    main()