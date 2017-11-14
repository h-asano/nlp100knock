import sys

from q30 import read_mecab


def main():
    for sent_id, sent_lis in enumerate(read_mecab(sys.stdin)):
        if sent_id > 20:
            break
        
        for i in range(len(sent_lis) - 2):
            if (sent_lis[i+1]['base'] == 'の' and sent_lis[i]['pos'] == '名詞'
                and sent_lis[i+2]['pos'] == '名詞'):
                print(''.join([sent_lis[i+x]['surface'] for x in range(3)]))

                
if __name__ == '__main__':
    main()