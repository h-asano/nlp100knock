import sys

from lxml import etree
tree = etree.parse(sys.stdin)
elems = ['word', 'lemma', 'POS']

for token in tree.xpath('//token'):  # /root/document/sentences/sentence/tokens/token/wordと同じ
    for elem in elems:
        print(token.findtext(elem), end='\t')
    print()