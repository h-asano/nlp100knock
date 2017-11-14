import sys

from q30 import read_mecab


def main():
    for i, sent_lis in enumerate(read_mecab(sys.stdin)):
        if i > 20:
            break
        
        for word in sent_lis:
            if word['pos1'] == 'サ変接続' and word['pos'] == '名詞':
                print(word['base'])

                
if __name__ == '__main__':
    main()