from collections import deque
import sys

from q14 import arg_lines


def tail(N):
    buf = deque(sys.stdin, N)
    for line in buf:
        print(line, end='')


if __name__ == '__main__':
    tail(arg_lines())