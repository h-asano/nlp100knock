import sys


for line in sys.stdin:
    lowered = line.lower()
    if lowered.startswith('[[category'):
        print(line.rstrip())