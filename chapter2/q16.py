import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description='Output pieces of FILE to FILE1, FILE2, ...;')
    parser.add_argument('file')
    parser.add_argument('-n', '--number', type=int,
                        help='split FILE into n pieces')
    args = parser.parse_args()
    file_split(args.file, args.number)

    
def file_split(filename, N):
    with open(filename) as fi:
        n_lines = sum(1 for line in fi)
        fi.seek(0)
        
        widths = ((n_lines + i) // N for i in range(N))
        for file_n, width in enumerate(widths):
            fo = open(filename + str(file_n), 'w')
            for _ in range(width):
                fo.write(fi.readline())
            fo.close()
        fi.close()


if __name__ == '__main__':
    main()