import argparse
import sys
import time
import timeit

from graph import problem_graph
from grassfire import grassfire
from dijkstra import dijkstra


def print_func(path: str, distance: str) -> None:
    print(" -> ".join(path))
    print(f'Total distance: {distance}')


def main(args: argparse.Namespace):
    graph_to_use = problem_graph

    if 'grassfire' in args.algorithm:
        print("Grassfire algorithm execution time:",
              timeit.timeit(lambda: grassfire(graph_to_use, "START", "GOAL"), number=1))

    elif 'dijkstra' in args.algorithm:
        print("Dijkstra's algorithm execution time:",
              timeit.timeit(lambda: dijkstra(graph_to_use, "START", "GOAL"), number=1))

    elif 'all' in args.algorithm:
        print("Grassfire algorithm execution time:",
              timeit.timeit(lambda: grassfire(graph_to_use, "START", "GOAL"), number=1))
        print(f'')
        print("Dijkstra's algorithm execution time:",
              timeit.timeit(lambda: dijkstra(graph_to_use, "START", "GOAL"), number=1))
    else:
        sys.exit(1)


if __name__ == '__main__':
    """ Create Argument NameSpace obj. and pass to main"""

    parser = argparse.ArgumentParser()
    # Required positional argument
    parser.add_argument('algorithm', choices=['grassfire', 'dijkstra', 'all'], help='generic input argument')
    parser.add_argument('--time', default=False, action='store_true',
                        help='set this flag to display the execution time of both algorithms')
    parser.add_argument('--gen_map', default=False, action='store_true',
                        help='set this flag to generate a random map')
    parser.add_argument('-n', '--nodes', type=int, help='set this flag to define number of nodes', default=10)
    parser.add_argument('-e', '--edges', type=int, help='set this flag to define the number of edges', default=20)
    parser.add_argument('-w', '--max_weight', type=int, help='set this flag to define max-weight', default=15)
    arguments = parser.parse_args()

    # Execute main
    main(arguments)
