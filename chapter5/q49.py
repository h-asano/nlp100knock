import sys
from itertools import combinations

from q40 import arg_int
from q41 import Sentence


def main():
    sent_id = arg_int()
    for i, sent in enumerate(Sentence.load_cabocha(sys.stdin), start=1):
        if i == sent_id:
            for c1, c2 in combinations(sent.chunks, 2):
                if not (c1.contain_pos('名詞') and c2.contain_pos('名詞')):
                    continue

                # c1 -> ... -> root
                dp1 = list(sent.trace_dep_path_from(c1))
                print(dp1)
                print(c2)

                # case 1: c1 -> ... -> c2 -> ... -> root
                if c2 in dp1:
                    # c1 -> ... -> c2
                    path_i_to_j = dp1[:dp1.index(c2)+1]

                    # head (c1) -> [mid] -> tail (c2)
                    head = path_i_to_j[0].abstract_np('X')
                    mid = [c.as_text() for c in path_i_to_j[1:-1]]
                    tail = path_i_to_j[-1].abstract_np('Y')
                    print(' -> '.join([head, *mid, tail]))
                    continue

                # c2 -> ... -> root
                dp2 = list(sent.trace_dep_path_from(c2))
                print(dp2)

                # case 2:
                # root <- ... <- junction <- ... <- c1
                # root <- ... <- junction <- ... <- c2
                for ch1, ch2 in zip(dp1[::-1], dp2[::-1]):
                    if ch1 != ch2:
                        break
                    # they share at least root
                    junction = ch1

                # x (c1) -> ... -> chunk [-> junction]
                x, *x_remindar = dp1[:dp1.index(junction)]

                # y (c2) -> ... -> chunk [-> junction]
                y, *y_remindar = dp2[:dp2.index(junction)]

                print(' | '.join([
                    ' -> '.join([x.abstract_np('X'), *[c.as_text() for c in x_remindar]]),
                    ' -> '.join([y.abstract_np('Y'), *[c.as_text() for c in y_remindar]]),
                    junction.as_text(),
                ]))

if __name__ == '__main__':
    main()