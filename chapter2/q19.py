from collections import Counter
import sys


col1_freq = Counter(line.split()[0] for line in sys.stdin)
for elem, num in col1_freq.most_common():
    print(num, elem)