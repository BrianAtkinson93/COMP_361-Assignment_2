import argparse
import sys

from graph import problem_graph
from grassfire import grassfire
from dijkstra import dijkstra


def print_func(path: str, distance: str) -> None:
    print(" -> ".join(path))
    print(f'Total distance: {distance}')


def main(args: argparse.Namespace):
    if 'grassfire' in args.algorithm:
        print(f'Grassfire Algorithm...')
        path, distance = grassfire(problem_graph, "START", "GOAL")

    elif 'dijkstra' in args.algorithm:
        print(f'Dijkstra Algorithm...')
        path, distance = dijkstra(problem_graph, 'START', 'GOAL')

    elif 'all' in args.algorithm:
        print(f'Running Both Algorithms...')
        print(f'Grassfire Algorithm...')
        path, distance = grassfire(problem_graph, "START", "GOAL")
        print_func(path, distance)
        print(f'Dijkstra Algorithm...')
        path, distance = dijkstra(problem_graph, 'START', 'GOAL')
    else:
        sys.exit(1)

    print_func(path, distance)


if __name__ == '__main__':
    """ Create Argument NameSpace obj. and pass to main"""

    parser = argparse.ArgumentParser()
    # Required positional argument
    parser.add_argument('algorithm', choices=['grassfire', 'dijkstra', 'all'], help='generic input argument')
    arguments = parser.parse_args()

    # Execute main
    main(arguments)
