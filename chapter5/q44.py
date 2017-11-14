import sys

from q40 import arg_int
from q41 import Sentence
import pydot


def main():
    sent_id = arg_int()
    for i, sent in enumerate(Sentence.load_cabocha(sys.stdin), start=1):
        if i == sent_id:
            edges = sent.dep_edge()
            n = pydot.Node('node')
            n.fontsize = 9
            graph = pydot.graph_from_edges(edges, directed=True)
            graph.add_node(n)
            graph.write_jpeg("dep_tree_neko{}.jpg".format(i))

if __name__ == "__main__":
    main()