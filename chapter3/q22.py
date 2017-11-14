import sys


for line in sys.stdin:
    print(line.lower().lstrip("[[category:").rstrip("]]\n"))