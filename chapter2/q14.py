import argparse
import sys


def arg_lines():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--lines', default='1', type=int)
    args = parser.parse_args()
    return args.lines


def head(N):
    for i, line in enumerate(sys.stdin):
        if i < N:
            print(line, end='')
        else:
            break


if __name__ == '__main__':
    head(arg_lines())