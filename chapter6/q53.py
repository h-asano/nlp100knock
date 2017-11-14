import sys

from lxml import etree


tree = etree.parse(sys.stdin)    # ファイル名文字列を渡してもOK
for word in tree.xpath('/root/document/sentences/sentence/tokens/token/word'):
    print(word.text)