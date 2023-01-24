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
    if 'grassfire' in args.algorithm:
        print("Grassfire algorithm execution time:",
              timeit.timeit(lambda: grassfire(problem_graph, "START", "GOAL"), number=1))

    elif 'dijkstra' in args.algorithm:
        print("Dijkstra's algorithm execution time:",
              timeit.timeit(lambda: dijkstra(problem_graph, "START", "GOAL"), number=1))

    elif 'all' in args.algorithm:
        print("Grassfire algorithm execution time:",
              timeit.timeit(lambda: grassfire(problem_graph, "START", "GOAL"), number=1))
        print("Dijkstra's algorithm execution time:",
              timeit.timeit(lambda: dijkstra(problem_graph, "START", "GOAL"), number=1))
    else:
        sys.exit(1)


if __name__ == '__main__':
    """ Create Argument NameSpace obj. and pass to main"""

    parser = argparse.ArgumentParser()
    # Required positional argument
    parser.add_argument('algorithm', choices=['grassfire', 'dijkstra', 'all'], help='generic input argument')
    arguments = parser.parse_args()

    # Execute main
    main(arguments)
